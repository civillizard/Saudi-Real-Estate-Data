# Ministry of Justice (MOJ; وزارة العدل) Real Estate Reference Number Audit
<p align="center">
  <a href="https://www.6ra3.com/track/r/rega-site-reference-number-audit?dest=https://rega.gov.sa"><img src="https://www.6ra3.com/track/rega/reference-number-audit" height="50" alt="REGA - Real Estate General Authority (الهيئة العامة للعقار)"></a>
  &nbsp;&nbsp;&nbsp;&nbsp;
  <a href="https://www.6ra3.com/track/r/moj-site-reference-number-audit?dest=https://moj.gov.sa"><img src="https://www.6ra3.com/track/moj/reference-number-audit" height="50" alt="MOJ - Ministry of Justice (وزارة العدل)"></a>
</p>

**Date:** 2026-03-12
**Scope:** Seizure, Release-Seizure, Enforcement-Sale, Mortgage, Mortgage-Release, Transfers — 2025 Q1–Q4
**Purpose:** Determine whether الرقم المرجعي can be used to link assets across transaction lifecycle stages

---

## Data Summary

| Category | Files | Records | Ref Range |
|---|---|---|---|
| Seizure (الحجز التحفظي) | Q1–Q3 | 736,808 | 27,035,248 – 31,477,550 |
| Release-Seizure (فك الحجز) | Q1–Q3 | 505,725 | 27,035,283 – 32,378,472 |
| Enforcement-Sale (قرار بيع) | Q1–Q4 | 8,286 | 14,095,408 – 17,400,305 |
| Mortgage (رهن) | Q1–Q3 | 36,525 | 27,037,272 – 32,378,025 |
| Mortgage-Release (فك رهن) | Q1–Q3 | 42,781 | 27,036,842 – 32,378,439 |
| Transfers (إفراغات) | Q1–Q3 | 221,229 | 26,406,201 – 32,377,689 |

---

## Step 1: Reference Number Format

All reference numbers are 8-digit plain integers. No prefixes, no category codes, no dashes.

**Key observation — two distinct numbering pools:**

- **Group A (27M–32M):** Seizure, Release-Seizure, Mortgage, Mortgage-Release, Transfers all share this range. Numbers are globally sequential and appear to be assigned chronologically across all electronic notary services (كتابة العدل). This suggests they draw from a **single shared counter** for all MOJ services, not separate per-category counters.

- **Group B (14M–17M):** Enforcement-Sale sits in a distinctly lower range, suggesting it draws from a **different system** — likely the enforcement court system (قضاء التنفيذ) rather than the notary registry. Its schema also differs (has a Hijri date field; uses "نوع السند الرئيسي" instead of "نوع القطاع").

Within each category, reference numbers are **100% unique** — no duplicates exist within any file set.

---

## Step 2: Cross-Category Overlap (Direct Matching)

**Result: ZERO overlapping reference numbers across all category pairs.**

| Pair | Overlaps |
|---|---|
| Seizure ∩ Release-Seizure | 0 |
| Seizure ∩ Enforcement-Sale | 0 |
| Seizure ∩ Mortgage | 0 |
| Release-Seizure ∩ Enforcement-Sale | 0 |
| Mortgage ∩ Mortgage-Release | 0 |
| All 15 pairwise combinations | 0 |
| Any ref appearing in 2+ categories | 0 |

**Interpretation:**
Although Seizure, Release-Seizure, Mortgage, Mortgage-Release, and Transfers all draw from the same 27M–32M range — and their ranges fully overlap numerically — no single number appears in two categories. This is **by design**: each transaction event gets a fresh, unique reference number. The الرقم المرجعي is a **transaction ID**, not a **property ID**. The same physical property that gets seized, released, and sold will have three completely different reference numbers — one per event.

---

## Step 3: Fuzzy Linking Potential

Since direct ref matching fails, we tested whether available fields could link Seizure records to Release-Seizure records.

**Fields available in both Seizure and Release-Seizure:**

| Field | Arabic | Notes |
|---|---|---|
| Region | المنطقة | Very low cardinality |
| City | المدينة | Extremely low cardinality — see below |
| Sector type | نوع القطاع | Only 2 values: public/private |
| Service type | نوع الخدمة | Only 2 values: electronic/partial |
| Date | التاريخ ميلادي | Gregorian date |

**Critical problem — geographic data is near-useless:**

- **Seizure (all Q1–Q3):** 736,808 records, but only **1 distinct city: الرياض**. The entire dataset covers only Riyadh.
- **Release-Seizure (all Q1–Q3):** 505,725 records, only **2–4 distinct values** (الرياض plus occasional ابها/الطائف/blank rows).

This means after matching on city + region + sector type + date within 1 year, a single seizure record has approximately **150,000–300,000 candidate matches** in the Release-Seizure dataset (the entire pool of Riyadh records within the year). Fuzzy linking here is not just imprecise — it is non-functional.

**Enforcement-Sale is even harder to link:**
- Enforcement-Sale uses a different schema (no sector type, different date fields, adds Hijri date)
- Its 1,641 Riyadh rows must be matched against 505,725 Release-Seizure Riyadh rows — a 1:308 ratio before any other filter
- No area (m²) field exists in any of these files — the one field that could help disambiguate physical properties is absent

**Fuzzy linking verdict: Not feasible with available data fields.**

---

## Step 4: Reference Number Format Analysis

**Format:** Plain 8-digit integers. No embedded metadata.

**Sequential behavior:** Numbers appear to increment globally across all notary service types. On a given date, you see numbers in the low-27M range for Q1-2025 and progressively higher numbers through Q3-2025, regardless of transaction category. This confirms they are **sequence numbers from the MOJ notary system's transaction log**, not property identifiers.

**Enforcement-Sale anomaly:** The 14M range is approximately 12 million lower than the 26M–32M range used by all other categories. This almost certainly means Enforcement-Sale numbers come from the **Enforcement Court system (نظام قضاء التنفيذ)**, which has its own independent counter. There is no structural relationship between an Enforcement-Sale ref number and any Seizure or Release-Seizure ref number.

**No shared underlying ID is encoded in the reference number itself.**

---

## Conclusions

### 1. Can reference numbers link assets across lifecycle stages?
**No.** The reference number is a transaction-level sequence number, not a property-level identifier. Each event (seizure, release, sale) gets a new unique number. There is no foreign key relationship between them.

### 2. Is the Enforcement-Sale system the same as the Notary system?
**No.** Enforcement-Sale draws from a separate system (enforcement courts) with a different number range (14M vs 27M+) and a different schema.

### 3. Is fuzzy linking feasible?
**No, with current data.** The geographic fields are too coarse — the Seizure/Release-Seizure datasets cover effectively only Riyadh as a single bucket. Without a property deed number (رقم الصك), plot ID (رقم القطعة), or property identity number (الهوية العقارية), there is no reliable way to link events to the same physical asset.

### 4. What would enable lifecycle tracking?
The data needed is either:
- **رقم الصك (Deed number):** Would appear in both the seizure order and the eventual transfer deed
- **الهوية العقارية (Property Identity Number):** MOJ has been issuing these; a separate file `MOJ-Property-Identity-2025-Q1.csv` exists in this dataset but wasn't part of this audit — worth examining
- **Plot coordinates or parcel ID** from REGA/MOJ spatial data
- **Court case number** (for Enforcement-Sale specifically) — Enforcement-Sale records may share a court case number with prior seizure orders, but this field is not in the current dataset

### 5. Data quality note
Seizure Q3 contains ~174,000 fully blank rows (all fields empty). These are not valid records and should be filtered before any analysis. They constitute ~46% of Q3 rows.

---

## Recommendation

Lifecycle tracking via the current MOJ quarterly files alone is **not possible**. The most promising path is:

1. **Examine `MOJ-Property-Identity-2025-Q1.csv`** — this file may contain property-level IDs that could be cross-referenced with deed numbers appearing in transfer records
2. **Request REGA/MOJ linked datasets** that join transaction events by deed number or parcel ID
3. **For mortgage lifecycle (رهن → فك رهن):** These files do share the same number range and similar volumes. The ~6,000 more Mortgage-Release records than Mortgage records in the same period suggests some releases predate Q1-2025. A property-deed-based join would be the right approach here too.
