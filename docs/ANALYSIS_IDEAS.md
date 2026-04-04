# Real Estate Data — Analysis Ideas & Use Cases

<p align="center">
  <a href="https://rega.gov.sa">REGA - Real Estate General Authority (الهيئة العامة للعقار)</a>
  &nbsp;&nbsp;&nbsp;&nbsp;
  <a href="https://moj.gov.sa">MOJ - Ministry of Justice (وزارة العدل)</a>
</p>

**Created:** 2026-03-12
**Status:** Living document — brainstorming phase
**Data sources:** MOJ transactions (5M rows), REGA indicators, Ejar rentals (104K), regulatory events

---

## Data Capability Summary (from audits)

### What we CAN do
- Track sale prices, volumes, and area by region/city/district quarterly (2020–2025)
- Distinguish residential/commercial/agricultural/industrial (use classification)
- Distinguish land vs built property — **only for 2023 Q1–Q3** (نوع العقار) and REGA aggregates
- Track seizure and release volumes by area (Riyadh only in 2025 data)
- Track mortgage issuance and release volumes
- Track enforcement (court-ordered) sales
- Track property division, merging, deed updates
- Track rental indicators by region (REGA) + actual Ejar contracts
- Overlay regulatory events (White Land Tax phases, vacant property fines) with known dates and districts

### What we CANNOT do (yet)
- Link individual assets across transaction categories (no shared property ID in open data)
- Distinguish land vs built for 2020–2022 and 2024+ (must infer from price/area patterns)
- Track individual asset lifecycles (seizure → release → sale)
- Identify specific properties subject to White Land Tax

### Workarounds to explore
- **Price/area inference:** Establish price-per-m² benchmarks for land vs built in each district using 2023 Q1–Q3 labeled data, then apply those ranges to classify unlabeled periods
- **Probabilistic matching:** Composite key matching (region + city + date proximity + area) for sales data where both price and area exist
- **REGA aggregate cross-check:** Use REGA's property-type breakdowns to validate/calibrate our inferences

---

## Analysis Ideas — Market Dynamics

### 1. Price per m² trend by district (2020→2025)
- **Data needed:** MOJ sales (1.4M rows)
- **Challenge:** Can't distinguish land vs built except 2023 Q1–Q3. Mixed asset types inflate noise.
- **Workaround:** Use 2023 labeled data to establish land vs built price bands per district, then segment other years probabilistically. Also use REGA aggregates (which have type breakdowns) as calibration.
- **Feasibility:** Medium — viable with inference layer
- **Uniqueness:** High — no one publishes district-level trends publicly
- **Commercial potential:** High — developers, investors, banks

### 2. Transaction volume trend by city
- **Data needed:** MOJ sales
- **Challenge:** Minimal — straightforward count + group by
- **Feasibility:** High
- **Uniqueness:** Medium — REGA publishes some aggregate indicators
- **Commercial potential:** Medium

### 3. Residential vs commercial vs agricultural price divergence
- **Data needed:** MOJ sales (تصنيف العقار field)
- **Challenge:** Only 4 categories. Within "residential," land and villas behave very differently.
- **Enhancement:** Layer in نوع العقار from 2023 files and REGA type breakdowns for deeper segmentation
- **Feasibility:** High for broad categories, medium for subtypes
- **Uniqueness:** High — cross-classification divergence analysis not published
- **Commercial potential:** High

### 4. Seasonal patterns — which quarters consistently outperform?
- **Data needed:** MOJ sales, 24 quarters of data
- **Challenge:** Need to separate seasonality from trend. Also Ramadan/Hajj timing shifts each year.
- **Feasibility:** High
- **Uniqueness:** Medium
- **Commercial potential:** Medium — timing guidance for investors

### 5. Emerging cities — low base, high growth
- **Data needed:** MOJ sales across all 175 cities
- **Challenge:** Small city data may be noisy (few transactions per quarter)
- **Feasibility:** High
- **Uniqueness:** High — no one is ranking emerging cities by growth rate
- **Commercial potential:** High — early-mover advantage for investors/developers

### 6. Average deal size + lot/unit size trends
- **Data needed:** MOJ sales (price + area fields)
- **Challenge:** More insightful if segmented by asset type. Median better than mean for skewed data.
- **Enhancement:** Track median lot size for land deals, median unit size for apartments (where identifiable). Are developers building smaller? Are lots being subdivided?
- **Feasibility:** High
- **Uniqueness:** High
- **Commercial potential:** Medium — market structure insight

---

## Analysis Ideas — Distress & Opportunity

### 7. Seizure-to-release ratio by district
- **Data needed:** MOJ seizure (737K) + release (506K)
- **Challenge:** Both limited to Riyadh in 2025 data. No asset-level linking — aggregate ratios only.
- **Feasibility:** Medium (Riyadh only, aggregate)
- **Uniqueness:** High — not published anywhere
- **Commercial potential:** High — distress signal for opportunity hunters

### 8. Seizure volume trend as financial stress indicator
- **Data needed:** MOJ seizure, quarterly
- **Challenge:** Only 3 quarters of data (2025 Q1–Q3). Need more history for trend.
- **Feasibility:** Low now, improves with future data collection
- **Uniqueness:** High
- **Commercial potential:** High

### 9. Enforcement sale prices vs market prices
- **Data needed:** MOJ enforcement sales (8K rows) + MOJ sales for same districts
- **Challenge:** Enforcement sales have NO price or area field — only reference number, date, city, and document type. Cannot compute discount.
- **Feasibility:** Low — missing price data in enforcement
- **Uniqueness:** Would be extremely high if feasible
- **Commercial potential:** Very high

### 10. Seizure spike → price decline delay
- **Data needed:** Seizure volumes + sales prices by district over time
- **Challenge:** Seizure data limited to Riyadh 2025. Need multi-year series to establish lag patterns.
- **Feasibility:** Low now
- **Uniqueness:** Very high
- **Commercial potential:** Very high

### 11. High seizure + high new mortgage districts = overleveraged areas
- **Data needed:** Seizure + mortgage volumes by district
- **Challenge:** Seizure is Riyadh only. Mortgage data covers all regions but only 3 quarters.
- **Feasibility:** Medium (Riyadh only)
- **Uniqueness:** Very high
- **Commercial potential:** High — banking/risk assessment

---

## Analysis Ideas — Mortgage & Lending

### 12. Mortgage volume vs sale volume — financing penetration rate
- **Data needed:** MOJ mortgage (36K) + MOJ sales
- **Challenge:** Different time coverage. Mortgage data is 2025 only, sales go back to 2020.
- **Feasibility:** Medium (limited to 2025 comparison)
- **Uniqueness:** High
- **Commercial potential:** High — banking sector interest

### 13. Mortgage release trend — repayment velocity
- **Data needed:** MOJ mortgage release (43K)
- **Challenge:** Only 2025 Q1–Q3. Trend needs more periods.
- **Feasibility:** Low now, improves over time
- **Uniqueness:** High
- **Commercial potential:** Medium

### 14. Net mortgage position by district
- **Data needed:** Mortgage (new) minus mortgage release by area
- **Challenge:** Same time limitation. Aggregate only (no property linking).
- **Feasibility:** Medium (snapshot, not trend)
- **Uniqueness:** High
- **Commercial potential:** High — leverage hotspot identification

### 15. RE Development Fund POA concentration
- **Data needed:** MOJ POA RE Fund (7K rows)
- **Challenge:** Small dataset. Shows where government-backed lending is concentrated.
- **Feasibility:** High
- **Uniqueness:** Medium
- **Commercial potential:** Medium — policy/development correlation

---

## Analysis Ideas — Ownership & Development Signals

### 16. Property division (فرز) hotspots
- **Data needed:** MOJ division (90K rows)
- **Challenge:** High volume, indicates active subdivision. But is it development or liquidation?
- **Cross-reference:** Layer with White Land Tax zone data — division in taxed zones likely = liquidation. Division in untaxed growth areas likely = development.
- **Feasibility:** High
- **Uniqueness:** Very high
- **Commercial potential:** High — supply pipeline indicator

### 17. Property merge hotspots — consolidation signal
- **Data needed:** MOJ merge RE (10K rows)
- **Challenge:** Small volume. Could indicate developer land assembly or administrative cleanup.
- **Feasibility:** High
- **Uniqueness:** High
- **Commercial potential:** Medium

### 18. Old deed registration by area — formalization map
- **Data needed:** MOJ register old deed (143K rows)
- **Challenge:** High volume. Shows where legacy ownership is being formalized — precursor to development or sale.
- **Feasibility:** High
- **Uniqueness:** High
- **Commercial potential:** Medium — development readiness indicator

### 19. Deed update activity — title cleanup map
- **Data needed:** MOJ deed updates (28K)
- **Feasibility:** High
- **Uniqueness:** Medium
- **Commercial potential:** Low–Medium

### 20. Physical registration (عيني) adoption rate
- **Data needed:** MOJ physical registration (501K — large dataset)
- **Challenge:** Shows rollout of the new property identity system. Geographic adoption patterns.
- **Feasibility:** High
- **Uniqueness:** Medium
- **Commercial potential:** Low — mostly governance interest

---

## Analysis Ideas — Rental & Yield

### 21. Gross rental yield by neighborhood
- **Data needed:** REGA rental indicators + MOJ sales prices
- **Challenge:** Different granularity (REGA is aggregate, MOJ is transactional). Need to aggregate MOJ to match.
- **Feasibility:** Medium
- **Uniqueness:** High — nobody publishes computed yields
- **Commercial potential:** Very high — direct investment decision input

### 22. Ejar actuals vs REGA indicators — accuracy check
- **Data needed:** Ejar collector (104K) + REGA rental indicators
- **Challenge:** Matching geography/time periods between the two sources.
- **Feasibility:** Medium
- **Uniqueness:** High — tests whether official stats reflect reality
- **Commercial potential:** Medium — data quality insight

### 23. Rental yield trend — compression analysis
- **Data needed:** Time series of both rental and sale data
- **Challenge:** Rental data (REGA) limited to 2019–2024. Need overlapping periods.
- **Feasibility:** Medium
- **Uniqueness:** High
- **Commercial potential:** High — bubble/value signal

### 24. High yield + low appreciation = cash flow plays
- **Data needed:** Combined yield + price trend analysis
- **Feasibility:** Medium (depends on #21 and #1 working)
- **Uniqueness:** Very high
- **Commercial potential:** Very high — direct investment strategy

### 25. Low yield + high appreciation = speculative markets
- **Data needed:** Same as #24
- **Feasibility:** Medium
- **Uniqueness:** Very high
- **Commercial potential:** Very high — risk identification

---

## Analysis Ideas — Cross-Source Signals

### 26. Seizure → enforcement → price impact chain
- **Data needed:** Seizure + enforcement + sales
- **Challenge:** No asset-level linking. Enforcement has no price. Aggregate correlation only.
- **Feasibility:** Low
- **Uniqueness:** Extremely high if feasible
- **Commercial potential:** Very high

### 27. Mortgage release surge + rising sales = refinancing into upgrades?
- **Data needed:** Mortgage release + sales by area/time
- **Challenge:** Limited overlap periods. Aggregate correlation.
- **Feasibility:** Medium
- **Uniqueness:** High
- **Commercial potential:** Medium

### 28. POA volume as leading indicator for transactions
- **Data needed:** POA (758K — large) + sales
- **Challenge:** POA is 2025 only. Need more history to establish lead-lag.
- **Feasibility:** Low now
- **Uniqueness:** High
- **Commercial potential:** High if confirmed

### 29. Division (فرز) volume → subsequent sale volume — supply pipeline
- **Data needed:** Division + sales by area/quarter
- **Challenge:** Division is 2025 only. Sales go back to 2020. Limited overlap.
- **Enhancement:** As we collect more quarters, this becomes testable.
- **Feasibility:** Low now, medium over time
- **Uniqueness:** Very high
- **Commercial potential:** High — supply forecasting

### 30. Register-without-deed clusters — informal ownership map
- **Data needed:** MOJ register-no-deed (21K rows)
- **Challenge:** Small volume. But concentrated areas may indicate informal/unregistered ownership hotspots — potential development friction or opportunity.
- **Feasibility:** High
- **Uniqueness:** Very high
- **Commercial potential:** Medium — due diligence tool

---

## Analysis Ideas — Regulatory Impact

### 31. White Land Tax impact — before/after by district
- **Data needed:** Sales + regulatory event timeline
- **Approach:** Compare transaction volume and prices in Tier 1 districts (10% fee) vs untaxed control districts in same city, 3 months before vs after enforcement dates.
- **Key dates:** Jan 2026 (first 60K Riyadh invoices), Phase 1 cities from 2017
- **Feasibility:** High for Riyadh (known zone maps), medium for other cities
- **Uniqueness:** Extremely high
- **Commercial potential:** Very high — policy impact quantification

### 32. Vacant property fine — rental market impact
- **Data needed:** Ejar contracts + regulatory timeline
- **Approach:** Monitor Ejar contract volume and rental rates in affected districts after fine announcements. Expect supply increase and price softening.
- **Key dates:** Regulations expected May 2026
- **Feasibility:** Medium (regulations not yet issued)
- **Uniqueness:** Very high
- **Commercial potential:** Very high

### 33. White Land Tax → division (فرز) correlation
- **Data needed:** Division volumes in taxed vs untaxed zones
- **Approach:** Do taxed zones show higher subdivision rates? This indicates owners breaking up land to sell parcels rather than pay the annual fee.
- **Feasibility:** High
- **Uniqueness:** Very high
- **Commercial potential:** High

### 34. Forced rental market entry — rental price elasticity
- **Data needed:** Ejar data + vacancy proxies + regulatory timeline
- **Approach:** As vacant fines push idle properties into rental market, measure the rental rate response in each district. Districts with already-high supply will see sharper drops.
- **Feasibility:** Medium (needs vacancy proxy, regulations pending)
- **Uniqueness:** Very high
- **Commercial potential:** Very high

---

## Analysis Ideas — Macro & Structural

### 35. E-service adoption rate by category
- **Data needed:** نوع الخدمة field across all operation files
- **Challenge:** Straightforward. Shows digitization progress.
- **Feasibility:** High
- **Uniqueness:** Low — MOJ publishes this
- **Commercial potential:** Low

### 36. Public vs private sector transaction split
- **Data needed:** نوع القطاع field
- **Feasibility:** High
- **Uniqueness:** Low
- **Commercial potential:** Low

### 37. Total market size — SAR transacted per quarter
- **Data needed:** MOJ sales (price column)
- **Feasibility:** High
- **Uniqueness:** Medium — REGA publishes some aggregates
- **Commercial potential:** Medium

### 38. Concentration risk — top 5 cities' share of total value
- **Data needed:** MOJ sales
- **Feasibility:** High
- **Uniqueness:** Medium
- **Commercial potential:** Medium — portfolio diversification input

### 39. The 2023 dip — uniform or localized?
- **Data needed:** MOJ sales by city/quarter
- **Approach:** Was the 47% volume drop (281K → 140K) uniform across regions, or concentrated? Did prices also drop, or just volume? Schema changed in 2023 — was it a data issue?
- **Feasibility:** High
- **Uniqueness:** High — nobody has explained this publicly
- **Commercial potential:** Medium — market understanding

---

## Analysis Ideas — Asset Type Inference (Workaround)

### 40. Build land/built classifier from 2023 labeled data
- **Data needed:** 2023 Q1–Q3 sales with نوع العقار
- **Approach:** Use 131K labeled transactions to establish price-per-m² distributions for land vs villa vs apartment in each district. Then apply those ranges to classify 2020–2022 and 2024+ unlabeled data probabilistically.
- **Feasibility:** Medium — accuracy depends on how distinct the distributions are
- **Uniqueness:** Novel methodology
- **Commercial potential:** Foundational — enables many other analyses

### 41. REGA aggregate calibration for asset type inference
- **Data needed:** REGA sales indicators (have type breakdowns) + MOJ sales
- **Approach:** REGA tells us "in District X, 60% of transactions were land, 30% villas, 10% apartments." Use this distribution to validate our price-based classifier from #40.
- **Feasibility:** Medium
- **Uniqueness:** High
- **Commercial potential:** Foundational

---

## Monitoring & Data Collection Ideas

### 42. Data source monitoring cron
- Monitor Saudi Open Data portal APIs for new MOJ/REGA quarterly releases
- Monitor idlelands.momah.gov.sa for new zone/phase announcements
- Monitor Ejar collector for schema changes
- Alert on new files or format changes

### 43. Regulatory event timeline database
- Curate White Land Tax phase dates, cities, districts, fee rates
- Vacant property fine announcements and effective dates
- Any new real estate regulatory changes
- Small DB (dozens of rows) but high interpretive value

### 44. Historical REGA/MOJ data gap-filling
- MOJ operations data only covers 2024–2025. Sales covers 2020+.
- Future portal checks may reveal older operation datasets being published retroactively.
- The monitoring cron should also watch for new datasets, not just new files in existing datasets.

---

## Priority Framework

### Scoring dimensions
- **Feasibility:** Can the current data answer this? (High/Medium/Low)
- **Uniqueness:** Is anyone else answering this publicly? (High = nobody, Low = already published)
- **Commercial potential:** Would someone pay for this insight? (High = investors/banks, Medium = government/researchers, Low = academic)

### Quick wins (High feasibility + High uniqueness)
- #2 Transaction volume trends
- #4 Seasonal patterns
- #5 Emerging cities
- #6 Deal size trends
- #16 Division hotspots
- #18 Old deed registration map
- #30 Informal ownership clusters
- #37 Total market size
- #38 Concentration risk
- #39 The 2023 dip investigation

### High-value targets (Medium feasibility, very high potential)
- #1 Price per m² by district (needs asset type inference)
- #21 Gross rental yield by neighborhood
- #24/#25 Cash flow vs speculative market identification
- #31 White Land Tax impact analysis
- #33 Tax → division correlation
- #40 Land/built classifier from 2023 data (foundational)

### Future potential (Low feasibility now, very high value)
- #9 Enforcement sale discounts (needs price data in enforcement)
- #10 Seizure → price decline lag
- #26 Full distress chain tracking
- #28 POA as leading indicator
- #29 Division → sale supply pipeline

---

## Open Questions

1. Can we access MOJ or REGA authenticated APIs for richer property-level data?
2. Will MOJ bring back the نوع العقار column in future quarterly releases?
3. What additional external data sources could enrich the analysis? (municipality permits, building completion data, population registry)
4. Are there commercial real estate data providers in Saudi we should benchmark against?

---

**Next steps:**
1. Build the monitoring cron
2. Ingest raw data into 3-DB architecture
3. Start with quick wins to validate the pipeline
4. Build the land/built classifier (#40) as foundation for deeper analysis
