# v2026-04-28 — REGA Monthly Bulletins (5 PDFs + parsed timeseries)

**Release date:** 2026-04-28
**Scope:** First inclusion of REGA's published monthly bulletins and quarterly indicator reports as a first-class data source. 5 PDFs (24.2 MB) plus a 108-row parsed timeseries CSV with the headline sales indicators in machine-readable form.

## TL;DR

- **5 PDFs** under new `rega/bulletins/pdfs/`:
  - 3 monthly bulletins (Jan / Feb / Mar 2026)
  - 2 quarterly indicators reports (Jan / Feb 2026)
- **`rega/bulletins/rega_bulletin_timeseries.csv`** — 108 rows × 14 columns, parsed from the bulletins. Sales transaction count, sales value, MoM and YoY percentages, broken out by region and segment (residential vs non-residential).
- **No change to existing CSVs.** The 9.49M-row consolidated dataset stays exactly as it was in v2026-04-11.

## What's in the bulletins

REGA — Saudi Arabia's Real Estate General Authority — publishes a monthly bulletin (النشرة الشهرية للسوق العقاري) and a quarterly indicators report (تقرير مؤشرات القطاع العقاري) summarising sales activity, price indicators, and rental movement across the Kingdom.

These have been the canonical aggregate view of the Saudi real estate market for several years, but they're only available as PDFs on the REGA media library — not in the existing Open Data portal where the per-transaction CSVs come from. Including them here closes that gap: now a single repo carries both the granular transaction data AND the official aggregate commentary REGA publishes against it.

### Bulletin contents (typical)

- **Sales transactions** by region (Riyadh, Makkah, Madinah, Eastern Province, etc.), broken out residential vs. non-residential, with month-over-month and year-over-year change.
- **Sales value totals** in SAR, same regional and segment breakdown.
- **Top regions / cities by activity.**
- **Brief market commentary** (Arabic) on quarterly trends.

The quarterly indicators reports are larger (6-13 MB) because they include geographic detail and chart-heavy historical context that the monthly bulletins skip.

## The parsed timeseries

`rega/bulletins/rega_bulletin_timeseries.csv` extracts the headline indicators from the 5 PDFs into a flat table for easy analysis:

```
month, publication_date, section, indicator, segment, sub_type,
region, region_rank, metric, value, unit, mom_pct, yoy_pct, source_pdf
```

Sample rows:

| month | section | indicator | segment | metric | value | unit | mom_pct | yoy_pct |
|---|---|---|---|---|---|---|---|---|
| 2026-03 | sales | txn_count | residential | txn_count | 14,222 | count | -22 | -52 |
| 2026-03 | sales | txn_value | residential | txn_value | 12,032,001,214 | SAR | -18 | -67 |
| 2026-03 | sales | txn_count | non_residential | txn_count | 1,500 | count | -30 | -52 |

Coverage is currently the headline figures only (national totals + regional sales transactions). A deeper pass extracting every indicator the bulletins publish (rental, price indicators, district-level breakdowns) is planned for a later release.

## File index

| Path | Size | Description |
|---|---|---|
| `rega/bulletins/pdfs/2026-01-monthly-bulletin.pdf` | 1.9 MB | January 2026 monthly bulletin |
| `rega/bulletins/pdfs/2026-02-monthly-bulletin.pdf` | 1.7 MB | February 2026 monthly bulletin |
| `rega/bulletins/pdfs/2026-03-monthly-bulletin.pdf` | 1.7 MB | March 2026 monthly bulletin |
| `rega/bulletins/pdfs/2026-01-indicators-report.pdf` | 13.8 MB | January 2026 quarterly indicators report |
| `rega/bulletins/pdfs/2026-02-indicators-report.pdf` | 6.5 MB | February 2026 indicators report |
| `rega/bulletins/rega_bulletin_timeseries.csv` | 13 KB | Parsed timeseries (108 rows × 14 cols) |

## Source authority

All PDFs are published primary sources from REGA's media library on rega.gov.sa. They are reproduced here under the same access terms REGA uses for its public bulletins (free public distribution as official statistics). No alteration was made to the PDF files themselves.

The parsed timeseries CSV is a derivative work of the PDFs — the values come directly from the bulletin tables; only the format has been changed (Arabic table → flat CSV with English column names) for analytic accessibility.

## Roadmap

- **Forward bulletins** — REGA publishes monthly. Future releases will batch in 3-6 months at a time.
- **Backfill** — older bulletins (2024, 2025) exist on the REGA media library and could be added in a follow-up release.
- **Deeper extraction** — the timeseries currently covers headline numbers only. Rental indicators, price indicators by district, and the chart-heavy figures from the quarterly reports could all be parsed and added.
