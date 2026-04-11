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
import hashlib  # noqa: F401 — used in build_repo_hash_index + write loop
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


def build_repo_hash_index(
    extensions: tuple[str, ...] = (".csv", ".xlsx"),
) -> dict[str, Path]:
    # Walk the repo and build a MD5 index of every tracked data file.
    # Used to detect byte-exact duplicates before writing new downloads —
    # the portal sometimes renames existing datasets with new Arabic slugs
    # and re-publishes them as "new" resources.
    # Materialize iCloud files first so the hash loop doesn't stall on
    # cold-cache blobs (see scripts/icloud_materialize.py).
    try:
        from icloud_materialize import materialize_files  # noqa: E402

        materialize_files(REPO_ROOT, patterns=tuple(f"*{e}" for e in extensions))
    except ImportError:
        pass

    index: dict[str, Path] = {}
    skip_dirs = {".git", "node_modules", "__pycache__", "social", "notebooks"}
    for p in REPO_ROOT.rglob("*"):
        if not p.is_file():
            continue
        if p.suffix.lower() not in extensions:
            continue
        if any(part in skip_dirs for part in p.relative_to(REPO_ROOT).parts):
            continue
        try:
            h = hashlib.md5(p.read_bytes()).hexdigest()
        except OSError:
            continue
        # Prefer the shorter / more canonical path when collisions already
        # exist in the repo (e.g. an Arabic-slug staging copy AND a
        # canonical English-slug copy of the same bytes).
        existing = index.get(h)
        if existing is None or len(str(p)) < len(str(existing)):
            index[h] = p
    return index


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
    ap.add_argument(
        "--no-dedup",
        action="store_true",
        help="Skip byte-exact dedup check against existing repo files",
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

    hash_index: dict[str, Path] = {}
    if not args.no_dedup:
        log.info("Building repo hash index for byte-exact dedup...")
        hash_index = build_repo_hash_index()
        log.info("  %d existing data files indexed", len(hash_index))

    opener = make_portal_client()

    counts = {
        "dl_ok": 0,
        "dl_skip_ondisk": 0,
        "dl_dup_of_existing": 0,
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

            # Byte-exact dedup against existing repo files. Protects against
            # the portal re-publishing the same dataset under a new Arabic
            # slug — see 2026-04-11 recovery where 11 REGA "new" resources
            # were hash-identical to existing files under old names.
            if hash_index:
                dl_hash = hashlib.md5(data).hexdigest()
                existing = hash_index.get(dl_hash)
                if existing is not None:
                    counts["dl_dup_of_existing"] += 1
                    log.info(
                        "  DUP [%s] %s  ==  %s (byte-exact match, skipping)",
                        category,
                        title_ar[:50],
                        existing.relative_to(REPO_ROOT),
                    )
                    time.sleep(args.rate)
                    continue

            local_path.parent.mkdir(parents=True, exist_ok=True)
            local_path.write_bytes(data)
            # Keep the index in sync so subsequent writes in the same run
            # dedup against files we just landed.
            if hash_index:
                hash_index[hashlib.md5(data).hexdigest()] = local_path
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
