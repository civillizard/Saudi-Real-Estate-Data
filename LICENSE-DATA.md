# Data License & Legal Status

## Source Data

All CSV data files in this repository originate from the following Saudi government open data portals:

| Source | Publisher | Portal |
|--------|-----------|--------|
| **MOJ** | Ministry of Justice (MOJ; وزارة العدل) | [open.data.gov.sa](https://open.data.gov.sa) |
| **REGA** | Real Estate General Authority (REGA; الهيئة العامة للعقار) | [open.data.gov.sa](https://open.data.gov.sa) + [rentalrei.rega.gov.sa](https://rentalrei.rega.gov.sa) |

This data is published under the **KSA Open Data License**, a custom government license administered by **Saudi Data & AI Authority (SDAIA; الهيئة السعودية للبيانات والذكاء الاصطناعي)** through the **National Data Management Office (NDMO)**.

## What the License Allows

Per the [Open Data Policy](https://open.data.gov.sa/en/pages/policies/open-data-policy) and [Open Data License](https://open.data.gov.sa/en/pages/policies/license) pages:

- **Redistribution:** Allowed. *"The open data can be re-used and redistributed, taking into account the requirements of the Open Data License under which such data were distributed."*
- **Derivative works:** Allowed. *"The Open Data License provides freedom to the users in distributing, producing, and transforming works regarding datasets, as well as building upon them."*
- **Commercial use:** Not explicitly prohibited. The platform states data is available *"without technical, financial or legal constraints."* Restrictions listed are: political use, criminal activity, discrimination, and content contrary to Kingdom customs.
- **Cost:** Free. *"Free of Charge"* is one of the nine NDMO Open Data Principles.

## Attribution Requirements

When redistributing or sharing, you must:

1. Follow the usage policy of the Open Data License
2. Include a copy of or reference to the Open Data License alongside the dataset
3. Preserve any copyright or data rights notices
4. Cite the source organization (MOJ / REGA) in references

Per MOJ's own policy:
> يجب الإشارة لوزارة العدل عند استخدام بياناتها في قسم المراجع وذلك للحفاظ على الملكية الفكرية للوزارة
>
> *"MOJ must be cited in references when using their data, to preserve the Ministry's intellectual property."*

## Raw Data vs. Derived Works

MOJ's open data policy includes:
> عند استخدام بيانات وزارة العدل لابد من الحفاظ عليها بعدم تعديلها
>
> *"When using MOJ data, it must be preserved without modification."*

**How this applies to this repository:**

- **`moj/` and `rega/` CSV files** are the raw, unmodified government data files exactly as downloaded from the portal. When citing these files, credit MOJ or REGA as the source.
- **Everything else** (registry, analyses, notebooks, glossary, scripts) are **derivative works** created by the maintainers of this repository. These are clearly not MOJ/REGA data and should not be attributed to them. If you modify or build upon the raw data, the resulting output is your own work — do not present derivative data as official government data.

## This Repository's Code

Scripts, tools, and documentation original to this repository (everything outside the raw CSV data files) are released under the [MIT License](LICENSE).

## Disclaimer

This is an independent community project. It is not affiliated with, endorsed by, or officially connected to MOJ, REGA, SDAIA, or any Saudi government entity. The data is provided as-is for research and analysis purposes. See [DISCLAIMER.md](DISCLAIMER.md) for details.

## Reference Links

- [KSA Open Data Policy](https://open.data.gov.sa/en/pages/policies/open-data-policy)
- [KSA Open Data License](https://open.data.gov.sa/en/pages/policies/license)
- [KSA Open Data Terms of Use](https://open.data.gov.sa/en/pages/policies/terms-of-use)
- [MOJ Open Data](https://www.moj.gov.sa/ar/opendata/Pages/reports.aspx)
- [REGA Open Data](https://www.rega.gov.sa/en/Ede/OpenData)
- [NDMO National Data Governance Interim Regulations](https://sdaia.gov.sa/ndmo/Files/PoliciesEn.pdf)
