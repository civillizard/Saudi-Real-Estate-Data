# Changelog

<p align="center">
  <a href="https://www.6ra3.com/track/r/rega-site-changelog?dest=https://rega.gov.sa"><img src="https://www.6ra3.com/track/rega/changelog" height="50" alt="REGA - Real Estate General Authority (الهيئة العامة للعقار)"></a>
  &nbsp;&nbsp;&nbsp;&nbsp;
  <a href="https://www.6ra3.com/track/r/moj-site-changelog?dest=https://moj.gov.sa"><img src="https://www.6ra3.com/track/moj/changelog" height="50" alt="MOJ - Ministry of Justice (وزارة العدل)"></a>
</p>

All notable updates to this dataset are documented here.

Format: date-based versions. Each entry lists new data added, corrections, and documentation changes.

---

## 2026-04-09 — Data Corrections + Update Checker

### Data Corrections
- **MOJ-Transfers-2025-Q2.csv:** 93 KB → 23.5 MB — was a stub file, now contains full quarterly transfer (إفراغ) data
- **MOJ-Transfers-2025-Q3.csv:** 96 KB → 27.8 MB — same issue, now complete
- **MOJ-Release-Seizure-2025-Q2.csv:** 15.1 MB → 25.0 MB — expanded with additional records
- **MOJ-Sales-2025-Q2.csv:** 5.6 MB → 6.2 MB — minor correction (+586 KB)
- **Total:** 303 CSVs, ~7.48M rows

### Tools
- `download_new_data.py --check-updates` — detects when the portal silently replaces files with corrected versions (compares local vs remote file size via Range GET)
- `download_new_data.py --redownload-changed` — re-downloads files flagged as changed
- `update_pipeline.sh` — fixed macOS compatibility (`grep -P` → `sed`)

### Notes
- The Saudi Open Data portal occasionally publishes metadata for files before uploading the actual data. 10 datasets (Doc Attorney 2023 monthly, Property Identity Q2 2025) have catalog entries but return 404 on the CDN. These will be downloaded automatically once uploaded.
- The Transfer files were originally uploaded as ~95 KB stubs (containing only headers + a few rows) and were silently replaced with full data (~25 MB each) sometime between Apr 7–9.

---

## 2026-04-07 — Major Data Update

### Data
- **129 new CSV files** added (72 in first batch + 57 in follow-up)
- **MOJ Monthly Operations:** 26 new monthly aggregate files (Feb 2024–Feb 2026), 8-column schema with operation type breakdowns by region/city
- **MOJ POA Issued:** 30 monthly files (Apr 2023–Feb 2026), power-of-attorney issuance by region
- **MOJ Q4 2025 backfills:** 13 files across existing categories (enforcement, mortgage, transfer, seizure, etc.)
- **18 new MOJ categories:** compensation, compensation ruins, enforcement auction sale, enforcement award buyer, enforcement sell property, grants, grant alternative, monthly operations, POA Ejar, POA issued, POA white land fee, transfer ownership, transfer will (no ownership), ownership rate (men), ownership rate (women), register old deed, register no deed
- **Total:** 288 CSVs, ~7.44M rows, 853 MB (was 159 CSVs, ~5.10M rows, 565 MB)

### Tools
- `scripts/download_new_data.py` — automated downloader using `odp-public` URL pattern (bypasses WAF)
- Registry builder updated with 42 classification rules (was 26), all new categories properly classified

### Notes
- Monthly files use a different schema (8 cols, aggregated counts) vs quarterly files (6 cols, individual records)
- Enforcement schema break: Q1 has 6 cols, Q2+ has 5 cols (Hijri date column dropped)
- Leading spaces in region names present in some new files (portal data quality issue)
- 67 files still missing from portal (mostly POA monthly — low priority)

---

## 2026-03-24 — Initial Public Release

### Data
- **Ministry of Justice (MOJ; وزارة العدل) Sales:** 24 quarterly files (2020-Q1 through 2025-Q4), 1.41M transaction rows
- **MOJ Real Estate Operations:** 86 files across 18 categories (2024-2025), 3.62M rows
- **MOJ Historical Index:** 3 files (2018-2021 market indices by region/city/district)
- **Real Estate General Authority (REGA; الهيئة العامة للعقار) Sales Indicators:** 31 quarterly files for 6 regions (2024-2025), 22K rows
- **REGA Rental Indicators:** 13 files covering all regions, 20K rows
- **REGA Gender Registration:** 1 file (2024)
- **REGA Consolidated Report:** 1 file (quarter-report-SI.csv), 32.7K rows
- **REGA Charts:** 8 infographic visualizations
- **Total:** 159 CSV files, ~5.10M rows, 565 MB

### Documentation
- Full repository documentation: README, glossary, data primer, legal status
- Data quality audits: survey report, asset type audit, reference number audit, property identity audit
- Research files: 44 analysis ideas, API research (13 sources), White Land Tax research
- MOJ data documentation with schemas, region breakdowns, yearly trends
- REGA Ejar API documentation

### Tools
- `scripts/build_registry.py` — self-describing metadata catalog builder
- `monitor/re_data_monitor.py` — automated portal monitoring for new datasets

---

## Update Cadence

New data is published by the source agencies on the following schedule:
- **MOJ Sales & Operations:** Quarterly (~2-4 weeks after quarter end)
- **REGA Sales Indicators:** Quarterly, per region
- **REGA Rental Indicators:** Irregular (typically annual)

This repository is updated when new data is detected by the monitoring system. Updates are tagged by date (e.g., `2026-06-15`).
