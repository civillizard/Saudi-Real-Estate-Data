"""iCloud file materializer — force-download iCloud-backed files before use.

The rega-data repo lives inside iCloud Drive
(`~/Library/Mobile Documents/com~apple~CloudDocs/Claude/REGA-Data`). macOS
lazy-downloads files from the cloud when they're first read. For
interactive one-off reads this is fine, but for batch scripts that scan
hundreds of files it creates a silent failure mode:

  - First N files read quickly (they're in the page cache)
  - N+1 hasn't been materialized yet → read blocks in
    `_bufferedreader_fill_buffer` waiting for iCloud to fetch the blob
  - Script appears hung at 0% CPU with no error, for tens of seconds
    per file

The fix: before any script reads all data files in this repo, touch each
file with a small read to materialize it. A parallel pre-read of 369 CSVs
takes ~3-4 minutes on a cold cache; the registry/crawler then runs at
full speed without stalls.

Usage from a script:
    from icloud_materialize import materialize_files
    materialize_files(Path(REPO_ROOT), patterns=("*.csv",))

Or as a standalone command:
    python3 scripts/icloud_materialize.py           # materialize all CSVs
    python3 scripts/icloud_materialize.py xlsx csv  # pick file types

Always safe to run — a no-op if files are already cached.
"""

from __future__ import annotations

import logging
import sys
import time
from pathlib import Path

log = logging.getLogger(__name__)

DEFAULT_PATTERNS = ("*.csv", "*.xlsx")
SKIP_DIRS = {".git", "charts", "__pycache__", "node_modules", "social"}
READ_CHUNK = 4096


def materialize_files(
    root: Path,
    patterns: tuple[str, ...] = DEFAULT_PATTERNS,
    log_progress: bool = True,
) -> tuple[int, float]:
    """Touch every file matching patterns so iCloud materializes it.

    Returns (count, elapsed_seconds).
    """
    start = time.time()
    count = 0
    for pattern in patterns:
        for path in root.rglob(pattern):
            if any(part in SKIP_DIRS for part in path.relative_to(root).parts):
                continue
            try:
                with open(path, "rb") as f:
                    f.read(READ_CHUNK)
            except OSError as exc:
                log.warning("materialize failed: %s: %s", path, exc)
                continue
            count += 1
            if log_progress and count % 50 == 0:
                log.info(
                    "  materialized %d files (%.1fs elapsed)",
                    count,
                    time.time() - start,
                )
    elapsed = time.time() - start
    if log_progress:
        log.info("iCloud materialize: %d files in %.1fs", count, elapsed)
    return count, elapsed


def main() -> int:
    logging.basicConfig(format="%(levelname)s: %(message)s", level=logging.INFO)
    repo_root = Path(__file__).parent.parent.resolve()
    args = sys.argv[1:]
    if args:
        patterns = tuple(f"*.{a.lstrip('.').lower()}" for a in args)
    else:
        patterns = DEFAULT_PATTERNS
    log.info("Materializing %s under %s", patterns, repo_root)
    materialize_files(repo_root, patterns)
    return 0


if __name__ == "__main__":
    sys.exit(main())
