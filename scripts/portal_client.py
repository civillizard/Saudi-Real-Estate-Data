"""Saudi Open Data portal client — shared stealth bundle.

The portal at open.data.gov.sa is WAF-protected. Every script that talks to
it MUST use the full stealth bundle from request 1: Safari User-Agent, Arabic-
friendly Accept/Accept-Language, portal Referer, cookie jar, and a warmup GET
to collect dm2/BPfffdc833146/BP407814ff before any data request. See
docs/saudi-open-data-portal.md for the full playbook.

Do not hand-roll new clients — import `make_portal_client()` from here so the
working stealth propagates to every codepath.
"""

from __future__ import annotations

import http.cookiejar
import json
import logging
import time
import urllib.error
import urllib.parse
import urllib.request
from typing import Any

log = logging.getLogger(__name__)

PORTAL_BASE = "https://open.data.gov.sa"
WARMUP_URL = f"{PORTAL_BASE}/en"

USER_AGENT = (
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
    "AppleWebKit/605.1.15 (KHTML, like Gecko) "
    "Version/17.0 Safari/605.1.15"
)
HEADERS = [
    ("User-Agent", USER_AGENT),
    ("Accept", "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"),
    ("Accept-Language", "en-US,en;q=0.9"),
    ("Referer", f"{PORTAL_BASE}/"),
]

REQUEST_TIMEOUT = 30
RETRY_BACKOFF = (2.0, 3.0, 4.0)  # seconds between tries; len = max tries
DEFAULT_RATE_LIMIT = 0.3  # seconds between consecutive requests — safe tested cadence

NO_DATA_SENTINEL = b"NO DATA FOUND"
WAF_SENTINEL = b"Request Rejected"


class PortalError(Exception):
    """Base class for portal client errors."""


class WAFBlocked(PortalError):
    """Portal WAF rejected the request. Usually means stealth was downgraded
    or the warmup cookies expired. Check the opener reuse chain."""


class DataWithdrawn(PortalError):
    """Portal returned the 13-byte NO DATA FOUND sentinel — file is gone."""


def make_portal_client() -> urllib.request.OpenerDirector:
    """Build an opener with cookies + browser headers and warm it up.

    Must be called once per script. Reuse the returned opener for all
    subsequent requests in that script so the WAF cookies persist.
    """
    cj = http.cookiejar.CookieJar()
    opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
    opener.addheaders = list(HEADERS)

    try:
        opener.open(WARMUP_URL, timeout=REQUEST_TIMEOUT).read(500)
    except Exception as exc:
        log.warning("Portal warmup failed: %s (continuing, cookies may be absent)", exc)

    cookies_loaded = sorted(c.name for c in cj)
    log.debug("Portal client warmed up. Cookies: %s", cookies_loaded)
    return opener


def encode_url(u: str) -> str:
    """Percent-encode spaces and non-ASCII characters in a portal URL's path.

    Portal filenames often contain spaces (`Doc Attorney CSV.csv`) that Python's
    urllib refuses to open. Quote each path segment individually so forward
    slashes stay intact.
    """
    parts = urllib.parse.urlsplit(u)
    encoded_path = "/".join(
        urllib.parse.quote(seg, safe="") for seg in parts.path.split("/")
    )
    return urllib.parse.urlunsplit(
        (parts.scheme, parts.netloc, encoded_path, parts.query, parts.fragment)
    )


def fetch_bytes(
    opener: urllib.request.OpenerDirector,
    url: str,
    timeout: int = REQUEST_TIMEOUT,
    tries: int = 3,
) -> bytes:
    """GET a URL with retries, WAF detection, and NO-DATA sentinel handling.

    Raises WAFBlocked, DataWithdrawn, or urllib.error.URLError on failure.
    """
    encoded = encode_url(url)
    last_exc: Exception | None = None
    for attempt in range(tries):
        try:
            data = opener.open(encoded, timeout=timeout).read()
        except (urllib.error.URLError, TimeoutError) as exc:
            last_exc = exc
            if attempt < tries - 1:
                time.sleep(RETRY_BACKOFF[min(attempt, len(RETRY_BACKOFF) - 1)])
            continue
        if WAF_SENTINEL in data[:200]:
            raise WAFBlocked(f"WAF rejected {url}")
        if data.strip() == NO_DATA_SENTINEL:
            raise DataWithdrawn(f"Portal returned NO DATA FOUND for {url}")
        return data
    assert last_exc is not None
    raise last_exc


def fetch_json(
    opener: urllib.request.OpenerDirector,
    url: str,
    timeout: int = REQUEST_TIMEOUT,
    tries: int = 3,
) -> Any:
    """GET a portal JSON endpoint with retry + backoff. Intermittent non-JSON
    responses on /data/api/datasets/resources are a known flakiness — retry
    handles them."""
    last_exc: Exception | None = None
    for attempt in range(tries):
        try:
            data = opener.open(url, timeout=timeout).read()
            return json.loads(data)
        except (json.JSONDecodeError, urllib.error.URLError, TimeoutError) as exc:
            last_exc = exc
            if attempt < tries - 1:
                time.sleep(RETRY_BACKOFF[min(attempt, len(RETRY_BACKOFF) - 1)])
    assert last_exc is not None
    raise last_exc


def get_dataset_resources(
    opener: urllib.request.OpenerDirector, dataset_id: str
) -> list[dict]:
    """Return the list of resources (CSV/XLSX/JSON/XML blobs) for a dataset."""
    url = f"{PORTAL_BASE}/data/api/datasets/resources?version=-1&dataset={dataset_id}"
    payload = fetch_json(opener, url)
    if isinstance(payload, dict):
        return payload.get("resources", [])
    if isinstance(payload, list):
        return payload
    return []
