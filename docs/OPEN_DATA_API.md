# Saudi Open Data Portal — API Reference & Download Guide

**Portal:** https://open.data.gov.sa
**Last verified:** 2026-04-07

This documents what works, what's blocked, and how to reliably download datasets from the Saudi National Open Data Platform.

---

## API Endpoints

### 1. Organization Datasets (works)

List all datasets for an organization.

```
GET https://open.data.gov.sa/data/api/organizations?version=-1&organization={org_name_ar_urlencoded}
```

**Example (MOJ):**
```
GET https://open.data.gov.sa/data/api/organizations?version=-1&organization=%D9%88%D8%B2%D8%A7%D8%B1%D8%A9%20%D8%A7%D9%84%D8%B9%D8%AF%D9%84
```

**Returns:** JSON with `datasets` array. Each dataset has `id`, `title`, `titleAr`, `organization`.

**MOJ org ID:** `35c63412-c4ae-4303-8fef-56cfd71303cf`

---

### 2. Dataset Detail (works — primary method for getting download URLs)

Get full dataset metadata including resource URLs.

```
GET https://open.data.gov.sa/api/datasets/{dataset_id}
```

**Returns:** JSON with `resources` array. Each resource has:
- `id` — resource UUID
- `name` — filename without extension (e.g., `Doc Attorney CSV`)
- `format` — file type (`CSV`, `XLSX`, `JSON`, `XML`)
- `url` — **relative path** for the odp-public download URL

**The `url` field is the key.** It gives the exact path with correct casing:
```
ORG_ID/DATASET_ID/v1/filename.ext
```

**Important:** Casing varies between datasets. Some use uppercase IDs (`35C63412-...`), some lowercase (`35c63412-...`). The filenames also vary (`docattorney_2023_04.csv` vs `Doc Attorney CSV.csv`). Always use the exact value from this API.

---

### 3. Dataset Resources API (works but unreliable)

```
GET https://open.data.gov.sa/data/api/datasets/resources?version=-1&dataset={dataset_id}
```

**Returns:** JSON array of resources with `id`, `format`, `name`.

**Caveats:**
- Returns empty JSON for ~5% of datasets (portal bug, not rate limiting)
- Sometimes returns resources from the wrong dataset (observed: asked for Aug 2023, got Apr 2023)
- Does NOT return the `url` field — only the resource ID
- Use the Dataset Detail API (endpoint 2) instead when possible

---

### 4. File Download via odp-public (works — WAF-immune)

Direct file access from the portal's static storage.

```
GET https://open.data.gov.sa/odp-public/{url_path_from_detail_api}
```

Construct by taking the `url` field from the Dataset Detail API and prepending the base:
```python
full_url = f"https://open.data.gov.sa/odp-public/{resource['url']}"
# URL-encode the filename part if it contains spaces
```

**This is the only reliable download method.** It serves files directly from storage without passing through the WAF.

---

### 5. ~~File Download via API~~ (WAF-BLOCKED — do not use)

```
GET https://open.data.gov.sa/data/api/datasets/resources/download/{resource_id}
```

**Status:** Permanently blocked by WAF (IP-based, not User-Agent-based).
- Returns 200 with HTML body: `<html><head><title>Request Rejected</title></head>...`
- Blocking is IP-based: same machine blocked regardless of browser, headers, or cookies
- Real Chromium browser also blocked (verified with Playwright)
- WAF does not reset after hours — appears to be a permanent policy on this endpoint

**Do not use this endpoint.** Use odp-public (endpoint 4) instead.

---

## Recommended Download Strategy

```python
# 1. Get dataset list
datasets = fetch_json(f"{ORG_API}?organization=وزارة العدل")

# 2. For each dataset, get exact resource URLs
for ds in datasets:
    detail = fetch_json(f"https://open.data.gov.sa/api/datasets/{ds['id']}")
    for resource in detail['resources']:
        if resource['format'] == 'CSV':
            url_path = resource['url']
            # URL-encode filename (may have spaces)
            parts = url_path.split('/')
            parts[-1] = urllib.parse.quote(parts[-1])
            download_url = f"https://open.data.gov.sa/odp-public/{'/'.join(parts)}"
            # 3. Download
            data = fetch(download_url)
```

**Rate limiting:** No explicit rate limit on odp-public, but add 2-3s delay between requests as courtesy. The metadata APIs also have no observed rate limiting.

---

## Casing Rules (discovered Apr 2026)

| File age | Org/Dataset ID casing | Filename casing |
|----------|-----------------------|-----------------|
| 2023 and earlier | UPPERCASE (`35C63412-...`) | lowercase (`docattorney_2023_04.csv`) |
| 2024-2025 | lowercase (`35c63412-...`) | Mixed case (`Doc Attorney CSV.csv`, `Total number of deeds transactions CSV.csv`) |
| Varies | Inconsistent | Always check the Dataset Detail API for exact casing |

**Rule:** Never guess the casing. Always use the `url` field from the Dataset Detail API verbatim.

---

## Known Portal Bugs

1. **Resources API returns wrong dataset's resources** — Observed for POA 2023 datasets. Asked for Aug 2023, got Apr 2023 resources. Use Dataset Detail API instead.

2. **Some datasets have no uploaded CSV** — The dataset entry exists (has ID, title, dates) but no CSV was ever uploaded. The Dataset Detail API returns an empty `resources` array or the `url` field is empty/missing. Examples: Monthly-Ops Jan 2024, Oct 2024; Compensation-Ruins Q2 2025; Property-Identity Q2 2025 (known 0-byte file).

3. **Resources API returns empty JSON for valid datasets** — ~5% of datasets return `{}` or `[]` from the resources endpoint. The datasets are valid and have downloadable files — the resources metadata just wasn't populated. The Dataset Detail API usually works for these.

4. **Inconsistent date coverage** — Some quarterly datasets exist for Q1-Q3 but not Q4 (or vice versa). No pattern — appears to be publishing delays or errors. Check periodically.

---

## Endpoint Summary

| Endpoint | Status | Use for |
|----------|--------|---------|
| `/data/api/organizations?organization=...` | Working | List all datasets for an org |
| `/api/datasets/{id}` | Working | Get resource URLs (primary) |
| `/data/api/datasets/resources?dataset=...` | Unreliable | Fallback metadata only |
| `/odp-public/{path}` | Working | **Download files** (WAF-immune) |
| `/data/api/datasets/resources/download/{id}` | **BLOCKED** | Do not use |

---

## Testing Checklist

When verifying API health, test in this order:

```bash
# 1. Can we list datasets?
curl -s "https://open.data.gov.sa/data/api/organizations?version=-1&organization=%D9%88%D8%B2%D8%A7%D8%B1%D8%A9%20%D8%A7%D9%84%D8%B9%D8%AF%D9%84" | python3 -m json.tool | head -5

# 2. Can we get dataset details?
curl -s "https://open.data.gov.sa/api/datasets/596f7335-afa5-4cb3-80a3-a1a67b947c35" | python3 -m json.tool | head -20

# 3. Can we download via odp-public?
curl -sI "https://open.data.gov.sa/odp-public/35c63412-c4ae-4303-8fef-56cfd71303cf/596f7335-afa5-4cb3-80a3-a1a67b947c35/v1/Transactions%20sale%20for%20real%20estate%20CSV.csv" | head -5

# 4. Is the download API still blocked?
curl -s "https://open.data.gov.sa/data/api/datasets/resources/download/ce73fbce-c63b-409a-9562-68324ec8e51c" | head -1
# Expected: <html><head><title>Request Rejected</title>...
```
