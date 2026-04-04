# Saudi Real Estate CSV Survey Report

<p align="center">
  <a href="https://rega.gov.sa">REGA - Real Estate General Authority (الهيئة العامة للعقار)</a>
  &nbsp;&nbsp;&nbsp;&nbsp;
  <a href="https://moj.gov.sa">MOJ - Ministry of Justice (وزارة العدل)</a>
</p>

_Generated: 2026-03-12 02:56:44_

## 1. Executive Summary

- **Total files surveyed:** 159
- **Total data rows (across all files):** 5,102,696
- **Categories:** 27
- **Files with parse errors:** 0
- **Encodings found:** {'utf-8': 6, 'utf-8-sig': 152, 'ascii': 1}

**Key risks identified:**
- Comma thousands separators: 133 column instances across files
- Arabic-Indic numerals: 0 column instances
- Mixed date formats: 0 columns

**Common patterns:**
- MOJ Sales files: 24 files, schema INCONSISTENT across all

---

## 2. Per-Category File Details


### MOJ Deed Define & Divide (3 files)


##### `MOJ-Deed-Define-Divide-2025-Q1.csv`

- **Size:** 897.3 KB  |  **Rows:** 8,045  |  **Cols:** 6
- **Encoding:** utf-8-sig  |  **BOM:** True  |  **Line ending:** CRLF
- **Delimiter:** ','  |  **Trailing empty rows:** 0
- **Sample rows analyzed:** 805

**Headers (6):** `المنطقة` | `المدينة` | `نوع القطاع` | `نوع الخدمة` | `التاريخ ميلادي` | `الرقم المرجعي`

**Column analysis:**

| Column | Type | Null% | Notes |
|--------|------|-------|-------|
| `المنطقة` | text | 0.0% |  |
| `المدينة` | text | 0.0% |  |
| `نوع القطاع` | text | 0.0% |  |
| `نوع الخدمة` | text | 0.0% |  |
| `التاريخ ميلادي` | date | 0.0% | Date format: YYYY/MM/DD |
| `الرقم المرجعي` | numeric (comma-sep thousands) | 0.0% | Comma thousands separators present |

##### `MOJ-Deed-Define-Divide-2025-Q2.csv`

- **Size:** 766.9 KB  |  **Rows:** 6,868  |  **Cols:** 6
- **Encoding:** utf-8-sig  |  **BOM:** True  |  **Line ending:** CRLF
- **Delimiter:** ','  |  **Trailing empty rows:** 0
- **Sample rows analyzed:** 687

**Headers (6):** `المنطقة` | `المدينة` | `نوع القطاع` | `نوع الخدمة` | `التاريخ ميلادي` | `الرقم المرجعي`

**Column analysis:**

| Column | Type | Null% | Notes |
|--------|------|-------|-------|
| `المنطقة` | text | 0.0% |  |
| `المدينة` | text | 0.0% |  |
| `نوع القطاع` | text | 0.0% |  |
| `نوع الخدمة` | text | 0.0% |  |
| `التاريخ ميلادي` | date | 0.0% | Date format: YYYY/MM/DD |
| `الرقم المرجعي` | numeric (comma-sep thousands) | 0.0% | Comma thousands separators present |

##### `MOJ-Deed-Define-Divide-2025-Q3.csv`

- **Size:** 788.0 KB  |  **Rows:** 7,053  |  **Cols:** 6
- **Encoding:** utf-8-sig  |  **BOM:** True  |  **Line ending:** CRLF
- **Delimiter:** ','  |  **Trailing empty rows:** 0
- **Sample rows analyzed:** 706

**Headers (6):** `المنطقة` | `المدينة` | `نوع القطاع` | `نوع الخدمة` | `التاريخ ميلادي` | `الرقم المرجعي`

**Column analysis:**

| Column | Type | Null% | Notes |
|--------|------|-------|-------|
| `المنطقة` | text | 0.0% |  |
| `المدينة` | text | 0.0% |  |
| `نوع القطاع` | text | 0.0% |  |
| `نوع الخدمة` | text | 0.0% |  |
| `التاريخ ميلادي` | date | 0.0% | Date format: YYYY/MM/DD |
| `الرقم المرجعي` | numeric (comma-sep thousands) | 0.0% | Comma thousands separators present |

### MOJ Divide (3 files)


##### `MOJ-Divide-2025-Q1.csv`

- **Size:** 3.4 MB  |  **Rows:** 31,343  |  **Cols:** 6
- **Encoding:** utf-8-sig  |  **BOM:** True  |  **Line ending:** CRLF
- **Delimiter:** ','  |  **Trailing empty rows:** 0
- **Sample rows analyzed:** 3135

**Headers (6):** `المنطقة` | `المدينة` | `نوع القطاع` | `نوع الخدمة` | `التاريخ ميلادي` | `الرقم المرجعي`

**Column analysis:**

| Column | Type | Null% | Notes |
|--------|------|-------|-------|
| `المنطقة` | text | 0.0% |  |
| `المدينة` | text | 0.0% |  |
| `نوع القطاع` | text | 0.0% |  |
| `نوع الخدمة` | text | 0.0% |  |
| `التاريخ ميلادي` | date | 0.0% | Date format: YYYY/MM/DD |
| `الرقم المرجعي` | numeric (comma-sep thousands) | 0.0% | Comma thousands separators present |

##### `MOJ-Divide-2025-Q2.csv`

- **Size:** 3.1 MB  |  **Rows:** 28,311  |  **Cols:** 6
- **Encoding:** utf-8-sig  |  **BOM:** True  |  **Line ending:** CRLF
- **Delimiter:** ','  |  **Trailing empty rows:** 0
- **Sample rows analyzed:** 2832

**Headers (6):** `المنطقة` | `المدينة` | `نوع القطاع` | `نوع الخدمة` | `التاريخ ميلادي` | `الرقم المرجعي`

**Column analysis:**

| Column | Type | Null% | Notes |
|--------|------|-------|-------|
| `المنطقة` | text | 0.0% |  |
| `المدينة` | text | 0.0% |  |
| `نوع القطاع` | text | 0.0% |  |
| `نوع الخدمة` | text | 0.0% |  |
| `التاريخ ميلادي` | date | 0.0% | Date format: DD/MM/YYYY or M/D/YYYY |
| `الرقم المرجعي` | numeric (comma-sep thousands) | 0.0% | Comma thousands separators present |

##### `MOJ-Divide-2025-Q3.csv`

- **Size:** 3.3 MB  |  **Rows:** 30,598  |  **Cols:** 6
- **Encoding:** utf-8-sig  |  **BOM:** True  |  **Line ending:** CRLF
- **Delimiter:** ','  |  **Trailing empty rows:** 0
- **Sample rows analyzed:** 3060

**Headers (6):** `المنطقة` | `المدينة` | `نوع القطاع` | `نوع الخدمة` | `التاريخ ميلادي` | `الرقم المرجعي`

**Column analysis:**

| Column | Type | Null% | Notes |
|--------|------|-------|-------|
| `المنطقة` | text | 0.0% |  |
| `المدينة` | text | 0.0% |  |
| `نوع القطاع` | text | 0.0% |  |
| `نوع الخدمة` | text | 0.0% |  |
| `التاريخ ميلادي` | date | 0.0% | Date format: YYYY/MM/DD |
| `الرقم المرجعي` | numeric (comma-sep thousands) | 0.0% | Comma thousands separators present |

### MOJ Enforcement Sale (4 files)


##### `MOJ-Enforcement-Sale-2025-Q1.csv`

- **Size:** 208.8 KB  |  **Rows:** 2,104  |  **Cols:** 6
- **Encoding:** utf-8-sig  |  **BOM:** True  |  **Line ending:** CRLF
- **Delimiter:** ','  |  **Trailing empty rows:** 0
- **Sample rows analyzed:** 211

**Headers (6):** `المنطقة` | `المدينة` | `نوع السند الرئيسي` | `تاريخ القرار ميلادي` | `تاريخ القرارهجري` | `الرقم المرجعي`

**Column analysis:**

| Column | Type | Null% | Notes |
|--------|------|-------|-------|
| `المنطقة` | text | 0.0% |  |
| `المدينة` | text | 0.0% |  |
| `نوع السند الرئيسي` | text | 0.0% |  |
| `تاريخ القرار ميلادي` | date | 0.0% | Date format: YYYY/MM/DD |
| `تاريخ القرارهجري` | date | 0.0% | Date format: YYYY/MM/DD |
| `الرقم المرجعي` | numeric (comma-sep thousands) | 0.0% | Comma thousands separators present |

##### `MOJ-Enforcement-Sale-2025-Q2.csv`

- **Size:** 131.4 KB  |  **Rows:** 1,701  |  **Cols:** 5
- **Encoding:** utf-8-sig  |  **BOM:** True  |  **Line ending:** CRLF
- **Delimiter:** ','  |  **Trailing empty rows:** 0
- **Sample rows analyzed:** 171

**Headers (5):** `المنطقة` | `المدينة` | `نوع السند الرئيسي` | `تاريخ القرار ميلادي` | `الرقم المرجعي`

**Column analysis:**

| Column | Type | Null% | Notes |
|--------|------|-------|-------|
| `المنطقة` | text | 0.0% |  |
| `المدينة` | text | 0.0% |  |
| `نوع السند الرئيسي` | text | 0.0% |  |
| `تاريخ القرار ميلادي` | date | 0.0% | Date format: YYYY/MM/DD |
| `الرقم المرجعي` | numeric (comma-sep thousands) | 0.0% | Comma thousands separators present |

##### `MOJ-Enforcement-Sale-2025-Q3.csv`

- **Size:** 174.3 KB  |  **Rows:** 2,298  |  **Cols:** 5
- **Encoding:** utf-8-sig  |  **BOM:** True  |  **Line ending:** CRLF
- **Delimiter:** ','  |  **Trailing empty rows:** 0
- **Sample rows analyzed:** 230

**Headers (5):** `المنطقة` | `المدينة` | `نوع السند الرئيسي` | `تاريخ القرار ميلادي` | `الرقم المرجعي`

**Column analysis:**

| Column | Type | Null% | Notes |
|--------|------|-------|-------|
| `المنطقة` | text | 0.0% |  |
| `المدينة` | text | 0.0% |  |
| `نوع السند الرئيسي` | text | 0.0% |  |
| `تاريخ القرار ميلادي` | date | 0.0% | Date format: YYYY/MM/DD |
| `الرقم المرجعي` | numeric (comma-sep thousands) | 0.0% | Comma thousands separators present |

##### `MOJ-Enforcement-Sale-2025-Q4.csv`

- **Size:** 163.5 KB  |  **Rows:** 2,184  |  **Cols:** 5
- **Encoding:** utf-8-sig  |  **BOM:** True  |  **Line ending:** CRLF
- **Delimiter:** ','  |  **Trailing empty rows:** 0
- **Sample rows analyzed:** 219

**Headers (5):** `المنطقة` | `المدينة` | `نوع السند الرئيسي` | `تاريخ القرار ميلادي` | `الرقم المرجعي`

**Column analysis:**

| Column | Type | Null% | Notes |
|--------|------|-------|-------|
| `المنطقة` | text | 0.0% |  |
| `المدينة` | text | 0.0% |  |
| `نوع السند الرئيسي` | text | 0.0% |  |
| `تاريخ القرار ميلادي` | date | 0.0% | Date format: YYYY/MM/DD |
| `الرقم المرجعي` | numeric (comma-sep thousands) | 0.0% | Comma thousands separators present |

### MOJ Merge Deed (3 files)


##### `MOJ-Merge-Deed-2025-Q1.csv`

- **Size:** 1.0 KB  |  **Rows:** 8  |  **Cols:** 6
- **Encoding:** utf-8-sig  |  **BOM:** True  |  **Line ending:** CRLF
- **Delimiter:** ','  |  **Trailing empty rows:** 0
- **Sample rows analyzed:** 8

**Headers (6):** `المنطقة` | `المدينة` | `نوع القطاع` | `نوع الخدمة` | `التاريخ ميلادي` | `الرقم المرجعي`

**Column analysis:**

| Column | Type | Null% | Notes |
|--------|------|-------|-------|
| `المنطقة` | text | 0.0% |  |
| `المدينة` | text | 0.0% |  |
| `نوع القطاع` | text | 0.0% |  |
| `نوع الخدمة` | text | 0.0% |  |
| `التاريخ ميلادي` | date | 0.0% | Date format: YYYY/MM/DD |
| `الرقم المرجعي` | numeric (comma-sep thousands) | 0.0% | Comma thousands separators present |

##### `MOJ-Merge-Deed-2025-Q2.csv`

- **Size:** 1.7 KB  |  **Rows:** 13  |  **Cols:** 6
- **Encoding:** utf-8-sig  |  **BOM:** True  |  **Line ending:** CRLF
- **Delimiter:** ','  |  **Trailing empty rows:** 0
- **Sample rows analyzed:** 13

**Headers (6):** `المنطقة` | `المدينة` | `نوع القطاع` | `نوع الخدمة` | `التاريخ ميلادي` | `الرقم المرجعي`

**Column analysis:**

| Column | Type | Null% | Notes |
|--------|------|-------|-------|
| `المنطقة` | text | 0.0% |  |
| `المدينة` | text | 0.0% |  |
| `نوع القطاع` | text | 0.0% |  |
| `نوع الخدمة` | text | 0.0% |  |
| `التاريخ ميلادي` | date | 0.0% | Date format: YYYY/MM/DD |
| `الرقم المرجعي` | numeric (comma-sep thousands) | 0.0% | Comma thousands separators present |

##### `MOJ-Merge-Deed-2025-Q3.csv`

- **Size:** 2.0 KB  |  **Rows:** 17  |  **Cols:** 6
- **Encoding:** utf-8-sig  |  **BOM:** True  |  **Line ending:** CRLF
- **Delimiter:** ','  |  **Trailing empty rows:** 0
- **Sample rows analyzed:** 17

**Headers (6):** `المنطقة` | `المدينة` | `نوع القطاع` | `نوع الخدمة` | `التاريخ ميلادي` | `الرقم المرجعي`

**Column analysis:**

| Column | Type | Null% | Notes |
|--------|------|-------|-------|
| `المنطقة` | text | 5.9% |  |
| `المدينة` | text | 5.9% |  |
| `نوع القطاع` | text | 5.9% |  |
| `نوع الخدمة` | text | 5.9% |  |
| `التاريخ ميلادي` | date | 5.9% | Date format: YYYY/MM/DD |
| `الرقم المرجعي` | numeric (comma-sep thousands) | 5.9% | Comma thousands separators present |

### MOJ Merge RE (3 files)


##### `MOJ-Merge-RE-2025-Q1.csv`

- **Size:** 415.6 KB  |  **Rows:** 3,688  |  **Cols:** 6
- **Encoding:** utf-8-sig  |  **BOM:** True  |  **Line ending:** CRLF
- **Delimiter:** ','  |  **Trailing empty rows:** 0
- **Sample rows analyzed:** 369

**Headers (6):** `المنطقة` | `المدينة` | `نوع القطاع` | `نوع الخدمة` | `التاريخ ميلادي` | `الرقم المرجعي`

**Column analysis:**

| Column | Type | Null% | Notes |
|--------|------|-------|-------|
| `المنطقة` | text | 0.0% |  |
| `المدينة` | text | 0.0% |  |
| `نوع القطاع` | text | 0.0% |  |
| `نوع الخدمة` | text | 0.0% |  |
| `التاريخ ميلادي` | date | 0.0% | Date format: YYYY/MM/DD |
| `الرقم المرجعي` | numeric (comma-sep thousands) | 0.0% | Comma thousands separators present |

##### `MOJ-Merge-RE-2025-Q2.csv`

- **Size:** 345.7 KB  |  **Rows:** 3,067  |  **Cols:** 6
- **Encoding:** utf-8-sig  |  **BOM:** True  |  **Line ending:** CRLF
- **Delimiter:** ','  |  **Trailing empty rows:** 0
- **Sample rows analyzed:** 307

**Headers (6):** `المنطقة` | `المدينة` | `نوع القطاع` | `نوع الخدمة` | `التاريخ ميلادي` | `الرقم المرجعي`

**Column analysis:**

| Column | Type | Null% | Notes |
|--------|------|-------|-------|
| `المنطقة` | text | 0.0% |  |
| `المدينة` | text | 0.0% |  |
| `نوع القطاع` | text | 0.0% |  |
| `نوع الخدمة` | text | 0.0% |  |
| `التاريخ ميلادي` | date | 0.0% | Date format: YYYY/MM/DD |
| `الرقم المرجعي` | numeric (comma-sep thousands) | 0.0% | Comma thousands separators present |

##### `MOJ-Merge-RE-2025-Q3.csv`

- **Size:** 413.5 KB  |  **Rows:** 3,674  |  **Cols:** 6
- **Encoding:** utf-8-sig  |  **BOM:** True  |  **Line ending:** CRLF
- **Delimiter:** ','  |  **Trailing empty rows:** 0
- **Sample rows analyzed:** 368

**Headers (6):** `المنطقة` | `المدينة` | `نوع القطاع` | `نوع الخدمة` | `التاريخ ميلادي` | `الرقم المرجعي`

**Column analysis:**

| Column | Type | Null% | Notes |
|--------|------|-------|-------|
| `المنطقة` | text | 0.0% |  |
| `المدينة` | text | 0.0% |  |
| `نوع القطاع` | text | 0.0% |  |
| `نوع الخدمة` | text | 0.0% |  |
| `التاريخ ميلادي` | date | 0.0% | Date format: YYYY/MM/DD |
| `الرقم المرجعي` | numeric (comma-sep thousands) | 0.0% | Comma thousands separators present |

### MOJ Mortgage (3 files)


##### `MOJ-Mortgage-2025-Q1.csv`

- **Size:** 1.2 MB  |  **Rows:** 11,167  |  **Cols:** 6
- **Encoding:** utf-8-sig  |  **BOM:** True  |  **Line ending:** CRLF
- **Delimiter:** ','  |  **Trailing empty rows:** 0
- **Sample rows analyzed:** 1117

**Headers (6):** `المنطقة` | `المدينة` | `نوع القطاع` | `نوع الخدمة` | `التاريخ ميلادي` | `الرقم المرجعي`

**Column analysis:**

| Column | Type | Null% | Notes |
|--------|------|-------|-------|
| `المنطقة` | text | 0.0% |  |
| `المدينة` | text | 0.0% |  |
| `نوع القطاع` | text | 0.0% |  |
| `نوع الخدمة` | text | 0.0% |  |
| `التاريخ ميلادي` | date | 0.0% | Date format: YYYY/MM/DD |
| `الرقم المرجعي` | numeric (comma-sep thousands) | 0.0% | Comma thousands separators present |

##### `MOJ-Mortgage-2025-Q2.csv`

- **Size:** 1.4 MB  |  **Rows:** 12,357  |  **Cols:** 6
- **Encoding:** utf-8-sig  |  **BOM:** True  |  **Line ending:** CRLF
- **Delimiter:** ','  |  **Trailing empty rows:** 0
- **Sample rows analyzed:** 1236

**Headers (6):** `المنطقة` | `المدينة` | `نوع القطاع` | `نوع الخدمة` | `التاريخ ميلادي` | `الرقم المرجعي`

**Column analysis:**

| Column | Type | Null% | Notes |
|--------|------|-------|-------|
| `المنطقة` | text | 0.0% |  |
| `المدينة` | text | 0.0% |  |
| `نوع القطاع` | text | 0.0% |  |
| `نوع الخدمة` | text | 0.0% |  |
| `التاريخ ميلادي` | date | 0.0% | Date format: YYYY/MM/DD |
| `الرقم المرجعي` | numeric (comma-sep thousands) | 0.0% | Comma thousands separators present |

##### `MOJ-Mortgage-2025-Q3.csv`

- **Size:** 1.4 MB  |  **Rows:** 13,003  |  **Cols:** 6
- **Encoding:** utf-8-sig  |  **BOM:** True  |  **Line ending:** CRLF
- **Delimiter:** ','  |  **Trailing empty rows:** 0
- **Sample rows analyzed:** 1301

**Headers (6):** `المنطقة` | `المدينة` | `نوع القطاع` | `نوع الخدمة` | `التاريخ ميلادي` | `الرقم المرجعي`

**Column analysis:**

| Column | Type | Null% | Notes |
|--------|------|-------|-------|
| `المنطقة` | text | 0.0% |  |
| `المدينة` | text | 0.0% |  |
| `نوع القطاع` | text | 0.0% |  |
| `نوع الخدمة` | text | 0.0% |  |
| `التاريخ ميلادي` | date | 0.0% | Date format: YYYY/MM/DD |
| `الرقم المرجعي` | numeric (comma-sep thousands) | 0.0% | Comma thousands separators present |

### MOJ Mortgage Release (3 files)


##### `MOJ-Mortgage-Release-2025-Q1.csv`

- **Size:** 1.6 MB  |  **Rows:** 14,698  |  **Cols:** 6
- **Encoding:** utf-8-sig  |  **BOM:** True  |  **Line ending:** CRLF
- **Delimiter:** ','  |  **Trailing empty rows:** 0
- **Sample rows analyzed:** 1470

**Headers (6):** `المنطقة` | `المدينة` | `نوع القطاع` | `نوع الخدمة` | `التاريخ ميلادي` | `الرقم المرجعي`

**Column analysis:**

| Column | Type | Null% | Notes |
|--------|------|-------|-------|
| `المنطقة` | text | 0.0% |  |
| `المدينة` | text | 0.0% |  |
| `نوع القطاع` | text | 0.0% |  |
| `نوع الخدمة` | text | 0.0% |  |
| `التاريخ ميلادي` | date | 0.0% | Date format: YYYY/MM/DD |
| `الرقم المرجعي` | numeric (comma-sep thousands) | 0.0% | Comma thousands separators present |

##### `MOJ-Mortgage-Release-2025-Q2.csv`

- **Size:** 1.4 MB  |  **Rows:** 13,040  |  **Cols:** 6
- **Encoding:** utf-8-sig  |  **BOM:** True  |  **Line ending:** CRLF
- **Delimiter:** ','  |  **Trailing empty rows:** 0
- **Sample rows analyzed:** 1304

**Headers (6):** `المنطقة` | `المدينة` | `نوع القطاع` | `نوع الخدمة` | `التاريخ ميلادي` | `الرقم المرجعي`

**Column analysis:**

| Column | Type | Null% | Notes |
|--------|------|-------|-------|
| `المنطقة` | text | 0.0% |  |
| `المدينة` | text | 0.0% |  |
| `نوع القطاع` | text | 0.0% |  |
| `نوع الخدمة` | text | 0.0% |  |
| `التاريخ ميلادي` | date | 0.0% | Date format: YYYY/MM/DD |
| `الرقم المرجعي` | numeric (comma-sep thousands) | 0.0% | Comma thousands separators present |

##### `MOJ-Mortgage-Release-2025-Q3.csv`

- **Size:** 1.6 MB  |  **Rows:** 15,045  |  **Cols:** 6
- **Encoding:** utf-8-sig  |  **BOM:** True  |  **Line ending:** CRLF
- **Delimiter:** ','  |  **Trailing empty rows:** 0
- **Sample rows analyzed:** 1505

**Headers (6):** `ج` | `المدينة` | `نوع القطاع` | `نوع الخدمة` | `التاريخ ميلادي` | `الرقم المرجعي`

**Column analysis:**

| Column | Type | Null% | Notes |
|--------|------|-------|-------|
| `ج` | text | 0.0% |  |
| `المدينة` | text | 0.0% |  |
| `نوع القطاع` | text | 0.0% |  |
| `نوع الخدمة` | text | 0.0% |  |
| `التاريخ ميلادي` | date | 0.0% | Date format: YYYY/MM/DD |
| `الرقم المرجعي` | numeric (comma-sep thousands) | 0.0% | Comma thousands separators present |

### MOJ Ownership (3 files)


##### `MOJ-Ownership-2025-Q1.csv`

- **Size:** 182.1 KB  |  **Rows:** 1,634  |  **Cols:** 6
- **Encoding:** utf-8-sig  |  **BOM:** True  |  **Line ending:** CRLF
- **Delimiter:** ','  |  **Trailing empty rows:** 0
- **Sample rows analyzed:** 164

**Headers (6):** `المنطقة` | `المدينة` | `نوع القطاع` | `نوع الخدمة` | `التاريخ ميلادي` | `الرقم المرجعي`

**Column analysis:**

| Column | Type | Null% | Notes |
|--------|------|-------|-------|
| `المنطقة` | text | 0.0% |  |
| `المدينة` | text | 0.0% |  |
| `نوع القطاع` | text | 0.0% |  |
| `نوع الخدمة` | text | 0.0% |  |
| `التاريخ ميلادي` | date | 0.0% | Date format: YYYY/MM/DD |
| `الرقم المرجعي` | numeric (comma-sep thousands) | 0.0% | Comma thousands separators present |

##### `MOJ-Ownership-2025-Q2.csv`

- **Size:** 179.9 KB  |  **Rows:** 1,633  |  **Cols:** 6
- **Encoding:** utf-8-sig  |  **BOM:** True  |  **Line ending:** CRLF
- **Delimiter:** ','  |  **Trailing empty rows:** 0
- **Sample rows analyzed:** 164

**Headers (6):** `المنطقة` | `المدينة` | `نوع القطاع` | `نوع الخدمة` | `التاريخ ميلادي` | `الرقم المرجعي`

**Column analysis:**

| Column | Type | Null% | Notes |
|--------|------|-------|-------|
| `المنطقة` | text | 0.0% |  |
| `المدينة` | text | 0.0% |  |
| `نوع القطاع` | text | 0.0% |  |
| `نوع الخدمة` | text | 0.0% |  |
| `التاريخ ميلادي` | date | 0.0% | Date format: DD/MM/YYYY or M/D/YYYY |
| `الرقم المرجعي` | numeric (comma-sep thousands) | 0.0% | Comma thousands separators present |

##### `MOJ-Ownership-2025-Q3.csv`

- **Size:** 216.5 KB  |  **Rows:** 1,943  |  **Cols:** 6
- **Encoding:** utf-8-sig  |  **BOM:** True  |  **Line ending:** CRLF
- **Delimiter:** ','  |  **Trailing empty rows:** 0
- **Sample rows analyzed:** 195

**Headers (6):** `المنطقة` | `المدينة` | `نوع القطاع` | `نوع الخدمة` | `التاريخ ميلادي` | `الرقم المرجعي`

**Column analysis:**

| Column | Type | Null% | Notes |
|--------|------|-------|-------|
| `المنطقة` | text | 0.0% |  |
| `المدينة` | text | 0.0% |  |
| `نوع القطاع` | text | 0.0% |  |
| `نوع الخدمة` | text | 0.0% |  |
| `التاريخ ميلادي` | date | 0.0% | Date format: YYYY/MM/DD |
| `الرقم المرجعي` | numeric (comma-sep thousands) | 0.0% | Comma thousands separators present |

### MOJ Ownership (Men) (3 files)


##### `MOJ-Ownership-Men-2025-Q1.csv`

- **Size:** 10.3 KB  |  **Rows:** 137  |  **Cols:** 6
- **Encoding:** utf-8-sig  |  **BOM:** True  |  **Line ending:** CRLF
- **Delimiter:** ','  |  **Trailing empty rows:** 0
- **Sample rows analyzed:** 69

**Headers (6):** `المنطقة` | `المدينة` | `السنة` | `ربع السنة` | `عدد الملاك النساء` | `نسبة تملك النساء`

**Column analysis:**

| Column | Type | Null% | Notes |
|--------|------|-------|-------|
| `المنطقة` | text | 1.4% |  |
| `المدينة` | text | 1.4% |  |
| `السنة` | date | 1.4% | Date format: YYYY |
| `ربع السنة` | text | 1.4% |  |
| `عدد الملاك النساء` | numeric | 1.4% | Comma thousands separators present |
| `نسبة تملك النساء` | percentage | 1.4% |  |

##### `MOJ-Ownership-Men-2025-Q2.csv`

- **Size:** 11.0 KB  |  **Rows:** 141  |  **Cols:** 6
- **Encoding:** utf-8-sig  |  **BOM:** True  |  **Line ending:** CRLF
- **Delimiter:** ','  |  **Trailing empty rows:** 0
- **Sample rows analyzed:** 71

**Headers (6):** `المنطقة` | `المدينة` | `السنة` | `ربع السنة` | `عدد الملاك النساء` | `نسبة تملك النساء`

**Column analysis:**

| Column | Type | Null% | Notes |
|--------|------|-------|-------|
| `المنطقة` | text | 0.0% |  |
| `المدينة` | text | 0.0% |  |
| `السنة` | date | 0.0% | Date format: YYYY |
| `ربع السنة` | text | 0.0% |  |
| `عدد الملاك النساء` | numeric | 0.0% | Comma thousands separators present |
| `نسبة تملك النساء` | percentage | 0.0% |  |

##### `MOJ-Ownership-Men-2025-Q3.csv`

- **Size:** 10.8 KB  |  **Rows:** 139  |  **Cols:** 6
- **Encoding:** utf-8-sig  |  **BOM:** True  |  **Line ending:** CRLF
- **Delimiter:** ','  |  **Trailing empty rows:** 0
- **Sample rows analyzed:** 70

**Headers (6):** `المنطقة` | `المدينة` | `السنة` | `ربع السنة` | `عدد الملاك النساء` | `نسبة تملك النساء`

**Column analysis:**

| Column | Type | Null% | Notes |
|--------|------|-------|-------|
| `المنطقة` | text | 0.0% |  |
| `المدينة` | text | 0.0% |  |
| `السنة` | date | 0.0% | Date format: YYYY |
| `ربع السنة` | text | 0.0% |  |
| `عدد الملاك النساء` | numeric | 0.0% | Comma thousands separators present |
| `نسبة تملك النساء` | percentage | 0.0% |  |

### MOJ POA RE Fund (2 files)


##### `MOJ-POA-RE-Fund-2025-Q1.csv`

- **Size:** 385.8 KB  |  **Rows:** 3,437  |  **Cols:** 6
- **Encoding:** utf-8-sig  |  **BOM:** True  |  **Line ending:** CRLF
- **Delimiter:** ','  |  **Trailing empty rows:** 0
- **Sample rows analyzed:** 344

**Headers (6):** `المنطقة` | `المدينة` | `نوع القطاع` | `نوع الخدمة` | `التاريخ ميلادي` | `الرقم المرجعي للوكالة`

**Column analysis:**

| Column | Type | Null% | Notes |
|--------|------|-------|-------|
| `المنطقة` | text | 0.0% |  |
| `المدينة` | text | 0.0% |  |
| `نوع القطاع` | text | 0.0% |  |
| `نوع الخدمة` | text | 0.0% |  |
| `التاريخ ميلادي` | date | 0.0% | Date format: YYYY/MM/DD |
| `الرقم المرجعي للوكالة` | numeric (comma-sep thousands) | 0.0% | Comma thousands separators present |

##### `MOJ-POA-RE-Fund-2025-Q3.csv`

- **Size:** 406.7 KB  |  **Rows:** 3,624  |  **Cols:** 6
- **Encoding:** utf-8-sig  |  **BOM:** True  |  **Line ending:** CRLF
- **Delimiter:** ','  |  **Trailing empty rows:** 0
- **Sample rows analyzed:** 363

**Headers (6):** `المنطقة` | `المدينة` | `نوع القطاع` | `نوع الخدمة` | `التاريخ ميلادي` | `الرقم المرجعي للوكالة`

**Column analysis:**

| Column | Type | Null% | Notes |
|--------|------|-------|-------|
| `المنطقة` | text | 0.0% |  |
| `المدينة` | text | 0.0% |  |
| `نوع القطاع` | text | 0.0% |  |
| `نوع الخدمة` | text | 0.0% |  |
| `التاريخ ميلادي` | date | 0.0% | Date format: YYYY/MM/DD |
| `الرقم المرجعي للوكالة` | numeric (comma-sep thousands) | 0.0% | Comma thousands separators present |

### MOJ POA Real Estate (3 files)


##### `MOJ-POA-RealEstate-2025-Q1.csv`

- **Size:** 27.2 MB  |  **Rows:** 246,026  |  **Cols:** 6
- **Encoding:** utf-8-sig  |  **BOM:** True  |  **Line ending:** CRLF
- **Delimiter:** ','  |  **Trailing empty rows:** 0
- **Sample rows analyzed:** 5021

**Headers (6):** `المنطقة` | `المدينة` | `نوع القطاع` | `نوع الخدمة` | `التاريخ ميلادي` | `الرقم المرجعي للوكالة`

**Column analysis:**

| Column | Type | Null% | Notes |
|--------|------|-------|-------|
| `المنطقة` | text | 0.0% |  |
| `المدينة` | text | 0.0% |  |
| `نوع القطاع` | text | 0.0% |  |
| `نوع الخدمة` | text | 0.0% |  |
| `التاريخ ميلادي` | date | 0.0% | Date format: YYYY/MM/DD |
| `الرقم المرجعي للوكالة` | numeric (comma-sep thousands) | 0.0% | Comma thousands separators present |

##### `MOJ-POA-RealEstate-2025-Q2.csv`

- **Size:** 26.6 MB  |  **Rows:** 240,360  |  **Cols:** 6
- **Encoding:** utf-8-sig  |  **BOM:** True  |  **Line ending:** CRLF
- **Delimiter:** ','  |  **Trailing empty rows:** 0
- **Sample rows analyzed:** 5008

**Headers (6):** `المنطقة` | `المدينة` | `نوع القطاع` | `نوع الخدمة` | `التاريخ ميلادي` | `الرقم المرجعي للوكالة`

**Column analysis:**

| Column | Type | Null% | Notes |
|--------|------|-------|-------|
| `المنطقة` | text | 0.0% |  |
| `المدينة` | text | 0.0% |  |
| `نوع القطاع` | text | 0.0% |  |
| `نوع الخدمة` | text | 0.0% |  |
| `التاريخ ميلادي` | date | 0.0% | Date format: YYYY/MM/DD |
| `الرقم المرجعي للوكالة` | numeric (comma-sep thousands) | 0.0% | Comma thousands separators present |

##### `MOJ-POA-RealEstate-2025-Q3.csv`

- **Size:** 30.1 MB  |  **Rows:** 271,618  |  **Cols:** 6
- **Encoding:** utf-8-sig  |  **BOM:** True  |  **Line ending:** CRLF
- **Delimiter:** ','  |  **Trailing empty rows:** 0
- **Sample rows analyzed:** 5030

**Headers (6):** `المنطقة` | `المدينة` | `نوع القطاع` | `نوع الخدمة` | `التاريخ ميلادي` | `الرقم المرجعي للوكالة`

**Column analysis:**

| Column | Type | Null% | Notes |
|--------|------|-------|-------|
| `المنطقة` | text | 0.0% |  |
| `المدينة` | text | 0.0% |  |
| `نوع القطاع` | text | 0.0% |  |
| `نوع الخدمة` | text | 0.0% |  |
| `التاريخ ميلادي` | date | 0.0% | Date format: YYYY/MM/DD |
| `الرقم المرجعي للوكالة` | numeric (comma-sep thousands) | 0.0% | Comma thousands separators present |

### MOJ Physical Registration (3 files)


##### `MOJ-Physical-Registration-2025-Q1.csv`

- **Size:** 16.4 MB  |  **Rows:** 165,689  |  **Cols:** 6
- **Encoding:** utf-8-sig  |  **BOM:** True  |  **Line ending:** CRLF
- **Delimiter:** ','  |  **Trailing empty rows:** 0
- **Sample rows analyzed:** 5021

**Headers (6):** `المنطقة` | `المدينة` | `نوع القطاع` | `نوع الخدمة` | `التاريخ ميلادي` | `الرقم المرجعي`

**Column analysis:**

| Column | Type | Null% | Notes |
|--------|------|-------|-------|
| `المنطقة` | text | 0.0% |  |
| `المدينة` | text | 0.0% |  |
| `نوع القطاع` | text | 0.0% |  |
| `نوع الخدمة` | text | 0.0% |  |
| `التاريخ ميلادي` | date | 0.0% | Date format: YYYY/MM/DD |
| `الرقم المرجعي` | numeric (comma-sep thousands) | 0.0% | Comma thousands separators present |

##### `MOJ-Physical-Registration-2025-Q2.csv`

- **Size:** 15.4 MB  |  **Rows:** 155,061  |  **Cols:** 6
- **Encoding:** utf-8-sig  |  **BOM:** True  |  **Line ending:** CRLF
- **Delimiter:** ','  |  **Trailing empty rows:** 0
- **Sample rows analyzed:** 5002

**Headers (6):** `المنطقة` | `المدينة` | `نوع القطاع` | `نوع الخدمة` | `التاريخ ميلادي` | `الرقم المرجعي`

**Column analysis:**

| Column | Type | Null% | Notes |
|--------|------|-------|-------|
| `المنطقة` | text | 0.0% |  |
| `المدينة` | text | 0.0% |  |
| `نوع القطاع` | text | 0.0% |  |
| `نوع الخدمة` | text | 0.0% |  |
| `التاريخ ميلادي` | date | 0.0% | Date format: YYYY/MM/DD |
| `الرقم المرجعي` | numeric (comma-sep thousands) | 0.0% | Comma thousands separators present |

##### `MOJ-Physical-Registration-2025-Q3.csv`

- **Size:** 17.9 MB  |  **Rows:** 180,302  |  **Cols:** 6
- **Encoding:** utf-8-sig  |  **BOM:** True  |  **Line ending:** CRLF
- **Delimiter:** ','  |  **Trailing empty rows:** 0
- **Sample rows analyzed:** 5009

**Headers (6):** `المنطقة` | `المدينة` | `نوع القطاع` | `نوع الخدمة` | `التاريخ ميلادي` | `الرقم المرجعي`

**Column analysis:**

| Column | Type | Null% | Notes |
|--------|------|-------|-------|
| `المنطقة` | text | 0.0% |  |
| `المدينة` | text | 0.0% |  |
| `نوع القطاع` | text | 0.0% |  |
| `نوع الخدمة` | text | 0.0% |  |
| `التاريخ ميلادي` | date | 0.0% | Date format: YYYY/MM/DD |
| `الرقم المرجعي` | numeric (comma-sep thousands) | 0.0% | Comma thousands separators present |

### MOJ Property Identity (2 files)


##### `MOJ-Property-Identity-2025-Q1.csv`

- **Size:** 1.7 MB  |  **Rows:** 15,605  |  **Cols:** 6
- **Encoding:** utf-8-sig  |  **BOM:** True  |  **Line ending:** CRLF
- **Delimiter:** ','  |  **Trailing empty rows:** 0
- **Sample rows analyzed:** 1561

**Headers (6):** `المنطقة` | `المدينة` | `نوع القطاع` | `نوع الخدمة` | `التاريخ ميلادي` | `الرقم المرجعي`

**Column analysis:**

| Column | Type | Null% | Notes |
|--------|------|-------|-------|
| `المنطقة` | text | 0.0% |  |
| `المدينة` | text | 0.0% |  |
| `نوع القطاع` | text | 0.0% |  |
| `نوع الخدمة` | text | 0.0% |  |
| `التاريخ ميلادي` | date | 0.0% | Date format: DD/MM/YYYY or M/D/YYYY |
| `الرقم المرجعي` | numeric (comma-sep thousands) | 0.0% | Comma thousands separators present |

##### `MOJ-Property-Identity-2025-Q3.csv`

- **Size:** 717.6 KB  |  **Rows:** 6,445  |  **Cols:** 6
- **Encoding:** utf-8-sig  |  **BOM:** True  |  **Line ending:** CRLF
- **Delimiter:** ','  |  **Trailing empty rows:** 0
- **Sample rows analyzed:** 645

**Headers (6):** `المنطقة` | `المدينة` | `نوع القطاع` | `نوع الخدمة` | `التاريخ ميلادي` | `الرقم المرجعي`

**Column analysis:**

| Column | Type | Null% | Notes |
|--------|------|-------|-------|
| `المنطقة` | text | 0.0% |  |
| `المدينة` | text | 0.0% |  |
| `نوع القطاع` | text | 0.0% |  |
| `نوع الخدمة` | text | 0.0% |  |
| `التاريخ ميلادي` | date | 0.0% | Date format: YYYY/MM/DD |
| `الرقم المرجعي` | numeric (comma-sep thousands) | 0.0% | Comma thousands separators present |

### MOJ RE Index (Price Indices) (3 files)


##### `MOJ-RE-Index-Cities-2018-2021.csv`

- **Size:** 19.1 KB  |  **Rows:** 220  |  **Cols:** 15
- **Encoding:** utf-8  |  **BOM:** False  |  **Line ending:** LF
- **Delimiter:** ','  |  **Trailing empty rows:** 0
- **Sample rows analyzed:** 55

**Headers (15):** `المؤشر العقاري لمدينة المدينة المنورة  في عام 2018 و2019 و2020 و 2021` | `Unnamed: 1` | `Unnamed: 2` | `Unnamed: 3` | `Unnamed: 4` | `Unnamed: 5` | `Unnamed: 6` | `Unnamed: 7` | `Unnamed: 8` | `Unnamed: 9` | `Unnamed: 10` | `Unnamed: 11` | `Unnamed: 12` | `Unnamed: 13` | `Unnamed: 14`

**Column analysis:**

| Column | Type | Null% | Notes |
|--------|------|-------|-------|
| `المؤشر العقاري لمدينة المدينة المنورة  في عام 2018 و2019 و2020 و 2021` | text | 3.6% |  |
| `Unnamed: 1` | text | 5.5% |  |
| `Unnamed: 2` | text | 29.1% |  |
| `Unnamed: 3` | numeric | 20.0% |  |
| `Unnamed: 4` | numeric | 20.0% | Date format: YYYY |
| `Unnamed: 5` | numeric | 20.0% |  |
| `Unnamed: 6` | numeric | 25.5% |  |
| `Unnamed: 7` | numeric | 25.5% |  |
| `Unnamed: 8` | numeric | 25.5% | Date format: YYYY |
| `Unnamed: 9` | numeric | 34.5% |  |
| `Unnamed: 10` | numeric | 34.5% |  |
| `Unnamed: 11` | numeric | 34.5% |  |
| `Unnamed: 12` | numeric | 70.9% |  |
| `Unnamed: 13` | numeric | 70.9% | Date format: YYYY |
| `Unnamed: 14` | numeric | 70.9% |  |

##### `MOJ-RE-Index-Districts-2018-2021.csv`

- **Size:** 136.6 KB  |  **Rows:** 2,128  |  **Cols:** 13
- **Encoding:** utf-8  |  **BOM:** False  |  **Line ending:** LF
- **Delimiter:** ','  |  **Trailing empty rows:** 0
- **Sample rows analyzed:** 213

**Headers (13):** `Unnamed: 0` | `Unnamed: 1` | `Unnamed: 2` | `Unnamed: 3` | `Unnamed: 4` | `Unnamed: 5` | `Unnamed: 6` | `Unnamed: 7` | `Unnamed: 8` | `Unnamed: 9` | `Unnamed: 10` | `Unnamed: 11` | `Unnamed: 12`

**Column analysis:**

| Column | Type | Null% | Notes |
|--------|------|-------|-------|
| `Unnamed: 0` | text | 0.0% |  |
| `Unnamed: 1` | numeric | 27.7% |  |
| `Unnamed: 2` | numeric | 27.7% | MIXED types: {'numeric': 136, 'date': 18}; Date format: YYYY |
| `Unnamed: 3` | numeric | 27.7% |  |
| `Unnamed: 4` | numeric | 19.2% |  |
| `Unnamed: 5` | numeric | 19.2% | MIXED types: {'numeric': 155, 'date': 17}; Date format: YYYY |
| `Unnamed: 6` | numeric | 19.2% |  |
| `Unnamed: 7` | numeric | 18.8% |  |
| `Unnamed: 8` | numeric | 18.8% | MIXED types: {'numeric': 154, 'date': 19}; Date format: YYYY |
| `Unnamed: 9` | numeric | 18.8% |  |
| `Unnamed: 10` | numeric | 66.2% |  |
| `Unnamed: 11` | numeric | 66.2% | Date format: YYYY |
| `Unnamed: 12` | numeric | 66.2% |  |

##### `MOJ-RE-Index-Regions-2018-2021.csv`

- **Size:** 102.3 KB  |  **Rows:** 660  |  **Cols:** 15
- **Encoding:** utf-8-sig  |  **BOM:** True  |  **Line ending:** CRLF
- **Delimiter:** ','  |  **Trailing empty rows:** 0
- **Sample rows analyzed:** 66

**Headers (15):** `المنطقة` | `الشهر` | `تصنيف العقار` | `2018` | `2018` | `2018` | `2019` | `2019` | `2019` | `2020` | `2020` | `2020` | `2021` | `2021` | `2021`

**Column analysis:**

| Column | Type | Null% | Notes |
|--------|------|-------|-------|
| `المنطقة` | text | 0.0% |  |
| `الشهر` | text | 0.0% |  |
| `تصنيف العقار` | text | 0.0% |  |
| `2018` | numeric | 4.5% | MIXED types: {'text': 1, 'numeric': 49, 'numeric_comma': 13}; Comma thousands separators present |
| `2019` | numeric | 4.5% | MIXED types: {'text': 1, 'numeric': 46, 'numeric_comma': 16}; Comma thousands separators present |
| `2020` | numeric | 6.1% | MIXED types: {'text': 1, 'numeric': 47, 'numeric_comma': 14}; Comma thousands separators present |
| `2021` | numeric | 68.2% | MIXED types: {'text': 1, 'numeric_comma': 6, 'numeric': 14}; Comma thousands separators present |

### MOJ RE Operations (27 files)


##### `MOJ-RE-Operations-2024-M01.csv`

- **Size:** 825.0 KB  |  **Rows:** 5,218  |  **Cols:** 8
- **Encoding:** utf-8-sig  |  **BOM:** True  |  **Line ending:** CRLF
- **Delimiter:** ','  |  **Trailing empty rows:** 0
- **Sample rows analyzed:** 522

**Headers (8):** `المنطقة` | `المدينة` | `نوع القطاع` | `نوع الخدمة` | `نوع العملية` | `التاريخ ميلادي` | `التاريخ هجري` | `عدد العمليات`

**Column analysis:**

| Column | Type | Null% | Notes |
|--------|------|-------|-------|
| `المنطقة` | text | 0.0% |  |
| `المدينة` | text | 0.0% |  |
| `نوع القطاع` | text | 0.0% |  |
| `نوع الخدمة` | text | 0.0% |  |
| `نوع العملية` | text | 0.0% |  |
| `التاريخ ميلادي` | date | 0.0% | Date format: YYYY/MM/DD |
| `التاريخ هجري` | date | 0.0% | Date format: YYYY/MM/DD |
| `عدد العمليات` | numeric | 0.0% | Comma thousands separators present |

##### `MOJ-RE-Operations-2024-M02.csv`

- **Size:** 731.8 KB  |  **Rows:** 4,633  |  **Cols:** 8
- **Encoding:** utf-8-sig  |  **BOM:** True  |  **Line ending:** CRLF
- **Delimiter:** ','  |  **Trailing empty rows:** 0
- **Sample rows analyzed:** 464

**Headers (8):** `المنطقة` | `المدينة` | `نوع القطاع` | `نوع الخدمة` | `نوع العملية` | `التاريخ ميلادي` | `التاريخ هجري` | `عدد العمليات`

**Column analysis:**

| Column | Type | Null% | Notes |
|--------|------|-------|-------|
| `المنطقة` | text | 0.0% |  |
| `المدينة` | text | 0.0% |  |
| `نوع القطاع` | text | 0.0% |  |
| `نوع الخدمة` | text | 0.0% |  |
| `نوع العملية` | text | 0.0% |  |
| `التاريخ ميلادي` | date | 0.0% | Date format: YYYY/MM/DD |
| `التاريخ هجري` | date | 0.0% | Date format: YYYY/MM/DD |
| `عدد العمليات` | numeric | 0.0% | Comma thousands separators present |

##### `MOJ-RE-Operations-2024-M03.csv`

- **Size:** 676.1 KB  |  **Rows:** 4,281  |  **Cols:** 8
- **Encoding:** utf-8-sig  |  **BOM:** True  |  **Line ending:** CRLF
- **Delimiter:** ','  |  **Trailing empty rows:** 0
- **Sample rows analyzed:** 429

**Headers (8):** `المنطقة` | `المدينة` | `نوع القطاع` | `نوع الخدمة` | `نوع العملية` | `التاريخ ميلادي` | `التاريخ هجري` | `عدد العمليات`

**Column analysis:**

| Column | Type | Null% | Notes |
|--------|------|-------|-------|
| `المنطقة` | text | 0.0% |  |
| `المدينة` | text | 0.0% |  |
| `نوع القطاع` | text | 0.0% |  |
| `نوع الخدمة` | text | 0.0% |  |
| `نوع العملية` | text | 0.0% |  |
| `التاريخ ميلادي` | date | 0.0% | Date format: YYYY/MM/DD |
| `التاريخ هجري` | date | 0.0% | Date format: YYYY/MM/DD |
| `عدد العمليات` | numeric | 0.0% | Comma thousands separators present |

##### `MOJ-RE-Operations-2024-M04.csv`

- **Size:** 506.1 KB  |  **Rows:** 3,211  |  **Cols:** 8
- **Encoding:** utf-8-sig  |  **BOM:** True  |  **Line ending:** CRLF
- **Delimiter:** ','  |  **Trailing empty rows:** 0
- **Sample rows analyzed:** 322

**Headers (8):** `المنطقة` | `المدينة` | `نوع القطاع` | `نوع الخدمة` | `نوع العملية` | `التاريخ ميلادي` | `التاريخ هجري` | `عدد العمليات`

**Column analysis:**

| Column | Type | Null% | Notes |
|--------|------|-------|-------|
| `المنطقة` | text | 0.3% |  |
| `المدينة` | text | 0.3% |  |
| `نوع القطاع` | text | 0.3% |  |
| `نوع الخدمة` | text | 0.3% |  |
| `نوع العملية` | text | 0.3% |  |
| `التاريخ ميلادي` | date | 0.3% | Date format: YYYY/MM/DD |
| `التاريخ هجري` | date | 0.3% | Date format: YYYY/MM/DD |
| `عدد العمليات` | numeric | 0.3% | Comma thousands separators present |

##### `MOJ-RE-Operations-2024-M05.csv`

- **Size:** 729.7 KB  |  **Rows:** 4,615  |  **Cols:** 8
- **Encoding:** utf-8-sig  |  **BOM:** True  |  **Line ending:** CRLF
- **Delimiter:** ','  |  **Trailing empty rows:** 0
- **Sample rows analyzed:** 462

**Headers (8):** `المنطقة` | `المدينة` | `نوع القطاع` | `نوع الخدمة` | `نوع العملية` | `التاريخ ميلادي` | `التاريخ هجري` | `عدد العمليات`

**Column analysis:**

| Column | Type | Null% | Notes |
|--------|------|-------|-------|
| `المنطقة` | text | 0.0% |  |
| `المدينة` | text | 0.0% |  |
| `نوع القطاع` | text | 0.0% |  |
| `نوع الخدمة` | text | 0.0% |  |
| `نوع العملية` | text | 0.0% |  |
| `التاريخ ميلادي` | date | 0.0% | Date format: YYYY/MM/DD |
| `التاريخ هجري` | date | 0.0% | Date format: YYYY/MM/DD |
| `عدد العمليات` | numeric | 0.0% | Comma thousands separators present |

##### `MOJ-RE-Operations-2024-M06.csv`

- **Size:** 459.8 KB  |  **Rows:** 2,899  |  **Cols:** 8
- **Encoding:** utf-8-sig  |  **BOM:** True  |  **Line ending:** CRLF
- **Delimiter:** ','  |  **Trailing empty rows:** 0
- **Sample rows analyzed:** 290

**Headers (8):** `المنطقة` | `المدينة` | `نوع القطاع` | `نوع الخدمة` | `نوع العملية` | `التاريخ ميلادي` | `التاريخ هجري` | `عدد العمليات`

**Column analysis:**

| Column | Type | Null% | Notes |
|--------|------|-------|-------|
| `المنطقة` | text | 0.0% |  |
| `المدينة` | text | 0.0% |  |
| `نوع القطاع` | text | 0.0% |  |
| `نوع الخدمة` | text | 0.0% |  |
| `نوع العملية` | text | 0.0% |  |
| `التاريخ ميلادي` | date | 0.0% | Date format: YYYY/MM/DD |
| `التاريخ هجري` | date | 0.0% | Date format: YYYY/MM/DD |
| `عدد العمليات` | numeric | 0.0% | Comma thousands separators present |

##### `MOJ-RE-Operations-2024-M07.csv`

- **Size:** 637.9 KB  |  **Rows:** 4,018  |  **Cols:** 8
- **Encoding:** utf-8-sig  |  **BOM:** True  |  **Line ending:** CRLF
- **Delimiter:** ','  |  **Trailing empty rows:** 0
- **Sample rows analyzed:** 402

**Headers (8):** `المنطقة` | `المدينة` | `نوع القطاع` | `نوع الخدمة` | `نوع العملية` | `التاريخ ميلادي` | `التاريخ هجري` | `عدد العمليات`

**Column analysis:**

| Column | Type | Null% | Notes |
|--------|------|-------|-------|
| `المنطقة` | text | 0.0% |  |
| `المدينة` | text | 0.0% |  |
| `نوع القطاع` | text | 0.0% |  |
| `نوع الخدمة` | text | 0.0% |  |
| `نوع العملية` | text | 0.0% |  |
| `التاريخ ميلادي` | date | 0.0% | Date format: YYYY/MM/DD |
| `التاريخ هجري` | date | 0.0% | Date format: YYYY/MM/DD |
| `عدد العمليات` | numeric | 0.0% | Comma thousands separators present |

##### `MOJ-RE-Operations-2024-M08.csv`

- **Size:** 607.3 KB  |  **Rows:** 3,822  |  **Cols:** 8
- **Encoding:** utf-8-sig  |  **BOM:** True  |  **Line ending:** CRLF
- **Delimiter:** ','  |  **Trailing empty rows:** 0
- **Sample rows analyzed:** 383

**Headers (8):** `المنطقة` | `المدينة` | `نوع القطاع` | `نوع الخدمة` | `نوع العملية` | `التاريخ ميلادي` | `التاريخ هجري` | `عدد العمليات`

**Column analysis:**

| Column | Type | Null% | Notes |
|--------|------|-------|-------|
| `المنطقة` | text | 0.0% |  |
| `المدينة` | text | 0.0% |  |
| `نوع القطاع` | text | 0.0% |  |
| `نوع الخدمة` | text | 0.0% |  |
| `نوع العملية` | text | 0.0% |  |
| `التاريخ ميلادي` | date | 0.0% | Date format: YYYY/MM/DD |
| `التاريخ هجري` | date | 0.0% | Date format: YYYY/MM/DD |
| `عدد العمليات` | numeric | 0.0% | Comma thousands separators present |

##### `MOJ-RE-Operations-2024-M09.csv`

- **Size:** 579.7 KB  |  **Rows:** 3,651  |  **Cols:** 8
- **Encoding:** utf-8-sig  |  **BOM:** True  |  **Line ending:** CRLF
- **Delimiter:** ','  |  **Trailing empty rows:** 0
- **Sample rows analyzed:** 366

**Headers (8):** `المنطقة` | `المدينة` | `نوع القطاع` | `نوع الخدمة` | `نوع العملية` | `التاريخ ميلادي` | `التاريخ هجري` | `عدد العمليات`

**Column analysis:**

| Column | Type | Null% | Notes |
|--------|------|-------|-------|
| `المنطقة` | text | 0.3% |  |
| `المدينة` | text | 0.3% |  |
| `نوع القطاع` | text | 0.3% |  |
| `نوع الخدمة` | text | 0.3% |  |
| `نوع العملية` | text | 0.3% |  |
| `التاريخ ميلادي` | date | 0.3% | Date format: YYYY/MM/DD |
| `التاريخ هجري` | date | 0.3% | Date format: YYYY/MM/DD |
| `عدد العمليات` | numeric | 0.3% | Comma thousands separators present |

##### `MOJ-RE-Operations-2024-M10.csv`

- **Size:** 641.2 KB  |  **Rows:** 4,019  |  **Cols:** 8
- **Encoding:** utf-8-sig  |  **BOM:** True  |  **Line ending:** CRLF
- **Delimiter:** ','  |  **Trailing empty rows:** 0
- **Sample rows analyzed:** 402

**Headers (8):** `المنطقة` | `المدينة` | `نوع القطاع` | `نوع الخدمة` | `نوع العملية` | `التاريخ ميلادي` | `التاريخ هجري` | `عدد العمليات`

**Column analysis:**

| Column | Type | Null% | Notes |
|--------|------|-------|-------|
| `المنطقة` | text | 0.0% |  |
| `المدينة` | text | 0.0% |  |
| `نوع القطاع` | text | 0.0% |  |
| `نوع الخدمة` | text | 0.0% |  |
| `نوع العملية` | text | 0.0% |  |
| `التاريخ ميلادي` | date | 0.0% | Date format: YYYY/MM/DD |
| `التاريخ هجري` | date | 0.0% | Date format: YYYY/MM/DD |
| `عدد العمليات` | numeric | 0.0% | Comma thousands separators present |

##### `MOJ-RE-Operations-2024-M11.csv`

- **Size:** 545.1 KB  |  **Rows:** 3,441  |  **Cols:** 8
- **Encoding:** utf-8-sig  |  **BOM:** True  |  **Line ending:** CRLF
- **Delimiter:** ','  |  **Trailing empty rows:** 0
- **Sample rows analyzed:** 345

**Headers (8):** `المنطقة` | `المدينة` | `نوع القطاع` | `نوع الخدمة` | `نوع العملية` | `التاريخ ميلادي` | `التاريخ هجري` | `عدد العمليات`

**Column analysis:**

| Column | Type | Null% | Notes |
|--------|------|-------|-------|
| `المنطقة` | text | 0.3% |  |
| `المدينة` | text | 0.3% |  |
| `نوع القطاع` | text | 0.3% |  |
| `نوع الخدمة` | text | 0.3% |  |
| `نوع العملية` | text | 0.3% |  |
| `التاريخ ميلادي` | date | 0.3% | Date format: YYYY/MM/DD |
| `التاريخ هجري` | date | 0.3% | Date format: YYYY/MM/DD |
| `عدد العمليات` | numeric | 0.3% | Comma thousands separators present |

##### `MOJ-RE-Operations-2024-M12.csv`

- **Size:** 607.5 KB  |  **Rows:** 3,816  |  **Cols:** 8
- **Encoding:** utf-8-sig  |  **BOM:** True  |  **Line ending:** CRLF
- **Delimiter:** ','  |  **Trailing empty rows:** 0
- **Sample rows analyzed:** 382

**Headers (8):** `المنطقة` | `المدينة` | `نوع القطاع` | `نوع الخدمة` | `نوع العملية` | `التاريخ ميلادي` | `التاريخ هجري` | `عدد العمليات`

**Column analysis:**

| Column | Type | Null% | Notes |
|--------|------|-------|-------|
| `المنطقة` | text | 0.0% |  |
| `المدينة` | text | 0.0% |  |
| `نوع القطاع` | text | 0.0% |  |
| `نوع الخدمة` | text | 0.0% |  |
| `نوع العملية` | text | 0.0% |  |
| `التاريخ ميلادي` | date | 0.0% | Date format: YYYY/MM/DD |
| `التاريخ هجري` | date | 0.0% | Date format: YYYY/MM/DD |
| `عدد العمليات` | numeric | 0.0% | Comma thousands separators present |

##### `MOJ-RE-Operations-2025-M01.csv`

- **Size:** 542.3 KB  |  **Rows:** 3,398  |  **Cols:** 8
- **Encoding:** utf-8-sig  |  **BOM:** True  |  **Line ending:** CRLF
- **Delimiter:** ','  |  **Trailing empty rows:** 0
- **Sample rows analyzed:** 340

**Headers (8):** `المنطقة` | `المدينة` | `نوع القطاع` | `نوع الخدمة` | `نوع العملية` | `التاريخ ميلادي` | `التاريخ هجري` | `عدد العمليات`

**Column analysis:**

| Column | Type | Null% | Notes |
|--------|------|-------|-------|
| `المنطقة` | text | 0.0% |  |
| `المدينة` | text | 0.0% |  |
| `نوع القطاع` | text | 0.0% |  |
| `نوع الخدمة` | text | 0.0% |  |
| `نوع العملية` | text | 0.0% |  |
| `التاريخ ميلادي` | date | 0.0% | Date format: YYYY/MM/DD |
| `التاريخ هجري` | date | 0.0% | Date format: YYYY/MM/DD |
| `عدد العمليات` | numeric | 0.0% | Comma thousands separators present |

##### `MOJ-RE-Operations-2025-M02.csv`

- **Size:** 478.6 KB  |  **Rows:** 3,003  |  **Cols:** 8
- **Encoding:** utf-8-sig  |  **BOM:** True  |  **Line ending:** CRLF
- **Delimiter:** ','  |  **Trailing empty rows:** 0
- **Sample rows analyzed:** 301

**Headers (8):** `المنطقة` | `المدينة` | `نوع القطاع` | `نوع الخدمة` | `نوع العملية` | `التاريخ ميلادي` | `التاريخ هجري` | `عدد العمليات`

**Column analysis:**

| Column | Type | Null% | Notes |
|--------|------|-------|-------|
| `المنطقة` | text | 0.0% |  |
| `المدينة` | text | 0.0% |  |
| `نوع القطاع` | text | 0.0% |  |
| `نوع الخدمة` | text | 0.0% |  |
| `نوع العملية` | text | 0.0% |  |
| `التاريخ ميلادي` | date | 0.0% | Date format: YYYY/MM/DD |
| `التاريخ هجري` | date | 0.0% | Date format: YYYY/MM/DD |
| `عدد العمليات` | numeric | 0.0% | Comma thousands separators present |

##### `MOJ-RE-Operations-2025-M03.csv`

- **Size:** 431.8 KB  |  **Rows:** 2,728  |  **Cols:** 8
- **Encoding:** utf-8-sig  |  **BOM:** True  |  **Line ending:** CRLF
- **Delimiter:** ','  |  **Trailing empty rows:** 0
- **Sample rows analyzed:** 273

**Headers (8):** `المنطقة` | `المدينة` | `نوع القطاع` | `نوع الخدمة` | `نوع العملية` | `التاريخ ميلادي` | `التاريخ هجري` | `عدد العمليات`

**Column analysis:**

| Column | Type | Null% | Notes |
|--------|------|-------|-------|
| `المنطقة` | text | 0.0% |  |
| `المدينة` | text | 0.0% |  |
| `نوع القطاع` | text | 0.0% |  |
| `نوع الخدمة` | text | 0.0% |  |
| `نوع العملية` | text | 0.0% |  |
| `التاريخ ميلادي` | date | 0.0% | Date format: YYYY/MM/DD |
| `التاريخ هجري` | date | 0.0% | Date format: YYYY/MM/DD |
| `عدد العمليات` | numeric | 0.0% | Comma thousands separators present |

##### `MOJ-RE-Operations-2025-M04.csv`

- **Size:** 486.4 KB  |  **Rows:** 3,069  |  **Cols:** 8
- **Encoding:** utf-8-sig  |  **BOM:** True  |  **Line ending:** CRLF
- **Delimiter:** ','  |  **Trailing empty rows:** 0
- **Sample rows analyzed:** 307

**Headers (8):** `المنطقة` | `المدينة` | `نوع القطاع` | `نوع الخدمة` | `نوع العملية` | `التاريخ ميلادي` | `التاريخ هجري` | `عدد العمليات`

**Column analysis:**

| Column | Type | Null% | Notes |
|--------|------|-------|-------|
| `المنطقة` | text | 0.0% |  |
| `المدينة` | text | 0.0% |  |
| `نوع القطاع` | text | 0.0% |  |
| `نوع الخدمة` | text | 0.0% |  |
| `نوع العملية` | text | 0.0% |  |
| `التاريخ ميلادي` | date | 0.0% | Date format: YYYY/MM/DD |
| `التاريخ هجري` | date | 0.0% | Date format: YYYY/MM/DD |
| `عدد العمليات` | numeric | 0.0% | Comma thousands separators present |

##### `MOJ-RE-Operations-2025-M05.csv`

- **Size:** 534.2 KB  |  **Rows:** 3,371  |  **Cols:** 8
- **Encoding:** utf-8-sig  |  **BOM:** True  |  **Line ending:** CRLF
- **Delimiter:** ','  |  **Trailing empty rows:** 0
- **Sample rows analyzed:** 338

**Headers (8):** `المنطقة` | `المدينة` | `نوع القطاع` | `نوع الخدمة` | `نوع العملية` | `التاريخ ميلادي` | `التاريخ هجري` | `عدد العمليات`

**Column analysis:**

| Column | Type | Null% | Notes |
|--------|------|-------|-------|
| `المنطقة` | text | 0.3% |  |
| `المدينة` | text | 0.3% |  |
| `نوع القطاع` | text | 0.3% |  |
| `نوع الخدمة` | text | 0.3% |  |
| `نوع العملية` | text | 0.3% |  |
| `التاريخ ميلادي` | date | 0.3% | Date format: YYYY/MM/DD |
| `التاريخ هجري` | date | 0.3% | Date format: YYYY/MM/DD |
| `عدد العمليات` | numeric | 0.3% | Comma thousands separators present |

##### `MOJ-RE-Operations-2025-M06.csv`

- **Size:** 377.9 KB  |  **Rows:** 2,381  |  **Cols:** 8
- **Encoding:** utf-8-sig  |  **BOM:** True  |  **Line ending:** CRLF
- **Delimiter:** ','  |  **Trailing empty rows:** 0
- **Sample rows analyzed:** 239

**Headers (8):** `المنطقة` | `المدينة` | `نوع القطاع` | `نوع الخدمة` | `نوع العملية` | `التاريخ ميلادي` | `التاريخ هجري` | `عدد العمليات`

**Column analysis:**

| Column | Type | Null% | Notes |
|--------|------|-------|-------|
| `المنطقة` | text | 0.0% |  |
| `المدينة` | text | 0.0% |  |
| `نوع القطاع` | text | 0.0% |  |
| `نوع الخدمة` | text | 0.0% |  |
| `نوع العملية` | text | 0.0% |  |
| `التاريخ ميلادي` | date | 0.0% | Date format: YYYY/MM/DD |
| `التاريخ هجري` | date | 0.0% | Date format: YYYY/MM/DD |
| `عدد العمليات` | numeric | 0.0% | Comma thousands separators present |

##### `MOJ-RE-Operations-2025-M07.csv`

- **Size:** 526.5 KB  |  **Rows:** 3,323  |  **Cols:** 8
- **Encoding:** utf-8-sig  |  **BOM:** True  |  **Line ending:** CRLF
- **Delimiter:** ','  |  **Trailing empty rows:** 0
- **Sample rows analyzed:** 333

**Headers (8):** `المنطقة` | `المدينة` | `نوع القطاع` | `نوع الخدمة` | `نوع العملية` | `التاريخ ميلادي` | `التاريخ هجري` | `عدد العمليات`

**Column analysis:**

| Column | Type | Null% | Notes |
|--------|------|-------|-------|
| `المنطقة` | text | 0.0% |  |
| `المدينة` | text | 0.0% |  |
| `نوع القطاع` | text | 0.0% |  |
| `نوع الخدمة` | text | 0.0% |  |
| `نوع العملية` | text | 0.0% |  |
| `التاريخ ميلادي` | date | 0.0% | Date format: YYYY/MM/DD |
| `التاريخ هجري` | date | 0.0% | Date format: YYYY/MM/DD |
| `عدد العمليات` | numeric | 0.0% | Comma thousands separators present |

##### `MOJ-RE-Operations-2025-M08.csv`

- **Size:** 498.9 KB  |  **Rows:** 3,141  |  **Cols:** 8
- **Encoding:** utf-8-sig  |  **BOM:** True  |  **Line ending:** CRLF
- **Delimiter:** ','  |  **Trailing empty rows:** 0
- **Sample rows analyzed:** 315

**Headers (8):** `المنطقة` | `المدينة` | `نوع القطاع` | `نوع الخدمة` | `نوع العملية` | `التاريخ ميلادي` | `التاريخ هجري` | `عدد العمليات`

**Column analysis:**

| Column | Type | Null% | Notes |
|--------|------|-------|-------|
| `المنطقة` | text | 0.3% |  |
| `المدينة` | text | 0.3% |  |
| `نوع القطاع` | text | 0.3% |  |
| `نوع الخدمة` | text | 0.3% |  |
| `نوع العملية` | text | 0.3% |  |
| `التاريخ ميلادي` | date | 0.3% | Date format: YYYY/MM/DD |
| `التاريخ هجري` | date | 0.3% | Date format: YYYY/MM/DD |
| `عدد العمليات` | numeric | 0.3% | Comma thousands separators present |

##### `MOJ-RE-Operations-2025-M09.csv`

- **Size:** 496.9 KB  |  **Rows:** 3,122  |  **Cols:** 8
- **Encoding:** utf-8-sig  |  **BOM:** True  |  **Line ending:** CRLF
- **Delimiter:** ','  |  **Trailing empty rows:** 0
- **Sample rows analyzed:** 313

**Headers (8):** `المنطقة` | `المدينة` | `نوع القطاع` | `نوع الخدمة` | `نوع العملية` | `التاريخ ميلادي` | `التاريخ هجري` | `عدد العمليات`

**Column analysis:**

| Column | Type | Null% | Notes |
|--------|------|-------|-------|
| `المنطقة` | text | 0.0% |  |
| `المدينة` | text | 0.0% |  |
| `نوع القطاع` | text | 0.0% |  |
| `نوع الخدمة` | text | 0.0% |  |
| `نوع العملية` | text | 0.0% |  |
| `التاريخ ميلادي` | date | 0.0% | Date format: YYYY/MM/DD |
| `التاريخ هجري` | date | 0.0% | Date format: YYYY/MM/DD |
| `عدد العمليات` | numeric | 0.0% | Comma thousands separators present |

##### `MOJ-RE-Operations-2025-M10.csv`

- **Size:** 521.2 KB  |  **Rows:** 3,270  |  **Cols:** 8
- **Encoding:** utf-8-sig  |  **BOM:** True  |  **Line ending:** CRLF
- **Delimiter:** ','  |  **Trailing empty rows:** 0
- **Sample rows analyzed:** 327

**Headers (8):** `المنطقة` | `المدينة` | `نوع القطاع` | `نوع الخدمة` | `نوع العملية` | `التاريخ ميلادي` | `التاريخ هجري` | `عدد العمليات`

**Column analysis:**

| Column | Type | Null% | Notes |
|--------|------|-------|-------|
| `المنطقة` | text | 0.0% |  |
| `المدينة` | text | 0.0% |  |
| `نوع القطاع` | text | 0.0% |  |
| `نوع الخدمة` | text | 0.0% |  |
| `نوع العملية` | text | 0.0% |  |
| `التاريخ ميلادي` | date | 0.0% | Date format: YYYY/MM/DD |
| `التاريخ هجري` | date | 0.0% | Date format: YYYY/MM/DD |
| `عدد العمليات` | numeric | 0.0% | Comma thousands separators present |

##### `MOJ-RE-Operations-2025-M11.csv`

- **Size:** 466.0 KB  |  **Rows:** 2,923  |  **Cols:** 8
- **Encoding:** utf-8-sig  |  **BOM:** True  |  **Line ending:** CRLF
- **Delimiter:** ','  |  **Trailing empty rows:** 0
- **Sample rows analyzed:** 293

**Headers (8):** `المنطقة` | `المدينة` | `نوع القطاع` | `نوع الخدمة` | `نوع العملية` | `التاريخ ميلادي` | `التاريخ هجري` | `عدد العمليات`

**Column analysis:**

| Column | Type | Null% | Notes |
|--------|------|-------|-------|
| `المنطقة` | text | 0.0% |  |
| `المدينة` | text | 0.0% |  |
| `نوع القطاع` | text | 0.0% |  |
| `نوع الخدمة` | text | 0.0% |  |
| `نوع العملية` | text | 0.0% |  |
| `التاريخ ميلادي` | date | 0.0% | Date format: YYYY/MM/DD |
| `التاريخ هجري` | date | 0.0% | Date format: YYYY/MM/DD |
| `عدد العمليات` | numeric | 0.0% | Comma thousands separators present |

##### `MOJ-RE-Operations-2025-M12.csv`

- **Size:** 513.2 KB  |  **Rows:** 3,206  |  **Cols:** 8
- **Encoding:** utf-8-sig  |  **BOM:** True  |  **Line ending:** CRLF
- **Delimiter:** ','  |  **Trailing empty rows:** 0
- **Sample rows analyzed:** 321

**Headers (8):** `المنطقة` | `المدينة` | `نوع القطاع` | `نوع الخدمة` | `نوع العملية` | `التاريخ ميلادي` | `التاريخ هجري` | `عدد العمليات`

**Column analysis:**

| Column | Type | Null% | Notes |
|--------|------|-------|-------|
| `المنطقة` | text | 0.0% |  |
| `المدينة` | text | 0.0% |  |
| `نوع القطاع` | text | 0.0% |  |
| `نوع الخدمة` | text | 0.0% |  |
| `نوع العملية` | text | 0.0% |  |
| `التاريخ ميلادي` | date | 0.0% | Date format: YYYY/MM/DD |
| `التاريخ هجري` | date | 0.0% | Date format: YYYY/MM/DD |
| `عدد العمليات` | numeric | 0.0% | Comma thousands separators present |

##### `MOJ-RE-Operations-2025-Q1.csv`

- **Size:** 40.9 KB  |  **Rows:** 362  |  **Cols:** 6
- **Encoding:** utf-8-sig  |  **BOM:** True  |  **Line ending:** CRLF
- **Delimiter:** ','  |  **Trailing empty rows:** 0
- **Sample rows analyzed:** 52

**Headers (6):** `المنطقة` | `المدينة` | `نوع القطاع` | `نوع الخدمة` | `التاريخ ميلادي` | `الرقم المرجعي`

**Column analysis:**

| Column | Type | Null% | Notes |
|--------|------|-------|-------|
| `المنطقة` | text | 0.0% |  |
| `المدينة` | text | 0.0% |  |
| `نوع القطاع` | text | 0.0% |  |
| `نوع الخدمة` | text | 0.0% |  |
| `التاريخ ميلادي` | date | 0.0% | Date format: YYYY/MM/DD |
| `الرقم المرجعي` | numeric (comma-sep thousands) | 0.0% | Comma thousands separators present |

##### `MOJ-RE-Operations-2025-Q2.csv`

- **Size:** 22.4 MB  |  **Rows:** 197,480  |  **Cols:** 6
- **Encoding:** utf-8-sig  |  **BOM:** True  |  **Line ending:** CRLF
- **Delimiter:** ','  |  **Trailing empty rows:** 0
- **Sample rows analyzed:** 5064

**Headers (6):** `المنطقة` | `المدينة` | `نوع القطاع` | `نوع الخدمة` | `التاريخ ميلادي` | `الرقم المرجعي`

**Column analysis:**

| Column | Type | Null% | Notes |
|--------|------|-------|-------|
| `المنطقة` | text | 0.0% |  |
| `المدينة` | text | 0.0% |  |
| `نوع القطاع` | text | 0.0% |  |
| `نوع الخدمة` | text | 0.0% |  |
| `التاريخ ميلادي` | date | 0.0% | Date format: YYYY/MM/DD |
| `الرقم المرجعي` | numeric (comma-sep thousands) | 0.0% | Comma thousands separators present |

##### `MOJ-RE-Operations-2025-Q3.csv`

- **Size:** 1.8 KB  |  **Rows:** 16  |  **Cols:** 6
- **Encoding:** utf-8-sig  |  **BOM:** True  |  **Line ending:** CRLF
- **Delimiter:** ','  |  **Trailing empty rows:** 0
- **Sample rows analyzed:** 16

**Headers (6):** `المنطقة` | `المدينة` | `نوع القطاع` | `نوع الخدمة` | `التاريخ ميلادي` | `الرقم المرجعي`

**Column analysis:**

| Column | Type | Null% | Notes |
|--------|------|-------|-------|
| `المنطقة` | text | 6.2% |  |
| `المدينة` | text | 6.2% |  |
| `نوع القطاع` | text | 6.2% |  |
| `نوع الخدمة` | text | 6.2% |  |
| `التاريخ ميلادي` | date | 6.2% | Date format: YYYY/MM/DD |
| `الرقم المرجعي` | numeric (comma-sep thousands) | 6.2% | Comma thousands separators present |

### MOJ Register No Deed (3 files)


##### `MOJ-Register-No-Deed-2025-Q1.csv`

- **Size:** 660.0 KB  |  **Rows:** 5,873  |  **Cols:** 6
- **Encoding:** utf-8-sig  |  **BOM:** True  |  **Line ending:** CRLF
- **Delimiter:** ','  |  **Trailing empty rows:** 0
- **Sample rows analyzed:** 588

**Headers (6):** `المنطقة` | `المدينة` | `نوع القطاع` | `نوع الخدمة` | `التاريخ ميلادي` | `الرقم المرجعي`

**Column analysis:**

| Column | Type | Null% | Notes |
|--------|------|-------|-------|
| `المنطقة` | text | 0.0% |  |
| `المدينة` | text | 0.0% |  |
| `نوع القطاع` | text | 0.0% |  |
| `نوع الخدمة` | text | 0.0% |  |
| `التاريخ ميلادي` | date | 0.0% | Date format: YYYY/MM/DD |
| `الرقم المرجعي` | numeric (comma-sep thousands) | 0.0% | Comma thousands separators present |

##### `MOJ-Register-No-Deed-2025-Q2.csv`

- **Size:** 744.1 KB  |  **Rows:** 6,643  |  **Cols:** 6
- **Encoding:** utf-8-sig  |  **BOM:** True  |  **Line ending:** CRLF
- **Delimiter:** ','  |  **Trailing empty rows:** 0
- **Sample rows analyzed:** 665

**Headers (6):** `المنطقة` | `المدينة` | `نوع القطاع` | `نوع الخدمة` | `التاريخ ميلادي` | `الرقم المرجعي`

**Column analysis:**

| Column | Type | Null% | Notes |
|--------|------|-------|-------|
| `المنطقة` | text | 0.0% |  |
| `المدينة` | text | 0.0% |  |
| `نوع القطاع` | text | 0.0% |  |
| `نوع الخدمة` | text | 0.0% |  |
| `التاريخ ميلادي` | date | 0.0% | Date format: YYYY/MM/DD |
| `الرقم المرجعي` | numeric (comma-sep thousands) | 0.0% | Comma thousands separators present |

##### `MOJ-Register-No-Deed-2025-Q3.csv`

- **Size:** 983.5 KB  |  **Rows:** 8,826  |  **Cols:** 6
- **Encoding:** utf-8-sig  |  **BOM:** True  |  **Line ending:** CRLF
- **Delimiter:** ','  |  **Trailing empty rows:** 0
- **Sample rows analyzed:** 883

**Headers (6):** `المنطقة` | `المدينة` | `نوع القطاع` | `نوع الخدمة` | `التاريخ ميلادي` | `الرقم المرجعي`

**Column analysis:**

| Column | Type | Null% | Notes |
|--------|------|-------|-------|
| `المنطقة` | text | 0.0% |  |
| `المدينة` | text | 0.0% |  |
| `نوع القطاع` | text | 0.0% |  |
| `نوع الخدمة` | text | 0.0% |  |
| `التاريخ ميلادي` | date | 0.0% | Date format: YYYY/MM/DD |
| `الرقم المرجعي` | numeric (comma-sep thousands) | 0.0% | Comma thousands separators present |

### MOJ Register Old Deed (3 files)


##### `MOJ-Register-Old-Deed-2025-Q1.csv`

- **Size:** 6.2 MB  |  **Rows:** 52,017  |  **Cols:** 6
- **Encoding:** utf-8-sig  |  **BOM:** True  |  **Line ending:** CRLF
- **Delimiter:** ','  |  **Trailing empty rows:** 0
- **Sample rows analyzed:** 5202

**Headers (6):** `المنطقة` | `المدينة` | `نوع القطاع` | `نوع الخدمة` | `التاريخ ميلادي` | `الرقم المرجعي`

**Column analysis:**

| Column | Type | Null% | Notes |
|--------|------|-------|-------|
| `المنطقة` | text | 0.0% |  |
| `المدينة` | text | 0.0% |  |
| `نوع القطاع` | text | 0.0% |  |
| `نوع الخدمة` | text | 0.0% |  |
| `التاريخ ميلادي` | date | 0.0% | Date format: YYYY/MM/DD |
| `الرقم المرجعي` | numeric (comma-sep thousands) | 0.0% | Comma thousands separators present |

##### `MOJ-Register-Old-Deed-2025-Q2.csv`

- **Size:** 4.9 MB  |  **Rows:** 41,172  |  **Cols:** 6
- **Encoding:** utf-8-sig  |  **BOM:** True  |  **Line ending:** CRLF
- **Delimiter:** ','  |  **Trailing empty rows:** 0
- **Sample rows analyzed:** 4118

**Headers (6):** `المنطقة` | `المدينة` | `نوع القطاع` | `نوع الخدمة` | `التاريخ ميلادي` | `الرقم المرجعي`

**Column analysis:**

| Column | Type | Null% | Notes |
|--------|------|-------|-------|
| `المنطقة` | text | 0.0% |  |
| `المدينة` | text | 0.0% |  |
| `نوع القطاع` | text | 0.0% |  |
| `نوع الخدمة` | text | 0.0% |  |
| `التاريخ ميلادي` | date | 0.0% | Date format: YYYY/MM/DD |
| `الرقم المرجعي` | numeric (comma-sep thousands) | 0.0% | Comma thousands separators present |

##### `MOJ-Register-Old-Deed-2025-Q3.csv`

- **Size:** 5.9 MB  |  **Rows:** 49,840  |  **Cols:** 6
- **Encoding:** utf-8-sig  |  **BOM:** True  |  **Line ending:** CRLF
- **Delimiter:** ','  |  **Trailing empty rows:** 0
- **Sample rows analyzed:** 4984

**Headers (6):** `المنطقة` | `المدينة` | `نوع القطاع` | `نوع الخدمة` | `التاريخ ميلادي` | `الرقم المرجعي`

**Column analysis:**

| Column | Type | Null% | Notes |
|--------|------|-------|-------|
| `المنطقة` | text | 0.0% |  |
| `المدينة` | text | 0.0% |  |
| `نوع القطاع` | text | 0.0% |  |
| `نوع الخدمة` | text | 0.0% |  |
| `التاريخ ميلادي` | date | 0.0% | Date format: YYYY/MM/DD |
| `الرقم المرجعي` | numeric (comma-sep thousands) | 0.0% | Comma thousands separators present |

### MOJ Release of Seizure (3 files)


##### `MOJ-Release-Seizure-2025-Q1.csv`

- **Size:** 15.2 MB  |  **Rows:** 154,875  |  **Cols:** 6
- **Encoding:** utf-8-sig  |  **BOM:** True  |  **Line ending:** CRLF
- **Delimiter:** ','  |  **Trailing empty rows:** 0
- **Sample rows analyzed:** 5163

**Headers (6):** `المنطقة` | `المدينة` | `نوع القطاع` | `نوع الخدمة` | `التاريخ ميلادي` | `الرقم المرجعي`

**Column analysis:**

| Column | Type | Null% | Notes |
|--------|------|-------|-------|
| `المنطقة` | text | 0.0% |  |
| `المدينة` | text | 0.0% |  |
| `نوع القطاع` | text | 0.0% |  |
| `نوع الخدمة` | text | 0.0% |  |
| `التاريخ ميلادي` | date | 0.0% | Date format: DD/MM/YYYY or M/D/YYYY |
| `الرقم المرجعي` | numeric (comma-sep thousands) | 0.0% | Comma thousands separators present |

##### `MOJ-Release-Seizure-2025-Q2.csv`

- **Size:** 14.4 MB  |  **Rows:** 145,648  |  **Cols:** 6
- **Encoding:** utf-8-sig  |  **BOM:** True  |  **Line ending:** CRLF
- **Delimiter:** ','  |  **Trailing empty rows:** 0
- **Sample rows analyzed:** 5023

**Headers (6):** `المنطقة` | `المدينة` | `نوع القطاع` | `نوع الخدمة` | `التاريخ ميلادي` | `الرقم المرجعي`

**Column analysis:**

| Column | Type | Null% | Notes |
|--------|------|-------|-------|
| `المنطقة` | text | 0.0% |  |
| `المدينة` | text | 0.0% |  |
| `نوع القطاع` | text | 0.0% |  |
| `نوع الخدمة` | text | 0.0% |  |
| `التاريخ ميلادي` | date | 0.0% | Date format: YYYY/MM/DD |
| `الرقم المرجعي` | numeric (comma-sep thousands) | 0.0% | Comma thousands separators present |

##### `MOJ-Release-Seizure-2025-Q3.csv`

- **Size:** 20.4 MB  |  **Rows:** 205,204  |  **Cols:** 6
- **Encoding:** utf-8-sig  |  **BOM:** True  |  **Line ending:** CRLF
- **Delimiter:** ','  |  **Trailing empty rows:** 0
- **Sample rows analyzed:** 5005

**Headers (6):** `المنطقة` | `المدينة` | `نوع القطاع` | `نوع الخدمة` | `التاريخ ميلادي` | `الرقم المرجعي`

**Column analysis:**

| Column | Type | Null% | Notes |
|--------|------|-------|-------|
| `المنطقة` | text | 0.0% |  |
| `المدينة` | text | 0.0% |  |
| `نوع القطاع` | text | 0.0% |  |
| `نوع الخدمة` | text | 0.0% |  |
| `التاريخ ميلادي` | date | 0.0% | Date format: YYYY/MM/DD |
| `الرقم المرجعي` | numeric (comma-sep thousands) | 0.0% | Comma thousands separators present |

### MOJ Sales Transactions (24 files)


##### `MOJ-Sales-2020-Q1.csv`

- **Size:** 10.0 MB  |  **Rows:** 80,635  |  **Cols:** 10
- **Encoding:** utf-8-sig  |  **BOM:** True  |  **Line ending:** CRLF
- **Delimiter:** ','  |  **Trailing empty rows:** 0
- **Sample rows analyzed:** 5040

**Headers (10):** `المنطقة` | `المدينة` | `المدينة / الحي` | `الرقم المرجعي للصفقة` | `تاريخ الصفقة ميلادي` | `تاريخ الصفقة هجري` | `تصنيف العقار` | `عدد العقارات` | `السعر` | `المساحة`

**Column analysis:**

| Column | Type | Null% | Notes |
|--------|------|-------|-------|
| `المنطقة` | text | 0.0% |  |
| `المدينة` | text | 0.0% |  |
| `المدينة / الحي` | text | 0.0% |  |
| `الرقم المرجعي للصفقة` | numeric | 0.0% |  |
| `تاريخ الصفقة ميلادي` | date | 0.0% | Date format: YYYY/MM/DD |
| `تاريخ الصفقة هجري` | date | 0.0% | Date format: YYYY/MM/DD |
| `تصنيف العقار` | text | 0.0% |  |
| `عدد العقارات` | numeric | 0.0% |  |
| `السعر` | numeric (comma-sep thousands) | 0.0% | Comma thousands separators present |
| `المساحة` | numeric | 0.0% | MIXED types: {'numeric': 4685, 'numeric_comma': 355}; Comma thousands separators present |

##### `MOJ-Sales-2020-Q2.csv`

- **Size:** 6.2 MB  |  **Rows:** 49,618  |  **Cols:** 10
- **Encoding:** utf-8-sig  |  **BOM:** True  |  **Line ending:** CRLF
- **Delimiter:** ','  |  **Trailing empty rows:** 0
- **Sample rows analyzed:** 4962

**Headers (10):** `المنطقة` | `المدينة` | `المدينة / الحي` | `الرقم المرجعي للصفقة` | `تاريخ الصفقة ميلادي` | `تاريخ الصفقة هجري` | `تصنيف العقار` | `عدد العقارات` | `السعر` | `المساحة`

**Column analysis:**

| Column | Type | Null% | Notes |
|--------|------|-------|-------|
| `المنطقة` | text | 0.0% |  |
| `المدينة` | text | 0.0% |  |
| `المدينة / الحي` | text | 0.0% |  |
| `الرقم المرجعي للصفقة` | numeric | 0.0% |  |
| `تاريخ الصفقة ميلادي` | date | 0.0% | Date format: YYYY/MM/DD |
| `تاريخ الصفقة هجري` | date | 0.0% | Date format: YYYY/MM/DD |
| `تصنيف العقار` | text | 0.0% |  |
| `عدد العقارات` | numeric | 0.0% |  |
| `السعر` | numeric (comma-sep thousands) | 0.0% | Comma thousands separators present |
| `المساحة` | numeric | 0.0% | MIXED types: {'numeric': 4445, 'numeric_comma': 517}; Comma thousands separators present |

##### `MOJ-Sales-2020-Q3.csv`

- **Size:** 8.0 MB  |  **Rows:** 64,317  |  **Cols:** 10
- **Encoding:** utf-8-sig  |  **BOM:** True  |  **Line ending:** CRLF
- **Delimiter:** ','  |  **Trailing empty rows:** 0
- **Sample rows analyzed:** 5360

**Headers (10):** `المنطقة` | `المدينة` | `المدينة / الحي` | `الرقم المرجعي للصفقة` | `تاريخ الصفقة ميلادي` | `تاريخ الصفقة هجري` | `تصنيف العقار` | `عدد العقارات` | `السعر` | `المساحة`

**Column analysis:**

| Column | Type | Null% | Notes |
|--------|------|-------|-------|
| `المنطقة` | text | 0.0% |  |
| `المدينة` | text | 0.0% |  |
| `المدينة / الحي` | text | 0.0% |  |
| `الرقم المرجعي للصفقة` | numeric | 0.0% |  |
| `تاريخ الصفقة ميلادي` | date | 0.0% | Date format: YYYY/MM/DD |
| `تاريخ الصفقة هجري` | date | 0.0% | Date format: YYYY/MM/DD |
| `تصنيف العقار` | text | 0.0% |  |
| `عدد العقارات` | numeric | 0.0% |  |
| `السعر` | numeric (comma-sep thousands) | 0.0% | Comma thousands separators present |
| `المساحة` | numeric | 0.0% | MIXED types: {'numeric': 4833, 'numeric_comma': 527}; Comma thousands separators present |

##### `MOJ-Sales-2020-Q4.csv`

- **Size:** 10.3 MB  |  **Rows:** 82,244  |  **Cols:** 10
- **Encoding:** utf-8-sig  |  **BOM:** True  |  **Line ending:** CRLF
- **Delimiter:** ','  |  **Trailing empty rows:** 0
- **Sample rows analyzed:** 5141

**Headers (10):** `المنطقة` | `المدينة` | `المدينة / الحي` | `الرقم المرجعي للصفقة` | `تاريخ الصفقة ميلادي` | `تاريخ الصفقة هجري` | `تصنيف العقار` | `عدد العقارات` | `السعر` | `المساحة`

**Column analysis:**

| Column | Type | Null% | Notes |
|--------|------|-------|-------|
| `المنطقة` | text | 0.0% |  |
| `المدينة` | text | 0.0% |  |
| `المدينة / الحي` | text | 0.0% |  |
| `الرقم المرجعي للصفقة` | numeric | 0.0% |  |
| `تاريخ الصفقة ميلادي` | date | 0.0% | Date format: YYYY/MM/DD |
| `تاريخ الصفقة هجري` | date | 0.0% | Date format: YYYY/MM/DD |
| `تصنيف العقار` | text | 0.0% |  |
| `عدد العقارات` | numeric | 0.0% |  |
| `السعر` | numeric (comma-sep thousands) | 0.0% | Comma thousands separators present |
| `المساحة` | numeric | 0.0% | MIXED types: {'numeric': 4575, 'numeric_comma': 566}; Comma thousands separators present |

##### `MOJ-Sales-2021-Q1.csv`

- **Size:** 11.6 MB  |  **Rows:** 92,963  |  **Cols:** 10
- **Encoding:** utf-8-sig  |  **BOM:** True  |  **Line ending:** CRLF
- **Delimiter:** ','  |  **Trailing empty rows:** 0
- **Sample rows analyzed:** 5165

**Headers (10):** `المنطقة` | `المدينة` | `المدينة / الحي` | `الرقم المرجعي للصفقة` | `تاريخ الصفقة ميلادي` | `تاريخ الصفقة هجري` | `تصنيف العقار` | `عدد العقارات` | `السعر` | `المساحة`

**Column analysis:**

| Column | Type | Null% | Notes |
|--------|------|-------|-------|
| `المنطقة` | text | 0.0% |  |
| `المدينة` | text | 0.0% |  |
| `المدينة / الحي` | text | 0.0% |  |
| `الرقم المرجعي للصفقة` | numeric | 0.0% |  |
| `تاريخ الصفقة ميلادي` | date | 0.0% | Date format: YYYY/MM/DD |
| `تاريخ الصفقة هجري` | date | 0.0% | Date format: YYYY/MM/DD |
| `تصنيف العقار` | text | 0.0% |  |
| `عدد العقارات` | numeric | 0.0% |  |
| `السعر` | numeric (comma-sep thousands) | 0.0% | Comma thousands separators present |
| `المساحة` | numeric | 0.0% | MIXED types: {'numeric': 4568, 'numeric_comma': 597}; Comma thousands separators present |

##### `MOJ-Sales-2021-Q2.csv`

- **Size:** 8.3 MB  |  **Rows:** 66,672  |  **Cols:** 10
- **Encoding:** utf-8-sig  |  **BOM:** True  |  **Line ending:** CRLF
- **Delimiter:** ','  |  **Trailing empty rows:** 0
- **Sample rows analyzed:** 5129

**Headers (10):** `المنطقة` | `المدينة` | `المدينة / الحي` | `الرقم المرجعي للصفقة` | `تاريخ الصفقة ميلادي` | `تاريخ الصفقة هجري` | `تصنيف العقار` | `عدد العقارات` | `السعر` | `المساحة`

**Column analysis:**

| Column | Type | Null% | Notes |
|--------|------|-------|-------|
| `المنطقة` | text | 0.0% |  |
| `المدينة` | text | 0.0% |  |
| `المدينة / الحي` | text | 0.0% |  |
| `الرقم المرجعي للصفقة` | numeric | 0.0% |  |
| `تاريخ الصفقة ميلادي` | date | 0.0% | Date format: YYYY/MM/DD |
| `تاريخ الصفقة هجري` | date | 0.0% | Date format: YYYY/MM/DD |
| `تصنيف العقار` | text | 0.0% |  |
| `عدد العقارات` | numeric | 0.0% |  |
| `السعر` | numeric (comma-sep thousands) | 0.0% | Comma thousands separators present |
| `المساحة` | numeric | 0.0% | MIXED types: {'numeric': 4532, 'numeric_comma': 597}; Comma thousands separators present |

##### `MOJ-Sales-2021-Q3.csv`

- **Size:** 7.0 MB  |  **Rows:** 55,911  |  **Cols:** 10
- **Encoding:** utf-8-sig  |  **BOM:** True  |  **Line ending:** CRLF
- **Delimiter:** ','  |  **Trailing empty rows:** 0
- **Sample rows analyzed:** 5083

**Headers (10):** `المنطقة` | `المدينة` | `المدينة / الحي` | `الرقم المرجعي للصفقة` | `تاريخ الصفقة ميلادي` | `تاريخ الصفقة هجري` | `تصنيف العقار` | `عدد العقارات` | `السعر` | `المساحة`

**Column analysis:**

| Column | Type | Null% | Notes |
|--------|------|-------|-------|
| `المنطقة` | text | 0.0% |  |
| `المدينة` | text | 0.0% |  |
| `المدينة / الحي` | text | 0.0% |  |
| `الرقم المرجعي للصفقة` | numeric | 0.0% |  |
| `تاريخ الصفقة ميلادي` | date | 0.0% | Date format: YYYY/MM/DD |
| `تاريخ الصفقة هجري` | date | 0.0% | Date format: YYYY/MM/DD |
| `تصنيف العقار` | text | 0.0% |  |
| `عدد العقارات` | numeric | 0.0% |  |
| `السعر` | numeric (comma-sep thousands) | 0.0% | Comma thousands separators present |
| `المساحة` | numeric | 0.0% | MIXED types: {'numeric': 4415, 'numeric_comma': 668}; Comma thousands separators present |

##### `MOJ-Sales-2021-Q4.csv`

- **Size:** 8.3 MB  |  **Rows:** 66,339  |  **Cols:** 10
- **Encoding:** utf-8-sig  |  **BOM:** True  |  **Line ending:** CRLF
- **Delimiter:** ','  |  **Trailing empty rows:** 0
- **Sample rows analyzed:** 5103

**Headers (10):** `المنطقة` | `المدينة` | `المدينة / الحي` | `الرقم المرجعي للصفقة` | `تاريخ الصفقة ميلادي` | `تاريخ الصفقة هجري` | `تصنيف العقار` | `عدد العقارات` | `السعر` | `المساحة`

**Column analysis:**

| Column | Type | Null% | Notes |
|--------|------|-------|-------|
| `المنطقة` | text | 0.0% |  |
| `المدينة` | text | 0.0% |  |
| `المدينة / الحي` | text | 0.0% |  |
| `الرقم المرجعي للصفقة` | numeric | 0.0% |  |
| `تاريخ الصفقة ميلادي` | date | 0.0% | Date format: YYYY/MM/DD |
| `تاريخ الصفقة هجري` | date | 0.0% | Date format: YYYY/MM/DD |
| `تصنيف العقار` | text | 0.0% |  |
| `عدد العقارات` | numeric | 0.0% |  |
| `السعر` | numeric (comma-sep thousands) | 0.0% | Comma thousands separators present |
| `المساحة` | numeric | 0.0% | MIXED types: {'numeric_comma': 650, 'numeric': 4453}; Comma thousands separators present |

##### `MOJ-Sales-2022-Q1.csv`

- **Size:** 9.0 MB  |  **Rows:** 71,252  |  **Cols:** 10
- **Encoding:** utf-8-sig  |  **BOM:** True  |  **Line ending:** CRLF
- **Delimiter:** ','  |  **Trailing empty rows:** 0
- **Sample rows analyzed:** 5090

**Headers (10):** `المنطقة` | `المدينة` | `المدينة / الحي` | `الرقم المرجعي للصفقة` | `تاريخ الصفقة ميلادي` | `تاريخ الصفقة هجري` | `تصنيف العقار` | `عدد العقارات` | `السعر` | `المساحة`

**Column analysis:**

| Column | Type | Null% | Notes |
|--------|------|-------|-------|
| `المنطقة` | text | 0.0% |  |
| `المدينة` | text | 0.0% |  |
| `المدينة / الحي` | text | 0.0% |  |
| `الرقم المرجعي للصفقة` | numeric | 0.0% |  |
| `تاريخ الصفقة ميلادي` | date | 0.0% | Date format: YYYY/MM/DD |
| `تاريخ الصفقة هجري` | date | 0.0% | Date format: YYYY/MM/DD |
| `تصنيف العقار` | text | 0.0% |  |
| `عدد العقارات` | numeric | 0.0% |  |
| `السعر` | numeric (comma-sep thousands) | 0.0% | Comma thousands separators present |
| `المساحة` | numeric | 0.0% | MIXED types: {'numeric': 4579, 'numeric_comma': 511}; Comma thousands separators present |

##### `MOJ-Sales-2022-Q2.csv`

- **Size:** 6.7 MB  |  **Rows:** 53,016  |  **Cols:** 10
- **Encoding:** utf-8-sig  |  **BOM:** True  |  **Line ending:** CRLF
- **Delimiter:** ','  |  **Trailing empty rows:** 0
- **Sample rows analyzed:** 5302

**Headers (10):** `المنطقة` | `المدينة` | `المدينة / الحي` | `الرقم المرجعي للصفقة` | `تاريخ الصفقة ميلادي` | `تاريخ الصفقة هجري` | `تصنيف العقار` | `عدد العقارات` | `السعر` | `المساحة`

**Column analysis:**

| Column | Type | Null% | Notes |
|--------|------|-------|-------|
| `المنطقة` | text | 0.0% |  |
| `المدينة` | text | 0.0% |  |
| `المدينة / الحي` | text | 0.0% |  |
| `الرقم المرجعي للصفقة` | numeric | 0.0% |  |
| `تاريخ الصفقة ميلادي` | date | 0.0% | Date format: YYYY/MM/DD |
| `تاريخ الصفقة هجري` | date | 0.0% | Date format: YYYY/MM/DD |
| `تصنيف العقار` | text | 0.0% |  |
| `عدد العقارات` | numeric | 0.0% |  |
| `السعر` | numeric (comma-sep thousands) | 0.0% | Comma thousands separators present |
| `المساحة` | numeric | 0.0% | MIXED types: {'numeric': 4746, 'numeric_comma': 556}; Comma thousands separators present |

##### `MOJ-Sales-2022-Q3.csv`

- **Size:** 5.8 MB  |  **Rows:** 45,976  |  **Cols:** 10
- **Encoding:** utf-8-sig  |  **BOM:** True  |  **Line ending:** CRLF
- **Delimiter:** ','  |  **Trailing empty rows:** 0
- **Sample rows analyzed:** 4598

**Headers (10):** `المنطقة` | `المدينة` | `المدينة / الحي` | `الرقم المرجعي للصفقة` | `تاريخ الصفقة ميلادي` | `تاريخ الصفقة هجري` | `تصنيف العقار` | `عدد العقارات` | `السعر` | `المساحة`

**Column analysis:**

| Column | Type | Null% | Notes |
|--------|------|-------|-------|
| `المنطقة` | text | 0.0% |  |
| `المدينة` | text | 0.0% |  |
| `المدينة / الحي` | text | 0.0% |  |
| `الرقم المرجعي للصفقة` | numeric | 0.0% |  |
| `تاريخ الصفقة ميلادي` | date | 0.0% | Date format: YYYY/MM/DD |
| `تاريخ الصفقة هجري` | date | 0.0% | Date format: YYYY/MM/DD |
| `تصنيف العقار` | text | 0.0% |  |
| `عدد العقارات` | numeric | 0.0% |  |
| `السعر` | numeric (comma-sep thousands) | 0.0% | Comma thousands separators present |
| `المساحة` | numeric | 0.0% | MIXED types: {'numeric': 4099, 'numeric_comma': 499}; Comma thousands separators present |

##### `MOJ-Sales-2022-Q4.csv`

- **Size:** 5.5 MB  |  **Rows:** 43,512  |  **Cols:** 10
- **Encoding:** utf-8-sig  |  **BOM:** True  |  **Line ending:** CRLF
- **Delimiter:** ','  |  **Trailing empty rows:** 0
- **Sample rows analyzed:** 4352

**Headers (10):** `المنطقة` | `المدينة` | `المدينة / الحي` | `الرقم المرجعي للصفقة` | `تاريخ الصفقة ميلادي` | `تاريخ الصفقة هجري` | `تصنيف العقار` | `عدد العقارات` | `السعر` | `المساحة`

**Column analysis:**

| Column | Type | Null% | Notes |
|--------|------|-------|-------|
| `المنطقة` | text | 0.0% |  |
| `المدينة` | text | 0.0% |  |
| `المدينة / الحي` | text | 0.0% |  |
| `الرقم المرجعي للصفقة` | numeric | 0.0% |  |
| `تاريخ الصفقة ميلادي` | date | 0.0% | Date format: YYYY/MM/DD |
| `تاريخ الصفقة هجري` | date | 0.0% | Date format: YYYY/MM/DD |
| `تصنيف العقار` | text | 0.0% |  |
| `عدد العقارات` | numeric | 0.0% |  |
| `السعر` | numeric (comma-sep thousands) | 0.0% | Comma thousands separators present |
| `المساحة` | numeric | 0.0% | MIXED types: {'numeric': 3885, 'numeric_comma': 467}; Comma thousands separators present |

##### `MOJ-Sales-2023-Q1.csv`

- **Size:** 6.9 MB  |  **Rows:** 44,091  |  **Cols:** 13
- **Encoding:** utf-8  |  **BOM:** False  |  **Line ending:** LF
- **Delimiter:** ','  |  **Trailing empty rows:** 0
- **Sample rows analyzed:** 4410

**Headers (13):** `رقم مرجعي` | `المنطقة` | `المدينة` | `الحي` | `المخطط` | `رقم القطعة` | `التاريخ` | `تصنيف العقار` | `نوع العقار` | `عدد العقارات` | `السعر بالريال السعودي` | `المساحة ` | `سعر المتر المربع`

**Column analysis:**

| Column | Type | Null% | Notes |
|--------|------|-------|-------|
| `رقم مرجعي` | numeric | 0.0% |  |
| `المنطقة` | text | 0.0% |  |
| `المدينة` | text | 0.0% |  |
| `الحي` | text | 0.0% |  |
| `المخطط` | text | 0.0% |  |
| `رقم القطعة` | text | 0.0% |  |
| `التاريخ` | date | 0.0% | Date format: DD/MM/YYYY or M/D/YYYY |
| `تصنيف العقار` | text | 0.0% |  |
| `نوع العقار` | text | 0.0% |  |
| `عدد العقارات` | numeric | 0.0% |  |
| `السعر بالريال السعودي` | numeric | 0.0% |  |
| `المساحة ` | numeric | 0.0% |  |
| `سعر المتر المربع` | numeric | 0.0% |  |

##### `MOJ-Sales-2023-Q2.csv`

- **Size:** 5.3 MB  |  **Rows:** 38,811  |  **Cols:** 11
- **Encoding:** utf-8  |  **BOM:** False  |  **Line ending:** LF
- **Delimiter:** ','  |  **Trailing empty rows:** 0
- **Sample rows analyzed:** 3882

**Headers (11):** `المنطقة` | `المدينة` | `المدينة / الحي` | `الرقم المرجعي للصفقة` | `تاريخ الصفقة ميلادي` | `تاريخ الصفقة هجري` | `تصنيف العقار` | `نوع العقار` | `عدد العقارات` | `السعر` | `المساحة`

**Column analysis:**

| Column | Type | Null% | Notes |
|--------|------|-------|-------|
| `المنطقة` | text | 0.0% |  |
| `المدينة` | text | 0.0% |  |
| `المدينة / الحي` | text | 0.0% |  |
| `الرقم المرجعي للصفقة` | numeric | 0.0% |  |
| `تاريخ الصفقة ميلادي` | date | 0.0% | Date format: YYYY/MM/DD |
| `تاريخ الصفقة هجري` | date | 0.0% | Date format: YYYY/MM/DD |
| `تصنيف العقار` | text | 0.0% |  |
| `نوع العقار` | text | 0.0% |  |
| `عدد العقارات` | numeric | 0.0% |  |
| `السعر` | numeric | 0.0% |  |
| `المساحة` | numeric | 0.0% |  |

##### `MOJ-Sales-2023-Q3.csv`

- **Size:** 6.6 MB  |  **Rows:** 48,545  |  **Cols:** 11
- **Encoding:** utf-8  |  **BOM:** False  |  **Line ending:** LF
- **Delimiter:** ','  |  **Trailing empty rows:** 0
- **Sample rows analyzed:** 4855

**Headers (11):** `المنطقة` | `المدينة` | `المدينة / الحي` | `الرقم المرجعي للصفقة` | `تاريخ الصفقة ميلادي` | `تاريخ الصفقة هجري` | `تصنيف العقار` | `نوع العقار` | `عدد العقارات` | `السعر` | `المساحة`

**Column analysis:**

| Column | Type | Null% | Notes |
|--------|------|-------|-------|
| `المنطقة` | text | 0.0% |  |
| `المدينة` | text | 0.0% |  |
| `المدينة / الحي` | text | 0.0% |  |
| `الرقم المرجعي للصفقة` | numeric | 0.0% |  |
| `تاريخ الصفقة ميلادي` | date | 0.0% | Date format: YYYY/MM/DD |
| `تاريخ الصفقة هجري` | date | 0.0% | Date format: YYYY/MM/DD |
| `تصنيف العقار` | text | 0.0% |  |
| `نوع العقار` | text | 0.0% |  |
| `عدد العقارات` | numeric | 0.0% |  |
| `السعر` | numeric | 0.0% |  |
| `المساحة` | numeric | 0.0% |  |

##### `MOJ-Sales-2023-Q4.csv`

- **Size:** 6.5 MB  |  **Rows:** 52,342  |  **Cols:** 10
- **Encoding:** utf-8-sig  |  **BOM:** True  |  **Line ending:** CRLF
- **Delimiter:** ','  |  **Trailing empty rows:** 0
- **Sample rows analyzed:** 5235

**Headers (10):** `المنطقة` | `المدينة` | `المدينة / الحي` | `الرقم المرجعي للصفقة` | `تاريخ الصفقة ميلادي` | `تاريخ الصفقة هجري` | `تصنيف العقار` | `عدد العقارات` | `السعر` | `المساحة`

**Column analysis:**

| Column | Type | Null% | Notes |
|--------|------|-------|-------|
| `المنطقة` | text | 0.0% |  |
| `المدينة` | text | 0.0% |  |
| `المدينة / الحي` | text | 0.0% |  |
| `الرقم المرجعي للصفقة` | numeric | 0.0% |  |
| `تاريخ الصفقة ميلادي` | date | 0.0% | Date format: YYYY/MM/DD |
| `تاريخ الصفقة هجري` | date | 0.0% | Date format: YYYY/MM/DD |
| `تصنيف العقار` | text | 0.0% |  |
| `عدد العقارات` | numeric | 0.0% |  |
| `السعر` | numeric (comma-sep thousands) | 0.0% | Comma thousands separators present |
| `المساحة` | numeric | 0.0% | MIXED types: {'numeric': 4763, 'numeric_comma': 472}; Comma thousands separators present |

##### `MOJ-Sales-2024-Q1.csv`

- **Size:** 7.4 MB  |  **Rows:** 59,099  |  **Cols:** 10
- **Encoding:** utf-8-sig  |  **BOM:** True  |  **Line ending:** CRLF
- **Delimiter:** ','  |  **Trailing empty rows:** 0
- **Sample rows analyzed:** 5373

**Headers (10):** `المنطقة` | `المدينة` | `المدينة / الحي` | `الرقم المرجعي للصفقة` | `تاريخ الصفقة ميلادي` | `تاريخ الصفقة هجري` | `تصنيف العقار` | `عدد العقارات` | `السعر` | `المساحة`

**Column analysis:**

| Column | Type | Null% | Notes |
|--------|------|-------|-------|
| `المنطقة` | text | 0.0% |  |
| `المدينة` | text | 0.0% |  |
| `المدينة / الحي` | text | 0.0% |  |
| `الرقم المرجعي للصفقة` | numeric | 0.0% |  |
| `تاريخ الصفقة ميلادي` | date | 0.0% | Date format: YYYY/MM/DD |
| `تاريخ الصفقة هجري` | date | 0.0% | Date format: YYYY/MM/DD |
| `تصنيف العقار` | text | 0.0% |  |
| `عدد العقارات` | numeric | 0.0% |  |
| `السعر` | numeric (comma-sep thousands) | 0.0% | Comma thousands separators present |
| `المساحة` | numeric | 0.0% | MIXED types: {'numeric': 4818, 'numeric_comma': 555}; Comma thousands separators present |

##### `MOJ-Sales-2024-Q2.csv`

- **Size:** 6.0 MB  |  **Rows:** 48,272  |  **Cols:** 10
- **Encoding:** utf-8-sig  |  **BOM:** True  |  **Line ending:** CRLF
- **Delimiter:** ','  |  **Trailing empty rows:** 0
- **Sample rows analyzed:** 4828

**Headers (10):** `المنطقة` | `المدينة` | `المدينة / الحي` | `الرقم المرجعي للصفقة` | `تاريخ الصفقة ميلادي` | `تاريخ الصفقة هجري` | `تصنيف العقار` | `عدد العقارات` | `السعر` | `المساحة`

**Column analysis:**

| Column | Type | Null% | Notes |
|--------|------|-------|-------|
| `المنطقة` | text | 0.0% |  |
| `المدينة` | text | 0.0% |  |
| `المدينة / الحي` | text | 0.0% |  |
| `الرقم المرجعي للصفقة` | numeric | 0.0% |  |
| `تاريخ الصفقة ميلادي` | date | 0.0% | Date format: YYYY/MM/DD |
| `تاريخ الصفقة هجري` | date | 0.0% | Date format: YYYY/MM/DD |
| `تصنيف العقار` | text | 0.0% |  |
| `عدد العقارات` | numeric | 0.0% |  |
| `السعر` | numeric (comma-sep thousands) | 0.0% | Comma thousands separators present |
| `المساحة` | numeric | 0.0% | MIXED types: {'numeric': 4351, 'numeric_comma': 477}; Comma thousands separators present |

##### `MOJ-Sales-2024-Q3.csv`

- **Size:** 8.6 MB  |  **Rows:** 69,021  |  **Cols:** 10
- **Encoding:** utf-8-sig  |  **BOM:** True  |  **Line ending:** CRLF
- **Delimiter:** ','  |  **Trailing empty rows:** 0
- **Sample rows analyzed:** 5310

**Headers (10):** `المنطقة` | `المدينة` | `المدينة / الحي` | `الرقم المرجعي للصفقة` | `تاريخ الصفقة ميلادي` | `تاريخ الصفقة هجري` | `تصنيف العقار` | `عدد العقارات` | `السعر` | `المساحة`

**Column analysis:**

| Column | Type | Null% | Notes |
|--------|------|-------|-------|
| `المنطقة` | text | 0.0% |  |
| `المدينة` | text | 0.0% |  |
| `المدينة / الحي` | text | 0.0% |  |
| `الرقم المرجعي للصفقة` | numeric | 0.0% |  |
| `تاريخ الصفقة ميلادي` | date | 0.0% | Date format: YYYY/MM/DD |
| `تاريخ الصفقة هجري` | date | 0.0% | Date format: YYYY/MM/DD |
| `تصنيف العقار` | text | 0.0% |  |
| `عدد العقارات` | numeric | 0.0% |  |
| `السعر` | numeric (comma-sep thousands) | 0.0% | Comma thousands separators present |
| `المساحة` | numeric | 0.0% | MIXED types: {'numeric_comma': 531, 'numeric': 4779}; Comma thousands separators present |

##### `MOJ-Sales-2024-Q4.csv`

- **Size:** 9.1 MB  |  **Rows:** 72,939  |  **Cols:** 10
- **Encoding:** utf-8-sig  |  **BOM:** True  |  **Line ending:** CRLF
- **Delimiter:** ','  |  **Trailing empty rows:** 0
- **Sample rows analyzed:** 5210

**Headers (10):** `المنطقة` | `المدينة` | `المدينة / الحي` | `الرقم المرجعي للصفقة` | `تاريخ الصفقة ميلادي` | `تاريخ الصفقة هجري` | `تصنيف العقار` | `عدد العقارات` | `السعر` | `المساحة`

**Column analysis:**

| Column | Type | Null% | Notes |
|--------|------|-------|-------|
| `المنطقة` | text | 0.0% |  |
| `المدينة` | text | 0.0% |  |
| `المدينة / الحي` | text | 0.0% |  |
| `الرقم المرجعي للصفقة` | numeric | 0.0% |  |
| `تاريخ الصفقة ميلادي` | date | 0.0% | Date format: YYYY/MM/DD |
| `تاريخ الصفقة هجري` | date | 0.0% | Date format: YYYY/MM/DD |
| `تصنيف العقار` | text | 0.0% |  |
| `عدد العقارات` | numeric | 0.0% |  |
| `السعر` | numeric (comma-sep thousands) | 0.0% | Comma thousands separators present |
| `المساحة` | numeric | 0.0% | MIXED types: {'numeric': 4737, 'numeric_comma': 473}; Comma thousands separators present |

##### `MOJ-Sales-2025-Q1.csv`

- **Size:** 8.2 MB  |  **Rows:** 65,729  |  **Cols:** 10
- **Encoding:** utf-8-sig  |  **BOM:** True  |  **Line ending:** CRLF
- **Delimiter:** ','  |  **Trailing empty rows:** 0
- **Sample rows analyzed:** 5057

**Headers (10):** `المنطقة` | `المدينة` | `المدينة / الحي` | `الرقم المرجعي للصفقة` | `تاريخ الصفقة ميلادي` | `تاريخ الصفقة هجري` | `تصنيف العقار` | `عدد العقارات` | `السعر` | `المساحة`

**Column analysis:**

| Column | Type | Null% | Notes |
|--------|------|-------|-------|
| `المنطقة` | text | 0.0% |  |
| `المدينة` | text | 0.0% |  |
| `المدينة / الحي` | text | 0.0% |  |
| `الرقم المرجعي للصفقة` | numeric | 0.0% |  |
| `تاريخ الصفقة ميلادي` | date | 0.0% | Date format: YYYY/MM/DD |
| `تاريخ الصفقة هجري` | date | 0.0% | Date format: YYYY/MM/DD |
| `تصنيف العقار` | text | 0.0% |  |
| `عدد العقارات` | numeric | 0.0% |  |
| `السعر` | numeric (comma-sep thousands) | 0.0% | Comma thousands separators present |
| `المساحة` | numeric | 0.0% | MIXED types: {'numeric': 4582, 'numeric_comma': 474}; Comma thousands separators present |

##### `MOJ-Sales-2025-Q2.csv`

- **Size:** 5.4 MB  |  **Rows:** 42,518  |  **Cols:** 10
- **Encoding:** utf-8-sig  |  **BOM:** True  |  **Line ending:** CRLF
- **Delimiter:** ','  |  **Trailing empty rows:** 0
- **Sample rows analyzed:** 4252

**Headers (10):** `المنطقة` | `المدينة` | `المدينة / الحي` | `الرقم المرجعي للصفقة` | `تاريخ الصفقة ميلادي` | `تاريخ الصفقة هجري` | `تصنيف العقار` | `عدد العقارات` | `السعر` | `المساحة`

**Column analysis:**

| Column | Type | Null% | Notes |
|--------|------|-------|-------|
| `المنطقة` | text | 0.0% |  |
| `المدينة` | text | 0.0% |  |
| `المدينة / الحي` | text | 0.0% |  |
| `الرقم المرجعي للصفقة` | numeric | 0.0% |  |
| `تاريخ الصفقة ميلادي` | date | 0.0% | Date format: YYYY/MM/DD |
| `تاريخ الصفقة هجري` | date | 0.0% | Date format: YYYY/MM/DD |
| `تصنيف العقار` | text | 0.0% |  |
| `عدد العقارات` | numeric | 0.0% |  |
| `السعر` | numeric (comma-sep thousands) | 0.0% | Comma thousands separators present |
| `المساحة` | numeric | 0.0% | MIXED types: {'numeric': 3886, 'numeric_comma': 366}; Comma thousands separators present |

##### `MOJ-Sales-2025-Q3.csv`

- **Size:** 6.2 MB  |  **Rows:** 48,820  |  **Cols:** 10
- **Encoding:** utf-8-sig  |  **BOM:** True  |  **Line ending:** CRLF
- **Delimiter:** ','  |  **Trailing empty rows:** 0
- **Sample rows analyzed:** 4882

**Headers (10):** `المنطقة` | `المدينة` | `المدينة / الحي` | `الرقم المرجعي للصفقة` | `تاريخ الصفقة ميلادي` | `تاريخ الصفقة هجري` | `تصنيف العقار` | `عدد العقارات` | `السعر` | `المساحة`

**Column analysis:**

| Column | Type | Null% | Notes |
|--------|------|-------|-------|
| `المنطقة` | text | 0.0% |  |
| `المدينة` | text | 0.0% |  |
| `المدينة / الحي` | text | 0.0% |  |
| `الرقم المرجعي للصفقة` | numeric | 0.0% |  |
| `تاريخ الصفقة ميلادي` | date | 0.0% | Date format: YYYY/MM/DD |
| `تاريخ الصفقة هجري` | date | 0.0% | Date format: YYYY/MM/DD |
| `تصنيف العقار` | text | 0.0% |  |
| `عدد العقارات` | numeric | 0.0% |  |
| `السعر` | numeric (comma-sep thousands) | 0.0% | Comma thousands separators present |
| `المساحة` | numeric | 0.0% | MIXED types: {'numeric': 4472, 'numeric_comma': 410}; Comma thousands separators present |

##### `MOJ-Sales-2025-Q4.csv`

- **Size:** 5.7 MB  |  **Rows:** 44,490  |  **Cols:** 10
- **Encoding:** utf-8-sig  |  **BOM:** True  |  **Line ending:** CRLF
- **Delimiter:** ','  |  **Trailing empty rows:** 0
- **Sample rows analyzed:** 4449

**Headers (10):** `المنطقة` | `المدينة` | `المدينة / الحي` | `الرقم المرجعي للصفقة` | `تاريخ الصفقة ميلادي` | `تاريخ الصفقة هجري` | `تصنيف العقار` | `عدد العقارات` | `السعر` | `المساحة`

**Column analysis:**

| Column | Type | Null% | Notes |
|--------|------|-------|-------|
| `المنطقة` | text | 0.0% |  |
| `المدينة` | text | 0.0% |  |
| `المدينة / الحي` | text | 0.0% |  |
| `الرقم المرجعي للصفقة` | numeric | 0.0% |  |
| `تاريخ الصفقة ميلادي` | date | 0.0% | Date format: YYYY/MM/DD |
| `تاريخ الصفقة هجري` | date | 0.0% | Date format: YYYY/MM/DD |
| `تصنيف العقار` | text | 0.0% |  |
| `عدد العقارات` | numeric | 0.0% |  |
| `السعر` | numeric (comma-sep thousands) | 0.0% | Comma thousands separators present |
| `المساحة` | numeric | 0.0% | MIXED types: {'numeric': 4053, 'numeric_comma': 396}; Comma thousands separators present |

### MOJ Seizure (3 files)


##### `MOJ-Seizure-2025-Q1.csv`

- **Size:** 28.7 MB  |  **Rows:** 292,680  |  **Cols:** 6
- **Encoding:** utf-8-sig  |  **BOM:** True  |  **Line ending:** CRLF
- **Delimiter:** ','  |  **Trailing empty rows:** 0
- **Sample rows analyzed:** 5047

**Headers (6):** `المنطقة` | `المدينة` | `نوع القطاع` | `نوع الخدمة` | `التاريخ ميلادي` | `الرقم المرجعي`

**Column analysis:**

| Column | Type | Null% | Notes |
|--------|------|-------|-------|
| `المنطقة` | text | 0.0% |  |
| `المدينة` | text | 0.0% |  |
| `نوع القطاع` | text | 0.0% |  |
| `نوع الخدمة` | text | 0.0% |  |
| `التاريخ ميلادي` | date | 0.0% | Date format: DD/MM/YYYY or M/D/YYYY |
| `الرقم المرجعي` | numeric (comma-sep thousands) | 0.0% | Comma thousands separators present |

##### `MOJ-Seizure-2025-Q2.csv`

- **Size:** 23.9 MB  |  **Rows:** 240,656  |  **Cols:** 6
- **Encoding:** utf-8-sig  |  **BOM:** True  |  **Line ending:** CRLF
- **Delimiter:** ','  |  **Trailing empty rows:** 0
- **Sample rows analyzed:** 5014

**Headers (6):** `المنطقة` | `المدينة` | `نوع القطاع` | `نوع الخدمة` | `التاريخ ميلادي` | `الرقم المرجعي`

**Column analysis:**

| Column | Type | Null% | Notes |
|--------|------|-------|-------|
| `المنطقة` | text | 0.0% |  |
| `المدينة` | text | 0.0% |  |
| `نوع القطاع` | text | 0.0% |  |
| `نوع الخدمة` | text | 0.0% |  |
| `التاريخ ميلادي` | date | 0.0% | Date format: YYYY/MM/DD |
| `الرقم المرجعي` | numeric (comma-sep thousands) | 0.0% | Comma thousands separators present |

##### `MOJ-Seizure-2025-Q3.csv`

- **Size:** 21.3 MB  |  **Rows:** 377,520  |  **Cols:** 6
- **Encoding:** utf-8-sig  |  **BOM:** True  |  **Line ending:** CRLF
- **Delimiter:** ','  |  **Trailing empty rows:** 0
- **Sample rows analyzed:** 5034

**Headers (6):** `المنطقة` | `المدينة` | `نوع القطاع` | `نوع الخدمة` | `التاريخ ميلادي` | `الرقم المرجعي`

**Column analysis:**

| Column | Type | Null% | Notes |
|--------|------|-------|-------|
| `المنطقة` | text | 46.1% |  |
| `المدينة` | text | 46.1% |  |
| `نوع القطاع` | text | 46.1% |  |
| `نوع الخدمة` | text | 46.1% |  |
| `التاريخ ميلادي` | date | 46.1% | Date format: YYYY/MM/DD |
| `الرقم المرجعي` | numeric (comma-sep thousands) | 46.1% | Comma thousands separators present |

### MOJ Transfers (3 files)


##### `MOJ-Transfers-2025-Q1.csv`

- **Size:** 24.8 MB  |  **Rows:** 219,591  |  **Cols:** 6
- **Encoding:** utf-8-sig  |  **BOM:** True  |  **Line ending:** CRLF
- **Delimiter:** ','  |  **Trailing empty rows:** 0
- **Sample rows analyzed:** 5107

**Headers (6):** `المنطقة` | `المدينة` | `نوع القطاع` | `نوع الخدمة` | `التاريخ ميلادي` | `الرقم المرجعي`

**Column analysis:**

| Column | Type | Null% | Notes |
|--------|------|-------|-------|
| `المنطقة` | text | 0.0% |  |
| `المدينة` | text | 0.0% |  |
| `نوع القطاع` | text | 0.0% |  |
| `نوع الخدمة` | text | 0.0% |  |
| `التاريخ ميلادي` | date | 0.0% | Date format: YYYY/MM/DD |
| `الرقم المرجعي` | numeric (comma-sep thousands) | 0.0% | Comma thousands separators present |

##### `MOJ-Transfers-2025-Q2.csv`

- **Size:** 90.9 KB  |  **Rows:** 813  |  **Cols:** 6
- **Encoding:** utf-8-sig  |  **BOM:** True  |  **Line ending:** CRLF
- **Delimiter:** ','  |  **Trailing empty rows:** 0
- **Sample rows analyzed:** 82

**Headers (6):** `المنطقة` | `المدينة` | `نوع القطاع` | `نوع الخدمة` | `التاريخ ميلادي` | `الرقم المرجعي`

**Column analysis:**

| Column | Type | Null% | Notes |
|--------|------|-------|-------|
| `المنطقة` | text | 0.0% |  |
| `المدينة` | text | 0.0% |  |
| `نوع القطاع` | text | 0.0% |  |
| `نوع الخدمة` | text | 0.0% |  |
| `التاريخ ميلادي` | date | 0.0% | Date format: DD/MM/YYYY or M/D/YYYY |
| `الرقم المرجعي` | numeric (comma-sep thousands) | 0.0% | Comma thousands separators present |

##### `MOJ-Transfers-2025-Q3.csv`

- **Size:** 93.5 KB  |  **Rows:** 825  |  **Cols:** 6
- **Encoding:** utf-8-sig  |  **BOM:** True  |  **Line ending:** CRLF
- **Delimiter:** ','  |  **Trailing empty rows:** 0
- **Sample rows analyzed:** 83

**Headers (6):** `المنطقة` | `المدينة` | `نوع القطاع` | `نوع الخدمة` | `التاريخ ميلادي` | `الرقم المرجعي`

**Column analysis:**

| Column | Type | Null% | Notes |
|--------|------|-------|-------|
| `المنطقة` | text | 0.0% |  |
| `المدينة` | text | 0.0% |  |
| `نوع القطاع` | text | 0.0% |  |
| `نوع الخدمة` | text | 0.0% |  |
| `التاريخ ميلادي` | date | 0.0% | Date format: YYYY/MM/DD |
| `الرقم المرجعي` | numeric (comma-sep thousands) | 0.0% | Comma thousands separators present |

### MOJ Update Deed (3 files)


##### `MOJ-Update-Deed-2025-Q1.csv`

- **Size:** 1.1 MB  |  **Rows:** 9,828  |  **Cols:** 6
- **Encoding:** utf-8-sig  |  **BOM:** True  |  **Line ending:** CRLF
- **Delimiter:** ','  |  **Trailing empty rows:** 0
- **Sample rows analyzed:** 983

**Headers (6):** `المنطقة` | `المدينة` | `نوع القطاع` | `نوع الخدمة` | `التاريخ ميلادي` | `الرقم المرجعي`

**Column analysis:**

| Column | Type | Null% | Notes |
|--------|------|-------|-------|
| `المنطقة` | text | 0.0% |  |
| `المدينة` | text | 0.0% |  |
| `نوع القطاع` | text | 0.0% |  |
| `نوع الخدمة` | text | 0.0% |  |
| `التاريخ ميلادي` | date | 0.0% | Date format: YYYY/MM/DD |
| `الرقم المرجعي` | numeric (comma-sep thousands) | 0.0% | Comma thousands separators present |

##### `MOJ-Update-Deed-2025-Q2.csv`

- **Size:** 803.7 KB  |  **Rows:** 6,839  |  **Cols:** 6
- **Encoding:** utf-8-sig  |  **BOM:** True  |  **Line ending:** CRLF
- **Delimiter:** ','  |  **Trailing empty rows:** 0
- **Sample rows analyzed:** 684

**Headers (6):** `المنطقة` | `المدينة` | `نوع القطاع` | `نوع الخدمة` | `التاريخ ميلادي` | `الرقم المرجعي`

**Column analysis:**

| Column | Type | Null% | Notes |
|--------|------|-------|-------|
| `المنطقة` | text | 0.0% |  |
| `المدينة` | text | 0.0% |  |
| `نوع القطاع` | text | 0.0% |  |
| `نوع الخدمة` | text | 0.0% |  |
| `التاريخ ميلادي` | date | 0.0% | Date format: YYYY/MM/DD |
| `الرقم المرجعي` | numeric (comma-sep thousands) | 0.0% | Comma thousands separators present |

##### `MOJ-Update-Deed-2025-Q3.csv`

- **Size:** 1.3 MB  |  **Rows:** 11,241  |  **Cols:** 6
- **Encoding:** utf-8-sig  |  **BOM:** True  |  **Line ending:** CRLF
- **Delimiter:** ','  |  **Trailing empty rows:** 0
- **Sample rows analyzed:** 1125

**Headers (6):** `المنطقة` | `المدينة` | `نوع القطاع` | `نوع الخدمة` | `التاريخ ميلادي` | `الرقم المرجعي`

**Column analysis:**

| Column | Type | Null% | Notes |
|--------|------|-------|-------|
| `المنطقة` | text | 0.0% |  |
| `المدينة` | text | 0.0% |  |
| `نوع القطاع` | text | 0.0% |  |
| `نوع الخدمة` | text | 0.0% |  |
| `التاريخ ميلادي` | date | 0.0% | Date format: YYYY/MM/DD |
| `الرقم المرجعي` | numeric (comma-sep thousands) | 0.0% | Comma thousands separators present |

### MOJ Update Old Deed (3 files)


##### `MOJ-Update-Old-Deed-2025-Q1.csv`

- **Size:** 40.4 KB  |  **Rows:** 331  |  **Cols:** 6
- **Encoding:** utf-8-sig  |  **BOM:** True  |  **Line ending:** CRLF
- **Delimiter:** ','  |  **Trailing empty rows:** 0
- **Sample rows analyzed:** 56

**Headers (6):** `المنطقة` | `المدينة` | `نوع القطاع` | `نوع الخدمة` | `التاريخ ميلادي` | `الرقم المرجعي`

**Column analysis:**

| Column | Type | Null% | Notes |
|--------|------|-------|-------|
| `المنطقة` | text | 0.0% |  |
| `المدينة` | text | 0.0% |  |
| `نوع القطاع` | text | 0.0% |  |
| `نوع الخدمة` | text | 0.0% |  |
| `التاريخ ميلادي` | date | 0.0% | Date format: YYYY/MM/DD |
| `الرقم المرجعي` | numeric (comma-sep thousands) | 0.0% | Comma thousands separators present |

##### `MOJ-Update-Old-Deed-2025-Q2.csv`

- **Size:** 61.2 KB  |  **Rows:** 502  |  **Cols:** 6
- **Encoding:** utf-8-sig  |  **BOM:** True  |  **Line ending:** CRLF
- **Delimiter:** ','  |  **Trailing empty rows:** 0
- **Sample rows analyzed:** 51

**Headers (6):** `المنطقة` | `المدينة` | `نوع القطاع` | `نوع الخدمة` | `التاريخ ميلادي` | `الرقم المرجعي`

**Column analysis:**

| Column | Type | Null% | Notes |
|--------|------|-------|-------|
| `المنطقة` | text | 0.0% |  |
| `المدينة` | text | 0.0% |  |
| `نوع القطاع` | text | 0.0% |  |
| `نوع الخدمة` | text | 0.0% |  |
| `التاريخ ميلادي` | date | 0.0% | Date format: YYYY/MM/DD |
| `الرقم المرجعي` | numeric (comma-sep thousands) | 0.0% | Comma thousands separators present |

##### `MOJ-Update-Old-Deed-2025-Q3.csv`

- **Size:** 58.8 KB  |  **Rows:** 482  |  **Cols:** 6
- **Encoding:** utf-8-sig  |  **BOM:** True  |  **Line ending:** CRLF
- **Delimiter:** ','  |  **Trailing empty rows:** 0
- **Sample rows analyzed:** 54

**Headers (6):** `المنطقة` | `المدينة` | `نوع القطاع` | `نوع الخدمة` | `التاريخ ميلادي` | `الرقم المرجعي`

**Column analysis:**

| Column | Type | Null% | Notes |
|--------|------|-------|-------|
| `المنطقة` | text | 0.0% |  |
| `المدينة` | text | 0.0% |  |
| `نوع القطاع` | text | 0.0% |  |
| `نوع الخدمة` | text | 0.0% |  |
| `التاريخ ميلادي` | date | 0.0% | Date format: YYYY/MM/DD |
| `الرقم المرجعي` | numeric (comma-sep thousands) | 0.0% | Comma thousands separators present |

### REGA Quarter Report (1 files)


##### `quarter-report-SI.csv`

- **Size:** 3.9 MB  |  **Rows:** 32,730  |  **Cols:** 11
- **Encoding:** utf-8  |  **BOM:** False  |  **Line ending:** LF
- **Delimiter:** ','  |  **Trailing empty rows:** 0
- **Sample rows analyzed:** 3273

**Headers (11):** `yearnumber` | `quarternumber` | `quarternamear` | `quarterid` | `region_ar` | `city_ar` | `district_ar` | `typecategoryar` | `deed_counts` | `RealEstatePrice_SUM` | `Meter_Price_W_Avg_IQR`

**Column analysis:**

| Column | Type | Null% | Notes |
|--------|------|-------|-------|
| `yearnumber` | date | 0.0% | Date format: YYYY |
| `quarternumber` | numeric | 0.0% |  |
| `quarternamear` | text | 0.0% |  |
| `quarterid` | numeric | 0.0% |  |
| `region_ar` | text | 0.9% |  |
| `city_ar` | text | 0.9% |  |
| `district_ar` | text | 28.7% |  |
| `typecategoryar` | text | 0.0% |  |
| `deed_counts` | numeric | 0.0% | Date format: YYYY |
| `RealEstatePrice_SUM` | numeric | 0.0% |  |
| `Meter_Price_W_Avg_IQR` | numeric | 49.1% |  |

### REGA Registered RE by Gender (1 files)


##### `Registered-Real-Estate-by-Gender-2024.csv`

- **Size:** 0.1 KB  |  **Rows:** 2  |  **Cols:** 3
- **Encoding:** ascii  |  **BOM:** False  |  **Line ending:** CRLF
- **Delimiter:** ','  |  **Trailing empty rows:** 0
- **Sample rows analyzed:** 2

**Headers (3):** `Gender ` | `RENs` | `Created Date `

**Column analysis:**

| Column | Type | Null% | Notes |
|--------|------|-------|-------|
| `Gender ` | text | 0.0% |  |
| `RENs` | numeric (comma-sep thousands) | 0.0% | Comma thousands separators present |
| `Created Date ` | text | 50.0% |  |

### REGA Rental Indicators (by City) (13 files)


##### `Rental-indicators-for-Cities-in-Riyadh-region.csv`

- **Size:** 303.8 KB  |  **Rows:** 4,486  |  **Cols:** 7
- **Encoding:** utf-8-sig  |  **BOM:** True  |  **Line ending:** CRLF
- **Delimiter:** ','  |  **Trailing empty rows:** 0
- **Sample rows analyzed:** 449

**Headers (7):** `السنة ` | `الربع` | `المنطقة ` | `المدينة ` | `نوع العقار ` | `مجموع الصفقات` | `المتوسط`

**Column analysis:**

| Column | Type | Null% | Notes |
|--------|------|-------|-------|
| `السنة ` | date | 0.0% | Date format: YYYY |
| `الربع` | numeric | 0.0% |  |
| `المنطقة ` | text | 0.0% |  |
| `المدينة ` | text | 0.0% |  |
| `نوع العقار ` | text | 0.0% |  |
| `مجموع الصفقات` | numeric | 0.0% | Date format: YYYY |
| `المتوسط` | numeric | 0.0% | MIXED types: {'date': 42, 'numeric': 407}; Date format: YYYY |

##### `Rental-indicators-for-cities-Asir-region.csv`

- **Size:** 140.0 KB  |  **Rows:** 2,162  |  **Cols:** 7
- **Encoding:** utf-8-sig  |  **BOM:** True  |  **Line ending:** CRLF
- **Delimiter:** ','  |  **Trailing empty rows:** 0
- **Sample rows analyzed:** 217

**Headers (7):** `السنة` | `الربع` | `المنطقة` | `المدينة` | `نوع العقار` | `مجموع الصفقات` | `المتوسط`

**Column analysis:**

| Column | Type | Null% | Notes |
|--------|------|-------|-------|
| `السنة` | date | 0.0% | Date format: YYYY |
| `الربع` | numeric | 0.0% |  |
| `المنطقة` | text | 0.0% |  |
| `المدينة` | text | 0.0% |  |
| `نوع العقار` | text | 0.0% |  |
| `مجموع الصفقات` | numeric | 0.0% | MIXED types: {'numeric': 203, 'date': 14}; Date format: YYYY |
| `المتوسط` | numeric | 0.0% | MIXED types: {'numeric': 203, 'date': 14}; Date format: YYYY |

##### `Rental-indicators-for-cities-in-Al-Baha-region.csv`

- **Size:** 58.3 KB  |  **Rows:** 890  |  **Cols:** 7
- **Encoding:** utf-8-sig  |  **BOM:** True  |  **Line ending:** CRLF
- **Delimiter:** ','  |  **Trailing empty rows:** 0
- **Sample rows analyzed:** 89

**Headers (7):** `السنة ` | `الربع` | `المنطقة ` | `المدينة ` | `نوع العقار ` | `مجموع الصفقات` | `المتوسط`

**Column analysis:**

| Column | Type | Null% | Notes |
|--------|------|-------|-------|
| `السنة ` | date | 0.0% | Date format: YYYY |
| `الربع` | numeric | 0.0% |  |
| `المنطقة ` | text | 0.0% |  |
| `المدينة ` | text | 0.0% |  |
| `نوع العقار ` | text | 0.0% |  |
| `مجموع الصفقات` | numeric | 0.0% | Date format: YYYY |
| `المتوسط` | numeric | 0.0% | MIXED types: {'numeric': 80, 'date': 9}; Date format: YYYY |

##### `Rental-indicators-for-cities-in-Al-jawf-region.csv`

- **Size:** 46.8 KB  |  **Rows:** 715  |  **Cols:** 7
- **Encoding:** utf-8-sig  |  **BOM:** True  |  **Line ending:** CRLF
- **Delimiter:** ','  |  **Trailing empty rows:** 0
- **Sample rows analyzed:** 72

**Headers (7):** `السنة` | `الربع` | `المنطقة` | `المدينة` | `نوع العقار` | `مجموع الصفقات` | `المتوسط`

**Column analysis:**

| Column | Type | Null% | Notes |
|--------|------|-------|-------|
| `السنة` | date | 0.0% | Date format: YYYY |
| `الربع` | numeric | 0.0% |  |
| `المنطقة` | text | 0.0% |  |
| `المدينة` | text | 0.0% |  |
| `نوع العقار` | text | 0.0% |  |
| `مجموع الصفقات` | numeric | 0.0% | Date format: YYYY |
| `المتوسط` | numeric | 0.0% | MIXED types: {'date': 4, 'numeric': 68}; Date format: YYYY |

##### `Rental-indicators-for-cities-in-Eastern-Province.csv`

- **Size:** 202.3 KB  |  **Rows:** 2,383  |  **Cols:** 7
- **Encoding:** utf-8-sig  |  **BOM:** True  |  **Line ending:** LF
- **Delimiter:** ','  |  **Trailing empty rows:** 0
- **Sample rows analyzed:** 239

**Headers (7):** `year` | `quarter` | `region_ar` | `city_ar` | `Category` | `total_deals` | `average`

**Column analysis:**

| Column | Type | Null% | Notes |
|--------|------|-------|-------|
| `year` | date | 0.0% | Date format: YYYY |
| `quarter` | numeric | 0.0% |  |
| `region_ar` | text | 0.0% |  |
| `city_ar` | text | 0.0% |  |
| `Category` | text | 0.0% |  |
| `total_deals` | numeric | 0.0% | MIXED types: {'numeric': 221, 'date': 18}; Date format: YYYY |
| `average` | numeric | 0.0% | Date format: YYYY |

##### `Rental-indicators-for-cities-in-Hail-region.csv`

- **Size:** 42.6 KB  |  **Rows:** 725  |  **Cols:** 7
- **Encoding:** utf-8-sig  |  **BOM:** True  |  **Line ending:** CRLF
- **Delimiter:** ','  |  **Trailing empty rows:** 0
- **Sample rows analyzed:** 73

**Headers (7):** `السنة` | `الربع` | `المنطقة` | `المدينة` | `نوع العقار` | `مجموع الصفقات` | `المتوسط`

**Column analysis:**

| Column | Type | Null% | Notes |
|--------|------|-------|-------|
| `السنة` | date | 0.0% | Date format: YYYY |
| `الربع` | numeric | 0.0% |  |
| `المنطقة` | text | 0.0% |  |
| `المدينة` | text | 0.0% |  |
| `نوع العقار` | text | 0.0% |  |
| `مجموع الصفقات` | numeric | 0.0% | MIXED types: {'numeric': 69, 'date': 4}; Date format: YYYY |
| `المتوسط` | numeric | 0.0% | MIXED types: {'numeric': 67, 'date': 6}; Date format: YYYY |

##### `Rental-indicators-for-cities-in-Jazan-region.csv`

- **Size:** 85.6 KB  |  **Rows:** 1,251  |  **Cols:** 7
- **Encoding:** utf-8-sig  |  **BOM:** True  |  **Line ending:** CRLF
- **Delimiter:** ','  |  **Trailing empty rows:** 0
- **Sample rows analyzed:** 126

**Headers (7):** `السنة` | `الربع` | `المنطقة` | `المدينة` | `نوع العقار` | `مجموع الصفقات` | `المتوسط`

**Column analysis:**

| Column | Type | Null% | Notes |
|--------|------|-------|-------|
| `السنة` | date | 0.0% | Date format: YYYY |
| `الربع` | numeric | 0.0% |  |
| `المنطقة` | text | 0.0% |  |
| `المدينة` | text | 0.0% |  |
| `نوع العقار` | text | 0.0% |  |
| `مجموع الصفقات` | numeric | 0.0% | MIXED types: {'numeric': 118, 'date': 8}; Date format: YYYY |
| `المتوسط` | numeric | 0.0% | MIXED types: {'numeric': 119, 'date': 7}; Date format: YYYY |

##### `Rental-indicators-for-cities-in-Madinah-region.csv`

- **Size:** 72.8 KB  |  **Rows:** 847  |  **Cols:** 7
- **Encoding:** utf-8-sig  |  **BOM:** True  |  **Line ending:** CRLF
- **Delimiter:** ','  |  **Trailing empty rows:** 0
- **Sample rows analyzed:** 85

**Headers (7):** `year` | `quarter` | `region_ar` | `city_ar` | `Category` | `total_deals` | `average`

**Column analysis:**

| Column | Type | Null% | Notes |
|--------|------|-------|-------|
| `year` | date | 0.0% | Date format: YYYY |
| `quarter` | numeric | 0.0% |  |
| `region_ar` | text | 0.0% |  |
| `city_ar` | text | 0.0% |  |
| `Category` | text | 0.0% |  |
| `total_deals` | numeric | 0.0% | MIXED types: {'numeric': 76, 'date': 9}; Date format: YYYY |
| `average` | numeric | 0.0% | MIXED types: {'numeric': 80, 'date': 5}; Date format: YYYY |

##### `Rental-indicators-for-cities-in-Makkah-region.csv`

- **Size:** 158.0 KB  |  **Rows:** 2,066  |  **Cols:** 7
- **Encoding:** utf-8-sig  |  **BOM:** True  |  **Line ending:** CRLF
- **Delimiter:** ','  |  **Trailing empty rows:** 0
- **Sample rows analyzed:** 207

**Headers (7):** `السنة ` | `الربع` | `المنطقة ` | `المدينة ` | `نوع العقار ` | `مجموع الصفقات` | `المتوسط`

**Column analysis:**

| Column | Type | Null% | Notes |
|--------|------|-------|-------|
| `السنة ` | date | 0.0% | Date format: YYYY |
| `الربع` | numeric | 0.0% |  |
| `المنطقة ` | text | 0.0% |  |
| `المدينة ` | text | 0.0% |  |
| `نوع العقار ` | text | 0.0% |  |
| `مجموع الصفقات` | numeric | 0.0% | MIXED types: {'numeric': 191, 'date': 16}; Date format: YYYY |
| `المتوسط` | numeric | 0.0% | MIXED types: {'numeric': 190, 'date': 17}; Date format: YYYY |

##### `Rental-indicators-for-cities-in-N-B-region.csv`

- **Size:** 62.6 KB  |  **Rows:** 770  |  **Cols:** 7
- **Encoding:** utf-8-sig  |  **BOM:** True  |  **Line ending:** CRLF
- **Delimiter:** ','  |  **Trailing empty rows:** 0
- **Sample rows analyzed:** 77

**Headers (7):** `السنة` | `الربع` | `المنطقة` | `المدينة` | `نوع العقار` | `مجموع الصفقات` | `المتوسط`

**Column analysis:**

| Column | Type | Null% | Notes |
|--------|------|-------|-------|
| `السنة` | date | 0.0% | Date format: YYYY |
| `الربع` | numeric | 0.0% |  |
| `المنطقة` | text | 0.0% |  |
| `المدينة` | text | 0.0% |  |
| `نوع العقار` | text | 0.0% |  |
| `مجموع الصفقات` | numeric | 0.0% | Date format: YYYY |
| `المتوسط` | numeric | 0.0% | MIXED types: {'numeric': 66, 'date': 11}; Date format: YYYY |

##### `Rental-indicators-for-cities-in-Najran-region.csv`

- **Size:** 38.6 KB  |  **Rows:** 613  |  **Cols:** 7
- **Encoding:** utf-8-sig  |  **BOM:** True  |  **Line ending:** CRLF
- **Delimiter:** ','  |  **Trailing empty rows:** 0
- **Sample rows analyzed:** 62

**Headers (7):** `السنة` | `الربع` | `المنطقة` | `المدينة` | `نوع العقار` | `مجموع الصفقات` | `المتوسط`

**Column analysis:**

| Column | Type | Null% | Notes |
|--------|------|-------|-------|
| `السنة` | date | 0.0% | Date format: YYYY |
| `الربع` | numeric | 0.0% |  |
| `المنطقة` | text | 0.0% |  |
| `المدينة` | text | 0.0% |  |
| `نوع العقار` | text | 0.0% |  |
| `مجموع الصفقات` | numeric | 0.0% | Date format: YYYY |
| `المتوسط` | numeric | 0.0% | MIXED types: {'numeric': 57, 'date': 5}; Date format: YYYY |

##### `Rental-indicators-for-cities-in-Qassim-region.csv`

- **Size:** 153.1 KB  |  **Rows:** 2,241  |  **Cols:** 7
- **Encoding:** utf-8-sig  |  **BOM:** True  |  **Line ending:** CRLF
- **Delimiter:** ','  |  **Trailing empty rows:** 0
- **Sample rows analyzed:** 225

**Headers (7):** `السنة` | `الربع` | `المنطقة` | `المدينة` | `نوع العقار` | `مجموع الصفقات` | `المتوسط`

**Column analysis:**

| Column | Type | Null% | Notes |
|--------|------|-------|-------|
| `السنة` | date | 0.0% | Date format: YYYY |
| `الربع` | numeric | 0.0% |  |
| `المنطقة` | text | 0.0% |  |
| `المدينة` | text | 0.0% |  |
| `نوع العقار` | text | 0.0% |  |
| `مجموع الصفقات` | numeric | 0.0% | Date format: YYYY |
| `المتوسط` | numeric | 0.0% | MIXED types: {'numeric': 202, 'date': 23}; Date format: YYYY |

##### `Rental-indicators-for-cities-in-Tabuk-region.csv`

- **Size:** 48.5 KB  |  **Rows:** 805  |  **Cols:** 7
- **Encoding:** utf-8-sig  |  **BOM:** True  |  **Line ending:** CRLF
- **Delimiter:** ','  |  **Trailing empty rows:** 0
- **Sample rows analyzed:** 81

**Headers (7):** `السنة` | `الربع` | `المنطقة` | `المدينة` | `نوع العقار` | `مجموع الصفقات` | `المتوسط`

**Column analysis:**

| Column | Type | Null% | Notes |
|--------|------|-------|-------|
| `السنة` | date | 0.0% | Date format: YYYY |
| `الربع` | numeric | 0.0% |  |
| `المنطقة` | text | 0.0% |  |
| `المدينة` | text | 0.0% |  |
| `نوع العقار` | text | 0.0% |  |
| `مجموع الصفقات` | numeric | 0.0% | Date format: YYYY |
| `المتوسط` | numeric | 0.0% | MIXED types: {'numeric': 72, 'date': 9}; Date format: YYYY |

### REGA Sales Transaction Indicators (31 files)


##### `Sales-transaction-indicators-in-EP-1st-Q-2025.csv`

- **Size:** 213.8 KB  |  **Rows:** 1,696  |  **Cols:** 14
- **Encoding:** utf-8-sig  |  **BOM:** True  |  **Line ending:** CRLF
- **Delimiter:** ','  |  **Trailing empty rows:** 0
- **Sample rows analyzed:** 170

**Headers (14):** `السنة` | `الربع` | `الربع ` | `المنطقة` | `المدينة` | `الحي` | `نوع العقار` | `تصنيف العقار` | `عدد الصكوك ` | `قيمة الصفقات` | `المساحة M2` | `متوسط سعر المتر` | `الحد الأعلى لسعر المتر` | `الحد الأدنى لسعر المتر `

**Column analysis:**

| Column | Type | Null% | Notes |
|--------|------|-------|-------|
| `السنة` | date | 0.0% | Date format: YYYY |
| `الربع` | numeric | 0.0% |  |
| `الربع ` | text | 0.0% |  |
| `المنطقة` | text | 0.0% |  |
| `المدينة` | text | 0.0% |  |
| `الحي` | text | 0.0% |  |
| `نوع العقار` | text | 0.0% |  |
| `تصنيف العقار` | text | 0.0% |  |
| `عدد الصكوك ` | numeric | 0.0% |  |
| `قيمة الصفقات` | numeric | 0.0% | Date format: YYYY |
| `المساحة M2` | numeric | 0.0% | MIXED types: {'numeric': 145, 'date': 25}; Date format: YYYY |
| `متوسط سعر المتر` | numeric | 72.4% |  |
| `الحد الأعلى لسعر المتر` | numeric | 72.4% | MIXED types: {'numeric': 34, 'date': 13}; Date format: YYYY |
| `الحد الأدنى لسعر المتر ` | numeric | 72.4% | Date format: YYYY |

##### `Sales-transaction-indicators-in-EP-2nd-Q-2025.csv`

- **Size:** 208.4 KB  |  **Rows:** 1,634  |  **Cols:** 14
- **Encoding:** utf-8-sig  |  **BOM:** True  |  **Line ending:** CRLF
- **Delimiter:** ','  |  **Trailing empty rows:** 0
- **Sample rows analyzed:** 164

**Headers (14):** `السنة` | `الربع` | `الربع ` | `المنطقة` | `المدينة` | `الحي` | `نوع العقار` | `تصنيف العقار` | `عدد الصكوك ` | `قيمة الصفقات` | `المساحة M2` | `متوسط سعر المتر` | `الحد الأعلى لسعر المتر` | `الحد الأدنى لسعر المتر `

**Column analysis:**

| Column | Type | Null% | Notes |
|--------|------|-------|-------|
| `السنة` | date | 0.0% | Date format: YYYY |
| `الربع` | numeric | 0.0% |  |
| `الربع ` | text | 0.0% |  |
| `المنطقة` | text | 0.0% |  |
| `المدينة` | text | 0.0% |  |
| `الحي` | text | 0.0% |  |
| `نوع العقار` | text | 0.0% |  |
| `تصنيف العقار` | text | 0.0% |  |
| `عدد الصكوك ` | numeric | 0.0% |  |
| `قيمة الصفقات` | numeric | 0.0% | Date format: YYYY |
| `المساحة M2` | numeric | 0.0% | MIXED types: {'numeric': 146, 'date': 18}; Date format: YYYY |
| `متوسط سعر المتر` | numeric | 73.8% | Date format: YYYY |
| `الحد الأعلى لسعر المتر` | numeric | 73.8% | Date format: YYYY |
| `الحد الأدنى لسعر المتر ` | numeric | 73.8% | MIXED types: {'numeric': 34, 'date': 9}; Date format: YYYY |

##### `Sales-transaction-indicators-in-EP-3rd-Q-2025.csv`

- **Size:** 86.4 KB  |  **Rows:** 1,696  |  **Cols:** 14
- **Encoding:** utf-8-sig  |  **BOM:** True  |  **Line ending:** CRLF
- **Delimiter:** ','  |  **Trailing empty rows:** 0
- **Sample rows analyzed:** 170

**Headers (14):** `السنة` | `الربع` | `الربع ` | `المنطقة` | `المدينة` | `الحي` | `نوع العقار` | `تصنيف العقار` | `عدد الصكوك ` | `قيمة الصفقات` | `المساحة M2` | `متوسط سعر المتر` | `الحد الأعلى لسعر المتر` | `الحد الأدنى لسعر المتر `

**Column analysis:**

| Column | Type | Null% | Notes |
|--------|------|-------|-------|
| `السنة` | date | 64.7% | Date format: YYYY |
| `الربع` | numeric | 64.7% |  |
| `الربع ` | text | 64.7% |  |
| `المنطقة` | text | 64.7% |  |
| `المدينة` | text | 64.7% |  |
| `الحي` | text | 64.7% |  |
| `نوع العقار` | text | 64.7% |  |
| `تصنيف العقار` | text | 64.7% |  |
| `عدد الصكوك ` | numeric | 64.7% |  |
| `قيمة الصفقات` | numeric | 64.7% |  |
| `المساحة M2` | numeric | 64.7% | Date format: YYYY |
| `متوسط سعر المتر` | numeric | 92.4% |  |
| `الحد الأعلى لسعر المتر` | numeric | 92.4% | Date format: YYYY |
| `الحد الأدنى لسعر المتر ` | numeric | 92.4% | Date format: YYYY |

##### `Sales-transaction-indicators-in-Hail-1st-Q-2025.csv`

- **Size:** 37.5 KB  |  **Rows:** 333  |  **Cols:** 14
- **Encoding:** utf-8-sig  |  **BOM:** True  |  **Line ending:** CRLF
- **Delimiter:** ','  |  **Trailing empty rows:** 0
- **Sample rows analyzed:** 56

**Headers (14):** `السنة` | `الربع` | `الربع ` | `المنطقة` | `المدينة` | `الحي` | `نوع العقار` | `تصنيف العقار` | `عدد الصكوك ` | `قيمة الصفقات` | `المساحة M2` | `متوسط سعر المتر` | `الحد الأعلى لسعر المتر` | `الحد الأدنى لسعر المتر `

**Column analysis:**

| Column | Type | Null% | Notes |
|--------|------|-------|-------|
| `السنة` | date | 0.0% | Date format: YYYY |
| `الربع` | numeric | 0.0% |  |
| `الربع ` | text | 0.0% |  |
| `المنطقة` | text | 0.0% |  |
| `المدينة` | text | 0.0% |  |
| `الحي` | text | 0.0% |  |
| `نوع العقار` | text | 0.0% |  |
| `تصنيف العقار` | text | 0.0% |  |
| `عدد الصكوك ` | numeric | 0.0% |  |
| `قيمة الصفقات` | numeric | 0.0% |  |
| `المساحة M2` | numeric | 0.0% | MIXED types: {'date': 6, 'numeric': 50}; Date format: YYYY |
| `متوسط سعر المتر` | numeric | 76.8% |  |
| `الحد الأعلى لسعر المتر` | numeric | 76.8% | Date format: YYYY |
| `الحد الأدنى لسعر المتر ` | numeric | 76.8% | Date format: YYYY |

##### `Sales-transaction-indicators-in-Hail-2nd-Q-2025.csv`

- **Size:** 30.7 KB  |  **Rows:** 298  |  **Cols:** 14
- **Encoding:** utf-8-sig  |  **BOM:** True  |  **Line ending:** CRLF
- **Delimiter:** ','  |  **Trailing empty rows:** 0
- **Sample rows analyzed:** 60

**Headers (14):** `السنة` | `الربع` | `الربع ` | `المنطقة` | `المدينة` | `الحي` | `نوع العقار` | `تصنيف العقار` | `عدد الصكوك ` | `قيمة الصفقات` | `المساحة M2` | `متوسط سعر المتر` | `الحد الأعلى لسعر المتر` | `الحد الأدنى لسعر المتر `

**Column analysis:**

| Column | Type | Null% | Notes |
|--------|------|-------|-------|
| `السنة` | date | 0.0% | Date format: YYYY |
| `الربع` | numeric | 0.0% |  |
| `الربع ` | text | 0.0% |  |
| `المنطقة` | text | 0.0% |  |
| `المدينة` | text | 0.0% |  |
| `الحي` | text | 0.0% |  |
| `نوع العقار` | text | 0.0% |  |
| `تصنيف العقار` | text | 0.0% |  |
| `عدد الصكوك ` | numeric | 0.0% |  |
| `قيمة الصفقات` | numeric | 0.0% | Date format: YYYY |
| `المساحة M2` | numeric | 0.0% | MIXED types: {'numeric': 53, 'date': 7}; Date format: YYYY |
| `متوسط سعر المتر` | numeric | 70.0% |  |
| `الحد الأعلى لسعر المتر` | numeric | 70.0% | Date format: YYYY |
| `الحد الأدنى لسعر المتر ` | numeric | 70.0% |  |

##### `Sales-transaction-indicators-in-Hail-3rd-Q-2025.csv`

- **Size:** 11.8 KB  |  **Rows:** 103  |  **Cols:** 14
- **Encoding:** utf-8-sig  |  **BOM:** True  |  **Line ending:** CRLF
- **Delimiter:** ','  |  **Trailing empty rows:** 0
- **Sample rows analyzed:** 52

**Headers (14):** `السنة` | `الربع` | `الربع ` | `المنطقة` | `المدينة` | `الحي` | `نوع العقار` | `تصنيف العقار` | `عدد الصكوك ` | `قيمة الصفقات` | `المساحة M2` | `متوسط سعر المتر` | `الحد الأعلى لسعر المتر` | `الحد الأدنى لسعر المتر `

**Column analysis:**

| Column | Type | Null% | Notes |
|--------|------|-------|-------|
| `السنة` | date | 0.0% | Date format: YYYY |
| `الربع` | numeric | 0.0% |  |
| `الربع ` | text | 0.0% |  |
| `المنطقة` | text | 0.0% |  |
| `المدينة` | text | 0.0% |  |
| `الحي` | text | 0.0% |  |
| `نوع العقار` | text | 0.0% |  |
| `تصنيف العقار` | text | 0.0% |  |
| `عدد الصكوك ` | numeric | 0.0% |  |
| `قيمة الصفقات` | numeric | 0.0% |  |
| `المساحة M2` | numeric | 0.0% | MIXED types: {'numeric': 45, 'date': 7}; Date format: YYYY |
| `متوسط سعر المتر` | numeric | 71.2% |  |
| `الحد الأعلى لسعر المتر` | numeric | 71.2% |  |
| `الحد الأدنى لسعر المتر ` | numeric | 71.2% |  |

##### `Sales-transaction-indicators-in-Madinah-1stQ-2024.csv`

- **Size:** 33.6 KB  |  **Rows:** 201  |  **Cols:** 14
- **Encoding:** utf-8-sig  |  **BOM:** True  |  **Line ending:** CRLF
- **Delimiter:** ','  |  **Trailing empty rows:** 0
- **Sample rows analyzed:** 51

**Headers (14):** `السنة` | `الربع` | `الربع ` | `رقم الربع ` | `المنطقة` | `المدينة` | `الحي` | `نوع العقار` | `عدد الصكوك ` | `مجموع سعر العقار` | `المساحة M2` | `متوسط سعر المتر` | `الحد الأعلى لسعر المتر` | `الحد الأدنى لسعر المتر `

**Column analysis:**

| Column | Type | Null% | Notes |
|--------|------|-------|-------|
| `السنة` | date | 0.0% | Date format: YYYY |
| `الربع` | numeric | 0.0% |  |
| `الربع ` | text | 0.0% |  |
| `رقم الربع ` | numeric | 0.0% |  |
| `المنطقة` | text | 0.0% |  |
| `المدينة` | text | 0.0% |  |
| `الحي` | text | 0.0% |  |
| `نوع العقار` | text | 0.0% |  |
| `عدد الصكوك ` | numeric | 0.0% |  |
| `مجموع سعر العقار` | numeric | 0.0% |  |
| `المساحة M2` | numeric | 0.0% | Date format: YYYY |
| `متوسط سعر المتر` | numeric | 66.7% |  |
| `الحد الأعلى لسعر المتر` | numeric | 66.7% | Date format: YYYY |
| `الحد الأدنى لسعر المتر ` | numeric | 66.7% | Date format: YYYY |

##### `Sales-transaction-indicators-in-Madinah-3rdQ-2024.csv`

- **Size:** 36.2 KB  |  **Rows:** 214  |  **Cols:** 14
- **Encoding:** utf-8-sig  |  **BOM:** True  |  **Line ending:** CRLF
- **Delimiter:** ','  |  **Trailing empty rows:** 0
- **Sample rows analyzed:** 54

**Headers (14):** `السنة` | `الربع` | `الربع ` | `رقم الربع ` | `المنطقة` | `المدينة` | `الحي` | `نوع العقار` | `عدد الصكوك ` | `مجموع سعر العقار` | `المساحة M2` | `متوسط سعر المتر` | `الحد الأعلى لسعر المتر` | `الحد الأدنى لسعر المتر `

**Column analysis:**

| Column | Type | Null% | Notes |
|--------|------|-------|-------|
| `السنة` | date | 0.0% | Date format: YYYY |
| `الربع` | numeric | 0.0% |  |
| `الربع ` | text | 0.0% |  |
| `رقم الربع ` | numeric | 0.0% |  |
| `المنطقة` | text | 0.0% |  |
| `المدينة` | text | 0.0% |  |
| `الحي` | text | 0.0% |  |
| `نوع العقار` | text | 0.0% |  |
| `عدد الصكوك ` | numeric | 0.0% |  |
| `مجموع سعر العقار` | numeric | 0.0% |  |
| `المساحة M2` | numeric | 0.0% | Date format: YYYY |
| `متوسط سعر المتر` | numeric | 53.7% |  |
| `الحد الأعلى لسعر المتر` | numeric | 53.7% | MIXED types: {'numeric': 19, 'date': 6}; Date format: YYYY |
| `الحد الأدنى لسعر المتر ` | numeric | 53.7% | MIXED types: {'numeric': 22, 'date': 3}; Date format: YYYY |

##### `Sales-transaction-indicators-in-Madinah-4th-Q-2024.csv`

- **Size:** 37.1 KB  |  **Rows:** 219  |  **Cols:** 14
- **Encoding:** utf-8-sig  |  **BOM:** True  |  **Line ending:** CRLF
- **Delimiter:** ','  |  **Trailing empty rows:** 0
- **Sample rows analyzed:** 55

**Headers (14):** `السنة` | `الربع` | `الربع ` | `رقم الربع ` | `المنطقة` | `المدينة` | `الحي` | `نوع العقار` | `عدد الصكوك ` | `مجموع سعر العقار` | `المساحة M2` | `متوسط سعر المتر` | `الحد الأعلى لسعر المتر` | `الحد الأدنى لسعر المتر `

**Column analysis:**

| Column | Type | Null% | Notes |
|--------|------|-------|-------|
| `السنة` | date | 0.0% | Date format: YYYY |
| `الربع` | numeric | 0.0% |  |
| `الربع ` | text | 0.0% |  |
| `رقم الربع ` | numeric | 0.0% |  |
| `المنطقة` | text | 0.0% |  |
| `المدينة` | text | 0.0% |  |
| `الحي` | text | 0.0% |  |
| `نوع العقار` | text | 0.0% |  |
| `عدد الصكوك ` | numeric | 0.0% |  |
| `مجموع سعر العقار` | numeric | 0.0% | Date format: YYYY |
| `المساحة M2` | numeric | 0.0% | MIXED types: {'numeric': 52, 'date': 3}; Date format: YYYY |
| `متوسط سعر المتر` | numeric | 56.4% |  |
| `الحد الأعلى لسعر المتر` | numeric | 56.4% | MIXED types: {'numeric': 21, 'date': 3}; Date format: YYYY |
| `الحد الأدنى لسعر المتر ` | numeric | 56.4% | Date format: YYYY |

##### `Sales-transaction-indicators-in-Madinah-Q2-2024.csv`

- **Size:** 32.7 KB  |  **Rows:** 194  |  **Cols:** 14
- **Encoding:** utf-8-sig  |  **BOM:** True  |  **Line ending:** CRLF
- **Delimiter:** ','  |  **Trailing empty rows:** 0
- **Sample rows analyzed:** 65

**Headers (14):** `السنة` | `الربع` | `الربع ` | `رقم الربع ` | `المنطقة` | `المدينة` | `الحي` | `نوع العقار` | `عدد الصكوك ` | `مجموع سعر العقار` | `المساحة M2` | `متوسط سعر المتر` | `الحد الأعلى لسعر المتر` | `الحد الأدنى لسعر المتر `

**Column analysis:**

| Column | Type | Null% | Notes |
|--------|------|-------|-------|
| `السنة` | date | 0.0% | Date format: YYYY |
| `الربع` | numeric | 0.0% |  |
| `الربع ` | text | 0.0% |  |
| `رقم الربع ` | numeric | 0.0% |  |
| `المنطقة` | text | 0.0% |  |
| `المدينة` | text | 0.0% |  |
| `الحي` | text | 0.0% |  |
| `نوع العقار` | text | 0.0% |  |
| `عدد الصكوك ` | numeric | 0.0% |  |
| `مجموع سعر العقار` | numeric | 0.0% |  |
| `المساحة M2` | numeric | 0.0% | MIXED types: {'numeric': 61, 'date': 4}; Date format: YYYY |
| `متوسط سعر المتر` | numeric | 56.9% | Date format: YYYY |
| `الحد الأعلى لسعر المتر` | numeric | 56.9% | MIXED types: {'numeric': 24, 'date': 4}; Date format: YYYY |
| `الحد الأدنى لسعر المتر ` | numeric | 56.9% | MIXED types: {'numeric': 24, 'date': 4}; Date format: YYYY |

##### `Sales-transaction-indicators-in-Makkah-1st-Q-2024.csv`

- **Size:** 61.1 KB  |  **Rows:** 428  |  **Cols:** 14
- **Encoding:** utf-8-sig  |  **BOM:** True  |  **Line ending:** CRLF
- **Delimiter:** ','  |  **Trailing empty rows:** 0
- **Sample rows analyzed:** 54

**Headers (14):** `السنة` | `الربع` | `الربع ` | `رقم الربع ` | `المنطقة` | `المدينة` | `الحي` | `نوع العقار` | `عدد الصكوك ` | `مجموع سعر العقار` | `المساحة M2` | `متوسط سعر المتر` | `الحد الأعلى لسعر المتر` | `الحد الأدنى لسعر المتر `

**Column analysis:**

| Column | Type | Null% | Notes |
|--------|------|-------|-------|
| `السنة` | date | 0.0% | Date format: YYYY |
| `الربع` | numeric | 0.0% |  |
| `الربع ` | text | 0.0% |  |
| `رقم الربع ` | numeric | 0.0% |  |
| `المنطقة` | text | 0.0% |  |
| `المدينة` | text | 0.0% |  |
| `الحي` | text | 0.0% |  |
| `نوع العقار` | text | 0.0% |  |
| `عدد الصكوك ` | numeric | 0.0% |  |
| `مجموع سعر العقار` | numeric | 0.0% |  |
| `المساحة M2` | numeric | 0.0% | Date format: YYYY |
| `متوسط سعر المتر` | numeric | 35.2% |  |
| `الحد الأعلى لسعر المتر` | numeric | 35.2% | MIXED types: {'numeric': 29, 'date': 6}; Date format: YYYY |
| `الحد الأدنى لسعر المتر ` | numeric | 35.2% | MIXED types: {'numeric': 25, 'date': 10}; Date format: YYYY |

##### `Sales-transaction-indicators-in-Makkah-1st-Q-2025.csv`

- **Size:** 250.8 KB  |  **Rows:** 1,919  |  **Cols:** 14
- **Encoding:** utf-8-sig  |  **BOM:** True  |  **Line ending:** CRLF
- **Delimiter:** ','  |  **Trailing empty rows:** 0
- **Sample rows analyzed:** 192

**Headers (14):** `السنة` | `الربع` | `الربع ` | `المنطقة` | `المدينة` | `الحي` | `نوع العقار` | `تصنيف العقار` | `عدد الصكوك ` | `قيمة الصفقات` | `المساحة M2` | `متوسط سعر المتر` | `الحد الأعلى لسعر المتر` | `الحد الأدنى لسعر المتر `

**Column analysis:**

| Column | Type | Null% | Notes |
|--------|------|-------|-------|
| `السنة` | date | 0.0% | Date format: YYYY |
| `الربع` | numeric | 0.0% |  |
| `الربع ` | text | 0.0% |  |
| `المنطقة` | text | 0.0% |  |
| `المدينة` | text | 0.0% |  |
| `الحي` | text | 0.0% |  |
| `نوع العقار` | text | 0.0% |  |
| `تصنيف العقار` | text | 0.0% |  |
| `عدد الصكوك ` | numeric | 0.0% |  |
| `قيمة الصفقات` | numeric | 0.0% |  |
| `المساحة M2` | numeric | 0.0% | MIXED types: {'numeric': 172, 'date': 20}; Date format: YYYY |
| `متوسط سعر المتر` | numeric | 66.1% | Date format: YYYY |
| `الحد الأعلى لسعر المتر` | numeric | 66.1% | MIXED types: {'numeric': 55, 'date': 10}; Date format: YYYY |
| `الحد الأدنى لسعر المتر ` | numeric | 66.1% | Date format: YYYY |

##### `Sales-transaction-indicators-in-Makkah-2nd-Q-2024.csv`

- **Size:** 60.6 KB  |  **Rows:** 418  |  **Cols:** 14
- **Encoding:** utf-8-sig  |  **BOM:** True  |  **Line ending:** CRLF
- **Delimiter:** ','  |  **Trailing empty rows:** 0
- **Sample rows analyzed:** 53

**Headers (14):** `السنة` | `الربع` | `الربع ` | `رقم الربع ` | `المنطقة` | `المدينة` | `الحي` | `نوع العقار` | `عدد الصكوك ` | `مجموع سعر العقار` | `المساحة M2` | `متوسط سعر المتر` | `الحد الأعلى لسعر المتر` | `الحد الأدنى لسعر المتر `

**Column analysis:**

| Column | Type | Null% | Notes |
|--------|------|-------|-------|
| `السنة` | date | 0.0% | Date format: YYYY |
| `الربع` | numeric | 0.0% |  |
| `الربع ` | text | 0.0% |  |
| `رقم الربع ` | numeric | 0.0% |  |
| `المنطقة` | text | 0.0% |  |
| `المدينة` | text | 0.0% |  |
| `الحي` | text | 0.0% |  |
| `نوع العقار` | text | 0.0% |  |
| `عدد الصكوك ` | numeric | 0.0% |  |
| `مجموع سعر العقار` | numeric | 0.0% |  |
| `المساحة M2` | numeric | 0.0% | MIXED types: {'numeric': 50, 'date': 3}; Date format: YYYY |
| `متوسط سعر المتر` | numeric | 37.7% |  |
| `الحد الأعلى لسعر المتر` | numeric | 37.7% | MIXED types: {'numeric': 29, 'date': 4}; Date format: YYYY |
| `الحد الأدنى لسعر المتر ` | numeric | 37.7% | MIXED types: {'numeric': 26, 'date': 7}; Date format: YYYY |

##### `Sales-transaction-indicators-in-Makkah-2nd-Q-2025.csv`

- **Size:** 247.5 KB  |  **Rows:** 1,872  |  **Cols:** 14
- **Encoding:** utf-8-sig  |  **BOM:** True  |  **Line ending:** CRLF
- **Delimiter:** ','  |  **Trailing empty rows:** 0
- **Sample rows analyzed:** 188

**Headers (14):** `السنة` | `الربع` | `الربع ` | `المنطقة` | `المدينة` | `الحي` | `نوع العقار` | `تصنيف العقار` | `عدد الصكوك ` | `قيمة الصفقات` | `المساحة M2` | `متوسط سعر المتر` | `الحد الأعلى لسعر المتر` | `الحد الأدنى لسعر المتر `

**Column analysis:**

| Column | Type | Null% | Notes |
|--------|------|-------|-------|
| `السنة` | date | 0.0% | Date format: YYYY |
| `الربع` | numeric | 0.0% |  |
| `الربع ` | text | 0.0% |  |
| `المنطقة` | text | 0.0% |  |
| `المدينة` | text | 0.0% |  |
| `الحي` | text | 0.0% |  |
| `نوع العقار` | text | 0.0% |  |
| `تصنيف العقار` | text | 0.0% |  |
| `عدد الصكوك ` | numeric | 0.0% |  |
| `قيمة الصفقات` | numeric | 0.0% | Date format: YYYY |
| `المساحة M2` | numeric | 0.0% | MIXED types: {'numeric': 174, 'date': 14}; Date format: YYYY |
| `متوسط سعر المتر` | numeric | 71.3% | Date format: YYYY |
| `الحد الأعلى لسعر المتر` | numeric | 71.3% | MIXED types: {'numeric': 44, 'date': 10}; Date format: YYYY |
| `الحد الأدنى لسعر المتر ` | numeric | 71.3% | MIXED types: {'numeric': 41, 'date': 13}; Date format: YYYY |

##### `Sales-transaction-indicators-in-Makkah-3rd-Q-2024.csv`

- **Size:** 62.9 KB  |  **Rows:** 434  |  **Cols:** 14
- **Encoding:** utf-8-sig  |  **BOM:** True  |  **Line ending:** CRLF
- **Delimiter:** ','  |  **Trailing empty rows:** 0
- **Sample rows analyzed:** 55

**Headers (14):** `السنة` | `الربع` | `الربع ` | `رقم الربع ` | `المنطقة` | `المدينة` | `الحي` | `نوع العقار` | `عدد الصكوك ` | `مجموع سعر العقار` | `المساحة M2` | `متوسط سعر المتر` | `الحد الأعلى لسعر المتر` | `الحد الأدنى لسعر المتر `

**Column analysis:**

| Column | Type | Null% | Notes |
|--------|------|-------|-------|
| `السنة` | date | 0.0% | Date format: YYYY |
| `الربع` | numeric | 0.0% |  |
| `الربع ` | text | 0.0% |  |
| `رقم الربع ` | numeric | 0.0% |  |
| `المنطقة` | text | 0.0% |  |
| `المدينة` | text | 0.0% |  |
| `الحي` | text | 0.0% |  |
| `نوع العقار` | text | 0.0% |  |
| `عدد الصكوك ` | numeric | 0.0% |  |
| `مجموع سعر العقار` | numeric | 0.0% |  |
| `المساحة M2` | numeric | 0.0% | MIXED types: {'numeric': 52, 'date': 3}; Date format: YYYY |
| `متوسط سعر المتر` | numeric | 29.1% |  |
| `الحد الأعلى لسعر المتر` | numeric | 29.1% | MIXED types: {'numeric': 29, 'date': 10}; Date format: YYYY |
| `الحد الأدنى لسعر المتر ` | numeric | 29.1% | MIXED types: {'numeric': 32, 'date': 7}; Date format: YYYY |

##### `Sales-transaction-indicators-in-Makkah-3rd-Q-2025.csv`

- **Size:** 89.7 KB  |  **Rows:** 679  |  **Cols:** 14
- **Encoding:** utf-8-sig  |  **BOM:** True  |  **Line ending:** CRLF
- **Delimiter:** ','  |  **Trailing empty rows:** 0
- **Sample rows analyzed:** 68

**Headers (14):** `السنة` | `الربع` | `الربع ` | `المنطقة` | `المدينة` | `الحي` | `نوع العقار` | `تصنيف العقار` | `عدد الصكوك ` | `قيمة الصفقات` | `المساحة M2` | `متوسط سعر المتر` | `الحد الأعلى لسعر المتر` | `الحد الأدنى لسعر المتر `

**Column analysis:**

| Column | Type | Null% | Notes |
|--------|------|-------|-------|
| `السنة` | date | 0.0% | Date format: YYYY |
| `الربع` | numeric | 0.0% |  |
| `الربع ` | text | 0.0% |  |
| `المنطقة` | text | 0.0% |  |
| `المدينة` | text | 0.0% |  |
| `الحي` | text | 0.0% |  |
| `نوع العقار` | text | 0.0% |  |
| `تصنيف العقار` | text | 0.0% |  |
| `عدد الصكوك ` | numeric | 0.0% |  |
| `قيمة الصفقات` | numeric | 0.0% |  |
| `المساحة M2` | numeric | 0.0% | MIXED types: {'numeric': 64, 'date': 4}; Date format: YYYY |
| `متوسط سعر المتر` | numeric | 73.5% |  |
| `الحد الأعلى لسعر المتر` | numeric | 73.5% |  |
| `الحد الأدنى لسعر المتر ` | numeric | 73.5% |  |

##### `Sales-transaction-indicators-in-Makkah-4th-Q-2024.csv`

- **Size:** 65.5 KB  |  **Rows:** 450  |  **Cols:** 14
- **Encoding:** utf-8-sig  |  **BOM:** True  |  **Line ending:** CRLF
- **Delimiter:** ','  |  **Trailing empty rows:** 0
- **Sample rows analyzed:** 50

**Headers (14):** `السنة` | `الربع` | `الربع ` | `رقم الربع ` | `المنطقة` | `المدينة` | `الحي` | `نوع العقار` | `عدد الصكوك ` | `مجموع سعر العقار` | `المساحة M2` | `متوسط سعر المتر` | `الحد الأعلى لسعر المتر` | `الحد الأدنى لسعر المتر `

**Column analysis:**

| Column | Type | Null% | Notes |
|--------|------|-------|-------|
| `السنة` | date | 0.0% | Date format: YYYY |
| `الربع` | numeric | 0.0% |  |
| `الربع ` | text | 0.0% |  |
| `رقم الربع ` | numeric | 0.0% |  |
| `المنطقة` | text | 0.0% |  |
| `المدينة` | text | 0.0% |  |
| `الحي` | text | 0.0% |  |
| `نوع العقار` | text | 0.0% |  |
| `عدد الصكوك ` | numeric | 0.0% |  |
| `مجموع سعر العقار` | numeric | 0.0% |  |
| `المساحة M2` | numeric | 0.0% | Date format: YYYY |
| `متوسط سعر المتر` | numeric | 24.0% |  |
| `الحد الأعلى لسعر المتر` | numeric | 24.0% | MIXED types: {'numeric': 31, 'date': 7}; Date format: YYYY |
| `الحد الأدنى لسعر المتر ` | numeric | 24.0% | MIXED types: {'numeric': 34, 'date': 4}; Date format: YYYY |

##### `Sales-transaction-indicators-in-Riyadh-1st-Q-2024.csv`

- **Size:** 71.0 KB  |  **Rows:** 522  |  **Cols:** 14
- **Encoding:** utf-8-sig  |  **BOM:** True  |  **Line ending:** CRLF
- **Delimiter:** ','  |  **Trailing empty rows:** 0
- **Sample rows analyzed:** 53

**Headers (14):** `السنة` | `الربع` | `الربع ` | `رقم الربع ` | `المنطقة` | `المدينة` | `الحي` | `نوع العقار` | `عدد الصكوك ` | `مجموع سعر العقار` | `المساحة M2` | `متوسط سعر المتر` | `الحد الأعلى لسعر المتر` | `الحد الأدنى لسعر المتر `

**Column analysis:**

| Column | Type | Null% | Notes |
|--------|------|-------|-------|
| `السنة` | date | 0.0% | Date format: YYYY |
| `الربع` | numeric | 0.0% |  |
| `الربع ` | text | 0.0% |  |
| `رقم الربع ` | numeric | 0.0% |  |
| `المنطقة` | text | 0.0% |  |
| `المدينة` | text | 0.0% |  |
| `الحي` | text | 0.0% |  |
| `نوع العقار` | text | 0.0% |  |
| `عدد الصكوك ` | numeric | 0.0% |  |
| `مجموع سعر العقار` | numeric | 0.0% |  |
| `المساحة M2` | numeric | 0.0% | MIXED types: {'numeric': 46, 'date': 7}; Date format: YYYY |
| `متوسط سعر المتر` | numeric | 39.6% |  |
| `الحد الأعلى لسعر المتر` | numeric | 39.6% | MIXED types: {'numeric': 21, 'date': 11}; Date format: YYYY |
| `الحد الأدنى لسعر المتر ` | numeric | 39.6% | MIXED types: {'numeric': 27, 'date': 5}; Date format: YYYY |

##### `Sales-transaction-indicators-in-Riyadh-2nd-Q-2024.csv`

- **Size:** 68.5 KB  |  **Rows:** 499  |  **Cols:** 14
- **Encoding:** utf-8-sig  |  **BOM:** True  |  **Line ending:** CRLF
- **Delimiter:** ','  |  **Trailing empty rows:** 0
- **Sample rows analyzed:** 56

**Headers (14):** `السنة` | `الربع` | `الربع ` | `رقم الربع ` | `المنطقة` | `المدينة` | `الحي` | `نوع العقار` | `عدد الصكوك ` | `مجموع سعر العقار` | `المساحة M2` | `متوسط سعر المتر` | `الحد الأعلى لسعر المتر` | `الحد الأدنى لسعر المتر `

**Column analysis:**

| Column | Type | Null% | Notes |
|--------|------|-------|-------|
| `السنة` | date | 0.0% | Date format: YYYY |
| `الربع` | numeric | 0.0% |  |
| `الربع ` | text | 0.0% |  |
| `رقم الربع ` | numeric | 0.0% |  |
| `المنطقة` | text | 0.0% |  |
| `المدينة` | text | 0.0% |  |
| `الحي` | text | 0.0% |  |
| `نوع العقار` | text | 0.0% |  |
| `عدد الصكوك ` | numeric | 0.0% |  |
| `مجموع سعر العقار` | numeric | 0.0% |  |
| `المساحة M2` | numeric | 0.0% | MIXED types: {'numeric': 51, 'date': 5}; Date format: YYYY |
| `متوسط سعر المتر` | numeric | 39.3% |  |
| `الحد الأعلى لسعر المتر` | numeric | 39.3% | MIXED types: {'numeric': 25, 'date': 9}; Date format: YYYY |
| `الحد الأدنى لسعر المتر ` | numeric | 39.3% | MIXED types: {'numeric': 23, 'date': 11}; Date format: YYYY |

##### `Sales-transaction-indicators-in-Riyadh-2nd-Q-2025.csv`

- **Size:** 306.6 KB  |  **Rows:** 2,492  |  **Cols:** 14
- **Encoding:** utf-8-sig  |  **BOM:** True  |  **Line ending:** CRLF
- **Delimiter:** ','  |  **Trailing empty rows:** 0
- **Sample rows analyzed:** 250

**Headers (14):** `السنة` | `الربع` | `الربع ` | `المنطقة` | `المدينة` | `الحي` | `نوع العقار` | `تصنيف العقار` | `عدد الصكوك ` | `قيمة الصفقات` | `المساحة M2` | `متوسط سعر المتر` | `الحد الأعلى لسعر المتر` | `الحد الأدنى لسعر المتر `

**Column analysis:**

| Column | Type | Null% | Notes |
|--------|------|-------|-------|
| `السنة` | date | 0.0% | Date format: YYYY |
| `الربع` | numeric | 0.0% |  |
| `الربع ` | text | 0.0% |  |
| `المنطقة` | text | 0.0% |  |
| `المدينة` | text | 0.0% |  |
| `الحي` | text | 0.0% |  |
| `نوع العقار` | text | 0.0% |  |
| `تصنيف العقار` | text | 0.0% |  |
| `عدد الصكوك ` | numeric | 0.0% |  |
| `قيمة الصفقات` | numeric | 0.0% |  |
| `المساحة M2` | numeric | 0.0% | MIXED types: {'numeric': 207, 'date': 43}; Date format: YYYY |
| `متوسط سعر المتر` | numeric | 72.0% | Date format: YYYY |
| `الحد الأعلى لسعر المتر` | numeric | 72.0% | MIXED types: {'numeric': 57, 'date': 13}; Date format: YYYY |
| `الحد الأدنى لسعر المتر ` | numeric | 72.0% | Date format: YYYY |

##### `Sales-transaction-indicators-in-Riyadh-3rd-Q-2025.csv`

- **Size:** 110.0 KB  |  **Rows:** 890  |  **Cols:** 14
- **Encoding:** utf-8-sig  |  **BOM:** True  |  **Line ending:** CRLF
- **Delimiter:** ','  |  **Trailing empty rows:** 0
- **Sample rows analyzed:** 89

**Headers (14):** `السنة` | `الربع` | `الربع ` | `المنطقة` | `المدينة` | `الحي` | `نوع العقار` | `تصنيف العقار` | `عدد الصكوك ` | `قيمة الصفقات` | `المساحة M2` | `متوسط سعر المتر` | `الحد الأعلى لسعر المتر` | `الحد الأدنى لسعر المتر `

**Column analysis:**

| Column | Type | Null% | Notes |
|--------|------|-------|-------|
| `السنة` | date | 0.0% | Date format: YYYY |
| `الربع` | numeric | 0.0% |  |
| `الربع ` | text | 0.0% |  |
| `المنطقة` | text | 0.0% |  |
| `المدينة` | text | 0.0% |  |
| `الحي` | text | 0.0% |  |
| `نوع العقار` | text | 0.0% |  |
| `تصنيف العقار` | text | 0.0% |  |
| `عدد الصكوك ` | numeric | 0.0% |  |
| `قيمة الصفقات` | numeric | 0.0% |  |
| `المساحة M2` | numeric | 0.0% | MIXED types: {'numeric': 74, 'date': 15}; Date format: YYYY |
| `متوسط سعر المتر` | numeric | 73.0% |  |
| `الحد الأعلى لسعر المتر` | numeric | 73.0% | Date format: YYYY |
| `الحد الأدنى لسعر المتر ` | numeric | 73.0% | Date format: YYYY |

##### `Sales-transaction-indicators-in-Riyadh-3rdQ-2024.csv`

- **Size:** 72.2 KB  |  **Rows:** 525  |  **Cols:** 14
- **Encoding:** utf-8-sig  |  **BOM:** True  |  **Line ending:** CRLF
- **Delimiter:** ','  |  **Trailing empty rows:** 0
- **Sample rows analyzed:** 53

**Headers (14):** `السنة` | `الربع` | `الربع ` | `رقم الربع ` | `المنطقة` | `المدينة` | `الحي` | `نوع العقار` | `عدد الصكوك ` | `مجموع سعر العقار` | `المساحة M2` | `متوسط سعر المتر` | `الحد الأعلى لسعر المتر` | `الحد الأدنى لسعر المتر `

**Column analysis:**

| Column | Type | Null% | Notes |
|--------|------|-------|-------|
| `السنة` | date | 0.0% | Date format: YYYY |
| `الربع` | numeric | 0.0% |  |
| `الربع ` | text | 0.0% |  |
| `رقم الربع ` | numeric | 0.0% |  |
| `المنطقة` | text | 0.0% |  |
| `المدينة` | text | 0.0% |  |
| `الحي` | text | 0.0% |  |
| `نوع العقار` | text | 0.0% |  |
| `عدد الصكوك ` | numeric | 0.0% | Date format: YYYY |
| `مجموع سعر العقار` | numeric | 0.0% |  |
| `المساحة M2` | numeric | 0.0% | MIXED types: {'numeric': 49, 'date': 4}; Date format: YYYY |
| `متوسط سعر المتر` | numeric | 34.0% |  |
| `الحد الأعلى لسعر المتر` | numeric | 34.0% | MIXED types: {'numeric': 23, 'date': 12}; Date format: YYYY |
| `الحد الأدنى لسعر المتر ` | numeric | 34.0% | MIXED types: {'numeric': 26, 'date': 9}; Date format: YYYY |

##### `Sales-transaction-indicators-in-Riyadh-4th-Q-2024.csv`

- **Size:** 72.4 KB  |  **Rows:** 525  |  **Cols:** 14
- **Encoding:** utf-8-sig  |  **BOM:** True  |  **Line ending:** CRLF
- **Delimiter:** ','  |  **Trailing empty rows:** 0
- **Sample rows analyzed:** 53

**Headers (14):** `السنة` | `الربع` | `الربع ` | `رقم الربع ` | `المنطقة` | `المدينة` | `الحي` | `نوع العقار` | `عدد الصكوك ` | `مجموع سعر العقار` | `المساحة M2` | `متوسط سعر المتر` | `الحد الأعلى لسعر المتر` | `الحد الأدنى لسعر المتر `

**Column analysis:**

| Column | Type | Null% | Notes |
|--------|------|-------|-------|
| `السنة` | date | 0.0% | Date format: YYYY |
| `الربع` | numeric | 0.0% |  |
| `الربع ` | text | 0.0% |  |
| `رقم الربع ` | numeric | 0.0% |  |
| `المنطقة` | text | 0.0% |  |
| `المدينة` | text | 0.0% |  |
| `الحي` | text | 0.0% |  |
| `نوع العقار` | text | 0.0% |  |
| `عدد الصكوك ` | numeric | 0.0% |  |
| `مجموع سعر العقار` | numeric | 0.0% |  |
| `المساحة M2` | numeric | 0.0% | MIXED types: {'numeric': 49, 'date': 4}; Date format: YYYY |
| `متوسط سعر المتر` | numeric | 37.7% |  |
| `الحد الأعلى لسعر المتر` | numeric | 37.7% | MIXED types: {'numeric': 27, 'date': 6}; Date format: YYYY |
| `الحد الأدنى لسعر المتر ` | numeric | 37.7% | MIXED types: {'numeric': 24, 'date': 9}; Date format: YYYY |

##### `Sales-transaction-indicators-in-Riyadh-Q1-2025.csv`

- **Size:** 355.9 KB  |  **Rows:** 2,903  |  **Cols:** 14
- **Encoding:** utf-8-sig  |  **BOM:** True  |  **Line ending:** CRLF
- **Delimiter:** ','  |  **Trailing empty rows:** 0
- **Sample rows analyzed:** 291

**Headers (14):** `السنة` | `الربع` | `الربع ` | `المنطقة` | `المدينة` | `الحي` | `نوع العقار` | `تصنيف العقار` | `عدد الصكوك ` | `قيمة الصفقات` | `المساحة M2` | `متوسط سعر المتر` | `الحد الأعلى لسعر المتر` | `الحد الأدنى لسعر المتر `

**Column analysis:**

| Column | Type | Null% | Notes |
|--------|------|-------|-------|
| `السنة` | date | 0.0% | Date format: YYYY |
| `الربع` | numeric | 0.0% |  |
| `الربع ` | text | 0.0% |  |
| `المنطقة` | text | 0.0% |  |
| `المدينة` | text | 0.0% |  |
| `الحي` | text | 0.0% |  |
| `نوع العقار` | text | 0.0% |  |
| `تصنيف العقار` | text | 0.0% |  |
| `عدد الصكوك ` | numeric | 0.0% | Date format: YYYY |
| `قيمة الصفقات` | numeric | 0.0% | Date format: YYYY |
| `المساحة M2` | numeric | 0.0% | MIXED types: {'numeric': 252, 'date': 39}; Date format: YYYY |
| `متوسط سعر المتر` | numeric | 63.9% |  |
| `الحد الأعلى لسعر المتر` | numeric | 63.9% | MIXED types: {'numeric': 88, 'date': 17}; Date format: YYYY |
| `الحد الأدنى لسعر المتر ` | numeric | 63.9% | MIXED types: {'numeric': 85, 'date': 20}; Date format: YYYY |

##### `Sales-transaction-indicators-in-albaha-1st-Q-2025.csv`

- **Size:** 6.6 KB  |  **Rows:** 61  |  **Cols:** 14
- **Encoding:** utf-8-sig  |  **BOM:** True  |  **Line ending:** CRLF
- **Delimiter:** ','  |  **Trailing empty rows:** 0
- **Sample rows analyzed:** 61

**Headers (14):** `السنة` | `الربع` | `الربع ` | `المنطقة` | `المدينة` | `الحي` | `نوع العقار` | `تصنيف العقار` | `عدد الصكوك ` | `قيمة الصفقات` | `المساحة M2` | `متوسط سعر المتر` | `الحد الأعلى لسعر المتر` | `الحد الأدنى لسعر المتر `

**Column analysis:**

| Column | Type | Null% | Notes |
|--------|------|-------|-------|
| `السنة` | date | 0.0% | Date format: YYYY |
| `الربع` | numeric | 0.0% |  |
| `الربع ` | text | 0.0% |  |
| `المنطقة` | text | 0.0% |  |
| `المدينة` | text | 0.0% |  |
| `الحي` | text | 0.0% |  |
| `نوع العقار` | text | 0.0% |  |
| `تصنيف العقار` | text | 0.0% |  |
| `عدد الصكوك ` | numeric | 0.0% |  |
| `قيمة الصفقات` | numeric | 0.0% | Date format: YYYY |
| `المساحة M2` | numeric | 0.0% | Date format: YYYY |
| `متوسط سعر المتر` | numeric | 77.0% |  |
| `الحد الأعلى لسعر المتر` | numeric | 77.0% |  |
| `الحد الأدنى لسعر المتر ` | numeric | 77.0% |  |

##### `Sales-transaction-indicators-in-albaha-2nd-Q-2025.csv`

- **Size:** 6.9 KB  |  **Rows:** 63  |  **Cols:** 14
- **Encoding:** utf-8-sig  |  **BOM:** True  |  **Line ending:** CRLF
- **Delimiter:** ','  |  **Trailing empty rows:** 0
- **Sample rows analyzed:** 63

**Headers (14):** `السنة` | `الربع` | `الربع ` | `المنطقة` | `المدينة` | `الحي` | `نوع العقار` | `تصنيف العقار` | `عدد الصكوك ` | `قيمة الصفقات` | `المساحة M2` | `متوسط سعر المتر` | `الحد الأعلى لسعر المتر` | `الحد الأدنى لسعر المتر `

**Column analysis:**

| Column | Type | Null% | Notes |
|--------|------|-------|-------|
| `السنة` | date | 0.0% | Date format: YYYY |
| `الربع` | numeric | 0.0% |  |
| `الربع ` | text | 0.0% |  |
| `المنطقة` | text | 0.0% |  |
| `المدينة` | text | 0.0% |  |
| `الحي` | text | 0.0% |  |
| `نوع العقار` | text | 0.0% |  |
| `تصنيف العقار` | text | 0.0% |  |
| `عدد الصكوك ` | numeric | 0.0% |  |
| `قيمة الصفقات` | numeric | 0.0% |  |
| `المساحة M2` | numeric | 0.0% | MIXED types: {'numeric': 53, 'date': 10}; Date format: YYYY |
| `متوسط سعر المتر` | numeric | 79.4% |  |
| `الحد الأعلى لسعر المتر` | numeric | 79.4% |  |
| `الحد الأدنى لسعر المتر ` | numeric | 79.4% |  |

##### `Sales-transaction-indicators-in-albaha-3rd-Q-2025.csv`

- **Size:** 2.5 KB  |  **Rows:** 21  |  **Cols:** 14
- **Encoding:** utf-8-sig  |  **BOM:** True  |  **Line ending:** CRLF
- **Delimiter:** ','  |  **Trailing empty rows:** 0
- **Sample rows analyzed:** 21

**Headers (14):** `السنة` | `الربع` | `الربع ` | `المنطقة` | `المدينة` | `الحي` | `نوع العقار` | `تصنيف العقار` | `عدد الصكوك ` | `قيمة الصفقات` | `المساحة M2` | `متوسط سعر المتر` | `الحد الأعلى لسعر المتر` | `الحد الأدنى لسعر المتر `

**Column analysis:**

| Column | Type | Null% | Notes |
|--------|------|-------|-------|
| `السنة` | date | 0.0% | Date format: YYYY |
| `الربع` | numeric | 0.0% |  |
| `الربع ` | text | 0.0% |  |
| `المنطقة` | text | 0.0% |  |
| `المدينة` | text | 0.0% |  |
| `الحي` | text | 0.0% |  |
| `نوع العقار` | text | 0.0% |  |
| `تصنيف العقار` | text | 0.0% |  |
| `عدد الصكوك ` | numeric | 0.0% |  |
| `قيمة الصفقات` | numeric | 0.0% |  |
| `المساحة M2` | numeric | 0.0% | MIXED types: {'numeric': 17, 'date': 4}; Date format: YYYY |
| `متوسط سعر المتر` | numeric | 66.7% |  |
| `الحد الأعلى لسعر المتر` | numeric | 66.7% |  |
| `الحد الأدنى لسعر المتر ` | numeric | 66.7% |  |

##### `Sales-transaction-indicators-in-the-EP-2nd-Q-2024.csv`

- **Size:** 23.7 KB  |  **Rows:** 172  |  **Cols:** 14
- **Encoding:** utf-8-sig  |  **BOM:** True  |  **Line ending:** CRLF
- **Delimiter:** ','  |  **Trailing empty rows:** 0
- **Sample rows analyzed:** 58

**Headers (14):** `السنة` | `الربع` | `الربع ` | `رقم الربع ` | `المنطقة` | `المدينة` | `الحي` | `نوع العقار` | `عدد الصكوك ` | `مجموع سعر العقار` | `المساحة M2` | `متوسط سعر المتر` | `الحد الأعلى لسعر المتر` | `الحد الأدنى لسعر المتر `

**Column analysis:**

| Column | Type | Null% | Notes |
|--------|------|-------|-------|
| `السنة` | date | 0.0% | Date format: YYYY |
| `الربع` | numeric | 0.0% |  |
| `الربع ` | text | 0.0% |  |
| `رقم الربع ` | numeric | 0.0% |  |
| `المنطقة` | text | 0.0% |  |
| `المدينة` | text | 0.0% |  |
| `الحي` | text | 0.0% |  |
| `نوع العقار` | text | 0.0% |  |
| `عدد الصكوك ` | numeric | 0.0% |  |
| `مجموع سعر العقار` | numeric | 0.0% |  |
| `المساحة M2` | numeric | 0.0% | MIXED types: {'numeric': 49, 'date': 9}; Date format: YYYY |
| `متوسط سعر المتر` | numeric | 53.4% |  |
| `الحد الأعلى لسعر المتر` | numeric | 53.4% | MIXED types: {'numeric': 22, 'date': 5}; Date format: YYYY |
| `الحد الأدنى لسعر المتر ` | numeric | 53.4% | MIXED types: {'numeric': 21, 'date': 6}; Date format: YYYY |

##### `Sales-transaction-indicators-in-the-EP-3rd-Q-2024.csv`

- **Size:** 23.3 KB  |  **Rows:** 168  |  **Cols:** 14
- **Encoding:** utf-8-sig  |  **BOM:** True  |  **Line ending:** CRLF
- **Delimiter:** ','  |  **Trailing empty rows:** 0
- **Sample rows analyzed:** 56

**Headers (14):** `السنة` | `الربع` | `الربع ` | `رقم الربع ` | `المنطقة` | `المدينة` | `الحي` | `نوع العقار` | `عدد الصكوك ` | `مجموع سعر العقار` | `المساحة M2` | `متوسط سعر المتر` | `الحد الأعلى لسعر المتر` | `الحد الأدنى لسعر المتر `

**Column analysis:**

| Column | Type | Null% | Notes |
|--------|------|-------|-------|
| `السنة` | date | 0.0% | Date format: YYYY |
| `الربع` | numeric | 0.0% |  |
| `الربع ` | text | 0.0% |  |
| `رقم الربع ` | numeric | 0.0% |  |
| `المنطقة` | text | 0.0% |  |
| `المدينة` | text | 0.0% |  |
| `الحي` | text | 0.0% |  |
| `نوع العقار` | text | 0.0% |  |
| `عدد الصكوك ` | numeric | 0.0% |  |
| `مجموع سعر العقار` | numeric | 0.0% |  |
| `المساحة M2` | numeric | 0.0% | MIXED types: {'numeric': 49, 'date': 7}; Date format: YYYY |
| `متوسط سعر المتر` | numeric | 53.6% | MIXED types: {'numeric': 23, 'date': 3}; Date format: YYYY |
| `الحد الأعلى لسعر المتر` | numeric | 53.6% | MIXED types: {'numeric': 21, 'date': 5}; Date format: YYYY |
| `الحد الأدنى لسعر المتر ` | numeric | 53.6% | MIXED types: {'numeric': 18, 'date': 8}; Date format: YYYY |

##### `Sales-transaction-indicators-in-the-EP-4th-Q-2024.csv`

- **Size:** 23.5 KB  |  **Rows:** 170  |  **Cols:** 14
- **Encoding:** utf-8-sig  |  **BOM:** True  |  **Line ending:** CRLF
- **Delimiter:** ','  |  **Trailing empty rows:** 0
- **Sample rows analyzed:** 57

**Headers (14):** `السنة` | `الربع` | `الربع ` | `رقم الربع ` | `المنطقة` | `المدينة` | `الحي` | `نوع العقار` | `عدد الصكوك ` | `مجموع سعر العقار` | `المساحة M2` | `متوسط سعر المتر` | `الحد الأعلى لسعر المتر` | `الحد الأدنى لسعر المتر `

**Column analysis:**

| Column | Type | Null% | Notes |
|--------|------|-------|-------|
| `السنة` | date | 0.0% | Date format: YYYY |
| `الربع` | numeric | 0.0% |  |
| `الربع ` | text | 0.0% |  |
| `رقم الربع ` | numeric | 0.0% |  |
| `المنطقة` | text | 0.0% |  |
| `المدينة` | text | 0.0% |  |
| `الحي` | text | 0.0% |  |
| `نوع العقار` | text | 0.0% |  |
| `عدد الصكوك ` | numeric | 0.0% |  |
| `مجموع سعر العقار` | numeric | 0.0% |  |
| `المساحة M2` | numeric | 0.0% | MIXED types: {'numeric': 50, 'date': 7}; Date format: YYYY |
| `متوسط سعر المتر` | numeric | 47.4% | Date format: YYYY |
| `الحد الأعلى لسعر المتر` | numeric | 47.4% | MIXED types: {'numeric': 18, 'date': 12}; Date format: YYYY |
| `الحد الأدنى لسعر المتر ` | numeric | 47.4% | MIXED types: {'numeric': 22, 'date': 8}; Date format: YYYY |

##### `Sales-transaction-indicators-in-the-EP-Q-2024.csv`

- **Size:** 23.5 KB  |  **Rows:** 172  |  **Cols:** 14
- **Encoding:** utf-8-sig  |  **BOM:** True  |  **Line ending:** CRLF
- **Delimiter:** ','  |  **Trailing empty rows:** 0
- **Sample rows analyzed:** 58

**Headers (14):** `السنة` | `الربع` | `الربع ` | `رقم الربع ` | `المنطقة` | `المدينة` | `الحي` | `نوع العقار` | `عدد الصكوك ` | `مجموع سعر العقار` | `المساحة M2` | `متوسط سعر المتر` | `الحد الأعلى لسعر المتر` | `الحد الأدنى لسعر المتر `

**Column analysis:**

| Column | Type | Null% | Notes |
|--------|------|-------|-------|
| `السنة` | date | 0.0% | Date format: YYYY |
| `الربع` | numeric | 0.0% |  |
| `الربع ` | text | 0.0% |  |
| `رقم الربع ` | numeric | 0.0% |  |
| `المنطقة` | text | 0.0% |  |
| `المدينة` | text | 0.0% |  |
| `الحي` | text | 0.0% |  |
| `نوع العقار` | text | 0.0% |  |
| `عدد الصكوك ` | numeric | 0.0% |  |
| `مجموع سعر العقار` | numeric | 0.0% |  |
| `المساحة M2` | numeric | 0.0% | Date format: YYYY |
| `متوسط سعر المتر` | numeric | 53.4% |  |
| `الحد الأعلى لسعر المتر` | numeric | 53.4% | MIXED types: {'numeric': 20, 'date': 7}; Date format: YYYY |
| `الحد الأدنى لسعر المتر ` | numeric | 53.4% | MIXED types: {'numeric': 18, 'date': 9}; Date format: YYYY |

## 3. Cross-File Consistency Analysis

### 3.1 Encodings

- `utf-8-sig`: 152 files
- `utf-8`: 6 files
- `ascii`: 1 files

### 3.2 Delimiters

- `','`: 159 files

### 3.3 Region Name Values Found (across all files)

- `منطقة تبوك` (57 occurrences)
- `منطقة نجران` (57 occurrences)
- `منطقة حائل` (57 occurrences)
- `منطقة مكة المكرمه` (56 occurrences)
- `منطقة الجوف` (55 occurrences)
- `منطقة الشرقية` (55 occurrences)
- `منطقة الباحة` (54 occurrences)
- `منطقة المدينة المنوره` (54 occurrences)
- `الرياض` (54 occurrences)
- `منطقة الحدود الشمالية` (52 occurrences)
- `منطقة جازان` (42 occurrences)
- `الخدمات الرقمية` (29 occurrences)
- `مكة المكرمه` (28 occurrences)
- `الشرقية` (26 occurrences)
- `عسير` (25 occurrences)
- `القصيم` (24 occurrences)
- `المدينة المنوره` (22 occurrences)
- `تبوك` (20 occurrences)
- `حائل` (19 occurrences)
- `جازان` (17 occurrences)
- `الباحة` (15 occurrences)
- `كتابة العدل الإفتراضية - الرياض` (12 occurrences)
- `الجوف` (10 occurrences)
- `نجران` (10 occurrences)
- `مكة المكرمة` (8 occurrences)
- `منطقة عسير` (7 occurrences)
- `منطقة الرياض` (5 occurrences)
- `المدينة المنورة` (5 occurrences)
- `المنطقة الشرقية` (4 occurrences)
- `منطقة القصيم` (4 occurrences)
- `منطقة مكة المكرمة` (3 occurrences)
- `منطقة المدينة المنورة` (3 occurrences)
- `الحدود الشمالية` (2 occurrences)
- `المنطقة` (1 occurrences)
- `الحدود الشماليه` (1 occurrences)
- `منطقة الحدود الشماليه` (1 occurrences)

### 3.4 City / District Name Values Found (across all files)

- `تبوك` (74 occurrences)
- `جده` (66 occurrences)
- `خميس مشيط` (60 occurrences)
- `حقل` (47 occurrences)
- `الرياض` (47 occurrences)
- `عام` (45 occurrences)
- `بلجرشي` (39 occurrences)
- `الزلفي` (37 occurrences)
- `الجبيل` (34 occurrences)
- `الدرعيه` (30 occurrences)
- `الليث` (29 occurrences)
- `الرس` (26 occurrences)
- `الظهران` (24 occurrences)
- `عيون الجوى` (24 occurrences)
- `مكة المكرمة` (23 occurrences)
- `الخبر` (23 occurrences)
- `جده/ الرياض` (22 occurrences)
- `الدمام` (22 occurrences)
- `سكاكا/ المروج` (20 occurrences)
- `الافلاج` (20 occurrences)
- `المدينة المنورة` (18 occurrences)
- `عرعر` (18 occurrences)
- `رابغ/ النعيم` (17 occurrences)
- `الرياض/ البيان` (17 occurrences)
- `المخواة` (17 occurrences)
- `المهد/أخرى` (15 occurrences)
- `بريده/ الهدية` (15 occurrences)
- `ابها` (15 occurrences)
- `طبرجل/ العيساوية` (14 occurrences)
- `ينبع` (14 occurrences)
- `رنيه` (13 occurrences)
- `تيماء` (13 occurrences)
- `حائل/ المزعبر` (12 occurrences)
- `كتابة عدل مدمجة - افتراضية` (12 occurrences)
- `الاحساء` (12 occurrences)
- `الطائف` (12 occurrences)
- `القصب/أخرى` (9 occurrences)
- `جده/ الكوثر` (9 occurrences)
- `الحائط` (9 occurrences)
- `جيزان` (9 occurrences)
- `سكاكا` (8 occurrences)
- `صامطه` (8 occurrences)
- `ثار` (8 occurrences)
- `الغاط/ المنتزة` (7 occurrences)
- `المجمعه` (7 occurrences)
- `العلا` (7 occurrences)
- `بقعاء` (7 occurrences)
- `جدة` (7 occurrences)
- `الغاط/ غرناطه` (6 occurrences)
- `الاحساء/ عين نجم` (6 occurrences)
- `المدينة المنورة/ شظاة فى منطقة قناة من مخطط شركة البشائر الذهبية` (6 occurrences)
- `حائل` (6 occurrences)
- `وادي الدواسر/ النزهة` (5 occurrences)
- `نجران` (5 occurrences)
- `البدائع` (5 occurrences)
- `خميس مشيط/ مخطط هيف وشركاه بالصفق` (4 occurrences)
- `حوطة سدير` (4 occurrences)
- `بريده` (4 occurrences)
- `المزاحميه` (4 occurrences)
- `الباحه` (4 occurrences)
- `الخرج` (4 occurrences)
- `الباحة` (4 occurrences)
- `العقيق` (4 occurrences)
- `طريف/ الفيصلية شرق` (3 occurrences)
- `الهفوف/ هجر التاسع` (3 occurrences)
- `ابها/ المحارث` (3 occurrences)
- `عقلة الصقور` (3 occurrences)
- `الرين` (3 occurrences)
- `وادي الدواسر` (3 occurrences)
- `ثادق` (3 occurrences)
- `ضباء` (3 occurrences)
- `القويعيه` (3 occurrences)
- `سميراء` (3 occurrences)
- `السليمي` (3 occurrences)
- `الجموم` (3 occurrences)
- `القنفذة` (3 occurrences)
- `خليص` (3 occurrences)
- `القطيف` (3 occurrences)
- `حفر الباطن` (3 occurrences)
- `الشملي` (3 occurrences)

### 3.5 Date Format Variations

- **MOJ-Deed-Define-Divide-2025-Q1.csv**: التاريخ ميلادي: Date format: YYYY/MM/DD
- **MOJ-Deed-Define-Divide-2025-Q2.csv**: التاريخ ميلادي: Date format: YYYY/MM/DD
- **MOJ-Deed-Define-Divide-2025-Q3.csv**: التاريخ ميلادي: Date format: YYYY/MM/DD
- **MOJ-Divide-2025-Q1.csv**: التاريخ ميلادي: Date format: YYYY/MM/DD
- **MOJ-Divide-2025-Q2.csv**: التاريخ ميلادي: Date format: DD/MM/YYYY or M/D/YYYY
- **MOJ-Divide-2025-Q3.csv**: التاريخ ميلادي: Date format: YYYY/MM/DD
- **MOJ-Enforcement-Sale-2025-Q1.csv**: تاريخ القرار ميلادي: Date format: YYYY/MM/DD; تاريخ القرارهجري: Date format: YYYY/MM/DD
- **MOJ-Enforcement-Sale-2025-Q2.csv**: تاريخ القرار ميلادي: Date format: YYYY/MM/DD
- **MOJ-Enforcement-Sale-2025-Q3.csv**: تاريخ القرار ميلادي: Date format: YYYY/MM/DD
- **MOJ-Enforcement-Sale-2025-Q4.csv**: تاريخ القرار ميلادي: Date format: YYYY/MM/DD
- **MOJ-Merge-Deed-2025-Q1.csv**: التاريخ ميلادي: Date format: YYYY/MM/DD
- **MOJ-Merge-Deed-2025-Q2.csv**: التاريخ ميلادي: Date format: YYYY/MM/DD
- **MOJ-Merge-Deed-2025-Q3.csv**: التاريخ ميلادي: Date format: YYYY/MM/DD
- **MOJ-Merge-RE-2025-Q1.csv**: التاريخ ميلادي: Date format: YYYY/MM/DD
- **MOJ-Merge-RE-2025-Q2.csv**: التاريخ ميلادي: Date format: YYYY/MM/DD
- **MOJ-Merge-RE-2025-Q3.csv**: التاريخ ميلادي: Date format: YYYY/MM/DD
- **MOJ-Mortgage-2025-Q1.csv**: التاريخ ميلادي: Date format: YYYY/MM/DD
- **MOJ-Mortgage-2025-Q2.csv**: التاريخ ميلادي: Date format: YYYY/MM/DD
- **MOJ-Mortgage-2025-Q3.csv**: التاريخ ميلادي: Date format: YYYY/MM/DD
- **MOJ-Mortgage-Release-2025-Q1.csv**: التاريخ ميلادي: Date format: YYYY/MM/DD
- **MOJ-Mortgage-Release-2025-Q2.csv**: التاريخ ميلادي: Date format: YYYY/MM/DD
- **MOJ-Mortgage-Release-2025-Q3.csv**: التاريخ ميلادي: Date format: YYYY/MM/DD
- **MOJ-Ownership-2025-Q1.csv**: التاريخ ميلادي: Date format: YYYY/MM/DD
- **MOJ-Ownership-2025-Q2.csv**: التاريخ ميلادي: Date format: DD/MM/YYYY or M/D/YYYY
- **MOJ-Ownership-2025-Q3.csv**: التاريخ ميلادي: Date format: YYYY/MM/DD
- **MOJ-Ownership-Men-2025-Q1.csv**: السنة: Date format: YYYY
- **MOJ-Ownership-Men-2025-Q2.csv**: السنة: Date format: YYYY
- **MOJ-Ownership-Men-2025-Q3.csv**: السنة: Date format: YYYY
- **MOJ-POA-RE-Fund-2025-Q1.csv**: التاريخ ميلادي: Date format: YYYY/MM/DD
- **MOJ-POA-RE-Fund-2025-Q3.csv**: التاريخ ميلادي: Date format: YYYY/MM/DD
- **MOJ-POA-RealEstate-2025-Q1.csv**: التاريخ ميلادي: Date format: YYYY/MM/DD
- **MOJ-POA-RealEstate-2025-Q2.csv**: التاريخ ميلادي: Date format: YYYY/MM/DD
- **MOJ-POA-RealEstate-2025-Q3.csv**: التاريخ ميلادي: Date format: YYYY/MM/DD
- **MOJ-Physical-Registration-2025-Q1.csv**: التاريخ ميلادي: Date format: YYYY/MM/DD
- **MOJ-Physical-Registration-2025-Q2.csv**: التاريخ ميلادي: Date format: YYYY/MM/DD
- **MOJ-Physical-Registration-2025-Q3.csv**: التاريخ ميلادي: Date format: YYYY/MM/DD
- **MOJ-Property-Identity-2025-Q1.csv**: التاريخ ميلادي: Date format: DD/MM/YYYY or M/D/YYYY
- **MOJ-Property-Identity-2025-Q3.csv**: التاريخ ميلادي: Date format: YYYY/MM/DD
- **MOJ-RE-Index-Cities-2018-2021.csv**: Unnamed: 4: Date format: YYYY; Unnamed: 8: Date format: YYYY; Unnamed: 13: Date format: YYYY
- **MOJ-RE-Index-Districts-2018-2021.csv**: Unnamed: 2: Date format: YYYY; Unnamed: 5: Date format: YYYY; Unnamed: 8: Date format: YYYY; Unnamed: 11: Date format: YYYY
- **MOJ-RE-Operations-2024-M01.csv**: التاريخ ميلادي: Date format: YYYY/MM/DD; التاريخ هجري: Date format: YYYY/MM/DD
- **MOJ-RE-Operations-2024-M02.csv**: التاريخ ميلادي: Date format: YYYY/MM/DD; التاريخ هجري: Date format: YYYY/MM/DD
- **MOJ-RE-Operations-2024-M03.csv**: التاريخ ميلادي: Date format: YYYY/MM/DD; التاريخ هجري: Date format: YYYY/MM/DD
- **MOJ-RE-Operations-2024-M04.csv**: التاريخ ميلادي: Date format: YYYY/MM/DD; التاريخ هجري: Date format: YYYY/MM/DD
- **MOJ-RE-Operations-2024-M05.csv**: التاريخ ميلادي: Date format: YYYY/MM/DD; التاريخ هجري: Date format: YYYY/MM/DD
- **MOJ-RE-Operations-2024-M06.csv**: التاريخ ميلادي: Date format: YYYY/MM/DD; التاريخ هجري: Date format: YYYY/MM/DD
- **MOJ-RE-Operations-2024-M07.csv**: التاريخ ميلادي: Date format: YYYY/MM/DD; التاريخ هجري: Date format: YYYY/MM/DD
- **MOJ-RE-Operations-2024-M08.csv**: التاريخ ميلادي: Date format: YYYY/MM/DD; التاريخ هجري: Date format: YYYY/MM/DD
- **MOJ-RE-Operations-2024-M09.csv**: التاريخ ميلادي: Date format: YYYY/MM/DD; التاريخ هجري: Date format: YYYY/MM/DD
- **MOJ-RE-Operations-2024-M10.csv**: التاريخ ميلادي: Date format: YYYY/MM/DD; التاريخ هجري: Date format: YYYY/MM/DD
- **MOJ-RE-Operations-2024-M11.csv**: التاريخ ميلادي: Date format: YYYY/MM/DD; التاريخ هجري: Date format: YYYY/MM/DD
- **MOJ-RE-Operations-2024-M12.csv**: التاريخ ميلادي: Date format: YYYY/MM/DD; التاريخ هجري: Date format: YYYY/MM/DD
- **MOJ-RE-Operations-2025-M01.csv**: التاريخ ميلادي: Date format: YYYY/MM/DD; التاريخ هجري: Date format: YYYY/MM/DD
- **MOJ-RE-Operations-2025-M02.csv**: التاريخ ميلادي: Date format: YYYY/MM/DD; التاريخ هجري: Date format: YYYY/MM/DD
- **MOJ-RE-Operations-2025-M03.csv**: التاريخ ميلادي: Date format: YYYY/MM/DD; التاريخ هجري: Date format: YYYY/MM/DD
- **MOJ-RE-Operations-2025-M04.csv**: التاريخ ميلادي: Date format: YYYY/MM/DD; التاريخ هجري: Date format: YYYY/MM/DD
- **MOJ-RE-Operations-2025-M05.csv**: التاريخ ميلادي: Date format: YYYY/MM/DD; التاريخ هجري: Date format: YYYY/MM/DD
- **MOJ-RE-Operations-2025-M06.csv**: التاريخ ميلادي: Date format: YYYY/MM/DD; التاريخ هجري: Date format: YYYY/MM/DD
- **MOJ-RE-Operations-2025-M07.csv**: التاريخ ميلادي: Date format: YYYY/MM/DD; التاريخ هجري: Date format: YYYY/MM/DD
- **MOJ-RE-Operations-2025-M08.csv**: التاريخ ميلادي: Date format: YYYY/MM/DD; التاريخ هجري: Date format: YYYY/MM/DD
- **MOJ-RE-Operations-2025-M09.csv**: التاريخ ميلادي: Date format: YYYY/MM/DD; التاريخ هجري: Date format: YYYY/MM/DD
- **MOJ-RE-Operations-2025-M10.csv**: التاريخ ميلادي: Date format: YYYY/MM/DD; التاريخ هجري: Date format: YYYY/MM/DD
- **MOJ-RE-Operations-2025-M11.csv**: التاريخ ميلادي: Date format: YYYY/MM/DD; التاريخ هجري: Date format: YYYY/MM/DD
- **MOJ-RE-Operations-2025-M12.csv**: التاريخ ميلادي: Date format: YYYY/MM/DD; التاريخ هجري: Date format: YYYY/MM/DD
- **MOJ-RE-Operations-2025-Q1.csv**: التاريخ ميلادي: Date format: YYYY/MM/DD
- **MOJ-RE-Operations-2025-Q2.csv**: التاريخ ميلادي: Date format: YYYY/MM/DD
- **MOJ-RE-Operations-2025-Q3.csv**: التاريخ ميلادي: Date format: YYYY/MM/DD
- **MOJ-Register-No-Deed-2025-Q1.csv**: التاريخ ميلادي: Date format: YYYY/MM/DD
- **MOJ-Register-No-Deed-2025-Q2.csv**: التاريخ ميلادي: Date format: YYYY/MM/DD
- **MOJ-Register-No-Deed-2025-Q3.csv**: التاريخ ميلادي: Date format: YYYY/MM/DD
- **MOJ-Register-Old-Deed-2025-Q1.csv**: التاريخ ميلادي: Date format: YYYY/MM/DD
- **MOJ-Register-Old-Deed-2025-Q2.csv**: التاريخ ميلادي: Date format: YYYY/MM/DD
- **MOJ-Register-Old-Deed-2025-Q3.csv**: التاريخ ميلادي: Date format: YYYY/MM/DD
- **MOJ-Release-Seizure-2025-Q1.csv**: التاريخ ميلادي: Date format: DD/MM/YYYY or M/D/YYYY
- **MOJ-Release-Seizure-2025-Q2.csv**: التاريخ ميلادي: Date format: YYYY/MM/DD
- **MOJ-Release-Seizure-2025-Q3.csv**: التاريخ ميلادي: Date format: YYYY/MM/DD
- **MOJ-Sales-2020-Q1.csv**: تاريخ الصفقة ميلادي: Date format: YYYY/MM/DD; تاريخ الصفقة هجري: Date format: YYYY/MM/DD
- **MOJ-Sales-2020-Q2.csv**: تاريخ الصفقة ميلادي: Date format: YYYY/MM/DD; تاريخ الصفقة هجري: Date format: YYYY/MM/DD
- **MOJ-Sales-2020-Q3.csv**: تاريخ الصفقة ميلادي: Date format: YYYY/MM/DD; تاريخ الصفقة هجري: Date format: YYYY/MM/DD
- **MOJ-Sales-2020-Q4.csv**: تاريخ الصفقة ميلادي: Date format: YYYY/MM/DD; تاريخ الصفقة هجري: Date format: YYYY/MM/DD
- **MOJ-Sales-2021-Q1.csv**: تاريخ الصفقة ميلادي: Date format: YYYY/MM/DD; تاريخ الصفقة هجري: Date format: YYYY/MM/DD
- **MOJ-Sales-2021-Q2.csv**: تاريخ الصفقة ميلادي: Date format: YYYY/MM/DD; تاريخ الصفقة هجري: Date format: YYYY/MM/DD
- **MOJ-Sales-2021-Q3.csv**: تاريخ الصفقة ميلادي: Date format: YYYY/MM/DD; تاريخ الصفقة هجري: Date format: YYYY/MM/DD
- **MOJ-Sales-2021-Q4.csv**: تاريخ الصفقة ميلادي: Date format: YYYY/MM/DD; تاريخ الصفقة هجري: Date format: YYYY/MM/DD
- **MOJ-Sales-2022-Q1.csv**: تاريخ الصفقة ميلادي: Date format: YYYY/MM/DD; تاريخ الصفقة هجري: Date format: YYYY/MM/DD
- **MOJ-Sales-2022-Q2.csv**: تاريخ الصفقة ميلادي: Date format: YYYY/MM/DD; تاريخ الصفقة هجري: Date format: YYYY/MM/DD
- **MOJ-Sales-2022-Q3.csv**: تاريخ الصفقة ميلادي: Date format: YYYY/MM/DD; تاريخ الصفقة هجري: Date format: YYYY/MM/DD
- **MOJ-Sales-2022-Q4.csv**: تاريخ الصفقة ميلادي: Date format: YYYY/MM/DD; تاريخ الصفقة هجري: Date format: YYYY/MM/DD
- **MOJ-Sales-2023-Q1.csv**: التاريخ: Date format: DD/MM/YYYY or M/D/YYYY
- **MOJ-Sales-2023-Q2.csv**: تاريخ الصفقة ميلادي: Date format: YYYY/MM/DD; تاريخ الصفقة هجري: Date format: YYYY/MM/DD
- **MOJ-Sales-2023-Q3.csv**: تاريخ الصفقة ميلادي: Date format: YYYY/MM/DD; تاريخ الصفقة هجري: Date format: YYYY/MM/DD
- **MOJ-Sales-2023-Q4.csv**: تاريخ الصفقة ميلادي: Date format: YYYY/MM/DD; تاريخ الصفقة هجري: Date format: YYYY/MM/DD
- **MOJ-Sales-2024-Q1.csv**: تاريخ الصفقة ميلادي: Date format: YYYY/MM/DD; تاريخ الصفقة هجري: Date format: YYYY/MM/DD
- **MOJ-Sales-2024-Q2.csv**: تاريخ الصفقة ميلادي: Date format: YYYY/MM/DD; تاريخ الصفقة هجري: Date format: YYYY/MM/DD
- **MOJ-Sales-2024-Q3.csv**: تاريخ الصفقة ميلادي: Date format: YYYY/MM/DD; تاريخ الصفقة هجري: Date format: YYYY/MM/DD
- **MOJ-Sales-2024-Q4.csv**: تاريخ الصفقة ميلادي: Date format: YYYY/MM/DD; تاريخ الصفقة هجري: Date format: YYYY/MM/DD
- **MOJ-Sales-2025-Q1.csv**: تاريخ الصفقة ميلادي: Date format: YYYY/MM/DD; تاريخ الصفقة هجري: Date format: YYYY/MM/DD
- **MOJ-Sales-2025-Q2.csv**: تاريخ الصفقة ميلادي: Date format: YYYY/MM/DD; تاريخ الصفقة هجري: Date format: YYYY/MM/DD
- **MOJ-Sales-2025-Q3.csv**: تاريخ الصفقة ميلادي: Date format: YYYY/MM/DD; تاريخ الصفقة هجري: Date format: YYYY/MM/DD
- **MOJ-Sales-2025-Q4.csv**: تاريخ الصفقة ميلادي: Date format: YYYY/MM/DD; تاريخ الصفقة هجري: Date format: YYYY/MM/DD
- **MOJ-Seizure-2025-Q1.csv**: التاريخ ميلادي: Date format: DD/MM/YYYY or M/D/YYYY
- **MOJ-Seizure-2025-Q2.csv**: التاريخ ميلادي: Date format: YYYY/MM/DD
- **MOJ-Seizure-2025-Q3.csv**: التاريخ ميلادي: Date format: YYYY/MM/DD
- **MOJ-Transfers-2025-Q1.csv**: التاريخ ميلادي: Date format: YYYY/MM/DD
- **MOJ-Transfers-2025-Q2.csv**: التاريخ ميلادي: Date format: DD/MM/YYYY or M/D/YYYY
- **MOJ-Transfers-2025-Q3.csv**: التاريخ ميلادي: Date format: YYYY/MM/DD
- **MOJ-Update-Deed-2025-Q1.csv**: التاريخ ميلادي: Date format: YYYY/MM/DD
- **MOJ-Update-Deed-2025-Q2.csv**: التاريخ ميلادي: Date format: YYYY/MM/DD
- **MOJ-Update-Deed-2025-Q3.csv**: التاريخ ميلادي: Date format: YYYY/MM/DD
- **MOJ-Update-Old-Deed-2025-Q1.csv**: التاريخ ميلادي: Date format: YYYY/MM/DD
- **MOJ-Update-Old-Deed-2025-Q2.csv**: التاريخ ميلادي: Date format: YYYY/MM/DD
- **MOJ-Update-Old-Deed-2025-Q3.csv**: التاريخ ميلادي: Date format: YYYY/MM/DD
- **Rental-indicators-for-Cities-in-Riyadh-region.csv**: السنة : Date format: YYYY; مجموع الصفقات: Date format: YYYY; المتوسط: Date format: YYYY
- **Rental-indicators-for-cities-Asir-region.csv**: السنة: Date format: YYYY; مجموع الصفقات: Date format: YYYY; المتوسط: Date format: YYYY
- **Rental-indicators-for-cities-in-Al-Baha-region.csv**: السنة : Date format: YYYY; مجموع الصفقات: Date format: YYYY; المتوسط: Date format: YYYY
- **Rental-indicators-for-cities-in-Al-jawf-region.csv**: السنة: Date format: YYYY; مجموع الصفقات: Date format: YYYY; المتوسط: Date format: YYYY
- **Rental-indicators-for-cities-in-Eastern-Province.csv**: year: Date format: YYYY; total_deals: Date format: YYYY; average: Date format: YYYY
- **Rental-indicators-for-cities-in-Hail-region.csv**: السنة: Date format: YYYY; مجموع الصفقات: Date format: YYYY; المتوسط: Date format: YYYY
- **Rental-indicators-for-cities-in-Jazan-region.csv**: السنة: Date format: YYYY; مجموع الصفقات: Date format: YYYY; المتوسط: Date format: YYYY
- **Rental-indicators-for-cities-in-Madinah-region.csv**: year: Date format: YYYY; total_deals: Date format: YYYY; average: Date format: YYYY
- **Rental-indicators-for-cities-in-Makkah-region.csv**: السنة : Date format: YYYY; مجموع الصفقات: Date format: YYYY; المتوسط: Date format: YYYY
- **Rental-indicators-for-cities-in-N-B-region.csv**: السنة: Date format: YYYY; مجموع الصفقات: Date format: YYYY; المتوسط: Date format: YYYY
- **Rental-indicators-for-cities-in-Najran-region.csv**: السنة: Date format: YYYY; مجموع الصفقات: Date format: YYYY; المتوسط: Date format: YYYY
- **Rental-indicators-for-cities-in-Qassim-region.csv**: السنة: Date format: YYYY; مجموع الصفقات: Date format: YYYY; المتوسط: Date format: YYYY
- **Rental-indicators-for-cities-in-Tabuk-region.csv**: السنة: Date format: YYYY; مجموع الصفقات: Date format: YYYY; المتوسط: Date format: YYYY
- **Sales-transaction-indicators-in-EP-1st-Q-2025.csv**: السنة: Date format: YYYY; قيمة الصفقات: Date format: YYYY; المساحة M2: Date format: YYYY; الحد الأعلى لسعر المتر: Date format: YYYY; الحد الأدنى لسعر المتر : Date format: YYYY
- **Sales-transaction-indicators-in-EP-2nd-Q-2025.csv**: السنة: Date format: YYYY; قيمة الصفقات: Date format: YYYY; المساحة M2: Date format: YYYY; متوسط سعر المتر: Date format: YYYY; الحد الأعلى لسعر المتر: Date format: YYYY; الحد الأدنى لسعر المتر : Date format: YYYY
- **Sales-transaction-indicators-in-EP-3rd-Q-2025.csv**: السنة: Date format: YYYY; المساحة M2: Date format: YYYY; الحد الأعلى لسعر المتر: Date format: YYYY; الحد الأدنى لسعر المتر : Date format: YYYY
- **Sales-transaction-indicators-in-Hail-1st-Q-2025.csv**: السنة: Date format: YYYY; المساحة M2: Date format: YYYY; الحد الأعلى لسعر المتر: Date format: YYYY; الحد الأدنى لسعر المتر : Date format: YYYY
- **Sales-transaction-indicators-in-Hail-2nd-Q-2025.csv**: السنة: Date format: YYYY; قيمة الصفقات: Date format: YYYY; المساحة M2: Date format: YYYY; الحد الأعلى لسعر المتر: Date format: YYYY
- **Sales-transaction-indicators-in-Hail-3rd-Q-2025.csv**: السنة: Date format: YYYY; المساحة M2: Date format: YYYY
- **Sales-transaction-indicators-in-Madinah-1stQ-2024.csv**: السنة: Date format: YYYY; المساحة M2: Date format: YYYY; الحد الأعلى لسعر المتر: Date format: YYYY; الحد الأدنى لسعر المتر : Date format: YYYY
- **Sales-transaction-indicators-in-Madinah-3rdQ-2024.csv**: السنة: Date format: YYYY; المساحة M2: Date format: YYYY; الحد الأعلى لسعر المتر: Date format: YYYY; الحد الأدنى لسعر المتر : Date format: YYYY
- **Sales-transaction-indicators-in-Madinah-4th-Q-2024.csv**: السنة: Date format: YYYY; مجموع سعر العقار: Date format: YYYY; المساحة M2: Date format: YYYY; الحد الأعلى لسعر المتر: Date format: YYYY; الحد الأدنى لسعر المتر : Date format: YYYY
- **Sales-transaction-indicators-in-Madinah-Q2-2024.csv**: السنة: Date format: YYYY; المساحة M2: Date format: YYYY; متوسط سعر المتر: Date format: YYYY; الحد الأعلى لسعر المتر: Date format: YYYY; الحد الأدنى لسعر المتر : Date format: YYYY
- **Sales-transaction-indicators-in-Makkah-1st-Q-2024.csv**: السنة: Date format: YYYY; المساحة M2: Date format: YYYY; الحد الأعلى لسعر المتر: Date format: YYYY; الحد الأدنى لسعر المتر : Date format: YYYY
- **Sales-transaction-indicators-in-Makkah-1st-Q-2025.csv**: السنة: Date format: YYYY; المساحة M2: Date format: YYYY; متوسط سعر المتر: Date format: YYYY; الحد الأعلى لسعر المتر: Date format: YYYY; الحد الأدنى لسعر المتر : Date format: YYYY
- **Sales-transaction-indicators-in-Makkah-2nd-Q-2024.csv**: السنة: Date format: YYYY; المساحة M2: Date format: YYYY; الحد الأعلى لسعر المتر: Date format: YYYY; الحد الأدنى لسعر المتر : Date format: YYYY
- **Sales-transaction-indicators-in-Makkah-2nd-Q-2025.csv**: السنة: Date format: YYYY; قيمة الصفقات: Date format: YYYY; المساحة M2: Date format: YYYY; متوسط سعر المتر: Date format: YYYY; الحد الأعلى لسعر المتر: Date format: YYYY; الحد الأدنى لسعر المتر : Date format: YYYY
- **Sales-transaction-indicators-in-Makkah-3rd-Q-2024.csv**: السنة: Date format: YYYY; المساحة M2: Date format: YYYY; الحد الأعلى لسعر المتر: Date format: YYYY; الحد الأدنى لسعر المتر : Date format: YYYY
- **Sales-transaction-indicators-in-Makkah-3rd-Q-2025.csv**: السنة: Date format: YYYY; المساحة M2: Date format: YYYY
- **Sales-transaction-indicators-in-Makkah-4th-Q-2024.csv**: السنة: Date format: YYYY; المساحة M2: Date format: YYYY; الحد الأعلى لسعر المتر: Date format: YYYY; الحد الأدنى لسعر المتر : Date format: YYYY
- **Sales-transaction-indicators-in-Riyadh-1st-Q-2024.csv**: السنة: Date format: YYYY; المساحة M2: Date format: YYYY; الحد الأعلى لسعر المتر: Date format: YYYY; الحد الأدنى لسعر المتر : Date format: YYYY
- **Sales-transaction-indicators-in-Riyadh-2nd-Q-2024.csv**: السنة: Date format: YYYY; المساحة M2: Date format: YYYY; الحد الأعلى لسعر المتر: Date format: YYYY; الحد الأدنى لسعر المتر : Date format: YYYY
- **Sales-transaction-indicators-in-Riyadh-2nd-Q-2025.csv**: السنة: Date format: YYYY; المساحة M2: Date format: YYYY; متوسط سعر المتر: Date format: YYYY; الحد الأعلى لسعر المتر: Date format: YYYY; الحد الأدنى لسعر المتر : Date format: YYYY
- **Sales-transaction-indicators-in-Riyadh-3rd-Q-2025.csv**: السنة: Date format: YYYY; المساحة M2: Date format: YYYY; الحد الأعلى لسعر المتر: Date format: YYYY; الحد الأدنى لسعر المتر : Date format: YYYY
- **Sales-transaction-indicators-in-Riyadh-3rdQ-2024.csv**: السنة: Date format: YYYY; عدد الصكوك : Date format: YYYY; المساحة M2: Date format: YYYY; الحد الأعلى لسعر المتر: Date format: YYYY; الحد الأدنى لسعر المتر : Date format: YYYY
- **Sales-transaction-indicators-in-Riyadh-4th-Q-2024.csv**: السنة: Date format: YYYY; المساحة M2: Date format: YYYY; الحد الأعلى لسعر المتر: Date format: YYYY; الحد الأدنى لسعر المتر : Date format: YYYY
- **Sales-transaction-indicators-in-Riyadh-Q1-2025.csv**: السنة: Date format: YYYY; عدد الصكوك : Date format: YYYY; قيمة الصفقات: Date format: YYYY; المساحة M2: Date format: YYYY; الحد الأعلى لسعر المتر: Date format: YYYY; الحد الأدنى لسعر المتر : Date format: YYYY
- **Sales-transaction-indicators-in-albaha-1st-Q-2025.csv**: السنة: Date format: YYYY; قيمة الصفقات: Date format: YYYY; المساحة M2: Date format: YYYY
- **Sales-transaction-indicators-in-albaha-2nd-Q-2025.csv**: السنة: Date format: YYYY; المساحة M2: Date format: YYYY
- **Sales-transaction-indicators-in-albaha-3rd-Q-2025.csv**: السنة: Date format: YYYY; المساحة M2: Date format: YYYY
- **Sales-transaction-indicators-in-the-EP-2nd-Q-2024.csv**: السنة: Date format: YYYY; المساحة M2: Date format: YYYY; الحد الأعلى لسعر المتر: Date format: YYYY; الحد الأدنى لسعر المتر : Date format: YYYY
- **Sales-transaction-indicators-in-the-EP-3rd-Q-2024.csv**: السنة: Date format: YYYY; المساحة M2: Date format: YYYY; متوسط سعر المتر: Date format: YYYY; الحد الأعلى لسعر المتر: Date format: YYYY; الحد الأدنى لسعر المتر : Date format: YYYY
- **Sales-transaction-indicators-in-the-EP-4th-Q-2024.csv**: السنة: Date format: YYYY; المساحة M2: Date format: YYYY; متوسط سعر المتر: Date format: YYYY; الحد الأعلى لسعر المتر: Date format: YYYY; الحد الأدنى لسعر المتر : Date format: YYYY
- **Sales-transaction-indicators-in-the-EP-Q-2024.csv**: السنة: Date format: YYYY; المساحة M2: Date format: YYYY; الحد الأعلى لسعر المتر: Date format: YYYY; الحد الأدنى لسعر المتر : Date format: YYYY
- **quarter-report-SI.csv**: yearnumber: Date format: YYYY; deed_counts: Date format: YYYY

### 3.6 Number Format Variations

**Comma thousands separators** (133 columns):
  - `MOJ-RE-Index-Regions-2018-2021.csv.2018`
  - `MOJ-RE-Index-Regions-2018-2021.csv.2019`
  - `MOJ-RE-Index-Regions-2018-2021.csv.2020`
  - `MOJ-RE-Index-Regions-2018-2021.csv.2021`
  - `MOJ-Sales-2020-Q1.csv.السعر`
  - `MOJ-Sales-2020-Q1.csv.المساحة`
  - `MOJ-Sales-2020-Q2.csv.السعر`
  - `MOJ-Sales-2020-Q2.csv.المساحة`
  - `MOJ-Sales-2020-Q3.csv.السعر`
  - `MOJ-Sales-2020-Q3.csv.المساحة`
  - `MOJ-Sales-2020-Q4.csv.السعر`
  - `MOJ-Sales-2020-Q4.csv.المساحة`
  - `MOJ-Sales-2021-Q1.csv.السعر`
  - `MOJ-Sales-2021-Q1.csv.المساحة`
  - `MOJ-Sales-2021-Q2.csv.السعر`
  - `MOJ-Sales-2021-Q2.csv.المساحة`
  - `MOJ-Sales-2021-Q3.csv.السعر`
  - `MOJ-Sales-2021-Q3.csv.المساحة`
  - `MOJ-Sales-2021-Q4.csv.السعر`
  - `MOJ-Sales-2021-Q4.csv.المساحة`
  - ... and 113 more

## 4. Risk Register

| Severity | Risk | Detail |
|----------|------|--------|
| **HIGH** | Comma as thousands separator in numbers | 109 files — inserting raw into INTEGER/REAL columns will fail or truncate: MOJ-Deed-Define-Divide-2025-Q1.csv, MOJ-Deed-Define-Divide-2025-Q2.csv, MOJ-Deed-Define-Divide-2025-Q3.csv, MOJ-Divide-2025-Q1.csv, MOJ-Divide-2025-Q2.csv, MOJ-Divide-2025-Q3.csv, MOJ-Enforcement-Sale-2025-Q1.csv, MOJ-Enforcement-Sale-2025-Q2.csv, MOJ-Enforcement-Sale-2025-Q3.csv, MOJ-Enforcement-Sale-2025-Q4.csv |
| **MEDIUM** | UTF-8 BOM present | 152 files — BOM will corrupt first column name if not handled: MOJ-RE-Index-Regions-2018-2021.csv, MOJ-Sales-2020-Q1.csv, MOJ-Sales-2020-Q2.csv, MOJ-Sales-2020-Q3.csv, MOJ-Sales-2020-Q4.csv, MOJ-Sales-2021-Q1.csv, MOJ-Sales-2021-Q2.csv, MOJ-Sales-2021-Q3.csv, MOJ-Sales-2021-Q4.csv, MOJ-Sales-2022-Q1.csv |
| **MEDIUM** | Mixed data types in same column | 108 columns: MOJ-RE-Index-Districts-2018-2021.csv.Unnamed: 2, MOJ-RE-Index-Districts-2018-2021.csv.Unnamed: 5, MOJ-RE-Index-Districts-2018-2021.csv.Unnamed: 8, MOJ-RE-Index-Regions-2018-2021.csv.2018, MOJ-RE-Index-Regions-2018-2021.csv.2019, MOJ-RE-Index-Regions-2018-2021.csv.2020, MOJ-RE-Index-Regions-2018-2021.csv.2021, MOJ-Sales-2020-Q1.csv.المساحة, MOJ-Sales-2020-Q2.csv.المساحة, MOJ-Sales-2020-Q3.csv.المساحة |
| **LOW** | CRLF line endings | 152 files — Python csv module handles this, but raw readline won't |
| **LOW** | Columns with >50% null rate | 84 columns (may indicate optional fields or schema mismatch): MOJ-RE-Index-Cities-2018-2021.csv.Unnamed: 12 (71% null); MOJ-RE-Index-Cities-2018-2021.csv.Unnamed: 13 (71% null); MOJ-RE-Index-Cities-2018-2021.csv.Unnamed: 14 (71% null); MOJ-RE-Index-Districts-2018-2021.csv.Unnamed: 10 (66% null); MOJ-RE-Index-Districts-2018-2021.csv.Unnamed: 11 (66% null); MOJ-RE-Index-Districts-2018-2021.csv.Unnamed: 12 (66% null); MOJ-RE-Index-Regions-2018-2021.csv.2021 (68% null); Sales-transaction-indicators-in-EP-1st-Q-2025.csv.متوسط سعر المتر (72% null); Sales-transaction-indicators-in-EP-1st-Q-2025.csv.الحد الأعلى لسعر المتر (72% null); Sales-transaction-indicators-in-EP-1st-Q-2025.csv.الحد الأدنى لسعر المتر  (72% null) |
---

## 5. Schema Drift Appendix

This section documents the exact header changes across file series that span multiple periods.

### 5.1 MOJ Sales — Three Distinct Schemas

**Schema A** — 2020-Q1 through 2022-Q4 (12 files), and 2023-Q2 through 2025-Q4 (13 files, minus 2023-Q1):
```
المنطقة | المدينة | المدينة / الحي | الرقم المرجعي للصفقة | تاريخ الصفقة ميلادي | تاريخ الصفقة هجري | تصنيف العقار | عدد العقارات | السعر | المساحة
(10 columns)
```

**Schema B** — 2023-Q1 ONLY (1 file, completely different):
```
رقم مرجعي | المنطقة | المدينة | الحي | المخطط | رقم القطعة | التاريخ | تصنيف العقار | نوع العقار | عدد العقارات | السعر بالريال السعودي | المساحة  | سعر المتر المربع
(13 columns — adds الحي, المخطط, رقم القطعة, سعر المتر; renames السعر to السعر بالريال السعودي; drops هجري date; note trailing space on المساحة)
```

**Schema A+** — 2023-Q2 and 2023-Q3 (2 files): Same as A but adds `نوع العقار` column (11 columns total).

**Key ingestion risk:** 2023-Q1 must be treated as a separate source table or mapped carefully. The column `المدينة / الحي` is not present; instead `الحي` and `المخطط` are separate. Price column is renamed. No Hijri date. Also: `المساحة ` has a trailing space in the header in this file.

### 5.2 MOJ Enforcement Sale — Dropped Hijri Date Column

- **2025-Q1**: 6 columns — includes `تاريخ القرارهجري` (Hijri date)
- **2025-Q2 to Q4**: 5 columns — `تاريخ القرارهجري` dropped

Note: `تاريخ القرارهجري` in Q1 has no space between words (unlike the Gregorian date column which has a space), suggesting a typo in the original that was later corrected by just removing the column.

### 5.3 MOJ Mortgage-Release — Corrupted First Column in Q3

- **2025-Q1, Q2**: First column = `المنطقة`
- **2025-Q3**: First column = `ج` (truncated — likely a file corruption or encoding issue where the BOM consumed part of the column name)

**Risk:** Do not rely on column-position indexing. When ingesting, always use the header name lookup; and validate that `المنطقة` resolves correctly. For Q3, the first column may need manual renaming before insert.

### 5.4 MOJ RE-Operations — Two Completely Different Schemas

**Monthly files** (2024-M01 through 2025-M12, 24 files):
```
المنطقة | المدينة | نوع القطاع | نوع الخدمة | نوع العملية | التاريخ ميلادي | التاريخ هجري | عدد العمليات
(8 columns — includes operation type, operation count, Hijri date)
```

**Quarterly files** (2025-Q1, Q2, Q3):
```
المنطقة | المدينة | نوع القطاع | نوع الخدمة | التاريخ ميلادي | الرقم المرجعي
(6 columns — drops نوع العملية, عدد العمليات, التاريخ هجري; adds الرقم المرجعي)
```

These are fundamentally different tables and must NOT be union-stacked without a schema mapping.

### 5.5 REGA Sales Transaction Indicators — Column Renamed Between 2024 and 2025

**2024 files** include:
```
رقم الربع  | مجموع سعر العقار
```

**2025 files** replace those with:
```
تصنيف العقار | قيمة الصفقات
```

The column `رقم الربع` (quarter number) was removed in 2025. `مجموع سعر العقار` (total property price) was renamed to `قيمة الصفقات` (deal value). A new `تصنيف العقار` (property classification) column was added. Files from different years cannot be stacked without mapping.

---

## 6. Ejar Collector Note

The Ejar collector directory contains only SQLite database files (`ejar.db`). There are no CSV exports — the collector writes directly to SQLite. No CSV survey was performed for this data source.

---

## 7. Index Files Note (MOJ RE Price Indices)

The three Index files (`MOJ-RE-Index-Cities-2018-2021.csv`, `MOJ-RE-Index-Districts-2018-2021.csv`, `MOJ-RE-Index-Regions-2018-2021.csv`) have a non-standard pivoted structure:

- Rows represent geographic units (cities/districts/regions)
- Columns are years (2018, 2019, 2020, 2021) with index values
- Many columns are labeled `Unnamed: N` because the original Excel pivot table had merged headers
- Multiple index series are stored side-by-side in the same file (residential, commercial, land)
- The `Unnamed` columns with 66-71% null rates are sub-series that don't apply to all rows
- **These files require unpivoting (melt) before ingestion into a normalized table**

