# REGA Ejar Rental Indicators API

Discovered 2026-02-22 via Playwright inspection of Sakani rental indicators page.

## Base URL

```
https://rentalrei.rega.gov.sa/RegaIndicatorsAPIs/api/IndicatorEjar/
```

## Authentication

**None required.** The frontend sends `Authorization: Bearer null`. All endpoints are publicly accessible with no API key, no login, no GeoIP restriction.

## Endpoints

### Reference Data

| Endpoint | Method | Params | Returns |
|----------|--------|--------|---------|
| `GetAllRegions` | GET | none | 13 administrative regions with lat/lng |
| `GetCitisByRegionId?regionId={id}` | GET | regionId (1-13) | Cities within region, with lat/lng, district count |
| `GetDistrictsByCityId?cityId={id}` | GET | cityId | Neighborhoods within city (e.g. Riyadh=194) |
| `GetAllRegionsForGeneralpriceindex?RENTAL_UNIT_USAGE=0` | GET | RENTAL_UNIT_USAGE: 0=residential, 1=commercial | 14 cities + national level (for price index) |
| `GetAllResidentialUnitsTypes` | GET | none | 6 unit types with min/max rent bounds |
| `GetLastContractDate` | GET | none | Latest available data (currently Dec 2025) |
| `GetToken` | POST | none | Token (unused — auth is "Bearer null") |

### Data Endpoints

#### GetDetailsV2 (POST) — Detailed Rental Data
**The main endpoint for neighborhood-level rental data.**

```json
{
  "trigger_Points": "0",          // "0" = city-level, or district ID for neighborhood
  "strt_date": "2025-03-31T21:00:00.000Z",
  "end_date": "2026-02-28T21:00:00.000Z",
  "cityId": 21282,                // from GetCitisByRegionId
  "strt_date2": "Sat Mar 01 2025 00:00:00 GMT+0300 (Arabian Standard Time)",
  "end_date2": "Sun Feb 01 2026 00:00:00 GMT+0300 (Arabian Standard Time)",
  "totalRooms": 0                 // 0 = all, or filter by room count
}
```

**Response fields per unit type:**
- `unitName`: appartment, duplex, floor, office_space, shop, studio, trade_exhibition, villa
- `sumDeals`: total transaction count
- `sumRent`: total rent value (SAR)
- `avg`: average annual rent (SAR)
- `avgMin_range_1`, `avgMax_range_1`: price range band 1 (lower third)
- `avgMin_range_2`, `avgMax_range_2`: price range band 2 (middle third)
- `avgMin_range_3`, `avgMax_range_3`: price range band 3 (upper third)
- `total_deals_range_1/2/3`: deal counts per price band
- `total_rent_sum_range_1/2/3`: total rent per price band
- `change_percent`: price change indicator

#### GetChartPublicIndicatorsDemo (POST) — Price Index
**Rental price index (base year 2022=1.0)**

```json
{
  "LKCityId": -1,         // -1 = national, or city ID
  "city": "على مستوى المملكة",
  "RENTAL_UNIT_USAGE": 0, // 0=residential, 1=commercial
  "annual": 1             // 1=annual, 0=quarterly
}
```

**Response:** Array of series (General, Apartment, Floor, Villa) with year/quarter arrays and index values.

#### GetChartClassicIndicatorEjar (POST) — Classic Chart
```json
{
  "trigger_Points": "0",
  "strt_date": "2025-03-31T21:00:00.000Z",
  "end_date": "2026-02-28T21:00:00.000Z",
  "cityId": 21282,
  "RentalUnitUsage": 0,
  "PeriodType": "1",
  "totalRooms": 0
}
```

#### GetRegionsStatistics (POST) — Regional Summary
```json
{}  // No parameters needed
```

#### GetSaudiStatistics (POST) — National Summary
Returns current year deal counts (residential + commercial, annual + last month).

#### brokersCount (POST) — Broker Statistics
Same params as GetDetailsV2.

## Data Coverage

- **Temporal:** 2019 to December 2025 (7 years)
- **Geographic hierarchy:** Region (13) → City (hundreds) → District/Neighborhood (thousands)
- **Riyadh alone:** 194 neighborhoods
- **Unit types:** 8 (apartment, duplex, floor, villa, studio, office_space, shop, trade_exhibition)
- **Residential vs Commercial:** Controlled by RENTAL_UNIT_USAGE param (0=residential, 1=commercial)
- **Date flexibility:** Any date range within 2019-2025

## Key IDs

### Regions
| ID | Arabic | English |
|----|--------|---------|
| 1 | الرياض | Riyadh |
| 2 | مكة المكرمة | Makkah |
| 3 | المدينة المنورة | Madinah |
| 4 | القصيم | Al Qassim |
| 5 | المنطقة الشرقية | Eastern |
| 6 | عسير | Asir |
| 7 | تبوك | Tabuk |
| 8 | حائل | Hail |
| 9 | الحدود الشماليه | Northern Borders |
| 10 | جازان | Jazan |
| 11 | نجران | Najran |
| 12 | الباحة | Al Bahah |
| 13 | الجوف | Al Jawf |

### Major Cities (sample)
| ID | City | Districts |
|----|------|-----------|
| 21282 | Riyadh | 194 (212 total, some inactive) |
| 18394 | Jeddah | TBD |
| 11048 | Dammam | TBD |
| 15423 | Makkah | TBD |
| 14001 | Madinah | TBD |

### Unit Types
| ID | English | Arabic | Min Rent | Max Rent |
|----|---------|--------|----------|----------|
| 19 | appartment | شقة | 500 | 300,000 |
| 24 | duplex | دوبلاكس | 7,000 | 700,000 |
| 18 | floor | دور | 4,800 | 500,000 |
| 25 | studio | استديو | 500 | 300,000 |
| 20 | villa | فيلا | 7,000 | 700,000 |

## Sample Data (Ash Shifa, Riyadh, Mar 2025 - Feb 2026)

| Unit | Deals | Avg Rent (SAR/yr) |
|------|-------|-------------------|
| Apartment | 2,534 | 19,386 |
| Floor | 809 | 27,628 |
| Villa | 123 | 43,150 |
| Studio | 91 | 15,382 |
| Duplex | 14 | 28,038 |
| Shop | 1,255 | 767/m2 |
| Office | 262 | 350/m2 |

## Scraping Strategy

To build a complete rental dataset:
1. Call `GetAllRegions` → 13 regions
2. For each region, call `GetCitisByRegionId` → all cities
3. For each city, call `GetDistrictsByCityId` → all neighborhoods
4. For each neighborhood, call `GetDetailsV2` with yearly date ranges (2019-2025)
5. Estimated total API calls: ~13 regions × ~30 cities avg × ~50 districts avg × 7 years = ~137,000 calls
6. **Rate limiting:** Unknown — test carefully. Start slow (1 req/sec), observe response times.
7. Commercial data: Repeat with `RENTAL_UNIT_USAGE=1`

## Frontend Source

The Sakani page at `sakani.sa/reports-and-data/rental-units` embeds an iframe from `rei.sakani.sa` which is a Vue.js app making these API calls. Pages:
- `/publicindicators` — general price index
- `/indicatorejar` — detailed indicators (map + district selection)
- `/districtcomparison` — compare districts
- `/districtsmartsearch` — smart search
- `/methodologey` — methodology documentation
