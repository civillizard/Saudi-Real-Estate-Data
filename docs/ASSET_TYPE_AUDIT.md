# Asset Type Audit — Saudi Real Estate Dataset
<p align="center">
  <a href="https://rega.gov.sa"><img src="" height="50" alt="REGA - Real Estate General Authority (الهيئة العامة للعقار)"></a>
  &nbsp;&nbsp;&nbsp;&nbsp;
  <a href="https://moj.gov.sa"><img src="" height="50" alt="MOJ - Ministry of Justice (وزارة العدل)"></a>
</p>

*Scanned: 159 CSV files across moj/sales, moj/real-estate, rega/*
*Date: 2026-03-12*

---

## Executive Summary

**Yes, the data does distinguish land (أرض) from built properties.** The key column is `نوع العقار` (property type), which exists in three distinct file groups:

1. **Ministry of Justice (MOJ; وزارة العدل) Sales 2023-Q1 through Q3** — row-level, richest vocabulary
2. **Real Estate General Authority (REGA; الهيئة العامة للعقار) Sales Indicator files** — district-level aggregates
3. **REGA Rental Indicator files** — richest built-type vocabulary

The standard `تصنيف العقار` column (سكني/تجاري/زراعي/صناعي) provides sector classification only and **cannot** distinguish land from built property.

---

## Column Inventory — All Flagged Columns

### 1. `تصنيف العقار` — Property Classification (Sector)
**Files:** All MOJ Sales files (2020–2025), RE-Index-Regions, REGA Sales indicators (newer vintages)

**Values observed:**
```
سكني       (residential)
تجاري      (commercial)
زراعي      (agricultural)
صناعي      (industrial)   ← only in RE-Index-Regions 2018-2021
أخرى       (other)        ← only in REGA Sales 2025 files
جميع التصانيف (all categories) ← only in RE-Index-Regions
```

**Verdict:** Sector-only. Cannot distinguish land vs built.

---

### 2. `نوع العقار` — Property Type *** KEY COLUMN ***
**Files:** MOJ Sales 2023-Q1, Q2, Q3 only; REGA Sales indicators; REGA Rental indicators

#### MOJ Sales 2023-Q1 / Q2 / Q3 (row-level transaction data):
```
قطعة أرض      — vacant plot               3,881 / 4,061 / 3,909
شقة            — apartment                   938 /   766 /   862
أرض زراعية    — agricultural land            128 /   103 /   157
بيت            — house                        31 /    39 /    47
فيلا           — villa                          7 /     5 /     6
معرض/محل      — showroom/shop                  3 /    16 /    16
عمارة          — apartment building             4 /     6 /     1
مرفق           — utility/facility               2 /     2 /     2
إستراحة        — rest house                     2 /     — /     —
مركز تجاري    — shopping center                1 /     2 /     —
```
**Note:** This column disappeared from 2023-Q4 onward — MOJ reverted to تصنيف العقار only.

#### REGA Sales Indicators — 2024 vintage (district-level):
```
قطعة أرض-سكنى     — residential plot
قطعة أرض-تجارى    — commercial plot
فيلا              — villa
شقة               — apartment
عمارة             — apartment building
قطعة أرض- زراعي   — agricultural plot
```

#### REGA Sales Indicators — 2025 vintage (district-level):
```
أرض               — land (generic)
فيلا              — villa
شقة               — apartment
أخرى              — other
دور               — floor/unit
دوبلكس            — duplex
مبنى              — building
عمارة             — apartment building
```

#### REGA Rental Indicators — All regions (city-level aggregates):
```
شقة - سكني         — apartment, residential
دور - سكني         — floor/unit, residential
فيلا - سكني        — villa, residential
استديو - سكني      — studio, residential
دوبلاكس - سكني    — duplex, residential
محل - تجاري        — shop, commercial
مكتب - تجاري       — office, commercial
معرض تجاري - تجاري — showroom, commercial
```
**Note:** Two files (Eastern Province, Madinah) use English column header `Category` but identical Arabic values.

#### quarter-report-SI.csv — `typecategoryar` column:
```
شقة               — apartment
أخرى              — other
فيلا              — villa
قطعة أرض-تجارى   — commercial plot
قطعة أرض-سكنى    — residential plot
عمارة             — apartment building
قطعة أرض- زراعي  — agricultural plot
```

---

### 3. `نوع القطاع` — Sector Type
**Files:** All moj/real-estate/ files (86 files)

**Values:**
```
القطاع العام    — public sector
القطاع الخاص   — private sector
```
**Verdict:** Not property type. Refers to whether the transaction party is public or private.

---

### 4. `نوع الخدمة` — Service Type
**Files:** All moj/real-estate/ files

**Values:**
```
خدمة إلكترونية جزئيا   — partially electronic service
خدمة إلكترونية         — fully electronic service
```
**Verdict:** Digitization status of the deed transaction. Not property type.

---

### 5. `نوع العملية` — Operation Type
**Files:** MOJ-RE-Operations monthly files (2024-M01 through 2025-M12)

**Values (30+ distinct types):**
```
عقارات/افراغ                           — title transfer (sale)
عقارات/تعديل صك                        — deed amendment
عقارات/رهن العقارات                    — mortgage registration
عقارات/تسجيل ملكية عقار بدون صك       — ownership without deed
عقارات/فك رهن العقارات                — mortgage release
عقارات/منح                             — grant
عقارات/تسجيل صك قديم                  — old deed registration
عقارات/فرز صكوك                        — deed sorting
عقارات/حجز/فك حجز                     — seizure/release
عقارات/دمج عقارات                      — property merge
... (25+ more operation types)
```
**Verdict:** Legal operation type on the deed, not property type.

---

### 6. `نوع السند الرئيسي` — Primary Instrument Type
**Files:** MOJ-Enforcement-Sale files

**Values:**
```
احكام و قرارات          — court judgments & orders
أوراق تجارية            — commercial paper (checks/bills)
عقود                    — contracts
اخلاء                   — eviction orders
أوراق تجارية إلكترونية  — electronic commercial paper
مزاد                    — auction
عام                     — general
```
**Verdict:** Legal instrument for enforcement sales. Not property type.

---

## Schema Evolution Summary (MOJ Sales)

| Period       | Cols | Has تصنيف العقار | Has نوع العقار | Notes |
|-------------|------|-----------------|----------------|-------|
| 2020-Q1 → 2022-Q4 | 10 | YES | NO  | Sector only |
| 2023-Q1    | 13 | YES | YES | **Richest schema** — also adds: رقم مرجعي, الحي, المخطط, رقم القطعة, سعر المتر |
| 2023-Q2–Q3 | 11 | YES | YES | نوع العقار present, fewer extra cols than Q1 |
| 2023-Q4 → present | 10 | YES | NO  | Reverted to standard 10-col schema |

**The 2023-Q1 expanded schema is the only MOJ Sales file with both sector and detailed property type, plus parcel/plot identifiers (المخطط, رقم القطعة).**

---

## Land vs Built Property — Definitive Answer

| Source | Can distinguish? | Land terms | Built terms |
|--------|-----------------|------------|-------------|
| MOJ Sales 2023 Q1-Q3 | YES | قطعة أرض, أرض زراعية | شقة, فيلا, بيت, عمارة, معرض/محل |
| REGA Sales indicators 2024 | YES | قطعة أرض-سكنى, قطعة أرض-تجارى, قطعة أرض-زراعي | فيلا, شقة, عمارة |
| REGA Sales indicators 2025 | YES | أرض | فيلا, شقة, دور, دوبلكس, مبنى, عمارة |
| REGA Rental indicators | YES (built only) | — (no land rentals) | شقة, دور, فيلا, استديو, دوبلاكس, محل, مكتب, معرض |
| MOJ Sales 2020–2022, 2024+ | NO | تصنيف only | تصنيف only |
| moj/real-estate/ (all 86 files) | NO | sector/operation data | no property type detail |

---

## Files with No Relevant Property Type Data

- `MOJ-RE-Index-Cities-2018-2021.csv` — malformed headers (pivot table format)
- `MOJ-RE-Index-Districts-2018-2021.csv` — malformed headers (pivot table format)
- `MOJ-Ownership-Men-2025-Q*.csv` — gender ownership statistics only
- `Registered-Real-Estate-by-Gender-2024.csv` — 3 cols: Gender, RENs, Created Date

---

## Recommendations

1. **Best source for land vs built classification:** `MOJ-Sales-2023-Q1.csv` — has both `نوع العقار` (detailed) and `تصنيف العقار` (sector), plus parcel IDs (المخطط, رقم القطعة). Use this as ground truth for vocabulary mapping.

2. **For ongoing data (2024+):** REGA Sales indicator files have `نوع العقار` at the district/city level — usable for aggregate analysis but not row-level transactions.

3. **For rental market:** REGA Rental files have the richest built-unit taxonomy (شقة/دور/فيلا/استديو/دوبلكس/محل/مكتب/معرض).

4. **Standard pipeline (2020–2022, 2024+):** No row-level distinction between land and built. `تصنيف العقار = سكني` could be either a villa or a plot. Data is fundamentally ambiguous for land vs built in this period.

5. **Recommended mapping for analysis:**
   ```
   أرض / قطعة أرض / أرض زراعية   → LAND
   فيلا / بيت / إستراحة            → BUILT_RESIDENTIAL_VILLA
   شقة / استديو                    → BUILT_RESIDENTIAL_APT
   دور / دوبلكس                   → BUILT_RESIDENTIAL_FLOOR
   عمارة / مبنى                   → BUILT_RESIDENTIAL_BUILDING
   معرض/محل / مركز تجاري          → BUILT_COMMERCIAL
   مكتب                           → BUILT_COMMERCIAL_OFFICE
   مرفق                           → BUILT_UTILITY
   ```
