#!/usr/bin/env bash
#
# Semi-automated data update pipeline for Saudi-Real-Estate-Data repo.
#
# Steps:
#   1. Download new files from Open Data portal
#   2. Rebuild registry (classification + metadata)
#   3. Export registry to CSV/JSON
#   4. Auto-generate CHANGELOG entry
#   5. Git commit + push
#
# Usage:
#   ./scripts/update_pipeline.sh              # Full pipeline
#   ./scripts/update_pipeline.sh --dry-run    # Check for new files only
#
# Requires: python3, git, gh (for releases)
# Designed to run after monitor/re_data_monitor.py detects new data.

set -euo pipefail

REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$REPO_ROOT"

DRY_RUN=false
[[ "${1:-}" == "--dry-run" ]] && DRY_RUN=true

TODAY=$(date +%Y-%m-%d)
LOG_PREFIX="[update-pipeline]"

log() { echo "$LOG_PREFIX $*"; }
die() { echo "$LOG_PREFIX ERROR: $*" >&2; exit 1; }

# ── Pre-flight checks ────────────────────────────────────────────────

command -v python3 >/dev/null || die "python3 not found"
command -v git >/dev/null || die "git not found"
[[ -d .git ]] || die "Not a git repo: $REPO_ROOT"
[[ -f monitor/monitor_state.db ]] || die "Monitor state DB not found — run re_data_monitor.py first"

# Ensure clean working tree (registry exports will be regenerated)
if [[ -n "$(git status --porcelain -- moj/ rega/)" ]]; then
    die "Uncommitted data files in moj/ or rega/. Commit or stash first."
fi

# ── Step 1: Download new files ────────────────────────────────────────

log "Step 1: Checking for new files..."

if $DRY_RUN; then
    python3 scripts/download_new_data.py --dry-run
    log "Dry run complete. No changes made."
    exit 0
fi

# Capture download output to parse count
DL_OUTPUT=$(python3 scripts/download_new_data.py 2>&1) || true
echo "$DL_OUTPUT"

# Extract download count
DL_COUNT=$(echo "$DL_OUTPUT" | grep -oP 'Downloaded:\s+\K\d+' || echo "0")
FAIL_COUNT=$(echo "$DL_OUTPUT" | grep -oP 'Failed:\s+\K\d+' || echo "0")

if [[ "$DL_COUNT" == "0" ]]; then
    log "No new files downloaded. Pipeline complete (nothing to do)."
    exit 0
fi

log "Downloaded $DL_COUNT new files ($FAIL_COUNT failed)"

# ── Step 2: Rebuild registry ──────────────────────────────────────────

log "Step 2: Rebuilding registry..."
REG_OUTPUT=$(python3 scripts/build_registry.py 2>&1)
echo "$REG_OUTPUT" | grep -E "^(REGISTRY|  Files|  Total|FILES)" | head -10

# Extract summary stats
TOTAL_FILES=$(echo "$REG_OUTPUT" | grep -oP 'Files cataloged:\s+\K[\d,]+' | tr -d ',')
TOTAL_ROWS=$(echo "$REG_OUTPUT" | grep -oP 'Total data rows:\s+\K[\d,]+' | tr -d ',')

log "Registry: $TOTAL_FILES files, $TOTAL_ROWS rows"

# ── Step 3: Export registry to CSV/JSON ───────────────────────────────

log "Step 3: Exporting registry..."
sqlite3 registry.db ".headers on" ".mode csv" "SELECT * FROM files;" > data/registry_files.csv
sqlite3 registry.db ".headers on" ".mode csv" "SELECT * FROM fields;" > data/registry_fields.csv
sqlite3 registry.db ".headers on" ".mode csv" "SELECT * FROM enum_values;" > data/registry_enums.csv

# JSON exports
python3 -c "
import sqlite3, json
conn = sqlite3.connect('registry.db')
conn.row_factory = sqlite3.Row
files = [dict(r) for r in conn.execute('SELECT * FROM files ORDER BY source, category, filename')]
with open('data/registry.json', 'w') as f:
    json.dump(files, f, indent=2, ensure_ascii=False)

categories = conn.execute('SELECT DISTINCT source, category FROM files WHERE source != \"UNKNOWN\" ORDER BY source, category').fetchall()
schema = {}
for src, cat in categories:
    fields = conn.execute('''
        SELECT DISTINCT f.name_ar, f.canonical_name, f.data_type, f.nullable
        FROM fields f JOIN files fi ON f.file_id = fi.id
        WHERE fi.source = ? AND fi.category = ?
        ORDER BY f.ordinal
    ''', (src, cat)).fetchall()
    schema[f'{src}/{cat}'] = {
        'fields': [{'name_ar': r[0], 'canonical': r[1], 'type': r[2], 'nullable': bool(r[3])} for r in fields],
        'file_count': conn.execute('SELECT count(*) FROM files WHERE source=? AND category=?', (src, cat)).fetchone()[0],
        'total_rows': conn.execute('SELECT sum(row_count) FROM files WHERE source=? AND category=?', (src, cat)).fetchone()[0],
    }
with open('data/schema.json', 'w') as f:
    json.dump(schema, f, indent=2, ensure_ascii=False)
conn.close()
print(f'Exported {len(files)} files, {len(schema)} categories')
"

log "Exports complete"

# ── Step 4: List new files for changelog ──────────────────────────────

log "Step 4: Generating changelog entry..."

# Get list of new CSV files (untracked in moj/ and rega/)
NEW_FILES=$(git ls-files --others --exclude-standard -- moj/ rega/ | sort)
NEW_COUNT=$(echo "$NEW_FILES" | grep -c . || echo "0")

# Categorize new files
NEW_MOJ_RE=$(echo "$NEW_FILES" | grep -c "^moj/real-estate/" || echo "0")
NEW_MOJ_MONTHLY=$(echo "$NEW_FILES" | grep -c "^moj/monthly/" || echo "0")
NEW_MOJ_SALES=$(echo "$NEW_FILES" | grep -c "^moj/sales/" || echo "0")
NEW_REGA=$(echo "$NEW_FILES" | grep -c "^rega/" || echo "0")

# Format total rows for display (e.g., 7447742 → 7.4M)
format_rows() {
    local n=$1
    if (( n >= 1000000 )); then
        printf "%.1fM" "$(echo "scale=1; $n / 1000000" | bc)"
    elif (( n >= 1000 )); then
        printf "%.0fK" "$(echo "scale=0; $n / 1000" | bc)"
    else
        echo "$n"
    fi
}

ROWS_DISPLAY=$(format_rows "$TOTAL_ROWS")
SIZE_MB=$(du -sm moj/ rega/ | awk '{s+=$1} END {print s}')

# Build the changelog entry
CHANGELOG_ENTRY="## $TODAY — Data Update

### Data
- **$NEW_COUNT new CSV files** downloaded from the Saudi Open Data portal
- MOJ Real Estate: $NEW_MOJ_RE files | MOJ Monthly: $NEW_MOJ_MONTHLY files | MOJ Sales: $NEW_MOJ_SALES files | REGA: $NEW_REGA files
- **Total:** $TOTAL_FILES CSVs, ~${ROWS_DISPLAY} rows, ${SIZE_MB} MB

### Files"

# Add file list (indented)
while IFS= read -r f; do
    [[ -z "$f" ]] && continue
    CHANGELOG_ENTRY="$CHANGELOG_ENTRY
- \`$f\`"
done <<< "$NEW_FILES"

# Insert after the "---" separator line (line 13 in the standard format)
# Find the first "## " entry and insert before it
python3 -c "
import sys
entry = sys.argv[1]
with open('CHANGELOG.md', 'r') as f:
    content = f.read()

# Find first '## ' after the header
parts = content.split('\n---\n', 1)
if len(parts) == 2:
    header = parts[0]
    body = parts[1]
    # Insert new entry at the top of body
    new_content = header + '\n---\n\n' + entry + '\n\n---\n' + body.lstrip()
    # Remove double separators
    new_content = new_content.replace('\n---\n\n---\n', '\n---\n')
else:
    new_content = content

with open('CHANGELOG.md', 'w') as f:
    f.write(new_content)
print('CHANGELOG.md updated')
" "$CHANGELOG_ENTRY"

# ── Step 5: Update badge in READMEs ──────────────────────────────────

log "Step 5: Updating README badges..."
sed -i '' "s/data%20updated-[0-9-]*-orange/data%20updated-${TODAY}-orange/g" README.md README-AR.md 2>/dev/null || true

# Update headline numbers in README.md
python3 -c "
import re
for readme in ['README.md', 'README-AR.md']:
    with open(readme, 'r') as f:
        content = f.read()
    # Update 'N million' / 'N ملف CSV'
    content = re.sub(r'covering \*\*[\d.]+\s*million\*\*', 'covering **${ROWS_DISPLAY}**'.replace('M', ' million'), content)
    content = re.sub(r'across \*\*\d+ CSV files\*\*', 'across **$TOTAL_FILES CSV files**', content)
    content = re.sub(r'تغطي \*\*[\d.]+ مليون\*\*', 'تغطي **${ROWS_DISPLAY}**'.replace('M', ' مليون'), content)
    content = re.sub(r'عبر \*\*\d+ ملف CSV\*\*', 'عبر **$TOTAL_FILES ملف CSV**', content)
    with open(readme, 'w') as f:
        f.write(content)
" 2>/dev/null || log "  (README number update skipped — manual check needed)"

# ── Step 6: Git commit + push ─────────────────────────────────────────

log "Step 6: Committing and pushing..."

# Stage new data files
git add moj/ rega/

# Stage updated metadata
git add data/registry_files.csv data/registry_fields.csv data/registry_enums.csv \
        data/registry.json data/schema.json \
        CHANGELOG.md README.md README-AR.md \
        scripts/build_registry.py 2>/dev/null || true

COMMIT_MSG="Add $NEW_COUNT new datasets ($TODAY)

Downloaded $DL_COUNT files from Saudi Open Data portal.
Registry: $TOTAL_FILES files, ${ROWS_DISPLAY} rows, ${SIZE_MB} MB."

git commit -m "$COMMIT_MSG"
git push

log "Pipeline complete: $NEW_COUNT new files committed and pushed."
log "To create a GitHub release: gh release create v$TODAY --generate-notes"
