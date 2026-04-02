# Saudi Real Estate API Research

<p align="center">
  <a href="https://www.6ra3.com/track/r/rega-site-api-research?dest=https://rega.gov.sa"><img src="https://www.6ra3.com/track/rega/api-research" height="50" alt="REGA - Real Estate General Authority (الهيئة العامة للعقار)"></a>
  &nbsp;&nbsp;&nbsp;&nbsp;
  <a href="https://www.6ra3.com/track/r/moj-site-api-research?dest=https://moj.gov.sa"><img src="https://www.6ra3.com/track/moj/api-research" height="50" alt="MOJ - Ministry of Justice (وزارة العدل)"></a>
</p>

Researched: 2026-03-12
Purpose: Identify APIs that can enrich **Ministry of Justice (MOJ; وزارة العدل)** / **Real Estate General Authority (REGA; الهيئة العامة للعقار)** open data analysis in `this repository`.

---

## Summary

| Tier | Source | Relevance |
|------|--------|-----------|
| HIGH | Wathq — Real Estate Deeds API | Property-level deed lookup by serial number |
| HIGH | National Address API (api.address.gov.sa) | Geocoding / lat-long for any address or short code |
| HIGH | KAPSARC Data Portal | Real estate price index timeseries, bulk download + API |
| HIGH | SAMA Open Data Portal | Mortgage volume, lending stats, quarterly download |
| HIGH | Etimad Developer Portal | Construction/real estate procurement tenders |
| MEDIUM | Saudi National Data Bank (data.gov.sa) CKAN | 11K+ datasets, includes MOJ + **Ministry of Municipal, Rural Affairs and Housing (MOMAH; وزارة الشؤون البلدية والقروية والإسكان)** open data |
| MEDIUM | REGA Geospatial Real Estate Portal | Interactive map; no public API but spatial layer data |
| MEDIUM | GASTAT / DataSaudi | Housing census, population, RPI quarterly PDFs |
| MEDIUM | SAMA Open Banking API | Mortgage/financing data with bank consent |
| MEDIUM | xMap.ai | Commercial enrichment: transaction geospatial dataset |
| LOW | Bayut KSA (unofficial API) | Listing prices, not transactional |
| LOW | Sakan (api.sakan.co) | Listing API, undocumented public access |
| LOW | Aqar.fm | No public API found |
| LOW | Monshaat Business Atlas | SME/sector indicators by region, no API docs |

---

## 1. Government APIs

### 1.1 Saudi National Data Bank — data.gov.sa (CKAN)

- **URL:** https://data.gov.sa/en
- **Developer docs:** https://data.gov.sa/en/developers
- **Authentication:** Open (CKAN API key optional for write; read is public)
- **Registration required:** No for read; account for API key
- **What's available:**
  - 11,439+ datasets from 230+ government entities
  - MOJ transaction data, MOMAH housing data, REGA indicators
  - Searchable by organization, tag, format
  - CKAN REST API: `data.gov.sa/api/3/action/...`
  - Standard CKAN endpoints: `package_list`, `package_search`, `resource_show`, `datastore_search`
  - Formats: CSV, JSON, XML, XLS
- **Rate limits:** Not published; CKAN standard applies
- **Cost:** Free
- **Notes:** This is the canonical aggregation point. MOJ already publishes open data here (see `moj.gov.sa/English/opendata`). Use `datastore_search` for streaming row-level access on datasets that support it. Not all datasets are in the datastore — some are file-only downloads.

---

### 1.2 Wathq Developer Portal — Real Estate Deeds API

- **URL:** https://developer.wathq.sa/en
- **API page:** https://developer.wathq.sa/en/api/13
- **Pricing:** https://developer.wathq.sa/en/Pricing
- **Authentication:** API key (subscription-based)
- **Registration required:** Yes — online account creation, then subscribe to a plan
- **What's available:**
  - **Real Estates Deeds** (API ID 13) — provided by MOJ. Returns deed serial number, property type, and related metadata from live MOJ database.
  - **National Address** (API ID 17) — address lookup
  - **Commercial Registration** — business entity data
  - Handles 20,000+ transactions/day across all services
- **Rate limits:**
  - Basic plan: 5 requests/second, prepaid per-transaction billing
  - Premium plan: 50–100 req/s (customizable), unlimited with premium support
- **Cost:** Paid per transaction (prepaid packages). VAT excluded. Check https://developer.wathq.sa/en/Pricing/page/prices/basic for per-call rates.
- **Notes:** This is the only programmatic way to query individual deed records from MOJ in real time. Useful for: verifying deed numbers in our dataset, resolving ambiguous property type codes, enriching records with live MOJ data. Integration latency: ~5 minutes to connect per docs.

---

### 1.3 National Address API — api.address.gov.sa

- **URL:** https://api.address.gov.sa/
- **Getting started:** https://api.address.gov.sa/gettingstarted
- **API reference:** https://api.address.gov.sa/apireference
- **Authentication:** Access token (subscription-based, generated in profile)
- **Registration required:** Yes — free registration on portal
- **What's available:**
  - Free-text address search
  - Geocode (lat/long → address)
  - Reverse geocode (address → lat/long)
  - Short address lookup (e.g. RJHH1234)
  - Address verification
  - Regions, cities, districts lists
  - Phone number → address
- **Rate limits:**
  - Starter package: 5 calls/minute, max 100 calls/week
  - Unlimited package: no rate cap
- **Cost:** Starter is likely free; Unlimited is paid (Saudi Post commercial tier)
- **Python wrappers:** `saudiaddress` on PyPI (`pip install saudiaddress`); also GitHub: `abduhbm/saudiaddress`
- **Notes:** Critical for geocoding our MOJ/REGA transaction records. MOJ data has district names but no coordinates. This API bridges that gap. The Starter tier (100 calls/week) is too low for batch enrichment — need Unlimited or a bulk approach. Also available through Wathq (API ID 17).

---

### 1.4 SAMA Open Data Portal — sama.gov.sa

- **URL:** https://www.sama.gov.sa/en-US/EconomicReports/pages/database.aspx
- **Authentication:** None (browse/download); API coming (announced but not yet live as of research date)
- **Registration required:** No for download
- **What's available:**
  - Mortgage lending statistics: new residential mortgages by quarter (e.g., Q3 2024: SAR 20.49B)
  - Real estate loan portfolio totals (SAR 226B+ reported in 2025)
  - Economic, monetary, financial indicators
  - Download formats: Excel, CSV (XML announced)
- **Rate limits:** N/A (file download)
- **Cost:** Free
- **Notes:** No live API yet — planned. For now, use scheduled CSV downloads. Most relevant dataset: "Real Estate Finance" under Banking Statistics. Good for cross-referencing transaction volumes in our MOJ data against credit cycle. Also see SAMA Open Banking (section 1.5) for bank-consented data.

---

### 1.5 SAMA Open Banking Framework

- **URL:** https://openbanking.sa/index-en.html
- **Framework docs:** https://sama.gov.sa/en-US/Documents/Open_Banking_Policy-EN.pdf
- **Authentication:** OAuth 2.0 (bank-consented, customer authorization required)
- **Registration required:** Yes — SAMA approval required for TPP (Third Party Provider) license
- **What's available:**
  - Phase 1 (live Q4 2023): Account Information Services — consolidated view of customer financial data
  - Phase 2 (live 2024): Payment Initiation Services
  - Future: Mortgage/property financing data (in roadmap under Open Finance expansion)
- **Cost:** Free framework; licensing has compliance costs
- **Notes:** Not directly useful for our dataset enrichment (requires per-customer consent). Relevant if building a consumer-facing product. Monitor for mortgage data phase.

---

### 1.6 GASTAT — General Authority for Statistics

- **URL:** https://stats.gov.sa/en/
- **DataSaudi platform:** https://datasaudi.sa/en
- **Authentication:** Open (downloads); DataSaudi has account for full API
- **Registration required:** Free account for DataSaudi API access
- **What's available:**
  - **Real Estate Price Index (RPI):** Quarterly, all 13 regions, by property type and sector. Published as PDF + dataset. Base year 2023. Uses AI + geospatial models.
  - **Housing & Population Census 2022:** District-level household counts, housing types, ownership rates
  - **Housing Survey Statistics:** Household dwelling characteristics
  - **DataSaudi:** Interactive economic/social data with API access for registered users
  - RPI Q3 2025: +1.3% annual (most recent as of research)
- **Rate limits:** Not published
- **Cost:** Free
- **Notes:** RPI data is available through KAPSARC Data Portal in a cleaner API format (see section 4.1). Census district data is critical for demand-side analysis — cross-reference with our MOJ transaction density by district.

---

### 1.7 MOJ — Real Estate Market Platform (SREM)

- **URL:** https://srem.moj.gov.sa
- **Authentication:** Nafath (National ID + Nafath app MFA) — citizen/resident login only
- **Registration required:** Yes — Saudi ID or Iqama + Nafath app
- **What's available:**
  - 4M+ property deeds database
  - Transaction history: value, location, price/sqm, area, date
  - All regions, all transaction types
  - Real-time monitoring of live transactions
- **API/bulk access:** None confirmed — portal is interactive only
- **Cost:** Free (citizen service)
- **Notes:** This is the most comprehensive transaction database, but it's behind Nafath authentication and has no public API. Our existing MOJ open data CSVs (4.96M rows in `this repository`) are the bulk-download version of this. Wathq's Real Estate Deeds API (section 1.2) provides programmatic deed lookup. For anything beyond that, direct MOJ data cooperation may be needed.

---

### 1.8 MOJ Open Data Page

- **URL:** https://www.moj.gov.sa/English/opendata/Pages/AdvantageOpenData.aspx
- **Authentication:** Open
- **What's available:**
  - Published datasets on the national data portal
  - Real estate transaction aggregates
  - Links to datasets on data.gov.sa
- **Notes:** The datasets we already use (`moj/`) come from here. Check periodically for new dataset additions or schema changes.

---

### 1.9 Etimad Developer Portal — Government Tenders API

- **URL:** https://apiportal.etimad.sa/en
- **Docs intro:** https://apiportal.etimad.sa/en/docs/introduction
- **Tenders Inquiry Service:** https://apiportal.etimad.sa/en/api_products/TendersInquiryService
- **Authentication:** API key (registration + approval required)
- **Registration required:** Yes — business entity registration with Etimad
- **What's available:**
  - Tenders Inquiry Service: query tender fields, filter by category/region
  - Government Contract Data Inquiry Service: existing and historical contract data
  - Construction/infrastructure tenders are filterable — real estate development contracts
- **Cost:** Subscription-based (pricing not public; contact Etimad)
- **Notes:** Useful for tracking real estate development pipeline — government-contracted construction projects signal future supply. Real estate tenders include housing projects, infrastructure, commercial development. Third-party alternative: TendersAlerts API (https://tendersalerts.com/en/tenders-api) — first third-party aggregator of Etimad data.

---

### 1.10 Balady Platform — Building Permits

- **URL:** https://balady.gov.sa/en
- **Authentication:** Nafath (citizen portal)
- **What's available:**
  - Building permit issuance (residential + commercial)
  - Building permit inquiry/status
  - Construction license data
- **API access:** None confirmed — citizen-facing portal only
- **Notes:** Building permit data would be valuable for leading indicator analysis (permits today → supply in 18-24 months). No public API found. Data may be published via data.gov.sa by MOMAH — check `data.gov.sa/organization/momah`. Alternatively, Wathq may add this in future (they partner with multiple ministries).

---

### 1.11 REGA Platforms

#### 1.11a Real Estate Indicators Platform
- **URL:** https://rega.gov.sa/en/rega-services/platforms/real-estate-indicators/
- **What's available:** Market indicators, sector dashboards
- **API:** None public — dashboard only
- **Notes:** Underlying data feeds into GASTAT RPI. No direct API.

#### 1.11b Geospatial Real Estate Portal
- **URL:** https://rega.gov.sa/en/rega-services/platforms/geospatial-real-estate-portal/
- **What's available:**
  - Interactive maps: regions, cities, neighborhoods, plots
  - POI layers: schools, hospitals, mosques, real estate offices
  - Off-plan sales projects
  - Brokerage office locations
- **API:** None public — web portal only
- **Notes:** Spatial data underlies this portal. REGA may share spatial datasets via data.gov.sa. Useful reference for building our own spatial enrichment layer.

#### 1.11c Real Estate Registry (RER)
- **URL:** https://rega.gov.sa/en/rega-services/platforms/real-estate-registry/
- **What's available:** National property identity registry (Aamal/RER)
- **API:** Not public — citizen/professional services only
- **Notes:** The RER assigns a unique property identity number (PIN) to each registered property. This is the key identifier linking deeds, valuations, and permits. No programmatic access without a license arrangement with REGA.

#### 1.11d Ejar Platform (Rental Contracts)
- **URL:** https://www.ejar.sa/en (REGA-operated)
- **What's available:** Rental contract registration, documentation, renewal
- **API:** Not public — no developer portal found
- **Notes:** Our existing Ejar Collector (in `~/rega-ejar-collector`) scrapes open data CSV exports from REGA's open data. Ejar open data is published on data.gov.sa with 104K+ rental rows in our DB. No live API. For more granular rental data, contact REGA directly for data partnership.

---

### 1.12 Taqeem — Saudi Authority for Accredited Valuers

- **URL:** https://taqeem.gov.sa/en
- **Qeem platform:** https://taqeem.gov.sa/en/sector/realEstate
- **Authentication:** Portal account
- **What's available:**
  - Accredited valuers directory (searchable)
  - Property valuation request submission (Qeem platform)
  - Valuation reports (per-property, by licensed firms)
- **API:** None public
- **Notes:** No programmatic access to assessed values. Valuation data stays with the requesting party. The valuers directory could be scraped as a reference dataset. For mass AVM (automated valuation model), third-party providers like xMap (section 5.2) are more practical.

---

### 1.13 GEOSA — General Authority for Survey and Geospatial Information

- **URL:** https://www.geosa.gov.sa/
- **National Geospatial Platform:** https://my.gov.sa/en/agencies/17408
- **Authentication:** Registration required for data layer access
- **What's available:**
  - National geodetic survey data
  - Topographic and hydrographic data
  - National Spatial Data Infrastructure (NSDI)
  - Geospatial data layers for registered users
- **API:** Exists (GIS-standard WMS/WFS likely) — registration required
- **Cost:** Free for government use; commercial licensing unclear
- **Notes:** Could provide parcel boundary geometries and coordinate systems for our transaction data. Worth registering to explore available layers.

---

### 1.14 Nafath — National Identity Verification

- **URL:** https://nafath.gov.sa
- **Developer integration docs:** Via Azakaw / third-party integration services
- **Authentication:** Government-issued integration credentials (requires **Saudi Data & AI Authority (SDAIA; الهيئة السعودية للبيانات والذكاء الاصطناعي)** approval)
- **What's available:**
  - Saudi National ID (NID) verification
  - Iqama (resident) verification
  - MFA for high-assurance flows
  - Returns government-verified personal information in real time
- **Use case for RE:** Identity verification in any property-linked service (brokers, developers, tenant verification via Ejar)
- **Notes:** Not useful for our offline dataset enrichment. Relevant only if building a consumer/professional-facing application.

---

### 1.15 MOMAH Open Data

- **URL:** https://momah.gov.sa/en/open-data
- **Authentication:** Open
- **What's available:**
  - Housing program data (Sakani)
  - Building permit statistics
  - Municipal services datasets
  - White Land Tax program data
  - Published on data.gov.sa
- **White Land portal:** https://idlelands.momah.gov.sa/ar (Riyadh rollout Oct 2025; tiered fees 2.5%–10% by zone)
- **Notes:** White Land Tax data could identify undeveloped urban plots — useful for supply constraint analysis. Registration deadline data from KPMG: Oct 30, 2025 for Riyadh Phase 1.

---

## 2. Semi-Government / Industry APIs

### 2.1 Wathq (see section 1.2 — fully covered above)

---

## 3. Commercial Data APIs

### 3.1 Bayut KSA — Real Estate Listings (Unofficial API)

- **Official API:** None for KSA (Bayut's official API on docs.bayutapi.com is UAE-only)
- **Unofficial/RapidAPI:** https://rapidapi.com/apidojo/api/bayut — UAE focused, not KSA
- **Bayut KSA app:** bayut.sa
- **Authentication:** N/A (no public API for KSA)
- **What's available (unofficial):** Properties, agencies, agents, transactions, floorplans — but UAE data only
- **Cost:** RapidAPI unofficial: free tier 750 calls/month
- **Notes:** No useful official API for Saudi Arabia data. Could scrape bayut.sa but ToS likely prohibits it. For listing data, Sakan or Aqar are better bets.

---

### 3.2 Sakan — Real Estate Platform

- **URL:** https://sakan.co / https://sa.sakan.co
- **API endpoint found:** https://api.sakan.co/en/project (existence confirmed; full docs not public)
- **Authentication:** Unclear — likely API key for partners
- **What's available:**
  - Property listings: buy/rent/vacation
  - Types: houses, apartments, offices, shops, land, villas, chalets
  - Multi-country (Saudi, UAE, Kuwait, etc.)
- **Notes:** The API endpoint `api.sakan.co` exists but no public developer docs found. Contact Sakan Business (sakan.co/en/about_us) for partnership API access. Could provide listing price benchmarks by district.

---

### 3.3 Aqar.fm — Saudi Real Estate Listings

- **URL:** https://sa.aqar.fm
- **API:** None public found
- **Scale:** 1.5M+ listings, 50M+ monthly visits, 21 categories
- **Authentication:** N/A
- **Notes:** No developer API. All listings require Nafath verification and REGA licensing. Could be scraped (check ToS) but no official programmatic access. Useful for listing price analysis if approached for a data partnership.

---

### 3.4 Google Maps Platform

- **URL:** https://mapsplatform.google.com
- **Authentication:** API key (Google Cloud account)
- **Registration required:** Yes — Google Cloud project + billing enabled
- **What's available:**
  - Places API: 200M+ global POIs with type, rating, hours, accessibility
  - Geocoding API: address → lat/long, lat/long → address
  - Maps JavaScript API + Static Maps
  - Distance Matrix, Directions
  - Places Insights in BigQuery: join your data with Google POI dataset
- **Rate limits:** Per-API, per-day quotas; generous free tier ($200/month credit)
- **Cost:** Pay-as-you-go; Geocoding: $5/1,000 requests; Places Details: $17/1,000; Nearby Search: $32/1,000
- **Notes:** Best-in-class geocoding for Saudi Arabia. Places data (schools, mosques, hospitals, malls) is a powerful enrichment layer for property value analysis. `Places Insights + BigQuery` could join our MOJ transaction data with neighborhood POI counts. Priority use: geocode MOJ transaction records (have district but no coordinates).

---

### 3.5 HERE Maps Geocoding API

- **URL:** https://developer.here.com
- **Authentication:** API key (free tier available)
- **What's available:**
  - Geocoding and address search
  - Short address (Saudi 4+4 format) support confirmed
  - Reverse geocoding
  - POI data
- **Cost:** Free tier: 250K transactions/month; paid beyond
- **Notes:** HERE specifically supports Saudi national short address format (documented in their blog post about Saudi 4-digit codes). Good alternative to Google for batch geocoding at lower cost. Relevant for geocoding our 4.96M row dataset.

---

### 3.6 xMap.ai — Geospatial Intelligence Platform

- **URL:** https://www.xmap.ai
- **Dataset page:** https://www.xmap.ai/data-catalogs/saudi-arabia-real-estate-transactions-dataset
- **Authentication:** Commercial contract
- **Registration required:** Yes — contact sales
- **What's available:**
  - Saudi Arabia Real Estate Transactions Dataset: transaction volumes, pricing trends, regional dynamics (residential + commercial)
  - Updated bi-annually
  - Geospatial enrichment: pedestrian movement, transport connectivity, neighborhood demographics
  - Mobility data for Saudi Arabia (separate dataset)
- **Cost:** Commercial (not public pricing)
- **Notes:** xMap aggregates and enriches Saudi RE transaction data with geospatial context. Their dataset overlaps with our MOJ data but may have coordinates and enrichment we don't have. Could be useful for AVM (automated valuation model) inputs. They have a Riyadh office.

---

### 3.7 KAPSARC Data Portal

- **URL:** https://datasource.kapsarc.org (legacy) and https://data.kapsarc.org
- **Authentication:** Free registration for full API access
- **What's available:**
  - Real Estate Indices by Regions (time series)
  - Real Estate Price Index by Sector & Type (2014=100, then 2023=100)
  - GDP by economic activity (quarterly)
  - All datasets: browse/download free, API for registered users
  - ODS (OpenDataSoft) platform — standard API: `datasource.kapsarc.org/api/explore/v2.1/catalog/datasets/real-estate-indices/records`
- **Cost:** Free
- **Notes:** This is the cleanest programmatic access to Saudi RPI data. OpenDataSoft API is well-documented, supports filtering, pagination, JSON output. Better than downloading PDFs from GASTAT. Registration is a 2-minute form.

---

### 3.8 TendersAlerts.com — Third-party Etimad Aggregator

- **URL:** https://tendersalerts.com/en/tenders-api
- **Docs:** https://docs.tendersalerts.com
- **Authentication:** API key
- **What's available:**
  - Saudi government tenders scraped/aggregated from Etimad
  - Filter by sector, region, ministry
  - Construction/real estate development tenders
- **Cost:** Subscription (contact for pricing)
- **Notes:** Alternative to direct Etimad API for companies that haven't completed Etimad's registration process.

---

## 4. Data Types Mapping

| Data Type Needed | Best Source | Status |
|-----------------|------------|--------|
| Property deed numbers | Wathq API 13 (paid) | Registration needed |
| Property type/description | Wathq API 13 + our MOJ CSV | Available |
| Lat/long geocoding | National Address API / Google Maps / HERE | Registration needed |
| Valuation / assessed values | No public API. Taqeem (manual). xMap (commercial) | Gap |
| Building permits | Balady (no API). MOMAH open data (aggregated) | Partial gap |
| Population / demographics | GASTAT Census 2022 (download). DataSaudi (API) | Available |
| Real estate price index | KAPSARC Data Portal (API, free) | Available |
| Rental contract data | Our Ejar Collector (running). Ejar open data via CKAN | Available |
| Transaction-level prices | Our MOJ CSVs (4.96M rows). SREM (Nafath-gated) | Available |
| Mortgage volume | SAMA Open Data (CSV download) | Available |
| Construction tenders | Etimad API / TendersAlerts | Registration needed |
| POI / neighborhood data | Google Maps Places API / REGA Geospatial portal | Available (paid) |
| White land parcels | MOMAH Idle Lands portal (Riyadh, Oct 2025 rollout) | No API yet |

---

## 5. Priority Action Items

### Immediate (free, easy)
1. **Register on KAPSARC Data Portal** (https://data.kapsarc.org) — free API access to RPI time series by region and type. Directly enriches our analysis.
2. **Register on National Address API** (https://api.address.gov.sa) — Starter plan (free, 100 calls/week) to prototype geocoding of MOJ records. Upgrade if batch volume needed.
3. **Register on DataSaudi** (https://datasaudi.sa) — free API access to GASTAT indicators including housing census by region.
4. **Pull SAMA mortgage CSV** from https://www.sama.gov.sa/en-US/EconomicReports/pages/database.aspx — no registration. Add to periodic download.

### Medium-term (paid / approval required)
5. **Wathq Real Estate Deeds API** — subscribe to Basic plan. Useful for deed verification and property type enrichment on records with ambiguous codes. Evaluate cost vs. coverage.
6. **Google Maps Geocoding API** — enable in Google Cloud. $5/1K requests. Budget ~$200–$500 for initial batch geocoding of district centroids (not every record — use district → centroid mapping).
7. **Etimad Tenders API** — apply for access at apiportal.etimad.sa. Filter for real estate/construction tenders by region to build a supply pipeline indicator.

### Lower priority / monitor
8. **HERE Maps** — alternative to Google for geocoding if cost is a constraint. Confirm Saudi short address support.
9. **xMap.ai** — commercial data partnership; evaluate if their enriched dataset fills gaps we can't fill via open data.
10. **Sakan/Aqar data partnership** — reach out for listing data access to benchmark transaction prices against asking prices.
11. **GEOSA registration** — for parcel-level spatial data (boundary geometries). May unlock district polygon files.

---

## 6. Existing Data We Already Have

For context, do not re-acquire:
- MOJ transaction CSVs: 4.96M rows, 170 CSVs in `moj/` (sales + 18 operation categories)
- REGA rental/sales indicators: `rega/`
- Ejar rental contracts: 104K+ rows in registry via `~/rega-ejar-collector`
- Registry DB: `registry.db`

---

*Research method: web search across 25+ sources, March 2026. All URLs verified as active during research.*
