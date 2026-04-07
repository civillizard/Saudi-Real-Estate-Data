#!/usr/bin/env python3
"""
Probe GASTAT datasets on Saudi Open Data portal for RE-related data.
One-time discovery script — produces a report of what's available.
"""

import json
import ssl
import time
import urllib.parse
import urllib.request
from datetime import datetime

UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15"
CTX = ssl.create_default_context()
API_BASE = "https://open.data.gov.sa/data/api"
ODP_BASE = "https://open.data.gov.sa/odp-public"
GASTAT_AR = "الهيئة العامة للإحصاء"
DELAY = 1.0


def fetch_json(url):
    req = urllib.request.Request(
        url, headers={"User-Agent": UA, "Accept-Language": "ar,en"}
    )
    with urllib.request.urlopen(req, timeout=30, context=CTX) as resp:
        return json.loads(resp.read())


def fetch_org_datasets(org_name_ar):
    encoded = urllib.parse.quote(org_name_ar)
    url = f"{API_BASE}/organizations?version=-1&organization={encoded}"
    data = fetch_json(url)
    if isinstance(data, dict):
        return data.get("datasets", [])
    return []


def fetch_resources(dataset_id):
    url = f"{API_BASE}/datasets/resources?version=-1&dataset={dataset_id}"
    try:
        result = fetch_json(url)
        if isinstance(result, list):
            return result
        if isinstance(result, dict):
            return result.get("resources", [])
    except Exception:
        pass
    return []


def fetch_dataset_detail(dataset_id):
    """Get full dataset detail including resource URLs."""
    url = f"https://open.data.gov.sa/api/datasets/{dataset_id}"
    try:
        return fetch_json(url)
    except Exception:
        return None


# RE keywords
RE_KEYWORDS = [
    "عقار",
    "سكن",
    "مسكن",
    "بناء",
    "تشييد",
    "إيجار",
    "أرض",
    "مؤشر الأسعار",
    "إسكان",
    "تضخم",
    "رخص بناء",
    "real estate",
    "housing",
    "construction",
    "building",
    "rent",
    "land",
    "property",
    "dwelling",
    "residential",
    "price index",
    "CPI",
    "permit",
    "mortgage",
]


def categorize(title):
    t = title.lower()
    if "الرقم القياسي لأسعار العقارات" in t or "real estate price index" in t:
        return "RE_PRICE_INDEX"
    if "تعداد 2022" in t:
        return "CENSUS_2022"
    if "construction material" in t or "مواد بناء" in t:
        return "CONSTRUCTION_MATERIALS"
    if "housing unit" in t or "وحدات سكنية" in t:
        return "HOUSING_UNITS"
    if "occupied house" in t or "مساكن" in t:
        return "HOUSING_CENSUS"
    if "تضخم" in t or "inflation" in t or "cpi" in t:
        return "CPI"
    if "wholesale price" in t:
        return "WHOLESALE_INDEX"
    return "OTHER"


def main():
    print(f"GASTAT Open Data Probe — {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    print("=" * 70)

    datasets = fetch_org_datasets(GASTAT_AR)
    print(f"Total GASTAT datasets: {len(datasets)}")

    # Filter RE-related
    matches = []
    for ds in datasets:
        title = (ds.get("titleAr", "") + " " + ds.get("title", "")).lower()
        if any(kw.lower() in title for kw in RE_KEYWORDS):
            matches.append(ds)

    print(f"RE-related: {len(matches)}")
    print()

    # Categorize
    by_category = {}
    for ds in matches:
        title = ds.get("titleAr", "") + " " + ds.get("title", "")
        cat = categorize(title)
        by_category.setdefault(cat, []).append(ds)

    # Probe resources for high-value categories
    HIGH_VALUE = {"RE_PRICE_INDEX", "CENSUS_2022", "CPI"}

    report = []

    for cat in sorted(by_category.keys()):
        items = by_category[cat]
        probe_resources = cat in HIGH_VALUE
        priority = "HIGH" if cat in HIGH_VALUE else "LOW"

        print(f"\n{'=' * 70}")
        print(f"Category: {cat} ({len(items)} datasets) — Priority: {priority}")
        print(f"{'=' * 70}")

        for ds in sorted(items, key=lambda x: x.get("titleAr", "")):
            ds_id = ds.get("id", "")
            title_ar = ds.get("titleAr", "")
            title_en = ds.get("title", "")
            display_title = title_ar or title_en

            resources = []
            download_urls = []

            if probe_resources and ds_id:
                time.sleep(DELAY)
                resources = fetch_resources(ds_id)

                # Also try detail API for download URLs
                time.sleep(DELAY)
                detail = fetch_dataset_detail(ds_id)
                if detail and isinstance(detail, dict):
                    for r in detail.get("resources", []):
                        url_path = r.get("url", "")
                        fmt = r.get("format", "")
                        if url_path and fmt:
                            full_url = f"{ODP_BASE}/{url_path}"
                            download_urls.append((fmt, full_url))

            res_summary = f"{len(resources)} resources"
            if download_urls:
                fmts = [f for f, _ in download_urls]
                res_summary += f" — formats: {', '.join(fmts)}"

            print(f"\n  {display_title}")
            if title_en and title_ar:
                print(f"  EN: {title_en}")
            print(f"  ID: {ds_id}")
            print(f"  {res_summary}")

            if download_urls:
                for fmt, url in download_urls[:3]:
                    print(f"    [{fmt}] {url}")

            report.append(
                {
                    "category": cat,
                    "priority": priority,
                    "dataset_id": ds_id,
                    "title_ar": title_ar,
                    "title_en": title_en,
                    "resource_count": len(resources),
                    "download_urls": download_urls,
                }
            )

    # Summary
    print(f"\n\n{'=' * 70}")
    print("SUMMARY")
    print(f"{'=' * 70}")
    for cat in sorted(by_category.keys()):
        items = by_category[cat]
        priority = "HIGH" if cat in HIGH_VALUE else "LOW"
        with_resources = sum(
            1 for r in report if r["category"] == cat and r["resource_count"] > 0
        )
        print(
            f"  {cat:25s} {len(items):3d} datasets  {with_resources:3d} with files  [{priority}]"
        )

    total_with_files = sum(1 for r in report if r["resource_count"] > 0)
    print(
        f"\n  Total: {len(matches)} datasets, {total_with_files} with downloadable files"
    )

    # Write JSON report
    with open("data/gastat_probe_report.json", "w") as f:
        json.dump(report, f, indent=2, ensure_ascii=False)
    print("\n  Report saved: data/gastat_probe_report.json")


if __name__ == "__main__":
    main()
