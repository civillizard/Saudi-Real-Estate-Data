# Ministry of Justice (MOJ; وزارة العدل) Property Identity Audit — Cross-Category Linkage Investigation

<p align="center">
  <a href="https://www.[redacted]/track/r/rega-site-property-identity-audit?dest=https://rega.gov.sa"><img src="https://www.[redacted]/track/rega/property-identity-audit" height="50" alt="REGA - Real Estate General Authority (الهيئة العامة للعقار)"></a>
  &nbsp;&nbsp;&nbsp;&nbsp;
  <a href="https://www.[redacted]/track/r/moj-site-property-identity-audit?dest=https://moj.gov.sa"><img src="https://www.[redacted]/track/moj/property-identity-audit" height="50" alt="MOJ - Ministry of Justice (وزارة العدل)"></a>
</p>

**Date:** 2026-03-12
**Analyst:** Mamdoh AlOqiel
**Objective:** Determine whether Property Identity files contain deed numbers, property IDs, or parcel identifiers that could bridge transactions across MOJ categories (seizure, transfer, mortgage, enforcement sale, etc.)

---

## Executive Summary

**Result: No cross-category bridge exists in the MOJ open data.**

The Property Identity files (ربط صك بالهوية العقارية) contain only 6 columns — the same minimal schema used across all 2025 real-estate category files — with no deed numbers, property identity numbers, parcel numbers, or plan numbers. Every reference number (الرقم المرجعي) in the entire MOJ dataset is globally unique and category-specific. There is zero overlap across any category pair, including logically paired categories like Seizure/Release-Seizure and Mortgage/Mortgage-Release.

The only MOJ file that ever contained المخطط (plan/plat number) and رقم القطعة (parcel number) was the one-off 2023-Q1 Sales anomaly, and those fields appear in no other file.

**The MOJ open data was designed for aggregate statistical reporting, not property-level tracking.**

---

## File Overview

| File | Rows | Date Range |
|------|------|------------|
| MOJ-Property-Identity-2025-Q1.csv | 15,605 | 2025-01-01 to 2025-03-31 |
| MOJ-Property-Identity-2025-Q3.csv | 6,445 | 2025-07-01 to 2025-09-30 |
| Q2 | Missing | MOJ never published |

---

## Column Analysis — Both Property Identity Files

Both files have **identical schemas** — 6 columns only.

| # | Column (Arabic) | Translation | Distinct Values (Q1 sample n=1,560) | Notes |
|---|-----------------|-------------|--------------------------------------|-------|
| 0 | المنطقة | Region | **1** — "الخدمات الرقمية" | Constant. Not a geographic region. Means "Digital Services" — indicates this is a count of digital service registrations, not a geographic breakdown. |
| 1 | المدينة | City | **1** — "عام" (General) | Constant. Not a city name. |
| 2 | نوع القطاع | Sector Type | **1** — "القطاع العام" (Public Sector) | Constant across entire file. |
| 3 | نوع الخدمة | Service Type | **1** — "خدمة إلكترونية" (Electronic Service) | Constant. All transactions fully electronic. |
| 4 | التاريخ ميلادي | Gregorian Date | 90 distinct dates in Q1 | Daily counts. Format: M/D/YYYY (Q1) or YYYY/MM/DD (Q3). |
| 5 | الرقم المرجعي | Reference Number | **All unique** (1,560 distinct in 1,560-row sample) | Per-transaction ID. Range Q1: 27,035,310–28,654,430. Range Q3: 30,407,662–32,377,851. NOT a property identifier. |

### Key Finding on First Four Columns

Columns 0–3 are completely constant across all 15,605 rows (Q1) and 6,445 rows (Q3). The file does not break down by region, city, sector type, or anything spatially meaningful. It is purely a timestamped log of digital service transactions — effectively a transaction count register where each row = one "property identity linking" service request processed on that date.

**There is NO:**
- رقم الصك (deed number)
- رقم الهوية العقارية (property identity/NCRE number)
- المخطط (plan/plat number)
- رقم القطعة (parcel/plot number)
- Any location below the national level
- Any property attribute

---

## Reference Number Analysis

### Nature of Reference Numbers

The الرقم المرجعي is a **per-transaction sequential system ID** assigned by MOJ's electronic services platform. Key properties:

1. **Globally unique** — tested across all 2025-Q1 real-estate files (1,238,992 total unique refs, zero duplicates across any pair)
2. **Category-isolated** — each category uses a distinct ID range that does not overlap any other category
3. **Sequential within time** — numbers increase monotonically with date within each category, confirming they are assignment-time IDs
4. **Not property-level** — one property can generate many reference numbers across different transaction types over time

### Reference Number Ranges by Category (2025-Q1)

| Category | Count | Min | Max |
|----------|-------|-----|-----|
| Property-Identity | 15,605 | 27,035,310 | 28,654,430 |
| Physical-Registration | 165,688 | 27,035,289 | 28,654,924 |
| Seizure | 292,680 | 27,035,248 | 28,654,276 |
| Release-Seizure | 154,875 | 27,035,283 | 28,654,965 |
| Transfers | 219,591 | 26,406,201 | 28,654,761 |
| Mortgage | 11,166 | 27,037,272 | 28,649,167 |
| Mortgage-Release | 14,697 | 27,036,842 | 28,637,290 |
| Register-Old-Deed | 52,016 | 27,035,290 | 28,654,981 |
| Register-No-Deed | 5,872 | 27,035,566 | 28,644,328 |
| Divide | 31,342 | 27,036,496 | 28,654,687 |
| Enforcement-Sale | 2,104 | 14,095,408 | 14,803,036 |
| POA-RealEstate | 246,026 | 37,331,827 | 38,647,251 |

**Note:** Despite overlapping ranges in the 27M–28M band, there is zero value-level overlap — the numbers are interleaved but unique. Enforcement Sale uses a completely different ID range (~14M). POA uses ~37–38M range.

### Cross-Category Overlap Test Results

| Pair | Overlap |
|------|---------|
| Property-Identity × Physical-Registration | **0** |
| Property-Identity × Register-Old-Deed | **0** |
| Property-Identity × Register-No-Deed | **0** |
| Property-Identity × Update-Deed | **0** |
| Seizure Q1 × Release-Seizure Q1 | **0** |
| Seizure Q1 × Release-Seizure Q2 | **0** |
| Seizure Q1 × Release-Seizure Q3 | **0** |
| Mortgage Q1 × Mortgage-Release Q1 | **0** |
| Mortgage Q1 × Mortgage-Release Q2 | **0** |
| Mortgage Q1 × Mortgage-Release Q3 | **0** |
| Transfers × Seizure | **0** |
| Transfers × Physical-Registration | **0** |

Zero cross-quarter overlap was also confirmed for logically related pairs (Seizure→Release, Mortgage→Release), confirming that even paired operations like placing and lifting a seizure use completely different reference numbers. There is no event-chain linkage.

---

## Cross-File Column Header Survey

Every CSV file in `moj/real-estate/` and `moj/sales/` was scanned for any identifier columns beyond الرقم المرجعي.

### Column Schema Distribution (2025 Real-Estate Files)

**Most common schema (applies to ~85% of all category files):**
```
المنطقة | المدينة | نوع القطاع | نوع الخدمة | التاريخ ميلادي | الرقم المرجعي
```
This includes: Property-Identity, Physical-Registration, Seizure, Release-Seizure, Mortgage, Mortgage-Release, Transfers, Register-Old-Deed, Register-No-Deed, Update-Deed, Update-Old-Deed, Divide, Merge-RE, Merge-Deed, Deed-Define-Divide, Ownership, RE-Operations.

**Enforcement Sale schema (unique column 3):**
```
المنطقة | المدينة | نوع السند الرئيسي | تاريخ القرار ميلادي | الرقم المرجعي
```
نوع السند الرئيسي (Primary Deed Type) values: احكام و قرارات (judgments), أوراق تجارية (commercial paper), عقود (contracts), اخلاء (eviction), أوراق تجارية إلكترونية.

**RE-Operations monthly files (2024) — extra field:**
```
المنطقة | المدينة | نوع القطاع | نوع الخدمة | نوع العملية | التاريخ ميلادي | التاريخ هجري | عدد العمليات
```
This is the only schema with عدد العمليات (count of operations) — an aggregate file, not row-per-transaction.

**Ownership-Men files — completely different:**
```
المنطقة | المدينة | السنة | ربع السنة | عدد الملاك النساء | نسبة تملك النساء
```
Aggregate gender ownership statistics, no identifiers.

**POA files — slightly different ref column name:**
```
... | الرقم المرجعي للوكالة
```
(Reference number for the power of attorney, not for the property)

### No Property Identifiers Found Anywhere

Searched all files for: رقم الصك, رقم الهوية العقارية, المخطط, رقم القطعة, الصك, NCRE.
**Result: None found** in any real-estate file header.

---

## The 2023-Q1 Sales Anomaly

MOJ-Sales-2023-Q1.csv is the **only file in the entire dataset** with المخطط and رقم القطعة:

```
رقم مرجعي | المنطقة | المدينة | الحي | المخطط | رقم القطعة | التاريخ | تصنيف العقار | نوع العقار | عدد العقارات | السعر بالريال السعودي | المساحة | سعر المتر المربع
```

**Stats:**
- 44,091 rows
- Reference numbers: 18,703,821–19,680,279 (distinct ~18M range, not matching any 2025 file range)
- المخطط: 4,886 distinct values, format `مخطط/[number or code]`, e.g. `مخطط/3057`, `مخطط/244/ ج/ س`, `مخطط/أخرى` (other/unknown) for ~20% of rows
- رقم القطعة: 12,046 distinct values, format ` قطعة [number]`, e.g. ` قطعة 505`, ` قطعة بدون` (no number) for ~6% of rows

**These fields appear in NO other sales file.** All files before and after (2023-Q2 onward) reverted to the standard 10-column schema without المخطط or رقم القطعة. This appears to have been a one-time data enrichment effort that was not continued.

**No cross-file grep is possible** — since no other file has these column types, there is nothing to grep against.

---

## Conclusions

### 1. The Property Identity Files Are Not What the Name Suggests

"ربط صك بالهوية العقارية" (Linking Deed to Property Identity) sounds like it would contain the NCRE property identity number. It does not. These files are simply transaction logs of the number of times the "link deed to property identity" digital service was used. They contain no actual deed numbers or property identity numbers.

### 2. No Property-Level Identifier Exists in the MOJ Open Data

The MOJ open data platform publishes only operational statistics — transaction counts by date and location. No file in the dataset contains:
- A deed number (رقم صك) that could link to other deed operations
- A property identity/NCRE number
- A plan number (مخطط) in any 2025 file
- A parcel number (رقم قطعة) in any 2025 file
- Any other property-level key

### 3. Reference Numbers Cannot Bridge Categories

Confirmed with zero-overlap tests across all category pairs. الرقم المرجعي is a service-request ID, not a property ID. Each service request gets a new ID regardless of which property it concerns.

### 4. The Only Path to Property-Level Linking

Given the above, cross-category linking requires either:
- **NCRE / Real Estate General Authority (REGA; الهيئة العامة للعقار) open data** — the National Real Estate Register may publish property identity numbers that appear in transaction records. Not yet investigated.
- **MOJ API access** (authenticated) — the full transaction records behind the open data portal likely contain deed numbers and property IDs not published in the CSVs.
- **REGA Ejar Collector data** — rental transaction data may have different identifiers worth checking.
- **Probabilistic matching** — link by (region + city + district + date + price + area) as a composite fuzzy key across Sales files, accepting false positives. Only feasible for Sales data since other categories lack price/area.
- **2023-Q1 Sales as a seed** — this one file has المخطط + رقم القطعة + sale price + area. If REGA or NCRE data also has these fields, it could serve as a bridge for that quarter's properties.

---

## Appendix: File Anomalies Noted

1. **MOJ-Mortgage-Release-2025-Q3.csv** — column 0 header is `ج` (truncated, should be `المنطقة`). Data appears intact.
2. **MOJ-Sales-2023-Q1.csv** — unique 13-column schema, only file with المخطط and رقم القطعة. One-time data enrichment, not repeated.
3. **MOJ-RE-Operations files** — two different schemas: monthly 2024 files (8 cols with count aggregates) vs quarterly 2025 files (6 cols with row-per-transaction). Different data products despite same name prefix.
4. **Enforcement Sale** — uses a completely different reference number range (~14M in 2025) vs all other categories (~27–32M). May use a different backend system.
5. **Q2 Property Identity** — MOJ never published this file. Confirmed missing.
