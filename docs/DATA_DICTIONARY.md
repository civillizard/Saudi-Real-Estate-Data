# Data Dictionary

Machine-readable field catalog for all 159 CSV files. Generated from [`registry.db`](#registry-database) built by [`scripts/build_registry.py`](../scripts/build_registry.py).

For CSV exports of this data, see [`data/registry_files.csv`](../data/registry_files.csv), [`data/registry_fields.csv`](../data/registry_fields.csv), and [`data/registry_enums.csv`](../data/registry_enums.csv).

---

## Table of Contents

- [Canonical Fields](#canonical-fields)
- [Categories](#categories)
  - [MOJ Categories](#moj-categories)
  - [REGA Categories](#rega-categories)
- [Enum Values](#enum-values)
- [Formatting Notes](#formatting-notes)
- [CSV Exports](#csv-exports)
- [Registry Database](#registry-database)

---

## Canonical Fields

41 canonical English field names mapped from Arabic headers. The `Files` column shows how many of the 159 CSVs contain each field.

| Canonical Name | Arabic Header(s) | Type | Files | Description |
|---------------|-------------------|------|-------|-------------|
| `region` | المنطقة / region_ar | text | 155 | Administrative region (13 total) |
| `city` | المدينة / city_ar | text | 155 | City name |
| `date_gregorian` | التاريخ ميلادي / تاريخ الصفقة ميلادي | date | 102 | Gregorian date (`YYYY/MM/DD` or `M/D/YYYY`) |
| `sector_type` | نوع القطاع | text | 79 | Public or private sector (enum) |
| `service_type` | نوع الخدمة | text | 79 | Electronic or partially electronic service (enum) |
| `reference_number` | الرقم المرجعي | integer | 54 | Transaction reference number (operations) |
| `date_hijri` | التاريخ هجري / تاريخ الصفقة هجري | date | 47 | Hijri (Islamic calendar) date |
| `year` | السنة / yearnumber | integer | 46 | Year (in aggregate/indicator files) |
| `property_type` | نوع العقار | text | 45 | Property type: land, apartment, villa, etc. (enum) |
| `quarter` | الربع / ربع السنة | text | 45 | Quarter of the year |
| `property_classification` | تصنيف العقار / typecategoryar | text | 41 | Sector classification: residential, commercial, agricultural, industrial (enum) |
| `district` | الحي / district_ar | text | 33 | Neighborhood / district name |
| `deed_count` | عدد الصكوك / deed_counts | integer | 32 | Number of title deeds |
| `area_m2` | المساحة M2 | decimal | 31 | Area in square meters (REGA indicators) |
| `avg_price_per_m2` | متوسط سعر المتر | decimal | 31 | Average price per m² (REGA indicators) |
| `max_price_per_m2` | الحد الأعلى لسعر المتر | decimal | 31 | Maximum price per m² (REGA indicators) |
| `min_price_per_m2` | الحد الأدنى لسعر المتر | decimal | 31 | Minimum price per m² (REGA indicators) |
| `area` | المساحة | decimal | 24 | Area in m² (MOJ sales — comma-formatted) |
| `operation_count` | عدد العمليات | integer | 24 | Number of operations (monthly aggregates) |
| `operation_type` | نوع العملية | text | 24 | Type of RE operation (monthly aggregates) |
| `property_count` | عدد العقارات | integer | 24 | Number of properties in transaction |
| `city_district` | المدينة / الحي | text | 23 | Combined city/district field (MOJ sales) |
| `price` | السعر | decimal | 23 | Transaction price in SAR (comma-formatted) |
| `transaction_ref` | الرقم المرجعي للصفقة | integer | 23 | Transaction reference (sales) |
| `transaction_value` | قيمة الصفقات | decimal | 15 | Total transaction value (REGA indicators) |
| `average` | المتوسط | decimal | 11 | Average value (REGA rental indicators) |
| `total_transactions` | مجموع الصفقات | integer | 11 | Total transaction count (REGA rental) |
| `decision_date_gregorian` | تاريخ القرار ميلادي | date | 4 | Court decision date (enforcement sales) |
| `main_document_type` | نوع السند الرئيسي | text | 4 | Legal document type (enforcement sales, enum) |
| `female_owner_count` | عدد الملاك النساء | integer | 3 | Female property owner count |
| `female_ownership_rate` | نسبة تملك النساء | decimal | 3 | Female ownership percentage |
| `decision_date_hijri` | تاريخ القرارهجري | date | 1 | Court decision date in Hijri |
| `month` | الشهر | integer | 1 | Month number |
| `quarter_id` | quarterid | integer | 1 | Quarter identifier (consolidated) |
| `quarter_name_ar` | quarternamear | text | 1 | Quarter name in Arabic (consolidated) |
| `quarter_number` | quarternumber | integer | 1 | Quarter number (consolidated) |
| `total_price` | RealEstatePrice_SUM | decimal | 1 | Sum of prices (consolidated) |
| `weighted_avg_price_per_m2` | Meter_Price_W_Avg_IQR | decimal | 1 | Weighted avg price/m² with IQR (consolidated) |
| `gender` | Gender | text | 1 | Gender (gender stats file) |
| `registered_count` | RENs | integer | 1 | Registered entity count (gender stats) |
| `created_date` | Created Date | date | 1 | Record creation date (gender stats) |

---

## Categories

### MOJ Categories

**22 categories, 113 files, 4,856,938 rows**

| Category | Files | Rows | Columns | Date Range | Description |
|----------|-------|------|---------|------------|-------------|
| `sales` | 24 | 1,407,120 | 10–13 | 2020–2025 | Individual sale transactions with price, area, location |
| `seizure` | 3 | 736,808 | 6 | 2025 Q1–Q3 | Court-ordered property freezes |
| `poa` | 3 | 758,003 | 6 | 2025 Q1–Q3 | Real estate power of attorney |
| `release_seizure` | 3 | 505,725 | 6 | 2025 Q1–Q3 | Lifting of seizure orders |
| `physical_reg` | 3 | 501,050 | 6 | 2025 Q1–Q3 | In-rem property registration |
| `operations` | 27 | 282,401 | 6–8 | 2024–2025 | Monthly aggregate operations by type |
| `transfer` | 3 | 221,229 | 6 | 2025 Q1–Q3 | Ownership transfers |
| `register_old_deed` | 3 | 143,027 | 6 | 2025 Q1–Q3 | Registration of pre-existing deeds |
| `division` | 3 | 90,250 | 6 | 2025 Q1–Q3 | Property subdivision |
| `mortgage_release` | 3 | 42,781 | 6 | 2025 Q1–Q3 | Mortgage discharge |
| `mortgage` | 3 | 36,525 | 6 | 2025 Q1–Q3 | New property mortgages |
| `update_deed` | 3 | 27,907 | 6 | 2025 Q1–Q3 | Title deed modifications |
| `property_identity` | 2 | 22,050 | 6 | 2025 Q1+Q3 | Linking deeds to property identity system |
| `deed_define_divide` | 3 | 21,963 | 6 | 2025 Q1–Q3 | Deed definition for subdivision |
| `register_no_deed` | 3 | 21,341 | 6 | 2025 Q1–Q3 | Ownership registration without deed |
| `merge_re` | 3 | 10,426 | 6 | 2025 Q1–Q3 | Property merging |
| `enforcement` | 4 | 8,286 | 5–6 | 2025 Q1–Q4 | Court-ordered forced sales |
| `poa_fund` | 2 | 7,060 | 6 | 2025 Q1+Q3 | RE Development Fund POA |
| `ownership` | 3 | 5,210 | 6 | 2025 Q1–Q3 | Ownership rate statistics |
| `index` | 3 | 3,002 | 13–15 | 2018–2021 | Historical price indices (pivot-table exports) |
| `update_old_deed` | 3 | 1,315 | 6 | 2025 Q1–Q3 | Old deed modifications |
| `ownership_men` | 3 | 416 | 6 | 2025 | Male ownership rates by city |
| `merge_deed` | 3 | 37 | 6 | 2025 Q1–Q3 | Title deed merging |

### REGA Categories

**4 categories, 46 files, 73,560 rows**

| Category | Files | Rows | Columns | Date Range | Description |
|----------|-------|------|---------|------------|-------------|
| `consolidated` | 1 | 32,730 | 11 | 2018–2023 | Quarterly report with district-level aggregates |
| `sales_indicators` | 31 | 20,874 | 14 | 2024–2025 | Regional sales indicators: avg/min/max price per m² |
| `rental_indicators` | 13 | 19,954 | 7 | 2019–2024 | Rental market indicators by city (all 13 regions) |
| `gender_stats` | 1 | 2 | 3 | — | Registered real estate by gender |

---

## Enum Values

Fields with a limited set of known values (up to 50 distinct). Full enum data in [`data/registry_enums.csv`](../data/registry_enums.csv).

### property_classification (تصنيف العقار)

Used in MOJ sales and REGA indicators. In MOJ sales, this is the broad sector:

| Value | English |
|-------|---------|
| سكني | Residential (~85% of sales) |
| تجاري | Commercial (~10.6%) |
| زراعي | Agricultural (~4%) |
| صناعي | Industrial (<0.1%) |
| جميع التصانيف | All classifications (used in REGA indicators as a "total" row) |

In the REGA consolidated file (`typecategoryar`), more granular types appear:

| Value | English |
|-------|---------|
| قطعة أرض-سكنى | Residential land plot |
| قطعة أرض-تجارى | Commercial land plot |
| فيلا | Villa |
| شقة | Apartment |
| قطعة أرض- زراعي | Agricultural land plot |
| عمارة | Building / apartment block |

### property_type (نوع العقار)

Only available in 2023 Q1–Q3 sales and REGA rental indicators. Distinguishes land from built properties:

| Value | English |
|-------|---------|
| قطعة أرض | Land plot |
| شقة | Apartment |
| أرض زراعية | Agricultural land |
| أرض | Land (generic) |
| بيت | House |
| فيلا | Villa |
| دوبلكس | Duplex |
| معرض/محل | Showroom / shop |
| عمارة | Building |
| شقة - سكني | Apartment - residential |
| دور - سكني | Floor unit - residential |
| محل - تجاري | Shop - commercial |
| فيلا - سكني | Villa - residential |
| استديو - سكني | Studio - residential |
| معرض تجاري - تجاري | Showroom - commercial |
| مكتب - تجاري | Office - commercial |
| دوبلاكس - سكني | Duplex - residential |

### sector_type (نوع القطاع)

| Value | English |
|-------|---------|
| القطاع العام | Public sector |
| القطاع الخاص | Private sector |

### service_type (نوع الخدمة)

| Value | English |
|-------|---------|
| خدمة إلكترونية | Electronic service (~97%) |
| خدمة إلكترونية جزئيا | Partially electronic (~3%) |

### main_document_type (نوع السند الرئيسي)

Enforcement sales only:

| Value | English | % |
|-------|---------|---|
| احكام و قرارات | Judgments & decisions | 49.3% |
| أوراق تجارية | Commercial papers | 32.8% |
| عقود | Contracts | 7.3% |
| اخلاء | Eviction | 5.3% |
| أوراق تجارية إلكترونية | Electronic commercial papers | 3.3% |
| مزاد | Auction | 1.4% |
| عام | General | 0.4% |

---

## Date Formats by Category

Date columns use two different formats across the CSVs. Most files use `YYYY/MM/DD`, but several categories switched to `M/D/YYYY`. Both Gregorian and Hijri calendars are present. REGA files have no per-record dates — they use separate `year` + `quarter` integer columns instead.

| Format | Example | Categories |
|--------|---------|------------|
| `YYYY/MM/DD` | `2025/01/01` | sales (2020–2022, 2024–2025), operations, mortgage, mortgage_release, transfer, division, physical_reg, poa, poa_fund, register_old_deed, register_no_deed, update_deed, update_old_deed, deed_define_divide, merge_re, merge_deed, ownership, enforcement |
| `M/D/YYYY` | `1/1/2025` | property_identity, release_seizure, seizure, sales (2023 Q2–Q4) |
| Year + Quarter columns | `2024` + `Q1` | All REGA categories (sales_indicators, rental_indicators, consolidated) |

**Hijri dates** (`date_hijri` / `تاريخ الصفقة هجري`) follow the same format as their Gregorian counterpart in each file. Present in sales and operations files. Not present in REGA files.

**Parsing tip:** Detect format per file by checking whether the first date component is >12 (must be `YYYY/...`) or ≤12 (ambiguous — check the third component length). Or use the category table above.

---

## Formatting Notes

Automatically detected quirks in the raw CSV data:

| Note | Meaning | Affected Fields |
|------|---------|----------------|
| `quoted_commas` | Values contain commas inside quotes (e.g., `"1,800,000"`) | `price`, `area`, `reference_number` |
| `NULL_literal` | The string `NULL` used instead of empty | Some operation files |
| `percentage_strings` | Values end with `%` symbol | `female_ownership_rate` |

See the `formatting_notes` column in [`data/registry_fields.csv`](../data/registry_fields.csv) for per-field detail.

---

## CSV Exports

Three CSV files export the full registry metadata for programmatic use without requiring SQLite:

| File | Rows | Description |
|------|------|-------------|
| [`data/registry_files.csv`](../data/registry_files.csv) | 159 | One row per CSV file: source, category, row/column counts, encoding, date range, region coverage |
| [`data/registry_fields.csv`](../data/registry_fields.csv) | 1,388 | One row per field per file: Arabic name, canonical English name, data type, nullability, distinct values, min/max, sample values |
| [`data/registry_enums.csv`](../data/registry_enums.csv) | 3,864 | One row per enum value per field: value text, count, percentage |

These files are regenerated by running:

```bash
python3 scripts/build_registry.py   # rebuild registry.db
scripts/export_registry.sh          # export to CSV (or use sqlite3 directly)
```

---

## Registry Database

The `registry.db` SQLite database is the authoritative metadata catalog. It is not tracked in git (regenerate with `python3 scripts/build_registry.py`).

**Schema:**

| Table | Rows | Description |
|-------|------|-------------|
| `files` | 159 | One row per CSV: source, category, path, size, row/col counts, encoding, date range, region coverage |
| `fields` | 1,388 | One row per column per file: Arabic/English names, data type, null stats, distinct count, min/max, samples |
| `enum_values` | 3,864 | Distinct values for text columns with ≤50 unique values, with counts and percentages |
| `samples` | 1,580 | 10 raw sample rows per file, both as CSV lines and parsed JSON |
| `field_aliases` | 56 | Cross-file mapping of Arabic header variants to canonical English names |

See [`scripts/build_registry.py`](../scripts/build_registry.py) for the full schema and Arabic-to-English field mapping (41 entries).
