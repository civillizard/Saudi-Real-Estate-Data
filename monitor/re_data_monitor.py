#!/usr/bin/env python3
"""
Real Estate Data Source Monitor

Checks Saudi Open Data portal for new MOJ/REGA datasets and monitors
regulatory announcement pages for changes. Sends email alerts via SSH relay.

Runs via launchd or cron. State tracked in local SQLite.
No external dependencies — stdlib only (Python 3.9+).
"""

from __future__ import annotations

import hashlib
import json
import logging
import os
import re
import ssl  # noqa: F401 — used in fetch_url for cert fallback
import sqlite3
import subprocess
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

# ── Configuration ─────────────────────────────────────────────────────

SCRIPT_DIR = Path(__file__).parent.resolve()
STATE_DB = SCRIPT_DIR / "monitor_state.db"
LOG_FILE = SCRIPT_DIR / "monitor.log"
CAPTURE_DIR = SCRIPT_DIR / "captured"  # auto-downloaded new files

NOTIFY_EMAIL = os.environ.get("NOTIFY_EMAIL", "")
SENDER_EMAIL = os.environ.get("SENDER_EMAIL", "")

# Saudi Open Data API
OPEN_DATA_API = "https://open.data.gov.sa/data/api/organizations"
USER_AGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15"

# Organizations to monitor
ORGANIZATIONS = {
    "MOJ": "وزارة العدل",
    "REGA": "الهيئة العامة للعقار",
    "GASTAT": "الهيئة العامة للإحصاء",
}

# Real estate keywords to filter MOJ/GASTAT datasets (they have 998/1180 total)
RE_KEYWORDS = [
    "عقار",
    "صك",
    "رهن",
    "إفراغ",
    "حجز",
    "فرز",
    "دمج",
    "ملكية",
    "تملك",
    "بيع",
    "صفقة",
    "إيجار",
    "مؤشر",
    "عيني",
    "وكال",
    "تسجيل",
    # GASTAT-specific
    "سكن",
    "مسكن",
    "بناء",
    "تشييد",
    "إسكان",
    "تضخم",
]

# Pages to monitor for changes (regulatory announcements)
MONITORED_PAGES = [
    {
        "name": "White Land Tax Portal",
        "url": "https://idlelands.momah.gov.sa/",
        "description": "رسوم الأراضي البيضاء — zone/phase announcements",
    },
    {
        "name": "REGA Open Data",
        "url": "https://www.rega.gov.sa/en/Ede/OpenData",
        "description": "REGA open data page — new indicator releases",
    },
    {
        "name": "Housing Ministry Open Data",
        "url": "https://open.data.gov.sa/data/api/organizations?version=-1&organization=%D9%88%D8%B2%D8%A7%D8%B1%D8%A9%20%D8%A7%D9%84%D8%B4%D8%A4%D9%88%D9%86%20%D8%A7%D9%84%D8%A8%D9%84%D8%AF%D9%8A%D8%A9",
        "description": "MOMAH datasets on open data portal — housing, land, municipal",
    },
    {
        "name": "MOJ Open Data Reports",
        "url": "https://www.moj.gov.sa/ar/opendata/Pages/reports.aspx",
        "description": "MOJ direct reports page — often updates before Open Data portal",
    },
    {
        "name": "MOJ Open Data Main",
        "url": "https://www.moj.gov.sa/ar/opendata/Pages/default.aspx",
        "description": "MOJ open data landing — new category announcements",
    },
    {
        "name": "NHC News",
        "url": "https://www.nhc.sa/en/news/",
        "description": "National Housing Company news — Sakani, Ejar, housing policy",
    },
    {
        "name": "REGA News",
        "url": "https://www.rega.gov.sa/en/MediaCenter/news",
        "description": "REGA regulatory updates — licensing, market rules, indicators",
    },
]

# ── API Endpoints to monitor ──────────────────────────────────────────
# Seeded on first run. check_type: "json_hash" (content change) or
# "json_count" (track record count in response array).
# Auth: NHC endpoints work with "Bearer null" header.

SEED_ENDPOINTS: list[dict] = [
    # ── NHC / Ejar Indicators (Bearer null auth) ───────────────────
    {
        "endpoint_id": "nhc-ejar-last-contract",
        "source": "NHC",
        "name": "Ejar Last Contract Date (freshness signal)",
        "url": "https://bisolutions.nhc.sa/RealEstateIndicatorsAPIs/api/IndicatorEjar/GetLastContractDate",
        "check_type": "json_hash",
    },
    {
        "endpoint_id": "nhc-ejar-saudi-stats",
        "source": "NHC",
        "name": "Ejar Saudi National Statistics",
        "url": "https://bisolutions.nhc.sa/RealEstateIndicatorsAPIs/api/IndicatorEjar/GetSaudiStatistics",
        "check_type": "json_hash",
        "method": "POST",
        "post_body": "{}",
    },
    {
        "endpoint_id": "nhc-ejar-regions-stats",
        "source": "NHC",
        "name": "Ejar Regional Statistics (13 regions)",
        "url": "https://bisolutions.nhc.sa/RealEstateIndicatorsAPIs/api/IndicatorEjar/GetRegionsStatistics",
        "check_type": "json_hash",
        "method": "POST",
        "post_body": "{}",
    },
    {
        "endpoint_id": "nhc-ejar-regions",
        "source": "NHC",
        "name": "Ejar Regions List",
        "url": "https://bisolutions.nhc.sa/RealEstateIndicatorsAPIs/api/IndicatorEjar/GetAllRegions",
        "check_type": "json_count",
    },
    # ── REGA Ejar Charts (Bearer null auth, REGA domain) ────────────
    {
        "endpoint_id": "rega-ejar-price-index",
        "source": "REGA",
        "name": "Ejar Price Index (quarterly timeseries)",
        "url": "https://rentalrei.rega.gov.sa/RegaIndicatorsAPIs/api/IndicatorEjar/GetChartPublicIndicatorsDemo",
        "check_type": "json_hash",
        "method": "POST",
        "post_body": "{}",
    },
    # ── KAPSARC (ODS v2.1 API — no auth needed) ────────────────────
    {
        "endpoint_id": "kapsarc-re-index-2014",
        "source": "KAPSARC",
        "name": "RE Price Index (2014=100)",
        "url": "https://data.kapsarc.org/api/explore/v2.1/catalog/datasets/real-estate-indices",
        "check_type": "json_hash",
    },
    {
        "endpoint_id": "kapsarc-re-index-2023",
        "source": "KAPSARC",
        "name": "RE Price Index (2023=100)",
        "url": "https://data.kapsarc.org/api/explore/v2.1/catalog/datasets/real-estate-price-index-by-sector-2023-100",
        "check_type": "json_hash",
    },
    {
        "endpoint_id": "kapsarc-re-regions-2014",
        "source": "KAPSARC",
        "name": "RE Index by Regions (2014=100)",
        "url": "https://data.kapsarc.org/api/explore/v2.1/catalog/datasets/real-estate-indices-by-regions",
        "check_type": "json_hash",
    },
    {
        "endpoint_id": "kapsarc-re-regions-2023",
        "source": "KAPSARC",
        "name": "RE Index by Regions (2023=100)",
        "url": "https://data.kapsarc.org/api/explore/v2.1/catalog/datasets/real-estate-indices-by-regions-2023-100",
        "check_type": "json_hash",
    },
    {
        "endpoint_id": "kapsarc-building-permits",
        "source": "KAPSARC",
        "name": "Building Permits by Region",
        "url": "https://data.kapsarc.org/api/explore/v2.1/catalog/datasets/building-permits-issued-by-municipalities-by-regions-and-type-of-permit-1987-201",
        "check_type": "json_hash",
    },
    {
        "endpoint_id": "kapsarc-construction-cost",
        "source": "KAPSARC",
        "name": "Construction Cost Index",
        "url": "https://data.kapsarc.org/api/explore/v2.1/catalog/datasets/construction-cost-indices-by-sector-and-section",
        "check_type": "json_hash",
    },
    {
        "endpoint_id": "kapsarc-new-re-datasets",
        "source": "KAPSARC",
        "name": "New KAPSARC RE Datasets",
        "url": "https://data.kapsarc.org/api/explore/v2.1/catalog/datasets?where=search(title,%22real%20estate%22)%20OR%20search(title,%22housing%22)%20OR%20search(title,%22construction%22)%20OR%20search(title,%22mortgage%22)&order_by=modified%20DESC&limit=20",
        "check_type": "json_count",
    },
    # ── SAMA (Monthly Statistical Bulletin — primary RE finance data) ─
    {
        "endpoint_id": "sama-monthly-bulletin-page",
        "source": "SAMA",
        "name": "SAMA Monthly Statistics Page",
        "url": "https://www.sama.gov.sa/en-US/EconomicReports/Pages/MonthlyStatistics.aspx",
        "check_type": "json_hash",
    },
    {
        "endpoint_id": "sama-fin-stability",
        "source": "SAMA",
        "name": "SAMA Financial Stability Reports Page",
        "url": "https://www.sama.gov.sa/en-US/EconomicReports/Pages/FinancialStabilityReport.aspx",
        "check_type": "json_hash",
    },
    # ── RSS / News Feeds ─────────────────────────────────────────────
    {
        "endpoint_id": "baladiya-news",
        "source": "BALADIYA",
        "name": "Baladiya Municipal News (JSON API)",
        "url": "https://balady.gov.sa/api/news?page=0",
        "check_type": "json_count",
    },
    {
        "endpoint_id": "saudigazette-business-rss",
        "source": "MEDIA",
        "name": "Saudi Gazette Business RSS",
        "url": "https://saudigazette.com.sa/rss/business",
        "check_type": "json_hash",
    },
    {
        "endpoint_id": "momah-sitemap",
        "source": "MOMAH",
        "name": "MOMAH News Sitemap",
        "url": "https://momah.gov.sa/sitemap.xml",
        "check_type": "json_hash",
    },
    # ── Etimad (Government Procurement — public API, no auth) ────────
    {
        "endpoint_id": "etimad-re-tenders",
        "source": "ETIMAD",
        "name": "Etimad RE & Land Tenders (Activity 4)",
        "url": "https://tenders.etimad.sa/Tender/AllSupplierTendersForVisitorAsync?PageSize=10&pageNumber=1&TenderActivityId=4&IsSearch=true&Sort=SubmitionDate&SortDirection=DESC",
        "check_type": "json_count",
    },
    {
        "endpoint_id": "etimad-construction-tenders",
        "source": "ETIMAD",
        "name": "Etimad Construction Tenders (Activity 2, Active)",
        "url": "https://tenders.etimad.sa/Tender/AllSupplierTendersForVisitorAsync?PageSize=10&pageNumber=1&TenderActivityId=2&TenderCategory=2&IsSearch=true&Sort=SubmitionDate&SortDirection=DESC",
        "check_type": "json_count",
    },
    # ── MOJ SharePoint REST API (cracked — no auth needed) ───────────
    {
        "endpoint_id": "moj-news-ar",
        "source": "MOJ",
        "name": "MOJ Arabic News (1,717 items via SharePoint API)",
        "url": "https://www.moj.gov.sa/_api/web/lists(guid'0509935e-ac5b-4a88-8488-ea39b14f05eb')/items?$top=5&$select=Id,Title,Created&$orderby=Created%20desc",
        "check_type": "json_hash",
    },
    # ── NHC Drupal API (cracked — POST to /api/news/) ────────────────
    {
        "endpoint_id": "nhc-news",
        "source": "NHC",
        "name": "NHC News (427 articles via Drupal proxy)",
        "url": "https://nhc.sa/api/news/",
        "check_type": "json_hash",
        "method": "POST",
        "post_body": '{"locale": "ar", "page": 1}',
    },
]

# Request settings
REQUEST_TIMEOUT = 30
REQUEST_DELAY = 1.0  # seconds between API calls

# ── Logging ───────────────────────────────────────────────────────────

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler(LOG_FILE, encoding="utf-8"),
        logging.StreamHandler(),
    ],
)
log = logging.getLogger("re_data_monitor")


# ── State Database ────────────────────────────────────────────────────


def init_state_db():
    """Create state tracking tables."""
    conn = sqlite3.connect(str(STATE_DB))
    conn.execute("PRAGMA journal_mode=WAL")
    conn.executescript("""
        CREATE TABLE IF NOT EXISTS known_datasets (
            dataset_id TEXT PRIMARY KEY,
            source TEXT NOT NULL,
            title_ar TEXT,
            title_en TEXT,
            resource_count INTEGER,
            first_seen TEXT NOT NULL,
            last_checked TEXT NOT NULL
        );

        CREATE TABLE IF NOT EXISTS known_resources (
            resource_id TEXT PRIMARY KEY,
            dataset_id TEXT NOT NULL,
            filename TEXT,
            format TEXT,
            first_seen TEXT NOT NULL,
            FOREIGN KEY (dataset_id) REFERENCES known_datasets(dataset_id)
        );

        CREATE TABLE IF NOT EXISTS page_hashes (
            url TEXT PRIMARY KEY,
            name TEXT,
            content_hash TEXT,
            last_checked TEXT NOT NULL,
            last_changed TEXT
        );

        CREATE TABLE IF NOT EXISTS file_sizes (
            file_path TEXT PRIMARY KEY,
            dataset_id TEXT,
            cdn_url TEXT,
            local_size INTEGER,
            remote_size INTEGER,
            last_checked TEXT NOT NULL
        );

        CREATE TABLE IF NOT EXISTS api_endpoints (
            endpoint_id TEXT PRIMARY KEY,
            source TEXT NOT NULL,
            name TEXT,
            url TEXT NOT NULL,
            method TEXT NOT NULL DEFAULT 'GET',
            post_body TEXT,
            check_type TEXT NOT NULL DEFAULT 'json_hash',
            last_hash TEXT,
            last_record_count INTEGER,
            last_checked TEXT,
            last_changed TEXT,
            enabled INTEGER DEFAULT 1
        );

        CREATE TABLE IF NOT EXISTS check_log (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            check_time TEXT NOT NULL,
            source TEXT,
            new_datasets INTEGER DEFAULT 0,
            new_resources INTEGER DEFAULT 0,
            page_changes INTEGER DEFAULT 0,
            api_changes INTEGER DEFAULT 0,
            size_changes INTEGER DEFAULT 0,
            errors TEXT,
            email_sent INTEGER DEFAULT 0
        );
    """)
    conn.commit()
    return conn


def seed_api_endpoints(conn: sqlite3.Connection) -> None:
    """Register seed API endpoints if not already present."""
    for ep in SEED_ENDPOINTS:
        existing = conn.execute(
            "SELECT endpoint_id FROM api_endpoints WHERE endpoint_id = ?",
            (ep["endpoint_id"],),
        ).fetchone()
        if existing is None:
            conn.execute(
                """INSERT INTO api_endpoints
                   (endpoint_id, source, name, url, method, post_body, check_type, enabled)
                   VALUES (?, ?, ?, ?, ?, ?, ?, 1)""",
                (
                    ep["endpoint_id"],
                    ep["source"],
                    ep["name"],
                    ep["url"],
                    ep.get("method", "GET"),
                    ep.get("post_body"),
                    ep["check_type"],
                ),
            )
            log.info(f"  Seeded endpoint: {ep['name']}")
    conn.commit()


# ── API Helpers ───────────────────────────────────────────────────────


def fetch_url(
    url: str,
    timeout: int = REQUEST_TIMEOUT,
    extra_headers: dict | None = None,
    post_data: bytes | None = None,
) -> bytes | None:
    """Fetch a URL with Safari user agent. Returns bytes or None on error."""
    headers = {
        "User-Agent": USER_AGENT,
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Language": "ar,en;q=0.9",
    }
    if extra_headers:
        headers.update(extra_headers)
    req = urllib.request.Request(url, headers=headers, data=post_data)
    # Some Saudi gov sites have cert issues — use unverified context as fallback
    ctx = ssl.create_default_context()
    try:
        with urllib.request.urlopen(req, timeout=timeout, context=ctx) as resp:
            return resp.read()
    except ssl.SSLError:
        log.info(f"SSL error for {url}, retrying with unverified context")
        ctx_noverify = ssl._create_unverified_context()
        try:
            with urllib.request.urlopen(
                req, timeout=timeout, context=ctx_noverify
            ) as resp:
                return resp.read()
        except Exception as e:
            log.warning(f"Failed to fetch {url} (even unverified): {e}")
            return None
    except (urllib.error.URLError, urllib.error.HTTPError, TimeoutError) as e:
        log.warning(f"Failed to fetch {url}: {e}")
        return None


def fetch_json(url: str) -> dict | list | None:
    """Fetch and parse JSON from a URL."""
    data = fetch_url(url)
    if data is None:
        return None
    try:
        return json.loads(data)
    except json.JSONDecodeError as e:
        log.warning(f"JSON decode error for {url}: {e}")
        return None


# ── Dataset Monitoring ────────────────────────────────────────────────


def fetch_org_datasets(org_name_ar: str) -> list[dict]:
    """Fetch all datasets for an organization from the Open Data portal."""
    encoded = urllib.parse.quote(org_name_ar)
    url = f"{OPEN_DATA_API}?version=-1&organization={encoded}"
    result = fetch_json(url)

    if result is None:
        return []

    # The API returns a dict with 'datasets' key
    if isinstance(result, dict):
        return result.get("datasets", [])
    elif isinstance(result, list):
        # Sometimes returns a list of orgs
        for org in result:
            if isinstance(org, dict) and org.get("datasets"):
                return org["datasets"]
    return []


def is_re_dataset(dataset: dict) -> bool:
    """Check if a dataset is real-estate related (for MOJ filtering)."""
    title = dataset.get("titleAr", "") + " " + dataset.get("title", "")
    return any(kw in title for kw in RE_KEYWORDS)


def fetch_dataset_resources(dataset_id: str) -> list[dict]:
    """Fetch resources (downloadable files) for a dataset."""
    url = f"https://open.data.gov.sa/data/api/datasets/resources?version=-1&dataset={dataset_id}"
    result = fetch_json(url)
    if isinstance(result, list):
        return result
    if isinstance(result, dict):
        return result.get("resources", [])
    return []


CAPTURABLE_FORMATS = {"CSV", "XLSX", "XLS", "JSON"}
DOWNLOAD_ODP_BASE = "https://open.data.gov.sa/odp-public"


def _try_capture_resource(
    source: str, dataset_id: str, res_name: str, res_format: str
) -> str | None:
    """Attempt to download a new resource file to captured/ staging directory.

    Returns the local file path on success, None on failure.
    Gov portals may publish files temporarily — grab them while available.
    """
    if res_format.upper() not in CAPTURABLE_FORMATS:
        return None

    CAPTURE_DIR.mkdir(exist_ok=True)
    ext = res_format.lower()
    today = datetime.now().strftime("%Y%m%d")
    safe_name = re.sub(r"[^\w\-.]", "_", res_name)[:80]
    local_path = CAPTURE_DIR / f"{source}_{today}_{safe_name}.{ext}"

    if local_path.exists():
        return str(local_path)

    # Try the dataset detail API to get the download URL
    detail_url = f"https://open.data.gov.sa/api/datasets/{dataset_id}"
    detail = fetch_json(detail_url)
    if detail and isinstance(detail, dict):
        for res in detail.get("resources", []):
            if res.get("format", "").upper() == res_format.upper():
                url_path = res.get("url", "")
                if url_path:
                    parts = url_path.split("/")
                    if len(parts) >= 4:
                        encoded = urllib.parse.quote(parts[-1])
                        dl_url = f"{DOWNLOAD_ODP_BASE}/{'/'.join(parts[:-1])}/{encoded}"
                    else:
                        dl_url = f"{DOWNLOAD_ODP_BASE}/{urllib.parse.quote(url_path)}"

                    data = fetch_url(dl_url)
                    if data and len(data) > 100 and b"Request Rejected" not in data:
                        local_path.write_bytes(data)
                        log.info(
                            f"    CAPTURED: {local_path.name} ({len(data):,} bytes)"
                        )
                        return str(local_path)

    log.debug(f"    Could not capture {res_name}.{ext}")
    return None


def check_datasets(conn: sqlite3.Connection) -> tuple[list[dict], list[dict]]:
    """
    Check all monitored organizations for new datasets and resources.
    Returns (new_datasets, new_resources).
    """
    now = datetime.now(timezone.utc).isoformat()
    new_datasets = []
    new_resources = []

    for source, org_name in ORGANIZATIONS.items():
        log.info(f"Checking {source} ({org_name})...")
        datasets = fetch_org_datasets(org_name)

        if not datasets:
            log.warning(f"No datasets returned for {source}")
            continue

        log.info(f"  Found {len(datasets)} total datasets for {source}")

        for ds in datasets:
            ds_id = ds.get("id", "")
            title_ar = ds.get("titleAr", "")
            title_en = ds.get("title", "")

            if not ds_id:
                continue

            # For MOJ/GASTAT, filter to RE-related datasets only (998/1180 total)
            if source in ("MOJ", "GASTAT") and not is_re_dataset(ds):
                continue

            # Check if we've seen this dataset before
            existing = conn.execute(
                "SELECT dataset_id, resource_count FROM known_datasets WHERE dataset_id = ?",
                (ds_id,),
            ).fetchone()

            if existing is None:
                # New dataset!
                new_datasets.append(
                    {
                        "source": source,
                        "dataset_id": ds_id,
                        "title_ar": title_ar,
                        "title_en": title_en,
                    }
                )
                conn.execute(
                    """INSERT INTO known_datasets
                       (dataset_id, source, title_ar, title_en, resource_count, first_seen, last_checked)
                       VALUES (?, ?, ?, ?, 0, ?, ?)""",
                    (ds_id, source, title_ar, title_en, now, now),
                )
                log.info(f"  NEW dataset: {title_ar} ({ds_id})")
            else:
                conn.execute(
                    "UPDATE known_datasets SET last_checked = ? WHERE dataset_id = ?",
                    (now, ds_id),
                )

            # Check resources for this dataset
            time.sleep(REQUEST_DELAY)
            resources = fetch_dataset_resources(ds_id)

            for res in resources:
                res_id = res.get("id", res.get("resourceId", ""))
                res_name = res.get("name", res.get("resourceName", ""))
                res_format = res.get("format", "")

                if not res_id:
                    continue

                existing_res = conn.execute(
                    "SELECT resource_id FROM known_resources WHERE resource_id = ?",
                    (res_id,),
                ).fetchone()

                if existing_res is None:
                    new_resources.append(
                        {
                            "source": source,
                            "dataset_id": ds_id,
                            "dataset_title": title_ar,
                            "resource_id": res_id,
                            "filename": res_name,
                            "format": res_format,
                        }
                    )
                    conn.execute(
                        """INSERT INTO known_resources
                           (resource_id, dataset_id, filename, format, first_seen)
                           VALUES (?, ?, ?, ?, ?)""",
                        (res_id, ds_id, res_name, res_format, now),
                    )
                    log.info(f"    NEW resource: {res_name} ({res_format})")

                    # Opportunistic capture — grab CSV/XLSX while available
                    captured = _try_capture_resource(
                        source, ds_id, res_name, res_format
                    )
                    if captured:
                        new_resources[-1]["captured_path"] = captured

            # Update resource count
            res_count = conn.execute(
                "SELECT COUNT(*) FROM known_resources WHERE dataset_id = ?",
                (ds_id,),
            ).fetchone()[0]
            conn.execute(
                "UPDATE known_datasets SET resource_count = ? WHERE dataset_id = ?",
                (res_count, ds_id),
            )

        time.sleep(REQUEST_DELAY)

    conn.commit()
    return new_datasets, new_resources


# ── Page Change Monitoring ────────────────────────────────────────────


def check_pages(conn: sqlite3.Connection) -> list[dict]:
    """Check monitored pages for content changes. Returns list of changed pages."""
    now = datetime.now(timezone.utc).isoformat()
    changes = []

    for page in MONITORED_PAGES:
        url = page["url"]
        name = page["name"]
        log.info(f"Checking page: {name} ({url})")

        content = fetch_url(url)
        if content is None:
            log.warning(f"  Could not fetch {name}")
            continue

        content_hash = hashlib.sha256(content).hexdigest()

        existing = conn.execute(
            "SELECT content_hash FROM page_hashes WHERE url = ?",
            (url,),
        ).fetchone()

        if existing is None:
            # First time seeing this page — record baseline
            conn.execute(
                """INSERT INTO page_hashes (url, name, content_hash, last_checked, last_changed)
                   VALUES (?, ?, ?, ?, ?)""",
                (url, name, content_hash, now, now),
            )
            log.info(f"  Baseline recorded for {name}")
        elif existing[0] != content_hash:
            # Page changed!
            changes.append(
                {
                    "name": name,
                    "url": url,
                    "description": page["description"],
                    "old_hash": existing[0][:12],
                    "new_hash": content_hash[:12],
                }
            )
            conn.execute(
                """UPDATE page_hashes
                   SET content_hash = ?, last_checked = ?, last_changed = ?
                   WHERE url = ?""",
                (content_hash, now, now, url),
            )
            log.info(f"  CHANGED: {name}")
        else:
            conn.execute(
                "UPDATE page_hashes SET last_checked = ? WHERE url = ?",
                (now, url),
            )
            log.info(f"  No change: {name}")

        time.sleep(REQUEST_DELAY)

    conn.commit()
    return changes


# ── File Size Change Detection ────────────────────────────────────────

DOWNLOAD_ODP = "https://open.data.gov.sa/odp-public"
MOJ_ORG_ID = "35c63412-c4ae-4303-8fef-56cfd71303cf"


def _get_remote_size(url: str) -> int | None:
    """Get remote file size via Range GET (HEAD Content-Length is unreliable)."""
    headers = {
        "User-Agent": USER_AGENT,
        "Range": "bytes=0-0",
    }
    req = urllib.request.Request(url, headers=headers)
    ctx = ssl._create_unverified_context()
    try:
        with urllib.request.urlopen(req, timeout=REQUEST_TIMEOUT, context=ctx) as resp:
            cr = resp.headers.get("Content-Range", "")
            if "/" in cr:
                try:
                    return int(cr.split("/")[1])
                except (ValueError, IndexError):
                    return None
    except Exception:
        return None
    return None


def check_file_sizes(conn: sqlite3.Connection) -> list[dict]:
    """Check tracked MOJ CSV files for size changes (corrections on portal)."""
    now = datetime.now(timezone.utc).isoformat()
    changes = []

    rows = conn.execute("""
        SELECT r.resource_id, r.dataset_id, r.filename, r.format
        FROM known_resources r
        JOIN known_datasets d ON d.dataset_id = r.dataset_id
        WHERE d.source = 'MOJ' AND r.format = 'CSV' AND r.filename IS NOT NULL
    """).fetchall()

    checked = 0
    for _res_id, ds_id, filename, _fmt in rows:
        encoded = urllib.parse.quote(f"{filename}.csv")
        cdn_url = f"{DOWNLOAD_ODP}/{MOJ_ORG_ID}/{ds_id}/v1/{encoded}"

        # Check if we have a recorded size
        existing = conn.execute(
            "SELECT local_size, remote_size FROM file_sizes WHERE cdn_url = ?",
            (cdn_url,),
        ).fetchone()

        remote_size = _get_remote_size(cdn_url)
        if remote_size is None:
            # Try uppercase
            cdn_url_upper = (
                f"{DOWNLOAD_ODP}/{MOJ_ORG_ID.upper()}/{ds_id.upper()}/v1/{encoded}"
            )
            remote_size = _get_remote_size(cdn_url_upper)
            if remote_size is not None:
                cdn_url = cdn_url_upper

        if remote_size is None:
            continue

        checked += 1

        if existing is None:
            # First time — record baseline
            conn.execute(
                """INSERT INTO file_sizes (file_path, dataset_id, cdn_url, local_size, remote_size, last_checked)
                   VALUES (?, ?, ?, ?, ?, ?)""",
                (filename, ds_id, cdn_url, remote_size, remote_size, now),
            )
        elif existing[1] != remote_size and abs(existing[1] - remote_size) > 3:
            old_size = existing[1]
            diff = remote_size - old_size
            sign = "+" if diff > 0 else ""
            changes.append(
                {
                    "filename": filename,
                    "old_size": old_size,
                    "new_size": remote_size,
                    "diff": f"{sign}{diff}",
                }
            )
            conn.execute(
                "UPDATE file_sizes SET remote_size = ?, last_checked = ? WHERE cdn_url = ?",
                (remote_size, now, cdn_url),
            )
            log.warning(
                f"  SIZE CHANGED: {filename} — {old_size} -> {remote_size} ({sign}{diff} bytes)"
            )
        else:
            conn.execute(
                "UPDATE file_sizes SET last_checked = ? WHERE cdn_url = ?",
                (now, cdn_url),
            )

        time.sleep(0.3)

    conn.commit()
    log.info(f"  Checked {checked} file sizes, {len(changes)} changed")
    return changes


# ── API Endpoint Monitoring ──────────────────────────────────────────


def check_api_endpoints(conn: sqlite3.Connection) -> list[dict]:
    """Check registered API endpoints for data changes."""
    now = datetime.now(timezone.utc).isoformat()
    changes = []

    rows = conn.execute(
        "SELECT endpoint_id, source, name, url, method, post_body, check_type, last_hash, last_record_count "
        "FROM api_endpoints WHERE enabled = 1"
    ).fetchall()

    for (
        eid,
        source,
        name,
        url,
        method,
        post_body,
        check_type,
        last_hash,
        last_count,
    ) in rows:
        # Source-specific headers
        extra = {}
        if source in ("NHC", "REGA"):
            extra["Authorization"] = "Bearer null"
        if source == "MOJ":
            extra["Accept"] = "application/json;odata=nometadata"
        if eid == "nhc-news":
            extra["Referer"] = "https://nhc.sa/ar/media-center/news/"
            extra["Origin"] = "https://nhc.sa"
        if method == "POST":
            extra["Content-Type"] = "application/json"

        data = fetch_url(
            url,
            extra_headers=extra or None,
            post_data=post_body.encode() if post_body else None,
        )
        if data is None:
            log.debug(f"  Could not fetch API endpoint: {name}")
            continue

        current_hash = hashlib.sha256(data).hexdigest()

        if check_type == "json_count":
            # Track record count from JSON response
            try:
                parsed = json.loads(data)
                if isinstance(parsed, list):
                    current_count = len(parsed)
                elif isinstance(parsed, dict):
                    # Try common wrapper patterns
                    for key in ("data", "results", "records", "items", "datasets"):
                        if key in parsed and isinstance(parsed[key], list):
                            current_count = len(parsed[key])
                            break
                    else:
                        current_count = None
                else:
                    current_count = None
            except json.JSONDecodeError:
                current_count = None

            if (
                current_count is not None
                and last_count is not None
                and current_count != last_count
            ):
                changes.append(
                    {
                        "source": source,
                        "name": name,
                        "url": url,
                        "detail": f"Record count: {last_count} -> {current_count}",
                    }
                )
                log.info(
                    f"  API CHANGED: {name} — {last_count} -> {current_count} records"
                )

            conn.execute(
                "UPDATE api_endpoints SET last_hash = ?, last_record_count = ?, last_checked = ? WHERE endpoint_id = ?",
                (current_hash, current_count, now, eid),
            )

        else:
            # Default: hash comparison
            if last_hash is not None and current_hash != last_hash:
                changes.append(
                    {
                        "source": source,
                        "name": name,
                        "url": url,
                        "detail": f"Content changed (hash {last_hash[:12]}... -> {current_hash[:12]}...)",
                    }
                )
                log.info(f"  API CHANGED: {name}")
                conn.execute(
                    "UPDATE api_endpoints SET last_hash = ?, last_checked = ?, last_changed = ? WHERE endpoint_id = ?",
                    (current_hash, now, now, eid),
                )
            else:
                conn.execute(
                    "UPDATE api_endpoints SET last_hash = ?, last_checked = ? WHERE endpoint_id = ?",
                    (current_hash, now, eid),
                )

        time.sleep(REQUEST_DELAY)

    conn.commit()
    log.info(f"  Checked {len(rows)} API endpoints, {len(changes)} changed")
    return changes


# ── Email Notification ────────────────────────────────────────────────


def send_email(subject: str, body: str) -> bool:
    """Send email through a remote mail relay via SSH.

    Configure via environment variables:
        MAIL_RELAY: SSH hostname of the mail relay (required for email alerts)
        NOTIFY_EMAIL: recipient address
        SENDER_EMAIL: sender address
    """
    mail_relay = os.environ.get("MAIL_RELAY", "")
    if not mail_relay:
        log.warning("MAIL_RELAY not set — email alerts disabled")
        return False

    message = f"""From: {SENDER_EMAIL}
To: {NOTIFY_EMAIL}
Subject: {subject}
Content-Type: text/plain; charset=UTF-8
MIME-Version: 1.0

{body}"""

    try:
        result = subprocess.run(
            ["ssh", mail_relay, "sendmail", "-t"],
            input=message,
            capture_output=True,
            text=True,
            timeout=30,
        )
        if result.returncode == 0:
            log.info(f"Email sent: {subject}")
            return True
        else:
            log.error(f"Email failed (rc={result.returncode}): {result.stderr}")
            return False
    except subprocess.TimeoutExpired:
        log.error("Email send timed out")
        return False
    except Exception as e:
        log.error(f"Email send error: {e}")
        return False


def build_alert_email(
    new_datasets: list[dict],
    new_resources: list[dict],
    page_changes: list[dict],
    api_changes: list[dict] | None = None,
    size_changes: list[dict] | None = None,
) -> tuple[str, str]:
    """Build email subject and body for alerts."""
    api_changes = api_changes or []
    size_changes = size_changes or []

    parts = []
    if new_datasets:
        parts.append(f"{len(new_datasets)} new dataset(s)")
    if new_resources:
        parts.append(f"{len(new_resources)} new file(s)")
    if page_changes:
        parts.append(f"{len(page_changes)} page change(s)")
    if api_changes:
        parts.append(f"{len(api_changes)} API update(s)")
    if size_changes:
        parts.append(f"{len(size_changes)} file correction(s)")

    subject = f"[RE Monitor] {', '.join(parts)}"

    lines = [
        "Real Estate Data Monitor — New Activity Detected",
        f"Check time: {datetime.now().strftime('%Y-%m-%d %H:%M')}",
        "",
    ]

    if new_datasets:
        lines.append("=" * 50)
        lines.append("NEW DATASETS")
        lines.append("=" * 50)
        for ds in new_datasets:
            lines.append(f"\n  Source: {ds['source']}")
            lines.append(f"  Title:  {ds['title_ar']}")
            if ds.get("title_en"):
                lines.append(f"  EN:     {ds['title_en']}")
            lines.append(f"  ID:     {ds['dataset_id']}")
        lines.append("")

    if new_resources:
        lines.append("=" * 50)
        lines.append("NEW FILES (Resources)")
        lines.append("=" * 50)
        for res in new_resources:
            lines.append(f"\n  Dataset: {res['dataset_title']}")
            lines.append(f"  File:    {res['filename']}")
            lines.append(f"  Format:  {res['format']}")
            lines.append(f"  Source:  {res['source']}")
            if res.get("captured_path"):
                lines.append(f"  >>> CAPTURED: {res['captured_path']}")
        lines.append("")

    if size_changes:
        lines.append("=" * 50)
        lines.append("FILE CORRECTIONS (Size Changes)")
        lines.append("=" * 50)
        for sc in size_changes:
            lines.append(f"\n  File:   {sc['filename']}")
            lines.append(
                f"  Size:   {sc['old_size']:,} -> {sc['new_size']:,} bytes ({sc['diff']})"
            )
        lines.append("")
        lines.append(
            "  Action: Run 'python3 scripts/download_new_data.py --check-updates --redownload-changed'"
        )
        lines.append("")

    if api_changes:
        lines.append("=" * 50)
        lines.append("API DATA UPDATES")
        lines.append("=" * 50)
        for ac in api_changes:
            lines.append(f"\n  Source: {ac['source']}")
            lines.append(f"  Name:   {ac['name']}")
            lines.append(f"  Detail: {ac['detail']}")
        lines.append("")

    if page_changes:
        lines.append("=" * 50)
        lines.append("PAGE CHANGES")
        lines.append("=" * 50)
        for pc in page_changes:
            lines.append(f"\n  Page: {pc['name']}")
            lines.append(f"  URL:  {pc['url']}")
            lines.append(f"  Info: {pc['description']}")
            lines.append(f"  Hash: {pc['old_hash']}... -> {pc['new_hash']}...")
        lines.append("")

    lines.append("-" * 50)
    lines.append("Action: Review new data and download if relevant.")
    lines.append("Open Data Portal: https://open.data.gov.sa")
    lines.append("White Land Tax: https://idlelands.momah.gov.sa/ar")

    return subject, "\n".join(lines)


# ── Main ──────────────────────────────────────────────────────────────


def main():
    log.info("=" * 50)
    log.info("Real Estate Data Monitor starting")

    conn = init_state_db()
    seed_api_endpoints(conn)
    errors = []

    # Check Open Data portal datasets (MOJ, REGA, GASTAT)
    try:
        new_datasets, new_resources = check_datasets(conn)
    except Exception as e:
        log.error(f"Dataset check failed: {e}")
        new_datasets, new_resources = [], []
        errors.append(f"Dataset check: {e}")

    # Check monitored pages for content changes
    try:
        page_changes = check_pages(conn)
    except Exception as e:
        log.error(f"Page check failed: {e}")
        page_changes = []
        errors.append(f"Page check: {e}")

    # Check API endpoints for data updates (NHC, KAPSARC, SAMA, etc.)
    try:
        api_changes = check_api_endpoints(conn)
    except Exception as e:
        log.error(f"API endpoint check failed: {e}")
        api_changes = []
        errors.append(f"API check: {e}")

    # Check existing MOJ files for size changes (portal corrections)
    # Only run on Wednesdays to avoid daily CDN hammering (195+ Range GETs)
    size_changes = []
    if datetime.now().weekday() == 2:  # Wednesday
        try:
            log.info("Weekly file size check (Wednesday)...")
            size_changes = check_file_sizes(conn)
        except Exception as e:
            log.error(f"File size check failed: {e}")
            errors.append(f"Size check: {e}")

    # Send notification if anything new
    email_sent = 0
    has_changes = (
        new_datasets or new_resources or page_changes or api_changes or size_changes
    )
    if has_changes:
        subject, body = build_alert_email(
            new_datasets, new_resources, page_changes, api_changes, size_changes
        )
        if send_email(subject, body):
            email_sent = 1
    else:
        log.info("No new data or changes detected")

    # Log the check
    now = datetime.now(timezone.utc).isoformat()
    conn.execute(
        """INSERT INTO check_log
           (check_time, source, new_datasets, new_resources, page_changes,
            api_changes, size_changes, errors, email_sent)
           VALUES (?, 'all', ?, ?, ?, ?, ?, ?, ?)""",
        (
            now,
            len(new_datasets),
            len(new_resources),
            len(page_changes),
            len(api_changes),
            len(size_changes),
            "; ".join(errors) if errors else None,
            email_sent,
        ),
    )
    conn.commit()

    # Summary
    total_datasets = conn.execute("SELECT COUNT(*) FROM known_datasets").fetchone()[0]
    total_resources = conn.execute("SELECT COUNT(*) FROM known_resources").fetchone()[0]
    total_endpoints = conn.execute(
        "SELECT COUNT(*) FROM api_endpoints WHERE enabled = 1"
    ).fetchone()[0]
    log.info(
        f"Done. Tracking {total_datasets} datasets, {total_resources} resources, "
        f"{total_endpoints} API endpoints. "
        f"New: {len(new_datasets)} datasets, {len(new_resources)} files, "
        f"{len(page_changes)} page changes, {len(api_changes)} API updates, "
        f"{len(size_changes)} size changes."
    )

    conn.close()
    return 0 if not errors else 1


if __name__ == "__main__":
    sys.exit(main())
