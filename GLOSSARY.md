# Glossary — Saudi Real Estate Terms

Arabic terms used in the data files, grouped by category.

## Government Entities

| Arabic | English | Role in this dataset |
|--------|---------|---------------------|
| وزارة العدل | Ministry of Justice (MOJ) | Registers all property transactions: sales, mortgages, transfers, deeds |
| الهيئة العامة للعقار | Real Estate General Authority (REGA) | Regulates real estate sector, publishes market indicators and rental data |
| وزارة الشؤون البلدية والقروية والإسكان | Ministry of Municipal, Rural Affairs and Housing (MOMAH) | Administers White Land Tax, housing policy, municipal zoning |
| الهيئة السعودية للبيانات والذكاء الاصطناعي | Saudi Data & AI Authority (SDAIA) | Manages the National Open Data Portal where this data is published |
| صندوق التنمية العقارية | Real Estate Development Fund (REDF) | Government fund providing subsidized mortgages to Saudi citizens |

## Property & Deeds

| Arabic | Transliteration | English | Context |
|--------|----------------|---------|---------|
| صك | Sakk | Title deed | Legal document proving property ownership. Central to all MOJ data |
| عقار | Aqar | Real estate / property | General term for any real property |
| أرض | Ard | Land (undeveloped) | Appears in `نوع العقار` (property type) column |
| فيلا | Villa | Villa | Standalone residential building |
| شقة | Shaqqa | Apartment / flat | Unit within a building |
| عمارة | Amara | Building / apartment block | Multi-unit residential or commercial building |
| دور | Dawr | Floor / story | A single floor in a building, sometimes traded separately |
| معرض | Ma'rad | Showroom | Commercial display space |
| مستودع | Mustawda' | Warehouse | Storage facility |
| استراحة | Istiraha | Rest house / chalet | Recreational property, common in Saudi market |
| مزرعة | Mazra'a | Farm | Agricultural property |
| المخطط | Al-Mukhatta | Plat / subdivision plan | The official survey plan number for a neighborhood |
| رقم القطعة | Raqam Al-Qit'a | Parcel/plot number | Identifies a specific lot within a plat |

## Transaction Types

| Arabic | Transliteration | English | Description |
|--------|----------------|---------|-------------|
| إفراغ | Ifraagh | Ownership transfer | The formal transfer of a property title from seller to buyer |
| بيع | Bay' | Sale | General sale transaction |
| رهن | Rahn | Mortgage | A lien placed on property as loan collateral |
| فك رهن | Fakk Rahn | Mortgage release | Removing a mortgage lien after loan repayment |
| حجز تحفظي | Hajz Tahaffuzi | Precautionary seizure | Court-ordered freeze on a property preventing sale or transfer |
| فك حجز | Fakk Hajz | Release of seizure | Lifting a court-ordered property freeze |
| فرز | Farz | Subdivision / division | Splitting one property into multiple separate titles |
| دمج | Damj | Merger | Combining multiple properties or deeds into one |
| وكالة | Wakala | Power of attorney (POA) | Authorization for someone to act on the owner's behalf in RE transactions |
| تسجيل عيني | Tasjeel Ayni | Physical/in-rem registration | Registering a property in the in-rem (land-based) registry system, as opposed to the traditional person-based deed system |
| قرار بيع | Qarar Bay' | Enforcement sale | Court-ordered forced sale (e.g., debt enforcement, bankruptcy) |
| نقل ملكية | Naql Milkiyya | Ownership transfer | Transferring property ownership (same as إفراغ in practice) |

## Property Classification

| Arabic | English | In data as |
|--------|---------|-----------|
| سكني | Residential | `تصنيف العقار` column — 85% of all transactions |
| تجاري | Commercial | `تصنيف العقار` column |
| زراعي | Agricultural | `تصنيف العقار` column |
| صناعي | Industrial | `تصنيف العقار` column — rare (<0.1%) |

Note: `تصنيف العقار` (property classification) tells you the **sector** but cannot distinguish land from buildings. For that, see `نوع العقار` (property type) — only available in 2023 Q1-Q3 sales and REGA indicator files.

## Service & Sector Types

| Arabic | English | Meaning |
|--------|---------|---------|
| القطاع العام | Public sector | Transaction involves a government entity |
| القطاع الخاص | Private sector | Transaction between private parties (individuals or companies) |
| خدمة إلكترونية | Electronic service | Transaction processed fully online through MOJ digital services |
| خدمة إلكترونية جزئيا | Partially electronic service | Transaction started online but required in-person steps |
| الخدمات الرقمية | Digital services | Aggregate label used in some files instead of a region name |

## Date Formats

| Arabic | English | Format |
|--------|---------|--------|
| تاريخ الصفقة ميلادي | Transaction date (Gregorian) | `YYYY/MM/DD` (most files) or `M/D/YYYY` (some 2024 monthly files) |
| تاريخ الصفقة هجري | Transaction date (Hijri) | `YYYY/MM/DD` in the Islamic calendar |
| التاريخ ميلادي | Date (Gregorian) | Shorter label used in operation files |
| التاريخ هجري | Date (Hijri) | Shorter label used in operation files |

Saudi official records use dual dating (Gregorian + Hijri). The Hijri calendar is lunar, ~11 days shorter per year than Gregorian. Python: `from hijri_converter import Hijri, Gregorian` for conversion.

## Regulatory Terms

| Arabic | English | Context |
|--------|---------|---------|
| رسوم الأراضي البيضاء | White Land Tax | Annual fee on undeveloped urban land to incentivize development |
| العقارات الشاغرة | Vacant real estate | Built properties left unoccupied — newly taxed since 2025 amendment |
| أجرة المثل | Fair market rent | Assessed rental value used to calculate vacant property fees |
| نظام التسجيل العيني | In-rem registration system | Saudi Arabia's ongoing transition from person-based deeds to a land-based registry (similar to Torrens system) |
| الهوية العقارية | Property identity | Unique digital ID assigned to registered properties in the new in-rem system |

## Geographic Terms

| Arabic | English |
|--------|---------|
| المنطقة | Region / administrative region (13 total in Saudi Arabia) |
| المدينة | City |
| الحي | District / neighborhood |
| المدينة / الحي | City/District (combined field in sales data) |
