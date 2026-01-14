"""
KEGG Pathway Enrichment Visualization - Top 10 Pathways (Figure 2B)
====================================================================
Visualization of top 10 KEGG pathway enrichment results from gProfiler
for all target genes of Polygonum cuspidatum compounds.

This script creates a bar chart showing the most significantly enriched pathways
ranked by -log10(adjusted P-value).

Works in both Google Colab and local Python environments.

Author: Jihong Oh
Date: 2025-12-06
License: MIT
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import sys
import os

# Check if running in Google Colab
try:
    from google.colab import files
    IN_COLAB = True
except ImportError:
    IN_COLAB = False

# ============================================
# Configuration
# ============================================
TOP_N = 10  # Number of top pathways to display
OUTPUT_PNG = 'Figure2B_Top10_KEGG_Pathways.png'
OUTPUT_PDF = 'Figure2B_Top10_KEGG_Pathways.pdf'
DPI = 300

# ============================================
# 1. File Upload/Input
# ============================================
print("=" * 60)
print("KEGG Pathway Enrichment Visualization - Top 10")
print("=" * 60)

if IN_COLAB:
    print("\n📁 Please upload your CSV file from gProfiler...")
    uploaded = files.upload()
    filename = list(uploaded.keys())[0]
    print(f"✓ File uploaded: {filename}")
else:
    if len(sys.argv) > 1:
        filename = sys.argv[1]
    else:
        filename = input("\n📁 Enter CSV file path: ").strip()
    
    if not os.path.exists(filename):
        print(f"✗ Error: File '{filename}' not found")
        sys.exit(1)
    print(f"✓ File loaded: {filename}")

# ============================================
# 2. Data Loading and Preprocessing
# ============================================
print("\n🔄 Loading data...")
df = pd.read_csv(filename)
print(f"  - Total pathways: {len(df)}")

# Clean term names
df["term_name"] = df["term_name"].astype(str).str.strip()

# Parse gene lists
df['gene_list'] = df['intersections'].apply(
    lambda x: [g.strip() for g in str(x).split(',')]
)
df['gene_count'] = df['gene_list'].apply(len)

# ============================================
# 3. Extract Top 10 Pathways
# ============================================
print(f"\n🔄 Extracting top {TOP_N} pathways...")

val_col = "negative_log10_of_adjusted_p_value"
df_top10 = df.nlargest(TOP_N, val_col).reset_index(drop=True)

print(f"\n✓ Top {TOP_N} KEGG pathways:")
for idx, row in df_top10.iterrows():
    print(f"  {idx+1}. {row['term_name']}")
    print(f"      -log10(Padj): {row[val_col]:.2f}, Genes: {row['gene_count']}")

# ============================================
# 4. Figure Creation
# ============================================
print("\n🎨 Creating visualization...")

n_pathways = len(df_top10)
fig, ax = plt.subplots(figsize=(12, max(6, n_pathways * 0.5)))

# Y coordinates
y_positions = np.arange(n_pathways)

# Color gradient based on -log10(Padj) (matching Figure 2A style)
max_val = df_top10[val_col].max()
colors = plt.cm.YlGnBu(0.4 + 0.6 * df_top10[val_col] / max_val)

# Draw bars
bars = ax.barh(
    y_positions,
    df_top10[val_col],
    color=colors,
    height=0.7,
    edgecolor='#2c5f77',
    linewidth=1.2
)

# Pathway labels
ax.set_yticks(y_positions)
ax.set_yticklabels(df_top10['term_name'], fontsize=15)
ax.invert_yaxis()  # Highest value on top

ax.set_xlabel(r'$-\log_{10}(P_{adj})$', fontsize=15, fontweight='bold')
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.grid(axis='x', alpha=0.3, linestyle='--', linewidth=0.5)
ax.set_ylim(n_pathways - 0.5, -0.5)

# Add value labels
for i, val in enumerate(df_top10[val_col]):
    ax.text(
        val + max_val * 0.02,
        i,
        f'{val:.2f}',
        va='center',
        ha='left',
        fontsize=10,
        fontweight='bold',
        color='#2c5f77'
    )

plt.tight_layout()

# ============================================
# 5. Save Figure
# ============================================
plt.savefig(OUTPUT_PNG, dpi=DPI, bbox_inches='tight', facecolor='white')
plt.savefig(OUTPUT_PDF, bbox_inches='tight', facecolor='white')
print(f"\n✓ Figure saved: {OUTPUT_PNG} and {OUTPUT_PDF}")

plt.show()

# Download in Colab
if IN_COLAB:
    files.download(OUTPUT_PNG)
    files.download(OUTPUT_PDF)
else:
    print(f"✓ Files saved to: {os.path.abspath(OUTPUT_PNG)}")

# ============================================
# 6. Statistics Summary
# ============================================
print("\n" + "=" * 60)
print("📊 Analysis Summary")
print("=" * 60)
print(f"Total pathways in dataset: {len(df)}")
print(f"Top {TOP_N} pathway statistics:")
print(f"  - Average -log10(Padj): {df_top10[val_col].mean():.2f}")
print(f"  - Average gene count: {df_top10['gene_count'].mean():.1f}")
print(f"\nDetailed Top {TOP_N}:")
for idx, row in df_top10.iterrows():
    genes_str = ', '.join(row['gene_list'])
    print(f"\n  {idx+1}. {row['term_name']}")
    print(f"      -log10(Padj): {row[val_col]:.2f}")
    print(f"      Genes ({row['gene_count']}): {genes_str}")
print("=" * 60)
