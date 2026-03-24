#!/usr/bin/env python3
"""
REGA/MOJ Data Registry Builder

Scans all CSVs in ~/rega-data/, introspects their structure, and builds
a self-describing SQLite registry database at ~/rega-data/registry.db.

No external dependencies — stdlib only.
"""

from __future__ import annotations

import csv
import json
import os
import re
import sqlite3
from collections import Counter
from pathlib import Path

BASE_DIR = Path(__file__).parent.resolve()
DB_PATH = BASE_DIR / "registry.db"

# How many rows to sample for type inference
SAMPLE_ROWS = 1000
# Max distinct values to treat a column as enum
ENUM_THRESHOLD = 50
# Sample values per field
SAMPLE_VALUES_COUNT = 5
# Raw sample rows per file
RAW_SAMPLE_COUNT = 10

# ── File classification rules ────────────────────────────────────────

CLASSIFICATION_RULES = [
    # (regex_pattern, source, category)
    # MOJ Sales
    (r"MOJ-Sales-\d{4}-Q\d\.csv", "MOJ", "sales"),
    # MOJ Index (pivot tables)
    (r"MOJ-RE-Index-.*\.csv", "MOJ", "index"),
    # MOJ RealEstate categories — order matters (longer patterns first)
    (r"MOJ-Release-Seizure-.*\.csv", "MOJ", "release_seizure"),
    (r"MOJ-Seizure-.*\.csv", "MOJ", "seizure"),
    (r"MOJ-Deed-Define-Divide-.*\.csv", "MOJ", "deed_define_divide"),
    (r"MOJ-Transfers-.*\.csv", "MOJ", "transfer"),
    (r"MOJ-POA-RE-Fund-.*\.csv", "MOJ", "poa_fund"),
    (r"MOJ-POA-RealEstate-.*\.csv", "MOJ", "poa"),
    (r"MOJ-Mortgage-Release-.*\.csv", "MOJ", "mortgage_release"),
    (r"MOJ-Mortgage-.*\.csv", "MOJ", "mortgage"),
    (r"MOJ-Physical-Registration-.*\.csv", "MOJ", "physical_reg"),
    (r"MOJ-Register-Old-Deed-.*\.csv", "MOJ", "register_old_deed"),
    (r"MOJ-Register-No-Deed-.*\.csv", "MOJ", "register_no_deed"),
    (r"MOJ-Divide-.*\.csv", "MOJ", "division"),
    (r"MOJ-Merge-RE-.*\.csv", "MOJ", "merge_re"),
    (r"MOJ-Merge-Deed-.*\.csv", "MOJ", "merge_deed"),
    (r"MOJ-Enforcement-Sale-.*\.csv", "MOJ", "enforcement"),
    (r"MOJ-Update-Old-Deed-.*\.csv", "MOJ", "update_old_deed"),
    (r"MOJ-Update-Deed-.*\.csv", "MOJ", "update_deed"),
    (r"MOJ-Property-Identity-.*\.csv", "MOJ", "property_identity"),
    (r"MOJ-Ownership-Men-.*\.csv", "MOJ", "ownership_men"),
    (r"MOJ-Ownership-.*\.csv", "MOJ", "ownership"),
    (r"MOJ-RE-Operations-.*\.csv", "MOJ", "operations"),
    # REGA
    (r"Sales-transaction-indicators-.*\.csv", "REGA", "sales_indicators"),
    (r"Rental-indicators-.*\.csv", "REGA", "rental_indicators"),
    (r"quarter-report-SI\.csv", "REGA", "consolidated"),
    (r"Registered-Real-Estate-.*\.csv", "REGA", "gender_stats"),
]

# ── Arabic → canonical English mapping ───────────────────────────────

ARABIC_TO_CANONICAL = {
    "المنطقة": "region",
    "المدينة": "city",
    "المدينة / الحي": "city_district",
    "الحي": "district",
    "الرقم المرجعي للصفقة": "transaction_ref",
    "الرقم المرجعي": "reference_number",
    "تاريخ الصفقة ميلادي": "date_gregorian",
    "تاريخ الصفقة هجري": "date_hijri",
    "التاريخ ميلادي": "date_gregorian",
    "التاريخ هجري": "date_hijri",
    "تاريخ القرار ميلادي": "decision_date_gregorian",
    "تاريخ القرارهجري": "decision_date_hijri",
    "تصنيف العقار": "property_classification",
    "نوع العقار": "property_type",
    "عدد العقارات": "property_count",
    "السعر": "price",
    "المساحة": "area",
    "المساحة M2": "area_m2",
    "نوع القطاع": "sector_type",
    "نوع الخدمة": "service_type",
    "نوع العملية": "operation_type",
    "عدد العمليات": "operation_count",
    "نوع السند الرئيسي": "main_document_type",
    "السنة": "year",
    "الربع": "quarter",
    "ربع السنة": "quarter",
    "عدد الصكوك": "deed_count",
    "قيمة الصفقات": "transaction_value",
    "متوسط سعر المتر": "avg_price_per_m2",
    "الحد الأعلى لسعر المتر": "max_price_per_m2",
    "الحد الأدنى لسعر المتر": "min_price_per_m2",
    "مجموع الصفقات": "total_transactions",
    "المتوسط": "average",
    "الشهر": "month",
    "عدد الملاك النساء": "female_owner_count",
    "نسبة تملك النساء": "female_ownership_rate",
    # English headers from quarter-report-SI.csv
    "yearnumber": "year",
    "quarternumber": "quarter_number",
    "quarternamear": "quarter_name_ar",
    "quarterid": "quarter_id",
    "region_ar": "region",
    "city_ar": "city",
    "district_ar": "district",
    "typecategoryar": "property_classification",
    "deed_counts": "deed_count",
    "RealEstatePrice_SUM": "total_price",
    "Meter_Price_W_Avg_IQR": "weighted_avg_price_per_m2",
    # Gender stats
    "Gender": "gender",
    "RENs": "registered_count",
    "Created Date": "created_date",
}


def classify_file(filename: str) -> tuple[str, str]:
    """Return (source, category) for a CSV filename."""
    for pattern, source, category in CLASSIFICATION_RULES:
        if re.match(pattern, filename):
            return source, category
    return "UNKNOWN", "unknown"


def detect_encoding(filepath: Path) -> tuple[str, bool]:
    """Check for UTF-8 BOM. Returns (encoding, has_bom)."""
    with open(filepath, "rb") as f:
        head = f.read(3)
    if head == b"\xef\xbb\xbf":
        return "utf-8-sig", True
    return "utf-8", False


def clean_value(val: str) -> str:
    """Strip whitespace and BOM artifacts from a value."""
    return val.strip().lstrip("\ufeff")


def clean_header(header: str) -> str:
    """Clean a header name — strip BOM, whitespace, invisible chars."""
    h = header.strip().lstrip("\ufeff")
    # Remove zero-width chars
    h = re.sub(r"[\u200b\u200c\u200d\u200e\u200f\ufeff]", "", h)
    return h


def parse_numeric(val: str) -> float | None:
    """Try to parse a string as a number, handling commas and percentages."""
    if not val or val.upper() == "NULL":
        return None
    # Strip quotes, commas, percentage signs
    cleaned = val.strip().strip('"').replace(",", "")
    if cleaned.endswith("%"):
        cleaned = cleaned[:-1]
    try:
        return float(cleaned)
    except ValueError:
        return None


def infer_type(values: list[str]) -> str:
    """Infer data type from a sample of non-null string values.

    Returns one of: 'integer', 'decimal', 'date', 'text'
    """
    if not values:
        return "text"

    date_patterns = [
        re.compile(r"^\d{4}/\d{1,2}/\d{1,2}$"),  # YYYY/MM/DD
        re.compile(r"^\d{1,2}/\d{1,2}/\d{4}$"),  # M/D/YYYY
    ]

    int_count = 0
    float_count = 0
    date_count = 0
    total = len(values)

    for v in values:
        stripped = v.strip().strip('"').replace(",", "")

        # Check date
        if any(p.match(stripped) for p in date_patterns):
            date_count += 1
            continue

        # Check percentage
        pct = stripped
        if pct.endswith("%"):
            pct = pct[:-1]

        try:
            f = float(pct)
            if "." in pct or stripped.endswith("%"):
                float_count += 1
            else:
                int_count += 1
        except ValueError:
            pass

    threshold = 0.8 * total
    if date_count >= threshold:
        return "date"
    if int_count >= threshold:
        return "integer"
    if (int_count + float_count) >= threshold:
        return "decimal"
    return "text"


def extract_date_range(values: list[str]) -> tuple[str | None, str | None]:
    """Extract min/max date strings from a list of date-like values."""
    dates = []
    for v in values:
        v = v.strip().strip('"')
        # Normalize to YYYY/MM/DD for sorting
        m = re.match(r"^(\d{4})/(\d{1,2})/(\d{1,2})$", v)
        if m:
            dates.append(
                (v, f"{m.group(1)}/{int(m.group(2)):02d}/{int(m.group(3)):02d}")
            )
            continue
        m = re.match(r"^(\d{1,2})/(\d{1,2})/(\d{4})$", v)
        if m:
            norm = f"{m.group(3)}/{int(m.group(1)):02d}/{int(m.group(2)):02d}"
            dates.append((v, norm))

    if not dates:
        return None, None

    dates.sort(key=lambda x: x[1])
    return dates[0][0], dates[-1][0]


def get_region_column_idx(headers: list[str]) -> int | None:
    """Find the index of a region column."""
    region_names = {"المنطقة", "region_ar"}
    for i, h in enumerate(headers):
        if clean_header(h) in region_names:
            return i
    return None


def get_date_column_idx(headers: list[str]) -> int | None:
    """Find the index of a Gregorian date column."""
    date_keys = {
        "تاريخ الصفقة ميلادي",
        "التاريخ ميلادي",
        "تاريخ القرار ميلادي",
    }
    for i, h in enumerate(headers):
        if clean_header(h) in date_keys:
            return i
    return None


def discover_csvs() -> list[Path]:
    """Find all CSV files under BASE_DIR."""
    csvs = []
    for root, dirs, files in os.walk(BASE_DIR):
        # Skip hidden dirs and charts
        dirs[:] = [d for d in dirs if not d.startswith(".") and d != "charts"]
        for f in files:
            if f.lower().endswith(".csv"):
                csvs.append(Path(root) / f)
    csvs.sort(key=lambda p: p.name)
    return csvs


def create_schema(conn: sqlite3.Connection):
    """Create all registry tables."""
    conn.executescript("""
        CREATE TABLE IF NOT EXISTS files (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            source TEXT NOT NULL,
            category TEXT NOT NULL,
            filename TEXT NOT NULL,
            path TEXT NOT NULL,
            file_size INTEGER,
            row_count INTEGER,
            col_count INTEGER,
            encoding TEXT,
            has_bom INTEGER,
            date_range_start TEXT,
            date_range_end TEXT,
            region_coverage TEXT,
            notes TEXT
        );

        CREATE TABLE IF NOT EXISTS fields (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            file_id INTEGER NOT NULL REFERENCES files(id),
            ordinal INTEGER NOT NULL,
            name_ar TEXT,
            name_en TEXT,
            canonical_name TEXT,
            data_type TEXT,
            nullable INTEGER,
            null_count INTEGER,
            distinct_count INTEGER,
            min_value TEXT,
            max_value TEXT,
            sample_values TEXT,
            formatting_notes TEXT
        );

        CREATE TABLE IF NOT EXISTS enum_values (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            field_id INTEGER NOT NULL REFERENCES fields(id),
            value TEXT,
            count INTEGER,
            percentage REAL
        );

        CREATE TABLE IF NOT EXISTS samples (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            file_id INTEGER NOT NULL REFERENCES files(id),
            row_number INTEGER NOT NULL,
            raw_line TEXT,
            parsed_json TEXT
        );

        CREATE TABLE IF NOT EXISTS field_aliases (
            canonical_name TEXT NOT NULL,
            name_ar TEXT NOT NULL,
            source TEXT NOT NULL,
            file_count INTEGER DEFAULT 1
        );
    """)


def process_file(filepath: Path, conn: sqlite3.Connection):
    """Process a single CSV file and insert into registry."""
    filename = filepath.name
    rel_path = str(filepath.relative_to(BASE_DIR))
    source, category = classify_file(filename)
    encoding, has_bom = detect_encoding(filepath)
    file_size = filepath.stat().st_size

    print(f"  {rel_path} [{source}/{category}]", end="", flush=True)

    # Read all raw lines for sampling
    with open(filepath, "r", encoding=encoding, newline="") as f:
        raw_lines = f.readlines()

    if not raw_lines:
        print(" (empty)")
        return

    # Parse CSV
    with open(filepath, "r", encoding=encoding, newline="") as f:
        reader = csv.reader(f)
        try:
            raw_headers = next(reader)
        except StopIteration:
            print(" (no headers)")
            return

        headers = [clean_header(h) for h in raw_headers]
        col_count = len(headers)

        # Read all rows (we need full counts)
        rows = []
        for row in reader:
            if row and any(c.strip() for c in row):  # skip blank rows
                rows.append(row)

    row_count = len(rows)

    # Detect notes about the file
    notes_parts = []
    if category == "index":
        notes_parts.append("pivot-table export with multi-row headers")

    # Per-column analysis
    col_data: list[dict] = []
    region_idx = get_region_column_idx(headers)
    date_idx = get_date_column_idx(headers)
    regions: set[str] = set()
    date_values: list[str] = []

    for col_idx in range(col_count):
        values = []
        null_count = 0
        formatting_notes: list[str] = []

        for row in rows:
            if col_idx < len(row):
                v = row[col_idx].strip()
                if not v or v.upper() == "NULL":
                    null_count += 1
                else:
                    values.append(v)
                    # Track regions
                    if col_idx == region_idx:
                        regions.add(v.strip())
                    # Track dates
                    if col_idx == date_idx:
                        date_values.append(v)
            else:
                null_count += 1

        # Detect formatting quirks
        has_quoted_commas = any('"' in v and "," in v.strip('"') for v in values[:200])
        has_null_literal = any(
            row[col_idx].strip().upper() == "NULL"
            for row in rows[:200]
            if col_idx < len(row) and row[col_idx].strip()
        )
        has_pct = any(v.endswith("%") for v in values[:200])

        if has_quoted_commas:
            formatting_notes.append("quoted_commas")
        if has_null_literal:
            formatting_notes.append("NULL_literal")
        if has_pct:
            formatting_notes.append("percentage_strings")

        # Distinct values (sample first SAMPLE_ROWS for performance)
        sample_slice = values[:SAMPLE_ROWS] if len(values) > SAMPLE_ROWS else values
        counter = Counter(sample_slice)
        distinct_count = len(set(values))

        # Type inference
        data_type = infer_type(sample_slice)

        # If enum check
        is_enum = (
            distinct_count <= ENUM_THRESHOLD
            and distinct_count > 0
            and data_type == "text"
        )

        # Min/max for numerics
        min_val = None
        max_val = None
        if data_type in ("integer", "decimal"):
            nums = [parse_numeric(v) for v in values]
            nums = [n for n in nums if n is not None]
            if nums:
                min_val = str(min(nums))
                max_val = str(max(nums))
        elif data_type == "date":
            d_start, d_end = extract_date_range(values)
            min_val = d_start
            max_val = d_end

        # Sample values (5 distinct)
        distinct_vals = list(dict.fromkeys(values))  # preserves order, deduplicates
        sample_vals = distinct_vals[:SAMPLE_VALUES_COUNT]

        # Canonical name
        header_name = headers[col_idx]
        canonical = ARABIC_TO_CANONICAL.get(header_name)

        col_data.append(
            {
                "ordinal": col_idx,
                "name_ar": header_name,
                "canonical_name": canonical,
                "data_type": data_type,
                "nullable": 1 if null_count > 0 else 0,
                "null_count": null_count,
                "distinct_count": distinct_count,
                "min_value": min_val,
                "max_value": max_val,
                "sample_values": json.dumps(sample_vals, ensure_ascii=False),
                "formatting_notes": ", ".join(formatting_notes)
                if formatting_notes
                else None,
                "is_enum": is_enum,
                "enum_counter": Counter(values) if is_enum else None,
            }
        )

    # Date range from date column
    date_start = None
    date_end = None
    if date_values:
        date_start, date_end = extract_date_range(date_values)
    # Fallback: try year column for REGA files
    if not date_start:
        for cd in col_data:
            if cd["canonical_name"] == "year" and cd["data_type"] in (
                "integer",
                "text",
            ):
                # Already have min/max
                date_start = cd["min_value"]
                date_end = cd["max_value"]
                break

    # Region coverage
    region_coverage = (
        json.dumps(sorted(regions), ensure_ascii=False) if regions else None
    )

    notes = "; ".join(notes_parts) if notes_parts else None

    # ── Insert file record ──
    cur = conn.execute(
        """
        INSERT INTO files (source, category, filename, path, file_size,
            row_count, col_count, encoding, has_bom,
            date_range_start, date_range_end, region_coverage, notes)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """,
        (
            source,
            category,
            filename,
            rel_path,
            file_size,
            row_count,
            col_count,
            encoding,
            int(has_bom),
            date_start,
            date_end,
            region_coverage,
            notes,
        ),
    )
    file_id = cur.lastrowid

    # ── Insert fields ──
    for cd in col_data:
        cur = conn.execute(
            """
            INSERT INTO fields (file_id, ordinal, name_ar, name_en,
                canonical_name, data_type, nullable, null_count,
                distinct_count, min_value, max_value, sample_values,
                formatting_notes)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """,
            (
                file_id,
                cd["ordinal"],
                cd["name_ar"],
                None,
                cd["canonical_name"],
                cd["data_type"],
                cd["nullable"],
                cd["null_count"],
                cd["distinct_count"],
                cd["min_value"],
                cd["max_value"],
                cd["sample_values"],
                cd["formatting_notes"],
            ),
        )
        field_id = cur.lastrowid

        # Enum values
        if cd["is_enum"] and cd["enum_counter"]:
            total = sum(cd["enum_counter"].values())
            for val, count in cd["enum_counter"].most_common():
                pct = round(count / total * 100, 2) if total else 0
                conn.execute(
                    """
                    INSERT INTO enum_values (field_id, value, count, percentage)
                    VALUES (?, ?, ?, ?)
                """,
                    (field_id, val, count, pct),
                )

    # ── Insert raw samples ──
    sample_indices = list(range(min(RAW_SAMPLE_COUNT, len(rows))))
    for idx in sample_indices:
        row = rows[idx]
        # Raw CSV line (from raw_lines, offset +1 for header)
        raw_idx = idx + 1  # skip header line
        raw_line = raw_lines[raw_idx].rstrip("\r\n") if raw_idx < len(raw_lines) else ""

        parsed = {}
        for col_idx, header in enumerate(headers):
            if col_idx < len(row):
                parsed[header] = row[col_idx].strip()
            else:
                parsed[header] = None

        conn.execute(
            """
            INSERT INTO samples (file_id, row_number, raw_line, parsed_json)
            VALUES (?, ?, ?, ?)
        """,
            (file_id, idx + 1, raw_line, json.dumps(parsed, ensure_ascii=False)),
        )

    print(f"  ({row_count} rows, {col_count} cols)")


def build_field_aliases(conn: sqlite3.Connection):
    """Build the field_aliases table grouping same-concept fields across files."""
    conn.execute("DELETE FROM field_aliases")

    rows = conn.execute("""
        SELECT f.canonical_name, f.name_ar, fi.source, COUNT(DISTINCT fi.id) as file_count
        FROM fields f
        JOIN files fi ON f.file_id = fi.id
        WHERE f.canonical_name IS NOT NULL
        GROUP BY f.canonical_name, f.name_ar, fi.source
        ORDER BY f.canonical_name, file_count DESC
    """).fetchall()

    for canonical, name_ar, source, file_count in rows:
        conn.execute(
            """
            INSERT INTO field_aliases (canonical_name, name_ar, source, file_count)
            VALUES (?, ?, ?, ?)
        """,
            (canonical, name_ar, source, file_count),
        )


def print_summary(conn: sqlite3.Connection):
    """Print a summary of the built registry."""
    file_count = conn.execute("SELECT COUNT(*) FROM files").fetchone()[0]
    field_count = conn.execute("SELECT COUNT(*) FROM fields").fetchone()[0]
    sample_count = conn.execute("SELECT COUNT(*) FROM samples").fetchone()[0]
    enum_count = conn.execute("SELECT COUNT(*) FROM enum_values").fetchone()[0]
    alias_count = conn.execute(
        "SELECT COUNT(DISTINCT canonical_name) FROM field_aliases"
    ).fetchone()[0]

    total_rows = conn.execute("SELECT SUM(row_count) FROM files").fetchone()[0] or 0

    print("\n" + "=" * 60)
    print("REGISTRY SUMMARY")
    print("=" * 60)
    print(f"  Files cataloged:     {file_count}")
    print(f"  Total data rows:     {total_rows:,}")
    print(f"  Fields cataloged:    {field_count}")
    print(f"  Enum values stored:  {enum_count}")
    print(f"  Sample rows stored:  {sample_count}")
    print(f"  Canonical fields:    {alias_count}")
    print()

    # By source/category
    print("FILES BY SOURCE/CATEGORY:")
    for source, category, cnt, rows in conn.execute("""
        SELECT source, category, COUNT(*), SUM(row_count)
        FROM files GROUP BY source, category ORDER BY source, category
    """):
        print(f"  {source}/{category}: {cnt} files, {rows:,} rows")

    # Top canonical fields
    print("\nTOP CANONICAL FIELDS (by file coverage):")
    for canonical, fc in conn.execute("""
        SELECT canonical_name, SUM(file_count)
        FROM field_aliases
        GROUP BY canonical_name
        ORDER BY SUM(file_count) DESC
        LIMIT 10
    """):
        print(f"  {canonical}: {fc} files")

    print(f"\nDatabase: {DB_PATH}")
    print(f"Size: {DB_PATH.stat().st_size / 1024:.0f} KB")


def main():
    print("REGA/MOJ Data Registry Builder")
    print(f"Scanning: {BASE_DIR}")
    print()

    # Discover CSVs
    csvs = discover_csvs()
    print(f"Found {len(csvs)} CSV files\n")

    # Remove old DB
    if DB_PATH.exists():
        DB_PATH.unlink()

    conn = sqlite3.connect(str(DB_PATH))
    conn.execute("PRAGMA journal_mode=WAL")
    conn.execute("PRAGMA synchronous=NORMAL")

    create_schema(conn)

    # Process each file
    print("Processing files:")
    for csv_path in csvs:
        try:
            process_file(csv_path, conn)
            conn.commit()
        except Exception as e:
            print(f"  ERROR: {e}")
            import traceback

            traceback.print_exc()

    # Build cross-file aliases
    print("\nBuilding field aliases...")
    build_field_aliases(conn)
    conn.commit()

    # Create indexes
    print("Creating indexes...")
    conn.executescript("""
        CREATE INDEX IF NOT EXISTS idx_fields_file_id ON fields(file_id);
        CREATE INDEX IF NOT EXISTS idx_fields_canonical ON fields(canonical_name);
        CREATE INDEX IF NOT EXISTS idx_enum_field_id ON enum_values(field_id);
        CREATE INDEX IF NOT EXISTS idx_samples_file_id ON samples(file_id);
        CREATE INDEX IF NOT EXISTS idx_aliases_canonical ON field_aliases(canonical_name);
        CREATE INDEX IF NOT EXISTS idx_files_source_cat ON files(source, category);
    """)
    conn.commit()

    print_summary(conn)
    conn.close()


if __name__ == "__main__":
    main()
