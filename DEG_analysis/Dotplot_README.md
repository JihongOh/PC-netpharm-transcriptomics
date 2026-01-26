# KEGG Pathway Enrichment Dot Plot

[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Publication-ready dot plot visualization for comparing KEGG pathway enrichment between two datasets based on g:Profiler analysis results.

## Overview

This tool creates high-quality dot plots comparing cardiometabolic KEGG pathway enrichment across different conditions (e.g., insulin-resistant vs insulin-sensitive adipose tissue, atheroma plaque vs intact arterial tissue).

## Features

- Automated pathway filtering (cardiometabolic-focused)
- Dual-dataset comparison visualization
- Color-coded by statistical significance (-log10(FDR))
- Point size proportional to gene count
- Publication-ready formatting (300 DPI)
- Google Colab compatible

## Requirements

### Python Version
- Python 3.8 or higher

### Required Packages
```
pandas>=1.3.0
numpy>=1.21.0
matplotlib>=3.4.0
```

### Input Data Requirements
- g:Profiler intersection CSV files from KEGG pathway analysis
- Benjamini-Hochberg FDR correction applied (threshold < 0.01)
- Required columns: `term_name`, `intersection_size`, `adjusted_p_value`, `negative_log10_of_adjusted_p_value`

## Installation

### Option 1: Google Colab (Recommended)
No installation required! Upload the Python script and run directly in Colab.

### Option 2: Local Installation
```bash
# Clone the repository
git clone https://github.com/JihongOh/PC-netpharm-transcriptomics.git
cd kegg-pathway-dotplot

# Install required packages
pip install pandas numpy matplotlib
```

## Usage

### Quick Start (Google Colab)

1. Upload `KEGG_Pathway_DotPlot.py` to Google Colab
2. Run the script
3. Upload your g:Profiler intersection CSV files when prompted
4. The script automatically generates and downloads the dot plot

### Input File Format

Your CSV files should be g:Profiler intersection results with these columns:
```
term_name, intersection_size, adjusted_p_value, negative_log10_of_adjusted_p_value
```

Example:
```csv
"term_name","intersection_size","adjusted_p_value","negative_log10_of_adjusted_p_value"
"AGE-RAGE signaling pathway in diabetic complications",8,6.14e-7,6.21
"TNF signaling pathway",7,0.0001,4.00
```

### Cardiometabolic Pathway Categories

The script focuses on three categories of KEGG pathways:

**1. Inflammation & Immune Response**
- TNF signaling pathway
- IL-17 signaling pathway
- Th17 cell differentiation
- Toll-like receptor signaling pathway
- NOD-like receptor signaling pathway
- Cytosolic DNA-sensing pathway
- HIF-1 signaling pathway

**2. Metabolic Dysfunction**
- AGE-RAGE signaling pathway in diabetic complications
- PPAR signaling pathway
- Insulin resistance
- FoxO signaling pathway
- Apelin signaling pathway

**3. Vascular Pathology & Atherosclerosis**
- Lipid and atherosclerosis
- Fluid shear stress and atherosclerosis
- Relaxin signaling pathway
- VEGF signaling pathway
- Adrenergic signaling in cardiomyocytes
- Efferocytosis

### Customization

To modify the pathway list, edit the `CARDIOMETABOLIC_PATHWAYS` list:

```python
CARDIOMETABOLIC_PATHWAYS = [
    "Your pathway 1",
    "Your pathway 2",
    # ... add more pathways
]
```

## Output

### Dot Plot Features
- **X-axis**: -log10(FDR) - statistical significance
- **Y-axis**: KEGG pathway names (ordered by maximum enrichment)
- **Point size**: Number of genes in intersection
- **Point color**: -log10(FDR) value (Red-Yellow-Blue scale)
- **Point shape**: 
  - ⭕ Circle = GSE20950 (Insulin-resistant vs insulin-sensitive)
  - ⬜ Square = GSE43292 (Atheroma plaque vs intact tissue)

### Output File
- `DotPlot_Cardiometabolic_GSE20950_GSE43292_Publication.png`
- Resolution: 300 DPI
- Format: PNG with white background

## Example Workflow

### 1. Prepare Gene Lists
```
# Identify shared genes between:
- PC (Polygonum cuspidatum) compound targets
- GSE20950 DEGs (differential expression genes)
- GSE43292 DEGs
```

### 2. Run g:Profiler Analysis
```
1. Go to https://biit.cs.ut.ee/gprofiler/gost
2. Input: Shared gene lists
3. Organism: Homo sapiens
4. Statistical domain: KEGG pathways
5. Correction method: Benjamini-Hochberg FDR
6. Threshold: FDR < 0.01
7. Download: Intersection results (CSV)
access date: 23 Jan, 2026 
```

### 3. Generate Dot Plot
```python
# Upload CSV files to Colab
# Run KEGG_Pathway_DotPlot.py
# Download generated plot
```

## Data Processing Pipeline

```
g:Profiler Results (CSV)
        ↓
Load and validate columns
        ↓
Filter for cardiometabolic pathways
        ↓
Combine both datasets
        ↓
Order by maximum -log10(FDR)
        ↓
Create dot plot with dual markers
        ↓
Save high-resolution output (300 DPI)
```

## Interpretation Guide

### Reading the Plot

**High -log10(FDR) values** (right side):
- More statistically significant enrichment
- Stronger pathway involvement

**Large point size**:
- More genes in the intersection
- Broader pathway activation

**Red color (RdYlBu_r scale)**:
- High statistical significance
- Strong enrichment

**Common pathways** (both datasets):
- Appear twice (circle + square)
- Indicate shared biological mechanisms

## Citation

If you use this code in your research, please cite:

```bibtex
@article{your_paper_2025,
  title={Your Paper Title},
  author={Your Name et al.},
  journal={Journal Name},
  year={2025},
  doi={your_doi}
}
```

## g:Profiler Reference

```bibtex
@article{gprofiler2019,
  title={g:Profiler: a web server for functional enrichment analysis and conversions of gene lists},
  author={Raudvere, Uku and Kolberg, Liis and Kuzmin, Ivan and Arak, Tambet and Adler, Priit and Peterson, Hedi and Vilo, Jaak},
  journal={Nucleic acids research},
  volume={47},
  number={W1},
  pages={W191--W198},
  year={2019},
  publisher={Oxford University Press}
}
```

## Troubleshooting

### Common Issues

**Issue**: "No cardiometabolic pathways found"
- **Solution**: Check if pathway names in your CSV match the predefined list exactly

**Issue**: File upload fails in Colab
- **Solution**: Ensure files are CSV format from g:Profiler intersection results

**Issue**: Plot is too crowded
- **Solution**: Reduce the number of pathways in `CARDIOMETABOLIC_PATHWAYS` list

**Issue**: Colors don't show variation
- **Solution**: Check if FDR values have sufficient range (try different enrichment threshold)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Datasets

- **GSE20950**: Subcutaneous adipose tissue - insulin-resistant vs insulin-sensitive
- **GSE43292**: Atherosclerotic plaque vs intact arterial tissue

Data source: [NCBI GEO](https://www.ncbi.nlm.nih.gov/geo/)

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Contact

For questions or issues, please open an issue on GitHub.

## Acknowledgments

- g:Profiler team for the pathway enrichment tool
- KEGG database for pathway annotations
- Matplotlib community for visualization tools
