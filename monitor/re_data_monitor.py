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

NOTIFY_EMAIL = os.environ.get("NOTIFY_EMAIL", "")
SENDER_EMAIL = os.environ.get("SENDER_EMAIL", "")

# Saudi Open Data API
OPEN_DATA_API = "https://open.data.gov.sa/data/api/organizations"
USER_AGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15"

# Organizations to monitor
ORGANIZATIONS = {
    "MOJ": "وزارة العدل",
    "REGA": "الهيئة العامة للعقار",
}

# Real estate keywords to filter MOJ datasets (they have 998 total)
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

        CREATE TABLE IF NOT EXISTS check_log (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            check_time TEXT NOT NULL,
            source TEXT,
            new_datasets INTEGER DEFAULT 0,
            new_resources INTEGER DEFAULT 0,
            page_changes INTEGER DEFAULT 0,
            errors TEXT,
            email_sent INTEGER DEFAULT 0
        );
    """)
    conn.commit()
    return conn


# ── API Helpers ───────────────────────────────────────────────────────


def fetch_url(url: str, timeout: int = REQUEST_TIMEOUT) -> bytes | None:
    """Fetch a URL with Safari user agent. Returns bytes or None on error."""
    headers = {
        "User-Agent": USER_AGENT,
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Language": "ar,en;q=0.9",
    }
    req = urllib.request.Request(url, headers=headers)
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

            # For MOJ, filter to RE-related datasets only
            if source == "MOJ" and not is_re_dataset(ds):
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
) -> tuple[str, str]:
    """Build email subject and body for alerts."""
    parts = []
    if new_datasets:
        parts.append(f"{len(new_datasets)} new dataset(s)")
    if new_resources:
        parts.append(f"{len(new_resources)} new file(s)")
    if page_changes:
        parts.append(f"{len(page_changes)} page change(s)")

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
    errors = []

    # Check datasets
    try:
        new_datasets, new_resources = check_datasets(conn)
    except Exception as e:
        log.error(f"Dataset check failed: {e}")
        new_datasets, new_resources = [], []
        errors.append(f"Dataset check: {e}")

    # Check pages
    try:
        page_changes = check_pages(conn)
    except Exception as e:
        log.error(f"Page check failed: {e}")
        page_changes = []
        errors.append(f"Page check: {e}")

    # Send notification if anything new
    email_sent = 0
    if new_datasets or new_resources or page_changes:
        subject, body = build_alert_email(new_datasets, new_resources, page_changes)
        if send_email(subject, body):
            email_sent = 1
    else:
        log.info("No new data or changes detected")

    # Log the check
    now = datetime.now(timezone.utc).isoformat()
    conn.execute(
        """INSERT INTO check_log
           (check_time, source, new_datasets, new_resources, page_changes, errors, email_sent)
           VALUES (?, 'all', ?, ?, ?, ?, ?)""",
        (
            now,
            len(new_datasets),
            len(new_resources),
            len(page_changes),
            "; ".join(errors) if errors else None,
            email_sent,
        ),
    )
    conn.commit()

    # Summary
    total_datasets = conn.execute("SELECT COUNT(*) FROM known_datasets").fetchone()[0]
    total_resources = conn.execute("SELECT COUNT(*) FROM known_resources").fetchone()[0]
    log.info(
        f"Done. Tracking {total_datasets} datasets, {total_resources} resources. "
        f"New: {len(new_datasets)} datasets, {len(new_resources)} files, "
        f"{len(page_changes)} page changes."
    )

    conn.close()
    return 0 if not errors else 1


if __name__ == "__main__":
    sys.exit(main())
