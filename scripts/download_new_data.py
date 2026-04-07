#!/usr/bin/env python3
"""
Download new MOJ datasets from the Saudi Open Data portal.

Reads known_datasets and known_resources from monitor/monitor_state.db,
maps Arabic titles to English filenames using our naming convention,
checks which files are already on disk, and downloads the missing ones.

Usage:
    python3 scripts/download_new_data.py
    python3 scripts/download_new_data.py --dry-run
    python3 scripts/download_new_data.py --verbose
"""

from __future__ import annotations

import argparse
import json
import logging
import re
import ssl
import sqlite3
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

# ── Paths ─────────────────────────────────────────────────────────────

REPO_ROOT = Path(__file__).parent.parent.resolve()
STATE_DB = REPO_ROOT / "monitor" / "monitor_state.db"
MOJ_SALES = REPO_ROOT / "moj" / "sales"  # Sales + RE-Index
MOJ_RE = REPO_ROOT / "moj" / "real-estate"  # per-category quarterly
MOJ_MONTHLY = REPO_ROOT / "moj" / "monthly"  # monthly aggregate ops + POA

DOWNLOAD_BASE = "https://open.data.gov.sa/data/api/datasets/resources/download"
RESOURCES_API = "https://open.data.gov.sa/data/api/datasets/resources"
USER_AGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15"
REQUEST_TIMEOUT = 60
DOWNLOAD_DELAY = 5.0  # seconds between downloads (WAF rate-limit avoidance)
WAF_BACKOFF = 30.0  # seconds to wait after WAF block before retrying
MAX_CONSECUTIVE_WAF = 5  # stop after this many consecutive WAF blocks

# ── Quarter / Month mappings ───────────────────────────────────────────

QUARTER_MAP: dict[str, str] = {
    "الربع الأول": "Q1",
    "الربع الاول": "Q1",  # without hamza variant
    "الربع الثاني": "Q2",
    "الربع الثالث": "Q3",
    "الربع الرابع": "Q4",
}

MONTH_MAP: dict[str, str] = {
    "يناير": "01",
    "فبراير": "02",
    "مارس": "03",
    "أبريل": "04",
    "ابريل": "04",  # without hamza
    "مايو": "05",
    "يونيو": "06",
    "يوليو": "07",
    "أغسطس": "08",
    "اغسطس": "08",
    "سبتمبر": "09",
    "أكتوبر": "10",
    "اكتوبر": "10",
    "نوفمبر": "11",
    "ديسمبر": "12",
}

# ── Arabic-to-English category mapping ────────────────────────────────
#
# Key: Arabic category fragment (matched as substring of title_ar after
#      stripping the common "العمليات العقارية المسجلة في" prefix).
# Value: English slug used in the filename.
#
# For datasets that are *not* sub-categories of "العمليات العقارية المسجلة في",
# the full title prefix is matched directly in parse_dataset().

CATEGORY_MAP: dict[str, str] = {
    # ── Transfers (إفراغ) ──────────────────────────────────────────
    "الإفراغات": "Transfers",
    "افراغ": "Transfers",  # spelling variant
    # ── Seizure / Release-Seizure ──────────────────────────────────
    "الحجز التحفظي على ممتلكات شخص": "Seizure",
    "فك الحجز التحفظي على ممتلكات شخص": "Release-Seizure",
    # ── Register Old Deed ──────────────────────────────────────────
    "تسجيل صك قديم": "Register-Old-Deed",
    # ── Register No Deed ──────────────────────────────────────────
    "تسجيل ملكية عقار بدون صك": "Register-No-Deed",
    # ── Update Deed ───────────────────────────────────────────────
    "تعديل صك قديم": "Update-Old-Deed",  # must come BEFORE "تعديل صك"
    "تعديل صك": "Update-Deed",
    # ── Deed-Define-Divide ────────────────────────────────────────
    "تعريف الصكوك للفرز": "Deed-Define-Divide",
    # ── Compensation / Grants ─────────────────────────────────────
    "تعويض أنقاض دون العقار": "Compensation-Ruins",
    "تعويضات": "Compensation",
    "منحة بديلة": "Grant-Alternative",  # must come BEFORE "منح"
    "منح": "Grant",
    # ── Ownership (share) ─────────────────────────────────────────
    "تملك نصيب": "Ownership",
    # ── Merge Deed / Merge RE ─────────────────────────────────────
    "دمج صكوك": "Merge-Deed",
    "دمج عقارات": "Merge-RE",
    # ── Property-Identity ─────────────────────────────────────────
    "ربط صك بالهوية العقارية": "Property-Identity",
    # ── Mortgage / Mortgage-Release ───────────────────────────────
    "رهن العقارات": "Mortgage",
    "فك رهن العقارات": "Mortgage-Release",
    # ── Divide ────────────────────────────────────────────────────
    "فرز صكوك": "Divide",
    # ── Physical-Registration ─────────────────────────────────────
    "مسجل عينيا": "Physical-Registration",
    # ── Transfer (annotation — not the same as إفراغ) ────────────
    "نقل شرح بانتقال ملكية": "Transfer-Ownership",
    "نقل شرح وصية بدون انتقال ملكية": "Transfer-Will-No-Ownership",
}

# ── POA sub-category map (الوكالات الصادرة في {sub}) ─────────────────
# Only the RE-relevant ones. All others are silently skipped.
# RE-adjacent POA categories that belong in moj/real-estate/:
POA_RE_SUBCATEGORY_MAP: dict[str, str] = {
    "العقارات": "POA-RealEstate",
    "صندوق التنمية العقارية": "POA-RE-Fund",
    "برنامج رسوم الأراضي البيضاء": "POA-WhiteLandFee",
    "شبكة إيجار الإلكترونية": "POA-Ejar",
}

# ── Logging ───────────────────────────────────────────────────────────

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[logging.StreamHandler()],
)
log = logging.getLogger("download_new_data")


# ── HTTP helpers ──────────────────────────────────────────────────────


def _make_ctx(verify: bool = True) -> ssl.SSLContext:
    if verify:
        return ssl.create_default_context()
    return ssl._create_unverified_context()  # noqa: SLF001


def fetch_url(url: str, timeout: int = REQUEST_TIMEOUT) -> bytes | None:
    headers = {
        "User-Agent": USER_AGENT,
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Language": "ar,en;q=0.9",
    }
    req = urllib.request.Request(url, headers=headers)
    for verify in (True, False):
        try:
            with urllib.request.urlopen(
                req, timeout=timeout, context=_make_ctx(verify)
            ) as resp:
                return resp.read()
        except ssl.SSLError:
            if verify:
                log.debug("SSL error, retrying without verify: %s", url)
                continue
            log.warning("SSL error (unverified) for %s", url)
            return None
        except (urllib.error.URLError, urllib.error.HTTPError, TimeoutError) as exc:
            log.warning("Failed to fetch %s: %s", url, exc)
            return None
    return None


def fetch_json(url: str) -> dict | list | None:
    data = fetch_url(url)
    if data is None:
        return None
    try:
        return json.loads(data)
    except json.JSONDecodeError as exc:
        log.warning("JSON decode error for %s: %s", url, exc)
        return None


# ── Title parsing ─────────────────────────────────────────────────────


def _extract_year(title: str) -> str | None:
    """Extract 4-digit year from Arabic title."""
    m = re.search(r"\b(20\d{2})\b", title)
    return m.group(1) if m else None


def _extract_quarter(title: str) -> str | None:
    """Return e.g. 'Q1' if a quarter phrase is found."""
    for ar, en in QUARTER_MAP.items():
        if ar in title:
            return en
    return None


def _extract_month(title: str) -> str | None:
    """Return zero-padded month number if a month name is found."""
    for ar, en in MONTH_MAP.items():
        if ar in title:
            return en
    return None


def _extract_part(title: str) -> str | None:
    """Return part suffix like '-Part1' for titles with 'الجزء N'."""
    m = re.search(r"الجزء\s+(\d+)", title)
    if m:
        return f"-Part{m.group(1)}"
    return None


def parse_dataset(title_ar: str) -> tuple[str | None, str | None] | None:
    """
    Parse an Arabic dataset title and return (dest_path, filename) or None.

    dest_path is relative to REPO_ROOT.
    filename is the CSV file name without extension.
    Returns None if the dataset should be skipped (non-RE, unrecognised).
    """
    t = title_ar.strip()

    year = _extract_year(t)
    quarter = _extract_quarter(t)
    month = _extract_month(t)
    part = _extract_part(t)

    # ── 1. الصفقات العقارية (Sales) ────────────────────────────────
    if t.startswith("الصفقات العقارية"):
        if not year or not quarter:
            return None
        fname = f"MOJ-Sales-{year}-{quarter}"
        return str(MOJ_SALES.relative_to(REPO_ROOT)), fname

    # ── 2. المؤشر العقاري (RE Index) ───────────────────────────────
    if t.startswith("المؤشر العقاري"):
        if "المناطق" in t or "للمناطق" in t:
            return str(
                MOJ_SALES.relative_to(REPO_ROOT)
            ), "MOJ-RE-Index-Regions-2018-2021"
        if "المدن" in t or "للمدن" in t:
            return str(
                MOJ_SALES.relative_to(REPO_ROOT)
            ), "MOJ-RE-Index-Cities-2018-2021"
        if "الأحياء" in t or "للأحياء" in t:
            return str(
                MOJ_SALES.relative_to(REPO_ROOT)
            ), "MOJ-RE-Index-Districts-2018-2021"
        return None

    # ── 3. الوكالات والإقرارات الصادرة في عام (annual POA+Declarations) ──
    if t.startswith("الوكالات والإقرارات الصادرة"):
        # Annual multi-year file — already in repo as static name
        return str(MOJ_RE.relative_to(REPO_ROOT)), "MOJ-POA-Declarations-2018-2021"

    # ── 4. الوكالات الصادرة (monthly POA — no sub-category) ────────
    #    These are monthly: "الوكالات الصادرة YYYY شهر"
    if re.match(r"^الوكالات الصادرة\s+\d{4}", t):
        if not year or not month:
            return None
        fname = f"MOJ-POA-Issued-{year}-{month}"
        return str(MOJ_MONTHLY.relative_to(REPO_ROOT)), fname

    # ── 5. الوكالات الصادرة في {sub-category} ──────────────────────
    if t.startswith("الوكالات الصادرة في"):
        sub_part = t[len("الوكالات الصادرة في") :].strip()
        # Remove trailing year+quarter/month
        sub_clean = re.sub(r"\s+\d{4}.*$", "", sub_part).strip()
        # Check if this sub-category is RE-relevant
        for ar_key, slug in POA_RE_SUBCATEGORY_MAP.items():
            if ar_key in sub_clean:
                if not year:
                    return None
                if quarter:
                    suffix = f"{year}-{quarter}"
                    if part:
                        suffix += part
                    fname = f"MOJ-{slug}-{suffix}"
                    return str(MOJ_RE.relative_to(REPO_ROOT)), fname
                if month:
                    fname = f"MOJ-{slug}-{year}-{month}"
                    return str(MOJ_MONTHLY.relative_to(REPO_ROOT)), fname
                return None
        # Non-RE POA sub-category — skip
        return None

    # ── 6. الوكالات المفسوخة / طلبات التوثيق (non-RE POA) ──────────
    if t.startswith("الوكالات المفسوخة") or t.startswith("طلبات التوثيق"):
        return None  # not RE-relevant

    # ── 7. نسب ومعدلات التملك (ownership rates — separate datasets) ─
    if "نسب ومعدلات التملك" in t:
        if "الرجال" in t or "الأفراد الرجال" in t:
            slug = "Ownership-Rate-Men"
        elif "النساء" in t or "الأفراد النساء" in t:
            slug = "Ownership-Rate-Women"
        else:
            slug = "Ownership-Rate"
        if not year or not quarter:
            return None
        fname = f"MOJ-{slug}-{year}-{quarter}"
        return str(MOJ_RE.relative_to(REPO_ROOT)), fname

    # ── 8. القرارات التنفيذية (Enforcement decisions) ───────────────
    if t.startswith("القرارات التنفيذية"):
        if "إحالة الأصل للبيع عبر المزاد" in t:
            slug = "Enforcement-Auction-Sale"
        elif "ترسية البيع على المشتري" in t:
            slug = "Enforcement-Award-Buyer"
        elif "بيع عقار أو منقول للمنفذ ضده" in t:
            slug = "Enforcement-Sell-Property"
        else:
            # Unknown enforcement sub-type
            slug = "Enforcement-Other"

        if not year:
            return None
        if quarter:
            suffix = f"{year}-{quarter}"
            if part:
                suffix += part
        elif month:
            suffix = f"{year}-{month}"
        else:
            return None
        fname = f"MOJ-{slug}-{suffix}"
        return str(MOJ_RE.relative_to(REPO_ROOT)), fname

    # ── 9. العمليات العقارية المسجلة (monthly aggregate — no sub) ───
    #    Pattern: "العمليات العقارية المسجلة   YYYY شهر"  (note extra spaces)
    if re.match(r"^العمليات العقارية المسجلة\s+\d{4}", t):
        if not year or not month:
            return None
        fname = f"MOJ-Monthly-Operations-{year}-{month}"
        return str(MOJ_MONTHLY.relative_to(REPO_ROOT)), fname

    # ── 10. العمليات العقارية المسجلة في {category} (quarterly) ─────
    if t.startswith("العمليات العقارية المسجلة في"):
        sub_part = t[len("العمليات العقارية المسجلة في") :].strip()
        # Strip year + quarter from sub_part to get category text
        sub_clean = re.sub(r"\s+\d{4}.*$", "", sub_part).strip()

        # Try longest-match first (dict insertion order is preserved in 3.7+,
        # but some entries need priority — handle by trying all and picking longest key match)
        best_key: str | None = None
        best_slug: str | None = None
        for ar_key, slug in CATEGORY_MAP.items():
            if ar_key in sub_clean and (
                best_key is None or len(ar_key) > len(best_key)
            ):
                best_key = ar_key
                best_slug = slug

        if best_slug is None:
            # Unknown category — use a sanitised slug from the Arabic text
            safe = re.sub(r"[^\w\u0600-\u06FF]", "-", sub_clean).strip("-")
            best_slug = f"Unknown-{safe[:40]}"
            log.warning("Unknown RE category, using slug '%s' for: %s", best_slug, t)

        if not year:
            return None
        if quarter:
            suffix = f"{year}-{quarter}"
            if part:
                suffix += part
        elif month:
            suffix = f"{year}-{month}"
        else:
            return None
        fname = f"MOJ-{best_slug}-{suffix}"
        return str(MOJ_RE.relative_to(REPO_ROOT)), fname

    # ── 11. العمليات العقارية المسجلة (quarterly aggregate) ──────────
    #    Pattern: "العمليات العقارية المسجلة YYYY الربع N"
    if t.startswith("العمليات العقارية المسجلة"):
        if not year or not quarter:
            return None
        fname = f"MOJ-RE-Operations-{year}-{quarter}"
        return str(MOJ_RE.relative_to(REPO_ROOT)), fname

    return None


# ── State DB helpers ──────────────────────────────────────────────────


def load_moj_datasets(conn: sqlite3.Connection) -> list[dict]:
    """Return all MOJ RE-related datasets with their CSV resource IDs."""
    rows = conn.execute("""
        SELECT
            d.dataset_id,
            d.title_ar,
            r.resource_id,
            r.format
        FROM known_datasets d
        LEFT JOIN known_resources r
            ON r.dataset_id = d.dataset_id
        WHERE d.source = 'MOJ'
        ORDER BY d.title_ar
    """).fetchall()

    # Group by dataset_id, prefer CSV resource
    datasets: dict[str, dict] = {}
    for ds_id, title_ar, res_id, fmt in rows:
        if ds_id not in datasets:
            datasets[ds_id] = {
                "dataset_id": ds_id,
                "title_ar": title_ar,
                "csv_resource_id": None,
            }
        if fmt and fmt.upper() == "CSV" and res_id:
            datasets[ds_id]["csv_resource_id"] = res_id

    return list(datasets.values())


def fetch_resources_from_api(dataset_id: str) -> str | None:
    """Try to fetch the CSV resource_id directly from the portal API."""
    url = f"{RESOURCES_API}?version=-1&dataset={dataset_id}"
    result = fetch_json(url)
    if result is None:
        return None
    resources = result if isinstance(result, list) else result.get("resources", [])
    for res in resources:
        fmt = res.get("format", "")
        res_id = res.get("id", res.get("resourceId", ""))
        if fmt and fmt.upper() == "CSV" and res_id:
            return res_id
    return None


# ── Download ──────────────────────────────────────────────────────────


def _is_waf_block(data: bytes) -> bool:
    """Detect WAF/error page responses disguised as downloads."""
    if len(data) < 1000 and b"Request Rejected" in data:
        return True
    if len(data) < 500 and b"<html" in data.lower():
        return True
    return False


def download_file(resource_id: str, dest_path: Path, dry_run: bool = False) -> str:
    """
    Download a CSV resource to dest_path.
    Returns "ok", "waf" (WAF block), or "fail" (network error).
    """
    url = f"{DOWNLOAD_BASE}/{resource_id}"
    if dry_run:
        log.info("  [DRY-RUN] would download: %s -> %s", url, dest_path)
        return "ok"

    log.info("  Downloading %s -> %s", url, dest_path.name)
    data = fetch_url(url)
    if data is None:
        log.error("  Download failed for resource %s", resource_id)
        return "fail"

    if _is_waf_block(data):
        log.warning("  WAF BLOCK detected for %s (%d bytes)", dest_path.name, len(data))
        return "waf"

    # Ensure UTF-8 BOM for consistency with existing repo data
    if not data.startswith(b"\xef\xbb\xbf"):
        data = b"\xef\xbb\xbf" + data

    dest_path.parent.mkdir(parents=True, exist_ok=True)
    dest_path.write_bytes(data)
    log.info("  Saved %d bytes to %s", len(data), dest_path)
    return "ok"


# ── Main logic ────────────────────────────────────────────────────────


def run(dry_run: bool = False, verbose: bool = False) -> int:
    if verbose:
        log.setLevel(logging.DEBUG)

    if not STATE_DB.exists():
        log.error("State DB not found: %s", STATE_DB)
        return 1

    conn = sqlite3.connect(str(STATE_DB))
    datasets = load_moj_datasets(conn)
    conn.close()

    log.info("Loaded %d MOJ datasets from state DB", len(datasets))

    stats = {
        "downloaded": 0,
        "already_exists": 0,
        "skipped_no_csv": 0,
        "skipped_unrecognised": 0,
        "waf_blocked": 0,
        "failed": 0,
    }
    consecutive_waf = 0

    for ds in datasets:
        title_ar = ds["title_ar"]
        ds_id = ds["dataset_id"]
        res_id = ds["csv_resource_id"]

        # Parse title into path + filename
        parsed = parse_dataset(title_ar)
        if parsed is None:
            log.debug("Skipping unrecognised dataset: %s", title_ar)
            stats["skipped_unrecognised"] += 1
            continue

        rel_dir, base_name = parsed
        dest_path = REPO_ROOT / rel_dir / f"{base_name}.csv"

        # Already on disk?
        if dest_path.exists():
            log.debug("Already exists: %s", dest_path.relative_to(REPO_ROOT))
            stats["already_exists"] += 1
            continue

        # No CSV resource in DB — try live API
        if res_id is None:
            log.info("No CSV resource in DB for '%s', querying API...", title_ar)
            res_id = fetch_resources_from_api(ds_id)
            time.sleep(DOWNLOAD_DELAY)
            if res_id is None:
                log.warning("No CSV resource found for: %s", title_ar)
                stats["skipped_no_csv"] += 1
                continue

        log.info("NEW: %s -> %s", title_ar, dest_path.relative_to(REPO_ROOT))
        result = download_file(res_id, dest_path, dry_run=dry_run)

        if result == "ok":
            stats["downloaded"] += 1
            consecutive_waf = 0
        elif result == "waf":
            stats["waf_blocked"] += 1
            consecutive_waf += 1
            if consecutive_waf >= MAX_CONSECUTIVE_WAF:
                log.error(
                    "WAF blocked %d consecutive downloads — stopping. "
                    "Try again later or run from a different IP (mr-ed).",
                    consecutive_waf,
                )
                break
            log.info("  Backing off %ds after WAF block...", int(WAF_BACKOFF))
            time.sleep(WAF_BACKOFF)
            continue  # skip the normal delay
        else:
            stats["failed"] += 1
            consecutive_waf = 0

        if not dry_run:
            time.sleep(DOWNLOAD_DELAY)

    # Summary
    print()
    print("=" * 55)
    print("Download summary")
    print("=" * 55)
    print(f"  Downloaded:          {stats['downloaded']}")
    print(f"  Already on disk:     {stats['already_exists']}")
    print(f"  WAF blocked:         {stats['waf_blocked']}")
    print(f"  Skipped (no CSV):    {stats['skipped_no_csv']}")
    print(f"  Skipped (unrecognised): {stats['skipped_unrecognised']}")
    print(f"  Failed:              {stats['failed']}")
    print("=" * 55)

    return 0 if stats["failed"] == 0 else 1


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Download new MOJ datasets from the Saudi Open Data portal."
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="List what would be downloaded without actually downloading.",
    )
    parser.add_argument(
        "--verbose",
        action="store_true",
        help="Show DEBUG-level output including already-exists entries.",
    )
    args = parser.parse_args()

    if args.dry_run:
        print("[DRY-RUN mode — no files will be written]\n")

    return run(dry_run=args.dry_run, verbose=args.verbose)


if __name__ == "__main__":
    sys.exit(main())
