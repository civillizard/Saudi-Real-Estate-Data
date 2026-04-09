# Ministry of Justice (MOJ; وزارة العدل) — Real Estate Data

<p align="center">
  <a href="https://www.6ra3.com/track/r/rega-site-moj-data?dest=https://rega.gov.sa"><img src="https://www.6ra3.com/track/rega/moj-data" height="50" alt="REGA - Real Estate General Authority (الهيئة العامة للعقار)"></a>
  &nbsp;&nbsp;&nbsp;&nbsp;
  <a href="https://www.6ra3.com/track/r/moj-site-moj-data?dest=https://moj.gov.sa"><img src="https://www.6ra3.com/track/moj/moj-data" height="50" alt="MOJ - Ministry of Justice (وزارة العدل)"></a>
</p>

## Overview

**Source:** Saudi National Open Data Platform (open.data.gov.sa)
**Publisher:** MOJ — Organization ID: `35c63412-c4ae-4303-8fef-56cfd71303cf`
**Publisher URL:** https://www.moj.gov.sa/ar/opendata/Pages/reports.aspx
**Total MOJ Datasets on Portal:** 998
**Real Estate Datasets:** 132 (downloaded 131 — 1 genuinely missing on portal)
**Downloaded:** 2026-02-11
**Total Size:** 546 MB
**Total Rows:** 5,025,031

## How We Accessed the Data

### API Endpoints Used

The Saudi Open Data Platform exposes both official public APIs and internal SPA APIs. Direct `curl` calls work with a Safari User-Agent header.

**Official Developer APIs** (documented at `/en/pages/developers-api`):

```
# Fetch organization info + dataset list
GET https://open.data.gov.sa/data/api/organizations?version=-1&organization=وزارة العدل

# Fetch dataset metadata
GET https://open.data.gov.sa/data/api/datasets?version=-1&dataset={DATASET_ID}

# Fetch dataset resources (CSV/XLSX download URLs)
GET https://open.data.gov.sa/data/api/datasets/resources?version=-1&dataset={DATASET_ID}
```

**Internal SPA API** (used as fallback when official API returned empty):
```
# Fetch dataset with embedded resources (includes resource IDs)
GET https://open.data.gov.sa/api/datasets/{DATASET_ID}
```

**Download URL Pattern:**
```
https://open.data.gov.sa/odp-public/{ORG_ID}/{DATASET_ID}/v{N}/{RESOURCE_NAME}.csv
```

### Recovery of Missing Files

3 datasets had broken resources API responses (returned empty JSON instead of download links). We recovered 4 of 5 missing files by reverse-engineering the download URL from working sibling datasets.

**The technique:**

1. Find a working sibling dataset in the same category (e.g., Update-Deed Q3 2025 which had a valid resources API response)
2. Extract the download URL: `https://open.data.gov.sa/odp-public/{ORG_ID}/{DATASET_ID}/v1/{RESOURCE_NAME}.csv`
3. Note that the URL pattern is consistent: the `ORG_ID` is always the MOJ organization UUID (`35c63412-c4ae-4303-8fef-56cfd71303cf`), the `DATASET_ID` is unique per dataset (available from the dataset list API even when resources are broken), and `v1` is the version
4. Substitute the broken dataset's ID into the same URL pattern
5. The resource filename follows a predictable convention within each category

**Example reconstruction:**

```
# Working sibling (Update-Deed Q3 2025):
https://open.data.gov.sa/odp-public/35c63412-.../bb7db946-.../v1/MOJ-Update-Deed-2025-Q3.csv

# Broken dataset (Update-Deed Q1 2025) — swap DATASET_ID, adjust filename:
https://open.data.gov.sa/odp-public/35c63412-.../a1b2c3d4-.../v1/MOJ-Update-Deed-2025-Q1.csv
```

**Results:**

| Dataset | Issue | Resolution |
|---------|-------|------------|
| Update-Deed Q1 2025 | Resources API empty | Recovered via URL pattern from Q3 sibling |
| Update-Deed Q2 2025 | Resources API empty | Recovered via URL pattern from Q3 sibling |
| POA-RE-Fund Q1 2025 | Resources API empty | Recovered via URL pattern from Q3 sibling |
| Property-Identity Q1 2025 | Resources API empty | Recovered via URL pattern from Q3 sibling |
| **Property-Identity Q2 2025** | **File never uploaded** | **Genuinely missing — URL resolves but returns 0-byte file. Dataset created on portal (2025-10-22) but CSV never uploaded.** |

This pattern works because the Open Data Portal stores files in a predictable path structure. If you encounter broken resource API responses for other MOJ datasets, the same technique should apply — get the dataset ID from the dataset list API, combine with the known org ID and a guessed filename based on the naming convention of siblings.

---

For a cross-source field catalog covering all 159 files (MOJ + REGA) with canonical English names, data types, and enum translations, see the [Data Dictionary](DATA_DICTIONARY.md). Machine-readable exports: [`data/schema.json`](../data/schema.json) (compact, for AI tools), [`data/registry.json`](../data/registry.json) (full), and `data/registry_*.csv` files.

## Data Structure

### 1. Sales Transactions (MOJ-Sales/)

**27 files, 179 MB, 1,407,132 transaction rows**

Individual real estate sale transactions registered through MOJ electronic services, judicial authorities, and certified private-sector notaries.

**Date Range:** 2020-01-01 to 2025-12-31 (24 quarterly files)
**Coverage:** All 13 administrative regions, 175 cities, 13,398 neighborhoods
**Total Transaction Value:** 1,426.8 Billion SAR
**Total Area Transacted:** 8,353 Million m²

#### Schema

| Column | Arabic | Type | Example |
|--------|--------|------|---------|
| Region | المنطقة | text | منطقة الرياض |
| City | المدينة | text | الرياض |
| City/Neighborhood | المدينة / الحي | text | الرياض/بدر |
| Transaction Reference | الرقم المرجعي للصفقة | numeric | 27049909 |
| Date (Gregorian) | تاريخ الصفقة ميلادي | date | 2025/01/01 |
| Date (Hijri) | تاريخ الصفقة هجري | date | 1446/07/01 |
| Property Classification | تصنيف العقار | text | سكني |
| Number of Properties | عدد العقارات | numeric | 1 |
| Price (SAR) | السعر | numeric | 1,800,000 |
| Area (m²) | المساحة | numeric | 600.00 |

#### Transactions by Region

| Region | Transactions | % | Notes |
|--------|-------------|---|-------|
| منطقة الرياض | 477,347 | 33.9% | Dominant market |
| منطقة مكة المكرمه | 269,282 | 19.1% | Includes Jeddah, Makkah, Taif |
| منطقة الشرقية | 188,337 | 13.4% | Dammam, Khobar, Hofuf |
| منطقة القصيم | 120,875 | 8.6% | Buraydah hub |
| منطقة عسير | 69,167 | 4.9% | |
| منطقة المدينة المنوره | 60,934 | 4.3% | |
| منطقة حائل | 59,352 | 4.2% | |
| منطقة جازان | 31,500 | 2.2% | |
| منطقة تبوك | 29,076 | 2.1% | |
| منطقة الجوف | 27,485 | 2.0% | |
| منطقة نجران | 24,124 | 1.7% | |
| منطقة الحدود الشمالية | 23,804 | 1.7% | |
| منطقة الباحة | 8,970 | 0.6% | Smallest market |

Note: Some region names have slight Arabic spelling variations across files (e.g., "منطقة مكة المكرمه" vs "منطقة مكة المكرمة", "منطقة الشرقية" vs "المنطقة الشرقية"). Normalize before aggregation.

#### Transactions by Year

| Year | Transactions | Notes |
|------|-------------|-------|
| 2020 | 276,811 | COVID year — still substantial |
| 2021 | 281,883 | Peak year |
| 2022 | 213,754 | Decline |
| 2023 | 139,697 | Lowest — note: Q3-Q4 filename format changed |
| 2024 | 249,328 | Strong recovery |
| 2025 | 201,556 | Partial year (Q1-Q4 available) |

#### Property Classification

| Type | Count | % |
|------|-------|---|
| سكني (Residential) | 1,201,675 | 85.4% |
| تجاري (Commercial) | 149,767 | 10.6% |
| زراعي (Agricultural) | 55,601 | 4.0% |
| صناعي (Industrial) | 74 | <0.1% |

#### Top 20 Cities by Transaction Volume

| City | Transactions | Total Value (B SAR) |
|------|-------------|-------------------|
| الرياض | 329,927 | 704.0 |
| جده | 163,666 | 217.5 |
| بريده | 62,425 | 25.5 |
| مكة المكرمة | 53,298 | 69.0 |
| المدينة المنورة | 52,211 | 40.6 |
| حائل | 38,152 | 11.6 |
| الدمام | 38,001 | 65.9 |
| الهفوف | 34,306 | 18.7 |
| الخبر | 32,756 | 55.6 |
| حفر الباطن | 29,958 | 5.3 |
| الطائف | 29,387 | 16.8 |
| الخرج | 26,887 | 11.0 |
| تبوك | 23,452 | 11.0 |
| عرعر | 17,751 | 2.0 |
| ابها | 17,634 | 12.5 |
| خميس مشيط | 17,340 | 10.0 |
| نجران | 17,092 | 3.7 |
| جيزان | 13,762 | 6.1 |
| عنيزه | 13,731 | 5.1 |
| المزاحميه | 12,868 | 7.4 |

### 2. Historical Index Files (MOJ-Sales/)

**3 files — real estate market indices from 2018-2021**

| File | Rows | Description |
|------|------|-------------|
| MOJ-RE-Index-Regions-2018-2021.csv | 660 | Monthly index by region and property classification (2018-2021) |
| MOJ-RE-Index-Districts-2018-2021.csv | 2,128 | Index by district/neighborhood |
| MOJ-RE-Index-Cities-2018-2021.csv | 220 | Index by city |

---

### 3. Other Real Estate Operations (MOJ-RealEstate/)

**86 files, 367 MB, 3,617,899 rows — all from 2024-2025**

Individual transaction-level records for various real estate operations processed through MOJ services.

#### Common Schema (most categories)

| Column | Arabic | Type | Example |
|--------|--------|------|---------|
| Region | المنطقة | text | الرياض |
| City | المدينة | text | الرياض |
| Sector Type | نوع القطاع | text | القطاع العام / القطاع الخاص |
| Service Type | نوع الخدمة | text | خدمة إلكترونية / خدمة إلكترونية جزئيا |
| Date (Gregorian) | التاريخ ميلادي | date | 2025/01/01 |
| Reference Number | الرقم المرجعي | numeric | 27,052,609 |

#### Categories

| Category | Arabic | Files | Rows | Description |
|----------|--------|-------|------|-------------|
| **Seizure** | الحجز التحفظي على ممتلكات | 3 (Q1-Q3 2025) | 910,856 | Court-ordered property freezes on assets |
| **RE Power of Attorney** | الوكالات الصادرة في العقارات | 3 (Q1-Q3 2025) | 758,004 | Real estate power of attorney issuances |
| **Release Seizure** | فك الحجز التحفظي | 3 (Q1-Q3 2025) | 505,727 | Lifting of property seizure orders |
| **Physical Registration** | مسجل عينيا | 3 (Q1-Q3 2025) | 501,052 | Physical property registration (in-rem) |
| **RE Operations** | العمليات العقارية المسجلة | 27 (monthly 2024 + 2025) | 282,417 | Monthly aggregate operations by type (special schema — see below) |
| **Property Transfers** | الإفراغات / نقل ملكية | 3 (Q1-Q3 2025) | 221,229 | Ownership transfers (إفراغات) |
| **Register Old Deed** | تسجيل صك قديم | 3 (Q1-Q3 2025) | 143,029 | Registration of pre-existing deeds |
| **Property Division** | فرز عقارات | 3 (Q1-Q3 2025) | 90,252 | Property subdivision/division |
| **Mortgage Release** | فك رهن العقارات | 3 (Q1-Q3 2025) | 42,783 | Mortgage discharge/release |
| **Mortgage** | رهن العقارات | 3 (Q1-Q3 2025) | 36,527 | New property mortgages |
| **Deed Updates** | تعديل صك | 3 (Q1-Q3 2025) | 27,908 | Title deed modifications |
| **Property Identity** | ربط صك بالهوية العقارية | 2 (Q1+Q3 2025) | 22,050 | Linking deeds to property identity system |
| **Deed Define/Divide** | تعريف الصكوك للفرز | 3 (Q1-Q3 2025) | 21,966 | Deed definition for subdivision |
| **Register Without Deed** | تسجيل ملكية عقار بدون صك | 3 (Q1-Q3 2025) | 21,342 | Property ownership registration without existing deed |
| **Merge RE** | دمج عقارات | 3 (Q1-Q3 2025) | 10,429 | Property merging |
| **Enforcement Sale** | قرار بيع عقار أو منقول | 4 (Q1-Q4 2025) | 8,287 | Court-ordered enforcement sales (special schema) |
| **POA RE Fund** | وكالات صندوق التنمية العقارية | 2 (Q1+Q3 2025) | 7,061 | RE Development Fund power of attorney |
| **Ownership** | نسب ومعدلات التملك العقاري | 3 (Q1-Q3 2025) | 5,210 | Ownership rate statistics |
| **Old Deed Updates** | تعديل صك قديم | 3 (Q1-Q3 2025) | 1,315 | Old title deed modifications |
| **Ownership Men** | التملك العقاري للأفراد الرجال | 3 (Q1-Q3 2025) | 417 | Male ownership rates by city (special schema) |
| **Merge Deed** | دمج صكوك | 3 (Q1-Q3 2025) | 38 | Title deed merging |

#### Special Schemas

**RE Operations (Monthly):**
| Column | Arabic | Type |
|--------|--------|------|
| Region | المنطقة | text |
| City | المدينة | text |
| Sector Type | نوع القطاع | text |
| Service Type | نوع الخدمة | text |
| Operation Type | نوع العملية | text (e.g., عقارات/افراغ) |
| Date (Gregorian) | التاريخ ميلادي | date |
| Date (Hijri) | التاريخ هجري | date |
| Operation Count | عدد العمليات | numeric |

**Enforcement Sale:**
| Column | Arabic | Type |
|--------|--------|------|
| Region | المنطقة | text |
| City | المدينة | text |
| Main Document Type | نوع السند الرئيسي | text (e.g., اخلاء) |
| Decision Date (Gregorian) | تاريخ القرار ميلادي | date |
| Decision Date (Hijri) | تاريخ القرارهجري | date |
| Reference Number | الرقم المرجعي | numeric |

**Ownership Men (Aggregate):**
| Column | Arabic | Type |
|--------|--------|------|
| Region | المنطقة | text |
| City | المدينة | text |
| Year | السنة | numeric |
| Quarter | ربع السنة | text |
| Female Owner Count | عدد الملاك النساء | numeric |
| Female Ownership Rate | نسبة تملك النساء | percent |

---

## File Inventory

### MOJ-Sales/ (27 files, 179 MB)

| File | Rows | Size |
|------|------|------|
| MOJ-Sales-2020-Q1.csv | 80,635 | 10.0 MB |
| MOJ-Sales-2020-Q2.csv | 49,618 | 6.2 MB |
| MOJ-Sales-2020-Q3.csv | 64,317 | 8.0 MB |
| MOJ-Sales-2020-Q4.csv | 82,244 | 10.3 MB |
| MOJ-Sales-2021-Q1.csv | 92,963 | 11.6 MB |
| MOJ-Sales-2021-Q2.csv | 66,672 | 8.3 MB |
| MOJ-Sales-2021-Q3.csv | 55,911 | 7.0 MB |
| MOJ-Sales-2021-Q4.csv | 66,339 | 8.3 MB |
| MOJ-Sales-2022-Q1.csv | 71,252 | 9.0 MB |
| MOJ-Sales-2022-Q2.csv | 53,016 | 6.7 MB |
| MOJ-Sales-2022-Q3.csv | 45,976 | 5.8 MB |
| MOJ-Sales-2022-Q4.csv | 43,512 | 5.5 MB |
| MOJ-Sales-2023-Q1.csv | 44,091 | 6.9 MB |
| MOJ-Sales-2023-Q2.csv | 38,811 | 5.3 MB |
| MOJ-Sales-2023-Q3.csv | 48,545 | 6.6 MB |
| MOJ-Sales-2023-Q4.csv | 52,342 | 6.5 MB |
| MOJ-Sales-2024-Q1.csv | 59,099 | 7.4 MB |
| MOJ-Sales-2024-Q2.csv | 48,272 | 6.0 MB |
| MOJ-Sales-2024-Q3.csv | 69,021 | 8.6 MB |
| MOJ-Sales-2024-Q4.csv | 72,939 | 9.1 MB |
| MOJ-Sales-2025-Q1.csv | 65,729 | 8.2 MB |
| MOJ-Sales-2025-Q2.csv | 42,518 | 5.4 MB |
| MOJ-Sales-2025-Q3.csv | 48,820 | 6.2 MB |
| MOJ-Sales-2025-Q4.csv | 44,490 | 5.7 MB |
| MOJ-RE-Index-Regions-2018-2021.csv | 660 | 102 KB |
| MOJ-RE-Index-Districts-2018-2021.csv | 2,128 | 137 KB |
| MOJ-RE-Index-Cities-2018-2021.csv | 220 | 19 KB |

### MOJ-RealEstate/ (86 files, 367 MB)

See category breakdown table above for row counts per file.

---

## Data Quality Notes

1. **Region name inconsistency:** The same region appears with slightly different Arabic spellings across files:
   - "منطقة مكة المكرمه" vs "منطقة مكة المكرمة" (final ه vs ة)
   - "منطقة الشرقية" vs "المنطقة الشرقية" (with/without منطقة)
   - "منطقة المدينة المنوره" vs "منطقة المدينة المنورة"
   - 12 rows have empty region fields

2. **Missing file:** Property-Identity Q2 2025 (dataset `a1001b31-0f3b-4231-a19c-1ca198001a06`) — MOJ created the dataset entry on 2025-10-22 but never uploaded the CSV/XLSX files. Download URLs are empty, resource files return 0 bytes.

3. **Price formatting:** Prices include commas as thousands separator (e.g., "1,800,000"). Parse with comma removal.

4. **Date formats vary:** Most files use `YYYY/MM/DD` but some 2024 monthly operations files use `M/D/YYYY`.

5. **Index files (2018-2021):** The 3 MOJ-RE-Index files have non-standard headers with "Unnamed" columns — they appear to be pivot-table exports rather than tidy CSV.

6. **2023 data gap:** 2023 has noticeably fewer transactions (139,697) compared to surrounding years. This may reflect a real market slowdown or a data collection change.

---

## Comparison with REGA Data

| Aspect | REGA | MOJ |
|--------|------|-----|
| **Publisher** | الهيئة العامة للعقار | وزارة العدل |
| **Data Level** | Aggregate indicators (neighborhood averages) | Individual transactions |
| **Sales Data** | 46 datasets, ~51K rows | 27 datasets, 1.4M rows |
| **Date Range** | 2024-2025 (sales), 2019-2024 (rental) | 2020-2025 (sales), 2024-2025 (operations) |
| **Has Price per Transaction** | No (avg/min/max per m²) | Yes (exact price per deed) |
| **Has Area per Transaction** | No (total area per group) | Yes (exact m² per deed) |
| **Has Reference Numbers** | No | Yes (الرقم المرجعي) |
| **Has Rental Data** | Yes (13 regions) | No |
| **Regional Coverage** | 6 regions (sales), 13 (rental) | All 13 regions |
| **Has Owner Info** | By gender count only | No PII |

---

## Technical Reference

### Dataset IDs (for API access)

All 132 MOJ real estate dataset IDs can be retrieved via:
```bash
curl -s -A "Mozilla/5.0 (Macintosh)" \
  "https://open.data.gov.sa/data/api/organizations?version=-1&organization=%D9%88%D8%B2%D8%A7%D8%B1%D8%A9%20%D8%A7%D9%84%D8%B9%D8%AF%D9%84" \
  | python3 -c "import json,sys; [print(d['id'],d['titleAr']) for d in json.load(sys.stdin)['datasets'] if any(k in d.get('titleAr','') for k in ['عقار','صك','رهن','إفراغ'])]"
```

### Download Pattern

```python
import urllib.request, urllib.parse

ORG_ID = "35c63412-c4ae-4303-8fef-56cfd71303cf"
DATASET_ID = "bb7db946-705b-46ee-82d0-d4f010c45c5d"  # example

# Step 1: Get resource download URL
url = f"https://open.data.gov.sa/data/api/datasets/resources?version=-1&dataset={DATASET_ID}"
# Step 2: URL-encode the download path (spaces in filenames)
# Step 3: Download with Safari User-Agent
```

### Rate Limits

The API returns `x-ratelimit-burst-capacity: 2000` and `x-ratelimit-replenish-rate: 1000`. In practice, adding a 0.3-1s delay between requests avoids empty responses.

---

Last updated: 2026-02-11
