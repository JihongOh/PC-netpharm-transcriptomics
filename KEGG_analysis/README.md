# KEGG Pathway Enrichment Visualization

Visualization of KEGG pathway enrichment analysis results from gProfiler for *Polygonum cuspidatum* (Korean: 호장근) compound target genes.

![Python](https://img.shields.io/badge/python-3.7+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

##  Overview

This repository contains scripts to visualize KEGG pathway enrichment results from two different gene sets:
- **Figure 2A**: Hub genes (targets shared by 2+ compounds) - Cardiometabolic pathways
- **Figure 2B**: All target genes - Top 10 pathways

##  Features

-  **Dual visualization** - Combined bar chart and gene heatmap (Figure 2A)
-  **Top pathway analysis** - Ranked by statistical significance (Figure 2B)
-  **Publication-ready** - High-resolution output (300 DPI)
-  **Cross-platform** - Works in Google Colab and local Python
-  **Automatic processing** - From gProfiler CSV to publication figure

##  Example Outputs

### Figure 2A: Hub Genes - Cardiometabolic Pathways
![Example 2A](/Figure2A_example.png)

*Enriched KEGG pathways from hub genes (degree ≥ 2) with gene distribution heatmap.*

### Figure 2B: All Targets - Top 10 Pathways
![Example 2B](/Figure2B_example.png)

*Top 10 KEGG pathways enriched from all target genes ranked by -log₁₀(adjusted P).*

## Workflow

### Step 1: Target Gene Identification

**For Figure 2A (Hub genes)**:
1. Identify target genes predicted for each of 4 major compounds from *P. cuspidatum*
2. Filter genes targeted by ≥2 compounds (hub genes)
3. Use this gene list for enrichment analysis

**For Figure 2B (All targets)**:
1. Collect all target genes from 4 major compounds
2. Use complete gene list for enrichment analysis

### Step 2: Run gProfiler Enrichment Analysis

1. **Go to gProfiler**: [https://biit.cs.ut.ee/gprofiler/gost](https://biit.cs.ut.ee/gprofiler/gost)

2. **Input your gene list**:
   - Paste gene symbols (one per line)
   - Or upload file

3. **Configure analysis**:
   - Click 'Advanced Options'
   - Organism: `Homo sapiens`
   - Significance threshold: `g:SCS threshold` (default)
   - User threshold: 0.01
   - Click 'Data Sources' : Select "KEGG"

4. **Run analysis**:
   - Click "Run query"
   - Wait for results

5. **Download results**:
   - Click "Detailed Results" -> "Download csv file"
   - Save the file

**Note**: The CSV file should be named like:
- `*_intersections.csv` (contains gene lists)

### Step 3: Visualize with These Scripts

Use the downloaded CSV files with the appropriate script.

## Quick Start

### Google Colab (Easiest)

**Figure 2A:**
```python
# Copy kegg_hub_genes_plot.py to Colab
# Run and upload hub genes CSV
```

**Figure 2B:**
```python
# Copy kegg_top10_plot.py to Colab
# Run and upload all targets CSV
```

### Local Python

```bash
# Install dependencies
pip install pandas numpy matplotlib

# Figure 2A
python kegg_hub_genes_plot.py hub_genes_gprofiler.csv

# Figure 2B
python kegg_top10_plot.py all_targets_gprofiler.csv
```

## Input Format

CSV file from gProfiler with these columns:

**Required columns:**
- `term_name`: Pathway name
- `term_id`: KEGG pathway ID
- `adjusted_p_value`: Adjusted p-value (FDR)
- `negative_log10_of_adjusted_p_value`: -log₁₀(adjusted P)
- `intersection_size`: Number of genes
- `intersections`: Comma-separated gene symbols

**Example:**
```csv
source,term_name,term_id,adjusted_p_value,negative_log10_of_adjusted_p_value,intersection_size,intersections
KEGG,AGE-RAGE signaling pathway in diabetic complications,KEGG:04933,3.93e-18,17.41,15,"BAX,NFKB1,STAT3,..."
```

##  Configuration

### Figure 2A (Hub Genes)

Edit the cardiometabolic pathways list in `kegg_hub_genes_plot.py`:

```python
CARDIOMETABOLIC_TERMS = [
    "AGE-RAGE signaling pathway in diabetic complications",
    "Lipid and atherosclerosis",
    "Insulin resistance",
    # ... add more pathways
]
```

### Figure 2B (Top 10)

Adjust number of pathways in `kegg_top10_plot.py`:

```python
TOP_N = 10  # Change to show more/fewer pathways
```

##  Methodology

### Statistical Analysis

**Enrichment test**: Hypergeometric test
**Multiple testing correction**: g:SCS (default method in g:Profiledr)
**Significance threshold**: Adjusted P < 0.01

### Hub Gene Definition

**Hub genes**: Genes predicted as targets for ≥2 compounds
- Indicates stronger confidence in target prediction
- Represents genes with potential multi-compound regulation

### Visualization Strategy

**Figure 2A**: 
- Focuses on cardiometabolic/inflammatory pathways
- Shows gene distribution across pathways
- Useful for identifying shared regulatory mechanisms

**Figure 2B**:
- Shows overall pathway enrichment landscape
- Ranked by statistical significance
- Broader biological interpretation

## Data Source Information

### Analysis Details

**Date**: December 6, 2025 (US format: 12/06/2025)

**Database versions**:
- Human genome: GRCh38.p14
- KEGG database: Release 2024-01-22

**Software versions**:
```
Python: 3.12.12 (Google Colab)
matplotlib: 3.10.0
numpy: 2.0.2
pandas: 2.2.2
scipy: 1.16.3
seaborn: 0.13.2
```

## License

MIT License - See [LICENSE](LICENSE) for details

## Contact

For questions or issues:
- Open an issue on GitHub
- Email: jihong421@gmail.com

## Acknowledgments

- [gProfiler](https://biit.cs.ut.ee/gprofiler/) for pathway enrichment analysis
- [KEGG](https://www.genome.jp/kegg/) for pathway database
