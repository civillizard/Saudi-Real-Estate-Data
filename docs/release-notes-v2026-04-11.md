# v2026-04-11 — Opportunistic Recovery + Portal Client Hardening

**Release date:** 2026-04-11
**Scope:** 138 recovered files (~1.5M new rows), reclassified into proper
English-slug taxonomy, plus a new shared portal client, a full Saudi Open
Data portal playbook, and a fix for the monitor's broken opportunistic-capture
path that had been silently dropping discoveries.

## TL;DR

- **Net data:** 312 → 360 CSVs + 85 XLSX siblings, 7.48M → 9.49M rows, ~+200 MB on disk.
- **New taxonomy:** `moj/poa-other/` for 38 non-RE Power-of-Attorney
  sub-categories that don't fit the real-estate buckets (courts, banks,
  traffic, commerce, foreign affairs, universities, civil status, …).
- **New data in existing taxonomy:** 5 monthly `MOJ-POA-Annulled-*` files,
  plus XLSX siblings alongside 22 pre-existing REGA/MOJ quarterlies.
- **New infrastructure:** shared portal client, reusable recovery
  downloader with byte-exact dedup, monitor capture fix, full portal
  playbook, audit-methodology rule for future sample-based decisions.

## How this release came to be

The monitor runs on a cron and scans the Saudi Open Data portal for new
datasets every few days. Its Apr 7 run found 180 new resources across 3 new
datasets — but the "opportunistic capture" path that was supposed to save
them on the spot silently failed and zero files were captured.

When I went to download them 4 days later, the usual `scripts/download_new_data.py`
reported 10 files as 404 and 235 files as "unrecognised". Digging in
revealed three overlapping root causes:

1. **URL encoding.** The portal has started publishing files with **spaces
   in the filename** — reusing generic placeholder names like
   `Doc Attorney CSV.csv` and `Total number of deeds transactions CSV.csv`
   across dozens of different datasets. Python's urllib refuses URLs with
   control characters, so every download that should have worked failed
   with an obscure exception.

2. **Wrong source field.** The downloader was using the `url` field from
   the dataset detail API and reconstructing paths by hand, instead of
   using the `downloadUrl` field the API provides ready-made. The
   reconstructed URLs mostly 404'd because the portal's real filenames no
   longer match the Arabic title slugs.

3. **WAF warmup.** Direct calls to the odp-public blob host get rejected by
   the portal's WAF ("Request Rejected" HTML) unless the client has first
   collected `dm2`, `BPfffdc833146`, and `BP407814ff` session cookies via a
   GET to `https://open.data.gov.sa/en`. Without the warmup, every download
   looks dead even when the file is live.

Once I fixed all three at once — using the full stealth bundle from request
one, not a minimal probe that escalates on failure — the recovery sweep
pulled **130 files on the first pass** and **8 more on a slower retry** out
of 86 candidate datasets. Only 4 POA files from Aug-Sep 2023 remain
unreachable, and those return 404 directly at the portal-advertised
downloadUrl — a portal-side inconsistency we can't fix client-side.

## What's new — data

### `moj/poa-other/` (NEW directory, 38 × CSV + XLSX = 76 files)

Non-RE Power-of-Attorney quarterly sub-categories. Each is a standalone
dataset published by MOJ under `الوكالات الصادرة في {جهة}`. Schema is the
standard 6-column POA layout (`region, city, sector_type, service_type,
gregorian_date, reference_number`).

Agricultural-Dev-Fund, Agricultural-Grants, Banks (Q2+Q3),
Boat-Fishing-Licenses, Civil-Affairs, Claims-Courts (Q2+Q4),
Commercial-Records (Q3+Q4), Companies (Q2+Q3), Compensation-Aid,
Court-Completions, Foreign-POA-Attest (Q2+Q3), Gov-Authorities (Q1+Q2),
Gov-Institutions (Q2+Q4), Housing-Grants (Q1+Q3), Labor-Recruitment,
Municipalities, Post (Q2+Q3), Recruitment-Office, Salaries-Dues,
Service-Requests, Social-Dev-Bank (Q2+Q4), Social-Security,
Telecom-Companies, Traffic (Q1+Q3+Q4), University-Rewards, Vehicles.

### `moj/monthly/` additions

- **MOJ-POA-Annulled-*** — 5 new monthly files (2024-02, 2025-01, 2025-02,
  2025-11, 2026-02). Schema is 8-column (adds `dissolution_type` +
  `hijri_date` to the base POA layout).
- **MOJ-POA-Issued-*** — 6 new XLSX siblings for existing CSVs
  (2024-01, 2024-06, 2024-09, 2025-05, 2025-10, 2026-02).
- **MOJ-Monthly-Operations-*** — 8 new XLSX siblings for existing CSVs
  (2024-05, 2024-11, 2025-06, 2025-07, 2025-09, 2025-10, 2025-11, 2026-01).

### `moj/real-estate/` additions

14 new XLSX siblings for existing quarterly sub-categories:
Compensation, Compensation-Ruins, Deed-Define-Divide, Divide,
Grant-Alternative, Merge-Deed (Q2–Q4), Mortgage-Release, Ownership,
POA-Ejar (Q2+Q3), POA-RE-Fund, Transfers.

### `moj/sales/` additions

- **MOJ-RE-Index-Cities-2018-2021.xlsx**
- **MOJ-RE-Index-Districts-2018-2021.xlsx**

### `rega/` additions

11 new XLSX siblings for existing REGA regional quarterlies — the portal
re-published these datasets under new Arabic names but the CSV bytes were
identical to what we already had. The XLSX copies are new.

## What's new — tools

### `scripts/portal_client.py` — shared Saudi Open Data client

One place for the working stealth bundle. Every script that talks to the
portal must import from here instead of rolling its own HTTP client.
Features:

- Safari User-Agent + Arabic-friendly Accept headers + portal Referer
- `http.cookiejar.CookieJar` warmed up via GET to `/en`
- Per-segment URL encoding so spaces in portal filenames don't crash urllib
- `downloadUrl` field used directly instead of reconstructed from titles
- `NO DATA FOUND` (13-byte portal sentinel) raised as `DataWithdrawn`
- `Request Rejected` HTML raised as `WAFBlocked`
- `fetch_json`/`fetch_bytes` wrappers with exponential-backoff retry for
  the flaky `/data/api/datasets/resources` endpoint

### `scripts/grab_new_findings.py` — recovery downloader

Sweeps `monitor/monitor_state.db` for datasets first seen after a given
date and downloads them opportunistically. Key features:

- Uses the shared portal client (full stealth from request 1)
- Maps Arabic titles through `parse_dataset()` for known RE categories,
  falls back to `moj/opportunistic/` with a slug for unknown ones
- **Byte-exact dedup**: builds a repo-wide MD5 index at startup and skips
  any download whose content hash matches an existing file. Protects
  against the portal re-publishing the same dataset under new Arabic
  slugs (exactly what happened with the 11 REGA indicators in this
  release). `--no-dedup` to override.
- Idempotent: already-on-disk files skipped, dedup matches logged as
  `DUP` so a re-run is safe.

### `scripts/reclassify_opportunistic.py` — staging → canonical mover

One-shot script to move files out of the `moj/opportunistic/` staging
directory into proper English-slug paths under `moj/poa-other/`,
`moj/monthly/`, or `rega/`. Contains the Arabic→English slug tables for
POA sub-categories, months, quarters, and regions. Uses `git mv` so the
rename is tracked. Run `--dry-run` first.

### `monitor/re_data_monitor.py` — capture fix

`_try_capture_resource()` now delegates to the shared portal client. The
previous implementation was broken in the exact three ways listed above:
reconstructed URLs, no URL encoding, no warmup. Apr 7 run captured zero
files as a result. After this fix, the monitor's own opportunistic capture
path is expected to succeed at the discovery step so we don't rely on
post-hoc recovery runs.

### `scripts/build_registry.py` — exclusions added

- `kapsarc/KAPSARC-Building-Permits.csv` (1.7 GB, gitignored) excluded —
  previously tanked registry build time for a file that doesn't ship.
- Derived `data/registry_*.csv` files excluded — would be circular.

## What's new — documentation

### `docs/saudi-open-data-portal.md` — portal playbook

Full operational knowledge of the Saudi Open Data portal, captured in one
place so future scripts don't re-learn it the hard way:

- Working client profile (exact headers, cookies, warmup URL)
- What NOT to do (minimal clients, new openers per file, skipping warmup)
- Dataset/resource API endpoints + known flakiness rates
- Download URL structure + URL-encoding rules
- NO DATA FOUND sentinel handling
- The generic placeholder filename pattern (Doc Attorney CSV.csv etc.)
- Retry policy per endpoint
- Historical findings log

**Read this before writing any new portal code.**

## Breaking changes

None. Existing files under `moj/sales/`, `moj/real-estate/`, `moj/monthly/`,
and `rega/` keep their canonical names. The only rename is internal — the
`moj/opportunistic/` staging directory was fully drained and removed as
part of this release; its contents live in their permanent homes now.

## Known issues

- **4 POA files unreachable.** `الوكالات الصادرة 2023 - أغسطس` and
  `الوكالات الصادرة 2023 - سبتمبر` (× CSV and XLSX each) return HTTP 404
  at the portal-advertised `downloadUrl`. Portal-side inconsistency, not a
  client bug. Tracked for a later re-sweep if the portal republishes.

- **gastat/REPI + KAPSARC/SAMA files classified as UNKNOWN.** The registry
  builder's classification rules don't yet have patterns for these. They
  exist on disk but show as `UNKNOWN/unknown` in `registry.db`. Follow-up
  work, low priority.

- **Registry build time.** Scanning + row-counting the full 361-file
  corpus takes ~3 minutes on macOS-over-iCloud. Acceptable for release
  prep; will be revisited if it becomes routine.

## Credit / process

This release exists because the Apr 7 monitor capture failure didn't just
disappear — it was investigated, root-caused, and turned into durable
infrastructure + a full playbook so the same class of silent failure
can't happen again. The fix was staged: recover first, understand second,
document third, commit in logical groups, then tag.

Rule of the release: **never probe a protected source with minimal
headers and escalate on failure**. One permanent block from a throwaway
probe is far worse than 10 extra lines of stealth upfront. This lesson is
now encoded in `~/.claude/projects/-Users-mao/memory/feedback_stealth_full_from_start.md`
and in the "Always use full stealth from the first request" section of
the portal playbook.
