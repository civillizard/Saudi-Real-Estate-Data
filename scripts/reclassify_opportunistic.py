#!/usr/bin/env python3
"""Reclassify moj/opportunistic/ into proper English-slug taxonomy.

Moves files from moj/opportunistic/ into:
  - moj/poa-other/       Non-RE POA quarterly sub-categories
  - moj/monthly/         Annulled POA monthly files
  - rega/                REGA regional sales + rental indicators

Uses git mv so the rename is tracked. Run with --dry-run first.
"""

from __future__ import annotations

import argparse
import logging
import re
import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).parent.parent.resolve()
OPPORTUNISTIC = REPO_ROOT / "moj" / "opportunistic"
POA_OTHER = REPO_ROOT / "moj" / "poa-other"
MOJ_MONTHLY = REPO_ROOT / "moj" / "monthly"
REGA_DIR = REPO_ROOT / "rega"

logging.basicConfig(format="%(levelname)s: %(message)s", level=logging.INFO)
log = logging.getLogger("reclassify")

# ── Arabic → English slug maps ────────────────────────────────────────

POA_SUB_MAP = {
    "المرور": "Traffic",
    "البريد": "Post",
    "البنوك-والمصارف": "Banks",
    "السجلات-التجارية": "Commercial-Records",
    "الشركات": "Companies",
    "المؤسسات-الحكومية": "Gov-Institutions",
    "المطالبات-و-المحاكم": "Claims-Courts",
    "المطالبات-والمحاكم": "Claims-Courts",
    "المنح-السكنية": "Housing-Grants",
    "الهيئات-الحكومية": "Gov-Authorities",
    "بنك-التنمية-الاجتماعية": "Social-Dev-Bank",
    "تصديق-الوكالات-الخارجية": "Foreign-POA-Attest",
    "إدارة-الأحوال-المدنية": "Civil-Affairs",
    "إنهائات-المحاكم": "Court-Completions",
    "استقدام-العمالة": "Labor-Recruitment",
    "الأمانات-والبلديات": "Municipalities",
    "التعويضات-والمساعدات": "Compensation-Aid",
    "الرواتب-والمستحقات": "Salaries-Dues",
    "السيارات": "Vehicles",
    "الضمان-الاجتماعي": "Social-Security",
    "المنح-الزراعية": "Agricultural-Grants",
    "تصاريح-القوارب-والصيد": "Boat-Fishing-Licenses",
    "شركات-الاتصالات": "Telecom-Companies",
    "صندوق-التنمية-الزراعية": "Agricultural-Dev-Fund",
    "طلب-الخدمات": "Service-Requests",
    "مكافآت-الجامعات-والمعاهد": "University-Rewards",
    "مكتب-الإستقدام": "Recruitment-Office",
}

MONTH_MAP = {
    "يناير": "01",
    "فبراير": "02",
    "مارس": "03",
    "أبريل": "04",
    "ابريل": "04",
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

QUARTER_MAP = {
    "الربع-الأول": "Q1",
    "الربع-الاول": "Q1",
    "الربع-الثاني": "Q2",
    "الربع-الثالث": "Q3",
    "الربع-الرابع": "Q4",
    "الربع-الثاني-الجزء-2": "Q2-Part2",
    "الربع-الثاني-الجزء2": "Q2-Part2",
}

REGION_MAP = {
    "الشرقية": "Eastern",
    "الباحة": "Albaha",
    "الرياض": "Riyadh",
    "حائل": "Hail",
    "المدينة-المنورة": "Madinah",
    "مكة-المكرمة": "Makkah",
}


def _extract_year(stem: str) -> str | None:
    m = re.search(r"(20\d{2})", stem)
    return m.group(1) if m else None


def _extract_quarter(stem: str) -> str | None:
    for ar, en in QUARTER_MAP.items():
        if ar in stem:
            return en
    return None


def _extract_month(stem: str) -> str | None:
    for ar, mm in MONTH_MAP.items():
        if ar in stem:
            return mm
    return None


def _extract_region(stem: str) -> str | None:
    for ar, en in REGION_MAP.items():
        if ar in stem:
            return en
    return None


def classify(stem: str) -> tuple[Path | None, str | None]:
    """Return (dest_dir, new_stem) or (None, reason_skipped)."""
    year = _extract_year(stem)

    # ── POA annulled monthly ──────────────────────────────────────
    if stem.startswith("الوكالات-المفسوخة-"):
        month = _extract_month(stem)
        if not year or not month:
            return (None, f"POA-annulled missing year/month: {stem}")
        return (MOJ_MONTHLY, f"MOJ-POA-Annulled-{year}-{month}")

    # ── POA quarterly sub-categories ─────────────────────────────
    if stem.startswith("الوكالات-الصادرة-في-"):
        quarter = _extract_quarter(stem)
        if not year or not quarter:
            return (None, f"POA-sub missing year/quarter: {stem}")
        # Strip prefix + year+quarter suffix to isolate the sub-category
        body = stem[len("الوكالات-الصادرة-في-") :]
        body = re.sub(r"-20\d{2}.*$", "", body)
        slug = POA_SUB_MAP.get(body)
        if not slug:
            return (None, f"POA sub not in map: '{body}'")
        return (POA_OTHER, f"MOJ-POA-{slug}-{year}-{quarter}")

    # ── REGA sales indicators (new naming: مؤشرات-صفقات-البيع) ──
    if stem.startswith("مؤشرات-صفقات-البيع"):
        region = _extract_region(stem)
        quarter = _extract_quarter(stem)
        if not region or not year or not quarter:
            return (None, f"REGA-sales missing region/year/quarter: {stem}")
        return (REGA_DIR, f"REGA-Sales-Indicators-{region}-{year}-{quarter}")

    # ── REGA sales indicators (old naming: مؤشرات-البيع-لمنطقة) ──
    if stem.startswith("مؤشرات-البيع-"):
        region = _extract_region(stem)
        quarter = _extract_quarter(stem)
        if not region or not year or not quarter:
            return (None, f"REGA-sales(old) missing region/year/quarter: {stem}")
        return (REGA_DIR, f"REGA-Sales-Indicators-{region}-{year}-{quarter}")

    # ── REGA rental indicators ──────────────────────────────────
    if stem.startswith("مؤشرات-الايجار-"):
        region = _extract_region(stem)
        if not region:
            return (None, f"REGA-rental missing region: {stem}")
        return (REGA_DIR, f"REGA-Rental-Indicators-{region}-Cities")

    return (None, f"unknown pattern: {stem[:80]}")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--no-git", action="store_true", help="plain mv, no git mv")
    args = ap.parse_args()

    if not OPPORTUNISTIC.exists():
        log.error("No opportunistic dir: %s", OPPORTUNISTIC)
        return 1

    files = sorted(OPPORTUNISTIC.iterdir())
    log.info("Found %d files in %s", len(files), OPPORTUNISTIC.relative_to(REPO_ROOT))

    POA_OTHER.mkdir(exist_ok=True)

    moved = 0
    skipped = 0
    conflicts = 0
    by_dest: dict[str, int] = {}

    # Group files by their (dest_dir, new_stem) target so CSV+XLSX siblings
    # share the same stem.
    for src in files:
        # Strip the `__uuid` suffix before classifying
        name = src.name
        if "__" not in name:
            skipped += 1
            log.warning("[skip] no __uuid suffix: %s", name)
            continue
        stem_and_uuid, ext = name.rsplit(".", 1)
        bare_stem = stem_and_uuid.rsplit("__", 1)[0]

        dest_dir, new_stem = classify(bare_stem)
        if dest_dir is None:
            skipped += 1
            log.warning("[skip] %s", new_stem)
            continue

        new_name = f"{new_stem}.{ext}"
        dest = dest_dir / new_name

        if dest.exists():
            conflicts += 1
            log.warning(
                "[conflict] dest exists: %s -> %s",
                src.relative_to(REPO_ROOT),
                dest.relative_to(REPO_ROOT),
            )
            continue

        log.info(
            "  %-12s %s -> %s",
            dest_dir.name,
            src.name[:60],
            dest.relative_to(REPO_ROOT),
        )
        by_dest[str(dest_dir.relative_to(REPO_ROOT))] = (
            by_dest.get(str(dest_dir.relative_to(REPO_ROOT)), 0) + 1
        )

        if args.dry_run:
            continue

        dest_dir.mkdir(parents=True, exist_ok=True)
        if args.no_git:
            src.rename(dest)
        else:
            subprocess.run(
                [
                    "git",
                    "mv",
                    str(src.relative_to(REPO_ROOT)),
                    str(dest.relative_to(REPO_ROOT)),
                ],
                cwd=REPO_ROOT,
                check=True,
            )
        moved += 1

    log.info("=" * 60)
    log.info("Summary:")
    log.info("  moved:     %d", moved)
    log.info("  skipped:   %d", skipped)
    log.info("  conflicts: %d", conflicts)
    log.info("  by dest:   %s", by_dest)
    log.info("=" * 60)

    return 0 if skipped == 0 and conflicts == 0 else 2


if __name__ == "__main__":
    sys.exit(main())
