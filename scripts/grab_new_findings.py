#!/usr/bin/env python3
"""Opportunistic recovery downloader for portal findings.

Sweeps monitor_state.db for datasets whose resources were first discovered
after a given date (default: 2026-04-07 — the Apr 7 findings that the broken
opportunistic-capture path failed to save). For each one:

  1. Fetch live resource list via shared portal client.
  2. Pick CSV + XLSX formats.
  3. Use parse_dataset() from download_new_data.py to derive a local filename
     when the Arabic title matches a known RE category.
  4. For titles that parse_dataset() skips (non-RE POA sub-categories, etc.),
     save to moj/opportunistic/ with a slug derived from the Arabic title.
  5. Skip files already on disk. Download the rest with dedup + sentinel
     handling (NO DATA FOUND, WAF, URL encoding).
  6. Log a full summary at the end.

Usage:
    python3 scripts/grab_new_findings.py
    python3 scripts/grab_new_findings.py --since 2026-04-01
    python3 scripts/grab_new_findings.py --dry-run
    python3 scripts/grab_new_findings.py --formats csv xlsx
"""

from __future__ import annotations

import argparse
import logging
import re
import sqlite3
import sys
import time
import unicodedata
from pathlib import Path

REPO_ROOT = Path(__file__).parent.parent.resolve()
sys.path.insert(0, str(REPO_ROOT / "scripts"))

from portal_client import (  # noqa: E402
    DEFAULT_RATE_LIMIT,
    DataWithdrawn,
    WAFBlocked,
    fetch_bytes,
    get_dataset_resources,
    make_portal_client,
)

from download_new_data import parse_dataset  # noqa: E402

STATE_DB = REPO_ROOT / "monitor" / "monitor_state.db"
OPPORTUNISTIC_DIR = REPO_ROOT / "moj" / "opportunistic"

DEFAULT_SINCE = "2026-04-07"
DEFAULT_FORMATS = ("CSV", "XLSX")

logging.basicConfig(
    format="%(asctime)s [%(levelname)s] %(message)s",
    level=logging.INFO,
)
log = logging.getLogger("grab_new_findings")


def slugify_arabic_title(title_ar: str) -> str:
    # Filesystem-safe slug: normalize NFKC, drop punctuation, collapse
    # whitespace to hyphens. Arabic letters pass through verbatim.

    cleaned = unicodedata.normalize("NFKC", title_ar)
    cleaned = re.sub(r"[،,:؛;()\[\]{}\"'<>|*?]", " ", cleaned)
    cleaned = re.sub(r"\s+", "-", cleaned.strip())
    # Remove disallowed FS characters
    cleaned = re.sub(r"[/\\]", "-", cleaned)
    return cleaned[:120]


def build_local_path(
    dataset_id: str, title_ar: str, res_format: str
) -> tuple[Path, str]:
    """Return (absolute_path, category_tag) for a dataset/format pair.

    Uses parse_dataset() when available (known RE categories), otherwise
    falls back to moj/opportunistic/ with an Arabic-derived slug.
    """
    ext = res_format.lower()
    parsed = parse_dataset(title_ar)
    if parsed is not None:
        dest_rel, stem = parsed
        return (REPO_ROOT / dest_rel / f"{stem}.{ext}", "known")

    slug = slugify_arabic_title(title_ar)
    short_id = dataset_id[:8]
    return (OPPORTUNISTIC_DIR / f"{slug}__{short_id}.{ext}", "opportunistic")


def fetch_new_datasets(conn: sqlite3.Connection, since: str) -> list[tuple[str, str]]:
    rows = conn.execute(
        """
        SELECT DISTINCT d.dataset_id, d.title_ar
        FROM known_datasets d
        JOIN known_resources r ON r.dataset_id = d.dataset_id
        WHERE r.first_seen >= ?
        ORDER BY d.title_ar
        """,
        (since,),
    ).fetchall()
    return rows


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--since", default=DEFAULT_SINCE, help="ISO date — min first_seen")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument(
        "--formats",
        nargs="+",
        default=list(DEFAULT_FORMATS),
        help="Resource formats to fetch (default: CSV XLSX)",
    )
    ap.add_argument("--rate", type=float, default=DEFAULT_RATE_LIMIT)
    ap.add_argument(
        "--limit", type=int, default=0, help="Stop after N downloads (0 = no limit)"
    )
    args = ap.parse_args()

    formats = {f.upper() for f in args.formats}

    if not STATE_DB.exists():
        log.error("monitor state db not found: %s", STATE_DB)
        return 2

    conn = sqlite3.connect(STATE_DB)
    datasets = fetch_new_datasets(conn, args.since)
    log.info("Found %d datasets with resources since %s", len(datasets), args.since)
    if not datasets:
        return 0

    OPPORTUNISTIC_DIR.mkdir(parents=True, exist_ok=True)

    opener = make_portal_client()

    counts = {
        "dl_ok": 0,
        "dl_skip_ondisk": 0,
        "dl_no_data": 0,
        "dl_waf": 0,
        "dl_err": 0,
        "api_err": 0,
        "no_matching_format": 0,
    }
    live_log_lines: list[str] = []

    for idx, (dataset_id, title_ar) in enumerate(datasets, start=1):
        try:
            resources = get_dataset_resources(opener, dataset_id)
        except Exception as exc:
            counts["api_err"] += 1
            log.warning("[%d/%d] api err %s: %s", idx, len(datasets), dataset_id, exc)
            continue

        matching = [r for r in resources if r.get("format", "").upper() in formats]
        if not matching:
            counts["no_matching_format"] += 1
            continue

        for res in matching:
            res_format = res.get("format", "").upper()
            download_url = res.get("downloadUrl", "")
            if not download_url:
                counts["api_err"] += 1
                continue

            local_path, category = build_local_path(dataset_id, title_ar, res_format)
            if local_path.exists() and local_path.stat().st_size > 100:
                counts["dl_skip_ondisk"] += 1
                continue

            if args.dry_run:
                log.info(
                    "[DRY] would save %s -> %s",
                    title_ar[:60],
                    local_path.relative_to(REPO_ROOT),
                )
                continue

            try:
                data = fetch_bytes(opener, download_url)
            except DataWithdrawn:
                counts["dl_no_data"] += 1
                log.info(
                    "[%d/%d] NO DATA FOUND: %s (%s)",
                    idx,
                    len(datasets),
                    title_ar[:60],
                    res_format,
                )
                continue
            except WAFBlocked as exc:
                counts["dl_waf"] += 1
                log.error(
                    "[%d/%d] WAF: %s — stealth downgraded? %s",
                    idx,
                    len(datasets),
                    title_ar[:60],
                    exc,
                )
                continue
            except Exception as exc:
                counts["dl_err"] += 1
                log.warning(
                    "[%d/%d] net err %s: %s",
                    idx,
                    len(datasets),
                    title_ar[:60],
                    exc,
                )
                continue

            local_path.parent.mkdir(parents=True, exist_ok=True)
            local_path.write_bytes(data)
            counts["dl_ok"] += 1
            line = (
                f"  OK  [{category:12}] {len(data):>11,}B  "
                f"{local_path.relative_to(REPO_ROOT)}"
            )
            log.info(line)
            live_log_lines.append(line)
            time.sleep(args.rate)

            if args.limit and counts["dl_ok"] >= args.limit:
                log.info("--limit %d reached, stopping", args.limit)
                _print_summary(counts)
                return 0

        time.sleep(args.rate)

    _print_summary(counts)
    return 0


def _print_summary(counts: dict) -> None:
    log.info("=" * 60)
    log.info("Opportunistic download summary")
    log.info("=" * 60)
    for k, v in counts.items():
        log.info("  %-25s %d", k, v)
    log.info("=" * 60)


if __name__ == "__main__":
    sys.exit(main())
