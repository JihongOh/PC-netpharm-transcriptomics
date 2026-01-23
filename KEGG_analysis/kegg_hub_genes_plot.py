"""
KEGG Pathway Enrichment Visualization - Hub Genes (Figure 2A)
==============================================================
Visualization of KEGG pathway enrichment results from gProfiler for hub genes
(genes targeted by 2+ compounds from Polygonum cuspidatum).

This script creates a combined bar chart and gene heatmap showing:
- Left panel: Enriched pathways ranked by significance
- Right panel: Gene distribution across pathways

Works in both Google Colab and local Python environments.

Author: Jihong Oh
Date: 2025-12-06
License: MIT
"""

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
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
# Cardiometabolic KEGG pathways of interest
CARDIOMETABOLIC_TERMS = [
    # 1. Inflammation & Immune Response 
    "TNF signaling pathway",
    "IL-17 signaling pathway",
    "Th17 cell differentiation",
    "Toll-like receptor signaling pathway",
    "NOD-like receptor signaling pathway",
    "Cytosolic DNA-sensing pathway",
    "HIF-1 signaling pathway", 

    # 2. Metabolic Dysfunction 
    "AGE-RAGE signaling pathway in diabetic complications", 
    "PPAR signaling pathway", 
    "Insulin resistance", 
    "FoxO signaling pathway",
    "Apelin signaling pathway", 

    # 3. Vascular Pathology & Atherosclerosis 
    "Lipid and atherosclerosis", 
    "Fluid shear stress and atherosclerosis", 
    "Relaxin signaling pathway",
    "VEGF signaling pathway",
    "Adrenergic signaling in cardiomyocytes", 
    "Efferocytosis" 
]

OUTPUT_PNG = 'Figure2A_Hub_Cardiometabolic_KEGG.png'
OUTPUT_PDF = 'Figure2A_Hub_Cardiometabolic_KEGG.pdf'
DPI = 300

# ============================================
# 1. File Upload/Input
# ============================================
print("=" * 60)
print("KEGG Pathway Enrichment Visualization - Hub Genes")
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

# Filter for cardiometabolic pathways
present_terms = set(df["term_name"].unique())
selected_terms = [t for t in CARDIOMETABOLIC_TERMS if t in present_terms]

print("\n✓ Selected cardiometabolic KEGG pathways:")
for t in selected_terms:
    print(f"  - {t}")

df_sel = df[df["term_name"].isin(selected_terms)].copy()

if df_sel.empty:
    raise ValueError("No selected pathways found in CSV. Please check term_name column.")

# ============================================
# 3. Data Processing
# ============================================
print("\n🔄 Processing gene information...")

# Sort by -log10(Padj) descending
val_col = "negative_log10_of_adjusted_p_value"
df_sel = df_sel.sort_values(val_col, ascending=False).reset_index(drop=True)

# Parse gene lists
df_sel['gene_list'] = df_sel['intersections'].apply(
    lambda x: [g.strip() for g in str(x).split(',')]
)
df_sel['gene_count'] = df_sel['gene_list'].apply(len)

# Extract all unique genes and sort
all_genes = sorted(set([gene for genes in df_sel['gene_list'] for gene in genes]))

print(f"  - Pathways: {len(df_sel)}")
print(f"  - Unique genes: {len(all_genes)}")
print(f"  - Genes: {', '.join(all_genes)}")

# ============================================
# 4. Figure Creation
# ============================================
print("\n🎨 Creating visualization...")

n_pathways = len(df_sel)
fig_height = max(8, n_pathways * 0.6)

fig, (ax1, ax2) = plt.subplots(
    1, 2,
    figsize=(18, fig_height),
    gridspec_kw={'width_ratios': [2.5, 1.5], 'wspace': 0.02}
)

# Y coordinates (same for both panels)
y_positions = np.arange(n_pathways)

# =========================================
# Left Panel: Pathway names and bar chart
# =========================================
# Color gradient based on -log10(Padj)
max_val = df_sel[val_col].max()
colors = plt.cm.YlGnBu(0.4 + 0.6 * df_sel[val_col] / max_val)

bars = ax1.barh(
    y_positions,
    df_sel[val_col],
    color=colors,
    height=0.7,
    edgecolor='#2c5f77',
    linewidth=1.2
)

# Pathway labels
ax1.set_yticks(y_positions)
ax1.set_yticklabels(df_sel['term_name'], fontsize=14)
ax1.invert_yaxis()  # Highest value on top

ax1.set_xlabel(r'$-\log_{10}(P_{adj})$', fontsize=15, fontweight='bold')
ax1.set_title('KEGG Pathway Enrichment', fontsize=14, fontweight='bold', pad=15)
ax1.spines['top'].set_visible(False)
ax1.spines['right'].set_visible(False)
ax1.grid(axis='x', alpha=0.3, linestyle='--', linewidth=0.5)
ax1.set_ylim(n_pathways - 0.5, -0.5)

# Add value labels
for i, (val, bar) in enumerate(zip(df_sel[val_col], bars)):
    ax1.text(
        val + max_val * 0.02,
        i,
        f'{val:.2f}',
        va='center',
        ha='left',
        fontsize=9,
        fontweight='bold',
        color='#2c5f77'
    )

# =========================================
# Right Panel: Gene distribution heatmap
# =========================================
# Create gene-pathway matrix
gene_matrix = np.zeros((n_pathways, len(all_genes)))
for i, genes in enumerate(df_sel['gene_list']):
    for gene in genes:
        j = all_genes.index(gene)
        gene_matrix[i, j] = 1

# Draw heatmap with matching bar height
bar_height = 0.7
for i in range(n_pathways):
    for j in range(len(all_genes)):
        if gene_matrix[i, j] == 1:
            rect = mpatches.Rectangle(
                (j - 0.35, y_positions[i] - bar_height/2),
                0.7, bar_height,
                facecolor='#2c3e50',
                edgecolor='white',
                linewidth=0.5
            )
            ax2.add_patch(rect)

# Axis settings (match left panel exactly)
ax2.set_xlim(-0.5, len(all_genes) - 0.5)
ax2.set_ylim(n_pathways - 0.5, -0.5)

# Y-axis ticks (for grid) but no labels
ax2.set_yticks(y_positions)
ax2.set_yticklabels([])

# X-axis: gene names (top)
ax2.xaxis.tick_top()
ax2.xaxis.set_label_position('top')

ax2.set_xticks(range(len(all_genes)))
ax2.set_xticklabels(
    all_genes,
    rotation=90,
    ha='center',
    va='bottom',
    fontsize=14,
    fontweight='bold'
)
ax2.set_xlabel('Related Genes', fontsize=13, fontweight='bold', labelpad=10)

# Remove borders
for spine in ax2.spines.values():
    spine.set_visible(False)
ax2.tick_params(top=True, bottom=False, left=False, right=False)

# Add grid
ax2.set_xticks(np.arange(len(all_genes)) - 0.5, minor=True)
ax2.grid(which='both', color='#e0e0e0', linestyle='-', linewidth=0.8, axis='y')
ax2.grid(which='minor', color='#e0e0e0', linestyle='-', linewidth=0.8, axis='x')

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
print(f"Total pathways analyzed: {len(df_sel)}")
print(f"Unique genes involved: {len(all_genes)}")
print(f"\nPathway-wise gene counts:")
for idx, row in df_sel.iterrows():
    genes_str = ', '.join(row['gene_list'])
    print(f"  {row['term_name']}: {row['gene_count']} genes")
    print(f"    ({genes_str})")
print("=" * 60)
