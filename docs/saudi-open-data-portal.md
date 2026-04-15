# Saudi Open Data Portal — Field Notes & Playbook

**Portal:** `https://open.data.gov.sa`
**Operator:** National Data Management Office (NDMO) / Saudi Data & AI Authority (SDAIA)
**Last verified:** 2026-04-11

Everything in this document is operational knowledge we paid real debug time to learn. **Read before touching any script that talks to this portal.** Do not downgrade or skip steps "because it sometimes works without them" — the portal blocks aggressively and recovery is hard.

---

## 1. WAF / Anti-bot — Working Client Profile

The portal uses a WAF (cookie fingerprint `BPfffdc833146`, `BP407814ff`, `dm2`) that blocks:
- Bare `curl` (WAF rejects with HTML "Request Rejected")
- `python-httpx` default User-Agent (same rejection)
- Python `urllib` with default UA (same rejection)
- Requests without a portal cookie session (returns "Request Rejected" on data endpoints)

**Always use the full stealth bundle from the very first request. Never probe with a minimal client.**

### Canonical working client (Python 3)

```python
import urllib.request, urllib.parse, http.cookiejar

def make_portal_client():
    cj = http.cookiejar.CookieJar()
    opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
    opener.addheaders = [
        ("User-Agent", "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
                       "AppleWebKit/605.1.15 (KHTML, like Gecko) "
                       "Version/17.0 Safari/605.1.15"),
        ("Accept", "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"),
        ("Accept-Language", "en-US,en;q=0.9"),
        ("Referer", "https://open.data.gov.sa/"),
    ]
    # Warmup — collects the three WAF cookies before any data request
    opener.open("https://open.data.gov.sa/en", timeout=20).read(500)
    return opener, cj
```

After warmup, the jar contains `dm2`, `BPfffdc833146`, `BP407814ff`. All downstream requests on the same opener inherit them and are waved through.

### What NOT to do

- **Don't use `curl` or `httpx` with default UA** — both are WAF'd even with the right Referer. Python `urllib` with browser UA is the known-good client.
- **Don't skip the warmup.** A first-request data fetch without the session cookies returns 13-byte "Request Rejected" HTML. You'll think the file is dead when it isn't.
- **Don't open a new opener per file.** Reuse one opener for the entire script so the cookies persist. New opener = new warmup = more WAF exposure.
- **Don't use `dangerouslyDisable` tricks, aggressive sleeps, or proxies.** The working client is cheap; deviation risks a permanent block.

---

## 2. Dataset Discovery API

### Org → datasets list

```
GET https://open.data.gov.sa/data/api/organizations/list/datasets?version=-1&organization={ORG_ID}&page=0&size=500
```

Returns `{ "datasets": [...] }`. Each dataset has `datasetId`, `titleAr`, `titleEn`, `resourceCount`, etc. **Titles are Arabic-first** — `titleEn` is often missing, placeholder, or wrong.

Known org IDs:
- MOJ (Ministry of Justice): `35c63412-c4ae-4303-8fef-56cfd71303cf`
- MOMAH / Housing Ministry: see monitor for current URL (changes occasionally)

### Dataset → resources list (what the monitor uses)

```
GET https://open.data.gov.sa/data/api/datasets/resources?version=-1&dataset={DATASET_ID}
```

Returns `{ "resources": [...] }`. Each resource has:
- `id` — resource UUID
- `name` — human-readable name (frequently a **generic placeholder** like `"Doc Attorney CSV"` or `"Total number of deeds transactions CSV"` reused across dozens of datasets — see §4)
- `format` — `CSV`, `XLSX`, `JSON`, `XML`
- `downloadUrl` — **use this directly** (see §3)
- `url` — usually empty, do not use

**Flakiness:** this endpoint is intermittently flaky and returns non-JSON on ~10-15% of calls. Retry 3× with 2-3s backoff. The flakiness is server-side, not a stealth problem.

### Dataset detail API (used by downloader)

```
GET https://open.data.gov.sa/api/datasets/{DATASET_ID}
```

Returns full metadata including `descriptionAr`, `descriptionEn`, `publisherId`, created/updated timestamps, and `resources` array. Same `downloadUrl` field as above.

---

## 3. Download URLs — Trust `downloadUrl`, Encode Spaces

The `downloadUrl` field on each resource points at the real odp-public blob path. **Example:**

```
https://open.data.gov.sa/odp-public/35C63412-C4AE-4303-8FEF-56CFD71303CF/16CB6B42-0411-480D-9145-8485F86B85D2/v1/attorney-in-2018-2019-2020-2021.csv
```

Structure: `/odp-public/{ORG_ID}/{DATASET_ID}/v{N}/{filename}`. Org and dataset IDs are always **UPPERCASE** in the blob path. Version prefix is `/v1/` for most files, occasionally `/v2/` for re-published resources.

### **CRITICAL: URL-encode path segments**

As of 2026-04-11 many new files are published with **spaces in the filename** — e.g. `Doc Attorney CSV.csv`, `Total number of deeds transactions CSV.csv`, `Total number of annulments CSV.csv`. These generic placeholder names are reused across dozens of unrelated datasets (see §4).

Python's `urllib.request.Request` raises `URL can't contain control characters` on spaces. You must quote the path before opening it:

```python
def encode_url(u):
    p = urllib.parse.urlsplit(u)
    path = "/".join(urllib.parse.quote(seg, safe="") for seg in p.path.split("/"))
    return urllib.parse.urlunsplit((p.scheme, p.netloc, path, p.query, p.fragment))
```

**Do NOT** reconstruct URLs yourself from the Arabic title. The downloader historically tried `odp-public/.../Attorney%20in%202018-2019-2020-2021.csv` but the real filename is `attorney-in-2018-2019-2020-2021.csv` (lowercase, hyphens). Always take the URL from the API and just encode it.

### Data-withdrawal sentinel

If the portal has removed a file but the URL is still live, it returns **13 bytes** exactly: `NO DATA FOUND`. Treat this as a hard miss — the resource was pulled. Capture this in the monitor's opportunistic-capture logic so we can distinguish "file gone" from "network failure" and not retry.

```python
if data.strip() == b"NO DATA FOUND":
    # file withdrawn, skip permanently
```

---

## 4. Generic Placeholder Filenames — Portal-Wide Pattern

**Discovered 2026-04-11.** For the most recent wave of MOJ datasets (hundreds of POA sub-categories, Power of Attorney, Total deeds transactions, annulments), the portal publishes every resource with one of ~5 generic placeholder names:

- `Doc Attorney CSV.csv` / `Doc Attorney Excel.xlsx`
- `Total number of deeds transactions CSV.csv` / `...Excel.xlsx`
- `Total number of annulments CSV.csv` / `...Excel.xlsx`

These names are **reused across dozens of unrelated datasets**. The uniqueness is in the `{DATASET_ID}` UUID segment of the URL path, not the filename. Two consequences:

1. **You cannot deduplicate by filename.** Always key on `{dataset_id, format}` or `{dataset_id, resource_id}`.
2. **The local filename has to be derived from the dataset title**, not the resource name. When saving locally, map the Arabic title to a meaningful English slug (see `scripts/download_new_data.py` CATEGORY_MAP for the MOJ real-estate and POA patterns).

This is why the downloader's old strategy of guessing filenames from titles fails: the *remote* filename is generic, but the *local* filename must be descriptive. You need both pieces.

---

## 5. Flaky Endpoints — Retry Policy

| Endpoint | Failure mode | Policy |
|---|---|---|
| `/data/api/datasets/resources` | JSON decode error | Retry 3×, backoff 2s, 3s, 4s |
| `/api/datasets/{id}` | Intermittent 5xx | Retry 3×, backoff 2s |
| `/odp-public/.../file.csv` | WAF "Request Rejected" | Almost always means stealth downgraded — verify warmup done, don't retry harder |
| `/odp-public/.../file.csv` | `NO DATA FOUND` | Do NOT retry — the file was withdrawn, mark permanently |
| `/odp-public/.../file.csv` | HTTP 404 | Check UPPERCASE vs lowercase path, then give up |

Rate-limit: **1 request per 300ms is safe**. `time.sleep(0.3)` between dataset probes was sustained for 86 requests without triggering anything. Don't push faster without testing.

---

## 6. Known Dataset Categories (MOJ Org)

For the `MOJ_ORG_ID = 35c63412-c4ae-4303-8fef-56cfd71303cf` organisation:

- **Sales transactions (`العمليات العقارية المسجلة في {category}`)** — quarterly per category. Categories enumerated in `scripts/download_new_data.py :: CATEGORY_MAP`. Save to `moj/real-estate/`.
- **Monthly operations (`العمليات العقارية المسجلة {YYYY} {month}`)** — aggregate deed counts per month. Save to `moj/monthly/` as `MOJ-Sales-{YYYY}-{MM}.csv`.
- **POA issued (`الوكالات الصادرة {YYYY} {month}`)** — monthly. Save to `moj/monthly/MOJ-POA-Issued-{YYYY}-{MM}.csv`.
- **POA sub-category (`الوكالات الصادرة في {sub} {YYYY} الربع {q}`)** — quarterly, many sub-categories (courts, banks, insurance, government, real estate, fuel, etc.). RE-adjacent ones go to `moj/real-estate/`, rest are non-RE and should be skipped by the downloader.
- **POA annulled / dissolved (`الوكالات المفسوخة`)** — monthly. Save to `moj/monthly/MOJ-POA-Annulled-{YYYY}-{MM}.csv`.
- **Declarations (`الإقرارات`)** — annual or historical bundle. Save with full year range in the filename.
- **Historical REGA bundles (`المؤشر العقاري للمدن في عام 2018 ،2019 ،2020 ،2021`)** — multi-year historical aggregates. Save to `rega/` or `moj/real-estate/`.

The CATEGORY_MAP in `download_new_data.py` has 40+ entries covering all the known sub-categories. When adding a new category, **extend the map** — don't rename files post-download.

---

## 7. Monitor Integration Gotchas

The `monitor/re_data_monitor.py` script has an opportunistic-capture path (`_try_capture_resource`) that tries to grab files at discovery time. As of 2026-04-11 it had bugs:

1. It was reconstructing URLs manually instead of using the API's `downloadUrl` field directly.
2. It did not URL-encode spaces, so the new generic-placeholder files (`Doc Attorney CSV.csv` etc.) all failed with "URL can't contain control characters".
3. It did not do a warmup GET, so the first request hit the WAF and returned 13-byte "Request Rejected" HTML which the code happened to filter but did not log.

**Lesson:** every new codepath to the portal must be reviewed against this playbook. Do not write new clients — import the shared helper from `monitor/portal_client.py` (TODO: factor out the shared `make_portal_client()` + `encode_url()` helpers).

---

## 8. Real Findings Log

| Date | What we learned |
|---|---|
| 2026-03-12 | Initial monitor run tracked 495 datasets, 792 resources across MOJ+REGA+GASTAT+NHC. |
| 2026-03-27 | Discovered WAF blocks curl + httpx default UA. Browser UA + Referer in Python urllib works. Documented in project web-extraction pitfalls notes. |
| 2026-04-07 | Monitor discovered 180 new resources (3 new datasets). Opportunistic capture silently failed — no files saved. |
| 2026-04-11 | Root-caused the capture failure: (a) wrong URL source field, (b) no URL-encoding of spaces in generic placeholder filenames, (c) no warmup. Retry with full stealth bundle recovered **73 of 86** Apr-7 datasets as live and downloadable, totalling hundreds of MB of POA + deed transaction data. Only 13 failed — all to flaky `/data/api/datasets/resources` endpoint, recoverable via retry. |
| 2026-04-11 | Learned the generic-placeholder-filename pattern — `Doc Attorney CSV.csv` etc. reused across dozens of datasets, uniqueness lives in the UUID path segment only. |
