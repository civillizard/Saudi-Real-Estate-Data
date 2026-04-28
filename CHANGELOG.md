# Changelog

<p align="center">
  <a href="https://rega.gov.sa"><img src="" height="50" alt="REGA - Real Estate General Authority (الهيئة العامة للعقار)"></a>
  &nbsp;&nbsp;&nbsp;&nbsp;
  <a href="https://moj.gov.sa"><img src="" height="50" alt="MOJ - Ministry of Justice (وزارة العدل)"></a>
</p>

All notable updates to this dataset are documented here.

Format: date-based versions. Each entry lists new data added, corrections, and documentation changes.

---

## 2026-04-28 — REGA Monthly Bulletins (5 PDFs + parsed timeseries)

### Data
- **5 new REGA-published PDFs** (24.2 MB) under new `rega/bulletins/pdfs/`:
  - `2026-01-monthly-bulletin.pdf` (1.9 MB) — January 2026 monthly bulletin (النشرة الشهرية للسوق العقاري)
  - `2026-02-monthly-bulletin.pdf` (1.7 MB) — February 2026 monthly bulletin
  - `2026-03-monthly-bulletin.pdf` (1.7 MB) — March 2026 monthly bulletin
  - `2026-01-indicators-report.pdf` (13.8 MB) — January 2026 quarterly indicators report (تقرير مؤشرات القطاع العقاري)
  - `2026-02-indicators-report.pdf` (6.5 MB) — February 2026 indicators report
- **Parsed timeseries** at `rega/bulletins/rega_bulletin_timeseries.csv` — 108 rows × 14 columns covering sales transaction count, sales value, MoM/YoY percentages by region and segment (residential, non-residential), extracted from the 5 PDFs above. Schema: `month, publication_date, section, indicator, segment, sub_type, region, region_rank, metric, value, unit, mom_pct, yoy_pct, source_pdf`.

### Source
REGA's Real Estate General Authority publishes monthly bulletins and quarterly indicator reports on rega.gov.sa. PDFs sourced from the original publication URLs; the timeseries CSV is a parsed extraction of the headline indicators in machine-readable form.

### Notes
- Original Arabic publication titles preserved in the bulletins themselves; English filenames used for predictability.
- Indicator report sizes vary (Q1 includes a much larger geographic breakdown than monthly bulletins).
- Timeseries currently covers only the headline national + regional indicators surfaced in the bulletins, not every figure published. A fuller extraction is planned for a later release.

---

## 2026-04-11 — Opportunistic Recovery + New Taxonomy (138 files, +2.0M rows)

### Data
- **138 new MOJ files recovered** (60 CSV, 78 XLSX) from the Apr 7 monitor findings that our discovery-time capture path had silently dropped.
- **`moj/opportunistic/`** — 108 files (54 CSV + 54 XLSX, ~222 MB, ~1.5 M rows) covering MOJ datasets that don't fit the main real-estate taxonomy:
  - **Non-RE Power-of-Attorney sub-categories** — POAs issued in courts, banks, traffic authority, civil status, government offices, foreign affairs (تصديق الوكالات الخارجية), Ministry of Commerce, boat/fishing licenses, university rewards, and more. Each POA sub-category is published as a standalone quarterly dataset.
  - **Annulled POAs (الوكالات المفسوخة)** — 4 monthly files (2024-02, 2025-01, 02, 11, 2026-02).
  - **REGA regional sales indicators** — 10 quarterly files for Riyadh (Q1/Q2/Q3 2025), Makkah (Q3 2024), Madinah (Q1/Q2 2024), Al-Baha (Q1/Q3 2025), Hail (Q3 2025), Eastern Province (Q3 2025).
  - **Makkah rental indicators** — city-level rental indicators for Makkah region.
- **`moj/real-estate/`** — 14 new XLSX siblings for existing quarterly sub-categories (Compensation, Compensation-Ruins, Deed-Define-Divide, Divide, Grant-Alternative, Merge-Deed Q2–Q4, Mortgage-Release, Ownership, POA-Ejar Q2+Q3, POA-RE-Fund, Transfers).
- **`moj/monthly/`** — 14 new XLSX siblings (Monthly-Operations 2024-05/11, 2025-06/07/09/10/11, 2026-01; POA-Issued 2024-01/06/09, 2025-05/10, 2026-02).
- **`moj/sales/`** — RE-Index Cities + Districts 2018-2021 XLSX siblings.
- **Total:** 360 CSVs (was 312) + 85 XLSX, ~9.49 M rows, 1.07 GB. The net CSV delta is lower than the raw file count because 11 REGA "new" resources turned out to be byte-exact duplicates of existing files under new Arabic names — they were removed rather than double-tracked.

### Reclassification — English-slug taxonomy
- **New `moj/poa-other/` directory** (76 files = 38 × CSV + XLSX) for non-RE Power-of-Attorney quarterly sub-categories: Agricultural-Dev-Fund, Agricultural-Grants, Banks, Boat-Fishing-Licenses, Civil-Affairs, Claims-Courts, Commercial-Records, Companies, Compensation-Aid, Court-Completions, Foreign-POA-Attest, Gov-Authorities, Gov-Institutions, Housing-Grants, Labor-Recruitment, Municipalities, Post, Recruitment-Office, Salaries-Dues, Service-Requests, Social-Dev-Bank, Social-Security, Telecom-Companies, Traffic, University-Rewards, Vehicles.
- **5 monthly `MOJ-POA-Annulled-*` files** added to `moj/monthly/` (2024-02, 2025-01, 2025-02, 2025-11, 2026-02). 8-column schema with dissolution reason + hijri date.
- **11 REGA XLSX siblings** merged alongside existing canonical CSVs in `rega/` with their original English slug names.
- `moj/opportunistic/` staging directory fully drained and removed.

### Tools / infrastructure
- **`scripts/portal_client.py`** (new) — shared Saudi Open Data client with full stealth bundle from request 1: Safari UA, warmup cookies, per-segment URL encoding, `downloadUrl` field used directly, `NO DATA FOUND` sentinel, retry for flaky `/data/api/datasets/resources` endpoint.
- **`scripts/grab_new_findings.py`** (new) — reusable opportunistic recovery downloader. Sweeps `monitor/monitor_state.db` by `--since` date, dedups against all existing repo files by MD5 before writing, falls back to a staging dir for unrecognised titles. `--no-dedup` to override.
- **`scripts/reclassify_opportunistic.py`** (new) — one-shot Arabic→English slug mover with git mv, guards against destination conflicts.
- **`scripts/icloud_materialize.py`** (new) — force-downloads iCloud-backed files before batch reads. The repo lives in iCloud Drive and cold-cache files stall batch scripts at 0% CPU in `_bufferedreader_fill_buffer` with no error. Registry builder and the hash-index walk both call this at startup.
- **`monitor/re_data_monitor.py`** — `_try_capture_resource()` rewritten to use the shared portal client. Verified working: fresh monitor run captured 53 files against the live portal (gitignored to `monitor/captured/`).
- **`scripts/build_registry.py`** — `kapsarc/KAPSARC-Building-Permits.csv` (1.7 GB, gitignored), derived `data/registry_*.csv`, and `monitor/` dir all excluded from the scan.
- **`docs/saudi-open-data-portal.md`** (new) — full portal playbook. Read before writing any script that talks to the portal.
- **`monitor/monitor_state.db`** schema fix: `check_log.api_changes` column added via `ALTER TABLE` so post-run summary INSERTs stop failing.

### Tools
- **`scripts/portal_client.py`** — new shared Saudi Open Data portal client. Every script that talks to the portal must use this helper instead of hand-rolling an HTTP path. Full stealth bundle from request 1: Safari User-Agent + warmup GET to `/en` to collect `dm2`, `BPfffdc833146`, `BP407814ff` cookies, per-segment URL encoding (portal now publishes files with spaces such as `Doc Attorney CSV.csv`), `downloadUrl` field used directly instead of reconstructed, `NO DATA FOUND` sentinel treated as data-withdrawn, retry with exponential backoff for the flaky `/data/api/datasets/resources` endpoint.
- **`scripts/grab_new_findings.py`** — one-shot recovery downloader. Sweeps `monitor/monitor_state.db` for datasets first discovered after `--since`, uses `parse_dataset()` from the main downloader for known RE categories and a slug fallback (`moj/opportunistic/`) for unrecognised titles. Handles dedup, WAF, NO DATA FOUND, and portal flakiness.
- **`monitor/re_data_monitor.py`** — `_try_capture_resource()` now delegates to the shared portal client. The previous implementation was broken: it reconstructed URLs manually instead of using the API's `downloadUrl` field, did not URL-encode spaces, and did not warm up the WAF cookies. Apr 7 run silently captured zero files.
- **`docs/saudi-open-data-portal.md`** — full playbook of every operational lesson learned from the portal (WAF bundle, flaky endpoints, generic placeholder filenames, sentinel handling, retry policy). Read this before writing any new portal code.

### Notes
- The Saudi Open Data portal has started publishing many MOJ datasets with **generic placeholder filenames** — every POA sub-category uses `Doc Attorney CSV.csv`, every deed aggregate uses `Total number of deeds transactions CSV.csv`, every annulment file uses `Total number of annulments CSV.csv`. These names are reused across dozens of unrelated datasets, so **uniqueness lives in the UUID path segment**, not the filename. The `moj/opportunistic/` directory uses Arabic-title slugs with a UUID prefix for disambiguation.
- The recovery sweep probed 86 datasets and found 73 live on the first pass. A slower retry pass recovered 8 more from the flaky `/data/api/datasets/resources` endpoint. 4 files remain hard-404 (POA Aug/Sep 2023 × CSV + XLSX) — portal returns a `downloadUrl` that returns 404 at the odp-public blob path, a portal-side inconsistency we can't fix client-side.
- The 10 datasets the Apr 9 note flagged as "missing from portal" (Doc Attorney 2023 monthly, Property Identity Q2 2025) are in fact live — the downloader was blocked by its own URL reconstruction bug, not a missing-file problem. These are now captured under `moj/opportunistic/` with the recovered data.
- `moj/opportunistic/` is a staging directory. Files will be reclassified and merged into `moj/real-estate/`, `moj/monthly/`, or a new `moj/poa-other/` taxonomy in a future release once the non-RE POA categories have been enumerated and mapped.

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
