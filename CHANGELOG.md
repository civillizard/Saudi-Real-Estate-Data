# Changelog

<p align="center">
  <a href="https://rega.gov.sa">REGA - Real Estate General Authority (الهيئة العامة للعقار)</a>
  &nbsp;&nbsp;&nbsp;&nbsp;
  <a href="https://moj.gov.sa">MOJ - Ministry of Justice (وزارة العدل)</a>
</p>

All notable updates to this dataset are documented here.

Format: date-based versions. Each entry lists new data added, corrections, and documentation changes.

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
