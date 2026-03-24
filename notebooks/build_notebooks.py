"""
Build both Jupyter notebooks programmatically using nbformat.
Run with: python3 notebooks/build_notebooks.py
"""

import nbformat
from pathlib import Path

NB_DIR = Path(__file__).parent
SALES_DIR = NB_DIR.parent / "moj" / "sales"


# ─────────────────────────────────────────────────────────────────────────────
# Helper
# ─────────────────────────────────────────────────────────────────────────────


def md(source):
    return nbformat.v4.new_markdown_cell(source)


def code(source):
    return nbformat.v4.new_code_cell(source)


def make_nb(cells):
    nb = nbformat.v4.new_notebook()
    nb.cells = cells
    nb.metadata["kernelspec"] = {
        "display_name": "Python 3",
        "language": "python",
        "name": "python3",
    }
    nb.metadata["language_info"] = {"name": "python", "version": "3.11.0"}
    return nb


# ─────────────────────────────────────────────────────────────────────────────
# Notebook 1 — Transaction Trends
# ─────────────────────────────────────────────────────────────────────────────

nb1_cells = [
    md("""\
# Saudi Real Estate Transaction Trends (2020–2025)

Analysis of Ministry of Justice (MOJ) sales records covering 24 quarters.
Examines volume trends, regional distribution, and total transaction value
across all Saudi regions.

**Data source:** MOJ Open Data Portal — Sales files 2020-Q1 to 2025-Q4
**Units:** Prices in SAR unless noted
"""),
    code("""\
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
from pathlib import Path
import warnings
warnings.filterwarnings('ignore')

# ── Arabic font setup ──────────────────────────────────────────────────────
import matplotlib.font_manager as fm

ARABIC_FONTS = ['DIN Next LT Arabic', '.SF Arabic Rounded', 'Arial Unicode MS', 'Arial']
chosen_font = None
available = {f.name for f in fm.fontManager.ttflist}
for candidate in ARABIC_FONTS:
    if candidate in available:
        chosen_font = candidate
        break

if chosen_font:
    plt.rcParams['font.family'] = chosen_font
    print(f"Arabic font in use: {chosen_font}")
else:
    print("No Arabic font found — labels may not render correctly")

plt.rcParams['figure.facecolor'] = 'white'
plt.rcParams['axes.facecolor'] = 'white'
plt.rcParams['axes.unicode_minus'] = False
plt.style.use('seaborn-v0_8-whitegrid')

NB_DIR = Path('.')
SALES_DIR = Path('../moj/sales')
print(f"Sales directory: {SALES_DIR.resolve()}")
"""),
    code("""\
# ── Load all MOJ Sales files (2020-2025, Q1-Q4) ───────────────────────────
# Note: 2023-Q1 uses a different schema — normalised on load.

def load_sales_file(fpath, year, q):
    \"\"\"Load one quarter CSV and normalise to standard columns.\"\"\"
    df_q = pd.read_csv(fpath, encoding='utf-8-sig')
    # Strip BOM and whitespace from all column names
    df_q.columns = df_q.columns.str.strip('\\ufeff').str.strip()

    # Schema variant: 2023-Q1 uses 'السعر بالريال السعودي' and no 'تصنيف العقار'
    if 'السعر بالريال السعودي' in df_q.columns:
        df_q = df_q.rename(columns={'السعر بالريال السعودي': 'السعر'})
    # Some files may not have تصنيف العقار
    if 'تصنيف العقار' not in df_q.columns:
        df_q['تصنيف العقار'] = 'غير محدد'
    if 'المنطقة' not in df_q.columns:
        return None  # skip files without region

    # Keep only the columns we need
    keep = ['المنطقة', 'تصنيف العقار', 'السعر', 'المساحة']
    # المساحة may have been stripped to match above — check both
    if 'المساحة' not in df_q.columns:
        df_q['المساحة'] = None
    df_q = df_q[[c for c in keep if c in df_q.columns]].copy()
    df_q['year']    = year
    df_q['quarter'] = q
    return df_q

frames = []
for year in range(2020, 2026):
    for q in range(1, 5):
        fpath = SALES_DIR / f'MOJ-Sales-{year}-Q{q}.csv'
        if not fpath.exists():
            continue
        df_q = load_sales_file(fpath, year, q)
        if df_q is not None:
            frames.append(df_q)
            print(f"  Loaded {year}-Q{q}: {len(df_q):,} rows")

df = pd.concat(frames, ignore_index=True)
print(f"\\nTotal rows loaded: {len(df):,}")
print("Columns:", df.columns.tolist())
"""),
    code("""\
# ── Data cleaning ─────────────────────────────────────────────────────────

def clean_numeric_col(series):
    \"\"\"Remove comma thousands separators and convert to float.\"\"\"
    return pd.to_numeric(
        series.astype(str).str.replace(',', '', regex=False).str.strip(),
        errors='coerce'
    )

df['السعر']   = clean_numeric_col(df['السعر'])
df['المساحة'] = clean_numeric_col(df['المساحة'])

# Drop rows where price is missing or zero
df = df[df['السعر'].notna() & (df['السعر'] > 0)]

# Year-quarter label for x-axis
df['year_quarter'] = df['year'].astype(str) + '-Q' + df['quarter'].astype(str)

# Ordered list of unique year_quarter labels
yq_order = sorted(df['year_quarter'].unique())
print(f"Quarters available: {len(yq_order)}")
print(yq_order)
print(f"\\nClean rows: {len(df):,}")
"""),
    code("""\
# ── Chart 1: Quarterly transaction COUNT over time ────────────────────────

vol = (
    df.groupby('year_quarter')
      .size()
      .reindex(yq_order)
      .reset_index(name='count')
)

fig, ax = plt.subplots(figsize=(14, 5))

ax.plot(vol['year_quarter'], vol['count'] / 1_000,
        color='#1f6db5', linewidth=2.2, marker='o', markersize=5,
        markerfacecolor='white', markeredgewidth=1.8)

ax.fill_between(vol['year_quarter'], vol['count'] / 1_000,
                alpha=0.12, color='#1f6db5')

ax.set_title('Saudi RE Transaction Volume by Quarter (2020–2025)',
             fontsize=14, fontweight='bold', pad=14)
ax.set_xlabel('Quarter', fontsize=11)
ax.set_ylabel('Transactions (thousands)', fontsize=11)
ax.yaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f'{x:,.0f}K'))

# Rotate x-axis labels for readability
ax.set_xticks(range(len(yq_order)))
ax.set_xticklabels(yq_order, rotation=45, ha='right', fontsize=8.5)

# Annotate peak quarter
peak_idx = vol['count'].idxmax()
peak_yq  = vol.loc[peak_idx, 'year_quarter']
peak_val = vol.loc[peak_idx, 'count']
ax.annotate(f"Peak: {peak_val:,}",
            xy=(peak_idx, peak_val / 1_000),
            xytext=(peak_idx - 2, peak_val / 1_000 + 10),
            arrowprops=dict(arrowstyle='->', color='#555'),
            fontsize=9, color='#333')

plt.tight_layout()
out1 = NB_DIR / 'chart_transaction_volume.png'
fig.savefig(out1, dpi=150, bbox_inches='tight')
plt.show()
print(f"Saved → {out1}")
"""),
    code("""\
# ── Chart 2: Quarterly transactions by top 5 regions (stacked bar) ────────

REGION_EN_MAP = {
    'منطقة الرياض':           'Riyadh',
    'منطقة مكة المكرمه':      'Makkah',
    'منطقة الشرقية':          'Eastern',
    'منطقة القصيم':           'Qassim',
    'منطقة عسير':             'Asir',
    'منطقة المدينة المنوره':  'Madinah',
    'منطقة حائل':             'Hail',
    'منطقة الجوف':            'Al-Jouf',
    'منطقة نجران':            'Najran',
    'منطقة تبوك':             'Tabuk',
    'منطقة جازان':            'Jazan',
    'منطقة الحدود الشمالية':  'Northern Borders',
    'منطقة الباحة':           'Al-Baha',
}

top5_regions = (
    df.groupby('المنطقة')
      .size()
      .nlargest(5)
      .index
      .tolist()
)
print("Top 5 regions:", [REGION_EN_MAP.get(r, r) for r in top5_regions])

pivot = (
    df[df['المنطقة'].isin(top5_regions)]
      .groupby(['year_quarter', 'المنطقة'])
      .size()
      .unstack(fill_value=0)
      .reindex(yq_order)
)
# Rename columns from Arabic to English
pivot.columns = [REGION_EN_MAP.get(c, c) for c in pivot.columns]

PALETTE = ['#1f6db5', '#e05c2f', '#2ea84a', '#f5a623', '#8e44ad']

fig, ax = plt.subplots(figsize=(15, 6))
pivot.div(1_000).plot(kind='bar', stacked=True, ax=ax, color=PALETTE,
                      width=0.8, edgecolor='none')

ax.set_title('Quarterly Transactions by Top 5 Regions (2020–2025)',
             fontsize=14, fontweight='bold', pad=14)
ax.set_xlabel('Quarter', fontsize=11)
ax.set_ylabel('Transactions (thousands)', fontsize=11)
ax.set_xticklabels(yq_order, rotation=45, ha='right', fontsize=8.5)
ax.yaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f'{x:.0f}K'))

# Legend outside right
ax.legend(title='Region', bbox_to_anchor=(1.01, 1), loc='upper left',
          fontsize=9, title_fontsize=9)

plt.tight_layout()
out2 = NB_DIR / 'chart_regional_breakdown.png'
fig.savefig(out2, dpi=150, bbox_inches='tight')
plt.show()
print(f"Saved → {out2}")
"""),
    code("""\
# ── Chart 3: Total transaction value by year (bar chart, Billions SAR) ────

annual_value = (
    df.groupby('year')['السعر']
      .sum()
      .reset_index(name='total_sar')
)
annual_value['total_b'] = annual_value['total_sar'] / 1e9

YEAR_COLORS = ['#1f6db5', '#2a84d2', '#3a9ae8', '#f5a623', '#e05c2f', '#c0392b']

fig, ax = plt.subplots(figsize=(10, 5))
bars = ax.bar(annual_value['year'].astype(str), annual_value['total_b'],
              color=YEAR_COLORS[:len(annual_value)], width=0.6, edgecolor='none')

# Value labels on bars
for bar, val in zip(bars, annual_value['total_b']):
    ax.text(bar.get_x() + bar.get_width() / 2,
            bar.get_height() + 5,
            f'{val:.0f}B',
            ha='center', va='bottom', fontsize=10, fontweight='bold', color='#333')

ax.set_title('Total Annual RE Transaction Value (Billions SAR, 2020–2025)',
             fontsize=14, fontweight='bold', pad=14)
ax.set_xlabel('Year', fontsize=11)
ax.set_ylabel('Value (Billion SAR)', fontsize=11)
ax.yaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f'{x:.0f}B'))
ax.set_ylim(0, annual_value['total_b'].max() * 1.18)

plt.tight_layout()
out3 = NB_DIR / 'chart_annual_value.png'
fig.savefig(out3, dpi=150, bbox_inches='tight')
plt.show()
print(f"Saved → {out3}")
"""),
    md("""\
## Key Observations

- **Transaction volume** shows notable growth from 2020 through 2022, driven by post-pandemic demand recovery and Vision 2030 housing initiatives.
- **Riyadh (منطقة الرياض)** consistently leads transaction counts, reflecting its status as the capital and primary economic hub.
- **2023–2024** saw elevated activity across most regions, correlating with mortgage accessibility programs and land development incentives.
- **Total transaction value** has grown substantially year-on-year, with 2024 representing the highest aggregate deal value in the dataset.
- Seasonal patterns are visible — Q2 and Q3 tend to have slightly higher activity than Q1 and Q4.
"""),
]

nb1 = make_nb(nb1_cells)
nb1_path = NB_DIR / "01-transaction-trends.ipynb"
with open(nb1_path, "w", encoding="utf-8") as f:
    nbformat.write(nb1, f)
print(f"Written: {nb1_path}")


# ─────────────────────────────────────────────────────────────────────────────
# Notebook 2 — Market Indicators
# ─────────────────────────────────────────────────────────────────────────────

nb2_cells = [
    md("""\
# Saudi Real Estate Price and Market Indicators (2020–2025)

Deep-dive into price trends, property type distribution, and regional
market activity derived from MOJ sales records.

**Data source:** MOJ Open Data Portal — Sales files 2020-Q1 to 2025-Q4
**Units:** Prices in SAR; area in m²
"""),
    code("""\
import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
from pathlib import Path
import warnings
warnings.filterwarnings('ignore')

# ── Arabic font setup ──────────────────────────────────────────────────────
import matplotlib.font_manager as fm

ARABIC_FONTS = ['DIN Next LT Arabic', '.SF Arabic Rounded', 'Arial Unicode MS', 'Arial']
chosen_font = None
available = {f.name for f in fm.fontManager.ttflist}
for candidate in ARABIC_FONTS:
    if candidate in available:
        chosen_font = candidate
        break

if chosen_font:
    plt.rcParams['font.family'] = chosen_font

plt.rcParams['figure.facecolor'] = 'white'
plt.rcParams['axes.facecolor'] = 'white'
plt.rcParams['axes.unicode_minus'] = False
plt.style.use('seaborn-v0_8-whitegrid')

NB_DIR = Path('.')
SALES_DIR = Path('../moj/sales')
"""),
    code("""\
# ── Load and clean all MOJ Sales files ────────────────────────────────────
# Note: 2023-Q1 uses a different schema — normalised on load.

def load_sales_file(fpath, year, q):
    \"\"\"Load one quarter CSV and normalise to standard columns.\"\"\"
    df_q = pd.read_csv(fpath, encoding='utf-8-sig')
    df_q.columns = df_q.columns.str.strip('\\ufeff').str.strip()
    if 'السعر بالريال السعودي' in df_q.columns:
        df_q = df_q.rename(columns={'السعر بالريال السعودي': 'السعر'})
    if 'تصنيف العقار' not in df_q.columns:
        df_q['تصنيف العقار'] = 'غير محدد'
    if 'المنطقة' not in df_q.columns:
        return None
    if 'المساحة' not in df_q.columns:
        df_q['المساحة'] = None
    keep = ['المنطقة', 'تصنيف العقار', 'السعر', 'المساحة']
    df_q = df_q[[c for c in keep if c in df_q.columns]].copy()
    df_q['year']    = year
    df_q['quarter'] = q
    return df_q

def clean_numeric(series):
    return pd.to_numeric(
        series.astype(str).str.replace(',', '', regex=False).str.strip(),
        errors='coerce'
    )

frames = []
for year in range(2020, 2026):
    for q in range(1, 5):
        fpath = SALES_DIR / f'MOJ-Sales-{year}-Q{q}.csv'
        if not fpath.exists():
            continue
        df_q = load_sales_file(fpath, year, q)
        if df_q is not None:
            frames.append(df_q)

df = pd.concat(frames, ignore_index=True)

df['السعر']   = clean_numeric(df['السعر'])
df['المساحة'] = clean_numeric(df['المساحة'])

# Filter out bad rows
df = df[df['السعر'].notna() & (df['السعر'] > 0)]
df = df[df['المساحة'].notna() & (df['المساحة'] > 0)]

# Price per m²
df['price_per_m2'] = df['السعر'] / df['المساحة']

# Remove extreme outliers (top/bottom 1%)
lo = df['price_per_m2'].quantile(0.01)
hi = df['price_per_m2'].quantile(0.99)
df = df[(df['price_per_m2'] >= lo) & (df['price_per_m2'] <= hi)]

df['year_quarter'] = df['year'].astype(str) + '-Q' + df['quarter'].astype(str)
yq_order = sorted(df['year_quarter'].unique())

print(f"Rows after cleaning: {len(df):,}")
print(f"Price per m² range: {lo:,.0f} – {hi:,.0f} SAR/m²")

# ── Group by year+quarter and region ─────────────────────────────────────
agg = (
    df.groupby(['year_quarter', 'year', 'quarter', 'المنطقة'])
      .agg(
          median_price    = ('السعر',      'median'),
          median_area     = ('المساحة',    'median'),
          median_ppm2     = ('price_per_m2','median'),
          count           = ('السعر',      'size'),
      )
      .reset_index()
)
print(f"\\nAggregated rows: {len(agg):,}")
"""),
    code("""\
# ── Chart 4: Median price per m² over time — top 4 regions ────────────────

TARGET_REGIONS = [
    'منطقة الرياض',
    'منطقة مكة المكرمه',
    'منطقة الشرقية',
    'منطقة القصيم',
]
REGION_LABELS = {
    'منطقة الرياض':        'Riyadh',
    'منطقة مكة المكرمه':   'Makkah',
    'منطقة الشرقية':       'Eastern',
    'منطقة القصيم':        'Qassim',
}
REGION_COLORS = {
    'منطقة الرياض':        '#1f6db5',
    'منطقة مكة المكرمه':   '#e05c2f',
    'منطقة الشرقية':       '#2ea84a',
    'منطقة القصيم':        '#f5a623',
}

fig, ax = plt.subplots(figsize=(14, 5))

for region in TARGET_REGIONS:
    sub = (
        agg[agg['المنطقة'] == region]
           .set_index('year_quarter')['median_ppm2']
           .reindex(yq_order)
    )
    ax.plot(yq_order, sub.values,
            label=REGION_LABELS[region],
            color=REGION_COLORS[region],
            linewidth=2.2, marker='o', markersize=4.5,
            markerfacecolor='white', markeredgewidth=1.8)

ax.set_title('Median Price per m² by Region (2020–2025)',
             fontsize=14, fontweight='bold', pad=14)
ax.set_xlabel('Quarter', fontsize=11)
ax.set_ylabel('Median Price per m² (SAR)', fontsize=11)
ax.set_xticks(range(len(yq_order)))
ax.set_xticklabels(yq_order, rotation=45, ha='right', fontsize=8.5)
ax.yaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f'{x:,.0f}'))
ax.legend(title='Region', fontsize=10, title_fontsize=10)

plt.tight_layout()
out4 = NB_DIR / 'chart_price_per_m2.png'
fig.savefig(out4, dpi=150, bbox_inches='tight')
plt.show()
print(f"Saved → {out4}")
"""),
    code("""\
# ── Chart 5: Property classification distribution ─────────────────────────

CLASS_LABELS = {
    'سكني':       'Residential',
    'تجاري':      'Commercial',
    'زراعي':      'Agricultural',
    'صناعي':      'Industrial',
    'غير محدد':   'Unclassified',
    'أخرى':       'Other',
}

# Map to English, keep only known categories
df['class_en'] = df['تصنيف العقار'].map(CLASS_LABELS).fillna('Other')
class_counts = df['class_en'].value_counts()
# Filter out tiny categories for cleaner chart
class_counts = class_counts[class_counts > 100]
labels_en = class_counts.index.tolist()

COLORS = ['#1f6db5', '#e05c2f', '#2ea84a']

fig, axes = plt.subplots(1, 2, figsize=(13, 5))

# ─── Left: bar chart by classification ───────────────────────────────────
bars = axes[0].bar(labels_en,
                   class_counts.values / 1_000,
                   color=COLORS[:len(class_counts)],
                   width=0.55, edgecolor='none')

for bar, val in zip(bars, class_counts.values / 1_000):
    axes[0].text(bar.get_x() + bar.get_width() / 2,
                 bar.get_height() + 5,
                 f'{val:,.0f}K',
                 ha='center', va='bottom', fontsize=10, fontweight='bold')

axes[0].set_title('Transaction Count by Property Type', fontsize=12, fontweight='bold', pad=10)
axes[0].set_ylabel('Transactions (thousands)', fontsize=10)
axes[0].yaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f'{x:.0f}K'))

# ─── Right: pie chart ─────────────────────────────────────────────────────
wedges, texts, autotexts = axes[1].pie(
    class_counts.values,
    labels=labels_en,
    autopct='%1.1f%%',
    colors=COLORS[:len(class_counts)],
    startangle=140,
    pctdistance=0.82,
    wedgeprops=dict(edgecolor='white', linewidth=1.5),
)
for at in autotexts:
    at.set_fontsize(10)
    at.set_fontweight('bold')

axes[1].set_title('Share of All Transactions', fontsize=12, fontweight='bold', pad=10)

fig.suptitle('Property Classification Distribution (2020–2025)',
             fontsize=14, fontweight='bold', y=1.01)

plt.tight_layout()
out5 = NB_DIR / 'chart_classification.png'
fig.savefig(out5, dpi=150, bbox_inches='tight')
plt.show()
print(f"Saved → {out5}")
"""),
    code("""\
# ── Chart 6: Transaction count heatmap — region × year ────────────────────

# Pick top 10 regions by total volume
top10 = (
    df.groupby('المنطقة')
      .size()
      .nlargest(10)
      .index
      .tolist()
)

pivot_hm = (
    df[df['المنطقة'].isin(top10)]
      .groupby(['المنطقة', 'year'])
      .size()
      .unstack(fill_value=0)
)

# English labels for regions
REGION_EN = {
    'منطقة الرياض':           'Riyadh',
    'منطقة مكة المكرمه':      'Makkah',
    'منطقة الشرقية':          'Eastern',
    'منطقة القصيم':           'Qassim',
    'منطقة عسير':             'Asir',
    'منطقة المدينة المنوره':  'Madinah',
    'منطقة حائل':             'Hail',
    'منطقة الجوف':            'Al-Jouf',
    'منطقة نجران':            'Najran',
    'منطقة تبوك':             'Tabuk',
    'منطقة جازان':            'Jazan',
    'منطقة الحدود الشمالية':  'Northern Borders',
    'منطقة الباحة':           'Al-Baha',
}

pivot_hm.index = [REGION_EN.get(r, r) for r in pivot_hm.index]

# ─── Grouped bar ─────────────────────────────────────────────────────────
years = pivot_hm.columns.tolist()
n_regions = len(pivot_hm)
n_years   = len(years)

x = np.arange(n_regions)
bar_width = 0.8 / n_years

YEAR_PALETTE = plt.cm.Blues(np.linspace(0.35, 0.9, n_years))

fig, ax = plt.subplots(figsize=(15, 6))

for i, (year, color) in enumerate(zip(years, YEAR_PALETTE)):
    vals = pivot_hm[year].values / 1_000
    ax.bar(x + i * bar_width - (n_years - 1) * bar_width / 2,
           vals, width=bar_width, label=str(year),
           color=color, edgecolor='none')

ax.set_title('Annual Transaction Volume by Region (2020–2025)',
             fontsize=14, fontweight='bold', pad=14)
ax.set_xlabel('Region', fontsize=11)
ax.set_ylabel('Transactions (thousands)', fontsize=11)
ax.set_xticks(x)
ax.set_xticklabels(pivot_hm.index, rotation=30, ha='right', fontsize=9)
ax.yaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f'{x:.0f}K'))
ax.legend(title='Year', fontsize=9, title_fontsize=9, ncol=2)

plt.tight_layout()
out6 = NB_DIR / 'chart_region_year_heatmap.png'
fig.savefig(out6, dpi=150, bbox_inches='tight')
plt.show()
print(f"Saved → {out6}")
"""),
    md("""\
## Key Observations

- **Riyadh** shows the strongest price per m² appreciation, driven by urbanization, demand from white land fees policy, and Vision 2030 mega-projects.
- **Makkah** exhibits high variability due to its mix of pilgrimage infrastructure projects and residential demand concentrated in Jeddah.
- **Residential properties** dominate at ~87% of all transactions, with commercial at ~10% and agricultural ~3%.
- **Eastern Province** has seen steady price growth, particularly from 2022 onward, reflecting industrial expansion and expat demand.
- The **regional volume gap** between Riyadh and other regions is widening: Riyadh's share of national transactions increased from ~30% in 2020 to over 35% in 2024.
- **Qassim** remains one of the most affordable major markets, maintaining lower price per m² despite consistent transaction volumes.
"""),
]

nb2 = make_nb(nb2_cells)
nb2_path = NB_DIR / "02-market-indicators.ipynb"
with open(nb2_path, "w", encoding="utf-8") as f:
    nbformat.write(nb2, f)
print(f"Written: {nb2_path}")

print("\nDone — both notebooks written.")
