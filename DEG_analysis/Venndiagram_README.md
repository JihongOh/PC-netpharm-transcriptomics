# PC Core-4 Compound-Target & DEG Overlap Analysis

[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Comprehensive analysis of overlapping genes between Polygonum cuspidatum (PC) core-4 compound targets and differentially expressed genes (DEGs) from metabolic and vascular disease datasets.

## Overview

This tool identifies and visualizes shared genes between:
- **PC Core-4 compound targets**: Polydatin, Resveratrol, Emodin, Physcion
- **GSE20950 DEGs**: Adipose tissue (insulin-resistant vs insulin-sensitive)
- **GSE43292 DEGs**: Atheroma plaque vs intact arterial tissue

## Features

- Automated DEG preprocessing and filtering
- Statistical threshold application (adj.P.Val < 0.01, |log2FC| > 0.58)
- Duplicate gene handling (keeps lowest adj.P.Val)
- Target degree calculation
- Overlap analysis with detailed tables
- 3-way Venn diagram visualization
- Excel output with formatted supplement tables
- 3-way common gene analysis

## Requirements

### Python Version
- Python 3.8 or higher

### Required Packages
```
pandas>=1.3.0
numpy>=1.21.0
matplotlib>=3.4.0
matplotlib-venn>=0.11.6
openpyxl>=3.0.9
```

### Input Data Requirements

**1. compound_target_network.csv**
- Columns: `compound`, `target`
- Format: CSV file
- Contains compound-gene target predictions

**2. GSE20950_top_table.tsv**
- NCBI GEO microarray differential expression results
- Required columns: `Gene.symbol`, `logFC`, `adj.P.Val`, `P.Value`
- Format: Tab-separated values

**3. GSE43292_top_table.tsv**
- NCBI GEO microarray differential expression results
- Required columns: `Gene.symbol`, `logFC`, `adj.P.Val`, `P.Value`
- Format: Tab-separated values

## Installation

### Google Colab (Recommended)
No installation required! Upload the Python script and run in Colab.

### Local Installation
```bash
# Clone repository
git clone https://github.com/yourusername/pc-core4-overlap-analysis.git
cd pc-core4-overlap-analysis

# Install requirements
pip install -r requirements.txt
```

## Usage

### Quick Start (Google Colab)

1. Upload `PC_Core4_DEG_Overlap_Analysis.py` to Google Colab
2. Run the script
3. Upload your three input files when prompted:
   - compound_target_network.csv
   - GSE20950_top_table.tsv
   - GSE43292_top_table.tsv
4. Results automatically download after completion

### Configuration

Default statistical thresholds (modifiable in script):

```python
ADJ_PVAL_THRESHOLD = 0.01      # Adjusted p-value threshold
LOG2FC_THRESHOLD = 0.58        # Log2 fold change threshold (absolute value)
```

Core-4 compounds (modifiable in script):

```python
CORE4_COMPOUNDS = ['Polydatin', 'Resveratrol', 'Emodin', 'Physcion']
```

## Data Processing Pipeline

```
Input Files
    ↓
1. Load compound-target network
    ↓
2. Load DEG data (TSV files)
    ↓
3. Clean DEG data:
   - Remove NaN/empty gene symbols
   - Remove ambiguous probes ('///')
   - Calculate -log10(adj.P.Val)
   - Remove duplicates (keep lowest adj.P.Val)
    ↓
4. Filter DEGs:
   - adj.P.Val < 0.01
   - |log2FC| > 0.58
    ↓
5. Calculate target degree
    ↓
6. Identify overlapping genes
    ↓
7. Generate supplement tables
    ↓
8. Create Venn diagram
    ↓
9. Analyze 3-way common genes
    ↓
Output Files
```

## Output Files

### 1. Supplement Tables (Excel)
**Supplement_Tables_PC_Core4_DEGs.xlsx**
- Sheet 1: GSE20950 overlap
- Sheet 2: GSE43292 overlap
- Columns:
  - Gene Symbol
  - Core-4 Compounds (connected compounds)
  - Degree (number of compound connections)
  - Log2(Fold Change)
  - -log10(adj P)

### 2. Venn Diagram
**PC_GSE20950_GSE43292_VennDiagram.png**
- 3-way Venn diagram
- Shows overlaps between:
  - PC target genes
  - GSE20950 DEGs
  - GSE43292 DEGs
- 300 DPI resolution

### 3. CSV Files
- **Supplement_Table_GSE20950.csv**: GSE20950 overlap table
- **Supplement_Table_GSE43292.csv**: GSE43292 overlap table
- **Common_Genes_3way.csv**: Genes common to all three sets (if any)

### 3-Way Common Gene Table Columns
- Gene Symbol
- Core-4 Compounds
- Degree
- GSE20950 logFC
- GSE20950 -log10P
- GSE43292 logFC
- GSE43292 -log10P

## Interpretation Guide

### Target Degree
- **Degree 1**: Gene targeted by 1 compound
- **Degree 2**: Gene targeted by 2 compounds
- **Degree 3**: Gene targeted by 3 compounds
- **Degree 4**: Gene targeted by all 4 core compounds

### Venn Diagram Regions
- **PC only**: Genes targeted by PC but not differentially expressed
- **GSE20950 only**: DEGs in adipose tissue only
- **GSE43292 only**: DEGs in atheroma plaque only
- **PC ∩ GSE20950**: Shared between PC targets and adipose DEGs
- **PC ∩ GSE43292**: Shared between PC targets and atheroma DEGs
- **GSE20950 ∩ GSE43292**: DEGs common to both tissues
- **All three**: Genes of highest interest (therapeutic targets)

### Statistical Significance
- **-log10(adj P)**: Higher values = more significant
- **Log2(Fold Change)**: 
  - Positive = upregulated
  - Negative = downregulated
  - |logFC| > 0.58 ≈ 1.5-fold change

## Example Workflow

### 1. Prepare Data
```
Download from NCBI GEO:
- GSE20950 differential expression results (top table)
- GSE43292 differential expression results (top table)

Prepare compound-target network:
- Format: compound, target
- Include: Polydatin, Resveratrol, Emodin, Physcion
```

### 2. Run Analysis
```python
# Upload script to Google Colab
# Run script
# Upload 3 files when prompted
# Wait for processing
# Download results automatically
```

### 3. Interpret Results
```
1. Check Venn diagram for overall overlap patterns
2. Review supplement tables for specific genes
3. Focus on high-degree genes (targeted by multiple compounds)
4. Examine 3-way common genes for therapeutic candidates
```

## Scientific Context

### Datasets

**GSE20950**: Gene expression profiling of subcutaneous adipose tissue
- **Comparison**: Insulin-resistant vs insulin-sensitive individuals
- **Relevance**: Metabolic dysfunction, insulin resistance, type 2 diabetes
- **Tissue**: Adipose tissue

**GSE43292**: Gene expression analysis of atherosclerotic lesions
- **Comparison**: Atheroma plaque vs intact arterial tissue
- **Relevance**: Atherosclerosis, cardiovascular disease, vascular inflammation
- **Tissue**: Arterial tissue

### PC Core-4 Compounds

**Polydatin**
- Resveratrol glycoside
- Anti-inflammatory, cardioprotective

**Resveratrol**
- Stilbene polyphenol
- Metabolic regulator, anti-aging

**Emodin**
- Anthraquinone derivative
- Anti-inflammatory, metabolic effects

**Physcion**
- Anthraquinone derivative
- Anti-inflammatory, anti-oxidant


## Datasets Citation

```bibtex
@article{gse20950,
  title={Gene expression profiling in subcutaneous adipose tissue},
  note={NCBI GEO accession: GSE20950}
}

@article{gse43292,
  title={Gene expression analysis of atherosclerotic lesions},
  note={NCBI GEO accession: GSE43292}
}
```

## Troubleshooting

### Common Issues

**Issue**: File upload fails
- **Solution**: Ensure files are in correct format (CSV/TSV) with required columns

**Issue**: No overlapping genes found
- **Solution**: Check that gene symbols in all files use consistent naming (case-insensitive matching is applied)

**Issue**: Duplicate genes in results
- **Solution**: Script automatically handles duplicates by keeping gene with lowest adj.P.Val

**Issue**: Empty 3-way common genes table
- **Solution**: This indicates no genes are shared across all three sets (PC targets, GSE20950 DEGs, GSE43292 DEGs)

**Issue**: Venn diagram regions don't match expectations
- **Solution**: Verify statistical thresholds (adj.P.Val < 0.01, |logFC| > 0.58) are appropriate for your data

## Statistical Methods

### DEG Filtering
- **Adjusted p-value**: Benjamini-Hochberg FDR correction
- **Fold change**: Log2 transformation
- **Threshold rationale**: 
  - adj.P.Val < 0.01 = 99% confidence
  - |log2FC| > 0.58 ≈ 1.5-fold change (biologically relevant)

### Duplicate Handling
- Multiple probes for same gene: Keep probe with lowest adj.P.Val
- Rationale: Most statistically significant probe represents true expression

### Case-Insensitive Matching
- Gene symbols converted to uppercase for matching
- Prevents false negatives from inconsistent capitalization

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Contact

For questions or issues, please open an issue on GitHub.

## Acknowledgments

- NCBI GEO for providing public datasets
- matplotlib-venn for Venn diagram visualization
- openpyxl for Excel file generation
