# Volcano Plot Analysis for Differential Gene Expression

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)

Automated volcano plot generation for visualizing differential gene expression analysis results from microarray datasets (GSE20950 and GSE43292).

## Overview

This repository contains code for generating publication-ready volcano plots with automatic gene label positioning. The analysis includes:

- Data preprocessing and quality control
- Differential gene expression filtering
- Volcano plot visualization with customizable thresholds
- Automatic label adjustment to prevent text overlap
- Gene-of-interest highlighting

## Features

-  Automated data cleaning (remove NaN, ambiguous probes, duplicates)
-  Customizable statistical thresholds (p-value and fold change)
-  Automatic label positioning using `adjustText`
-  High-resolution output (300 DPI)
-  Publication-ready formatting
-  Support for multiple datasets

## Requirements

### Python Version
- Python 3.8 or higher

### Required Packages
```
pandas>=1.3.0
numpy>=1.21.0
matplotlib>=3.4.0
adjustText>=0.8
```

## Installation

### Option 1: Google Colab (Recommended)
No installation required! Simply upload the notebook to Google Colab and run.

### Option 2: Local Installation
```bash
# Clone the repository
git clone https://github.com/JihongOh/PC-netpharm-transcriptomics.git
cd volcano-plot-analysis

# Install required packages
pip install pandas numpy matplotlib adjustText
```

## Usage

### Quick Start (Google Colab)

1. Open `Volcano_Plot_Analysis.ipynb` in Google Colab
2. Run the first cell to install `adjustText`
3. Upload your TSV files when prompted:
   - `GSE20950_top_table.tsv`
   - `GSE43292_top_table.tsv`
4. The script will automatically generate volcano plots

### Input Data Format

Your TSV files should contain the following columns:
- `ID`: Probe ID
- `Gene.symbol`: Gene symbol
- `logFC`: Log2 fold change
- `P.Value`: Raw p-value
- `adj.P.Val`: Adjusted p-value (for duplicate filtering)

Example:
```
ID          adj.P.Val   P.Value     logFC       Gene.symbol
8019622     0.0000133   7.30e-10    0.535       TMEM106A
7932985     0.0000133   1.18e-09    0.589       NRP1
```

### Configuration

Default thresholds can be modified in the notebook:
```python
PVAL_THRESHOLD = 0.01      # P-value threshold
LOG2FC_THRESHOLD = 0.58    # Log2 fold change threshold (|logFC| > 0.58)
```

Gene list for labeling:
```python
GENES_OF_INTEREST = [
    'AKT1', 'BAX', 'BCL2', 'CASP1', 'CCL2', 'CTNNB1', 'GSK3B', 'HMOX1',
    'ICAM1', 'IFNB1', 'IFNG', 'IL10', 'IL1B', 'IL6', 'INS', 'KDR',
    # ... add more genes as needed
]
```

## Output

The script generates two volcano plots:
- `GSE20950_volcano_plot.png` - Insulin-resistant vs insulin-sensitive adipose tissue
- `GSE43292_volcano_plot.png` - Atheroma plaque vs intact arterial tissue

### Output Features
- High resolution (300 DPI)
- Color-coded points:
  - 🔵 Blue: Downregulated genes
  - 🔴 Red: Upregulated genes
  - ⚫ Gray: Non-significant genes
- Dotted threshold lines
- Gene labels with automatic positioning
- Larger fonts and points for better visibility

## Data Processing Pipeline

1. **Data Loading**: Read TSV files
2. **Quality Control**:
   - Remove genes with missing symbols (NaN/empty)
   - Remove ambiguous probes (containing '///')
   - Remove duplicates (keep gene with lowest adj.P.Val)
3. **Statistical Filtering**:
   - Filter by p-value threshold
   - Filter by fold change threshold
4. **Visualization**:
   - Plot all genes
   - Highlight significant DEGs
   - Label genes of interest
   - Adjust labels to prevent overlap

## Example Datasets

Sample datasets are provided in the `example_data/` directory:
- `GSE20950_top_table_example.tsv`
- `GSE43292_top_table_example.tsv`

## Citation

If you use this code in your research, please cite:

```bibtex
@article{,
  title={Network Pharmacology and Transcriptome Analysis Reveal Potential Cardiometabolic Targets of Polygonum cuspidatum},
  author={Jihong Oh et al.},
  journal={biomedicine},
  year={2026},
  doi={}
}
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Datasets

- **GSE20950**: Gene expression profiling in subcutaneous adipose tissue from insulin-resistant and insulin-sensitive individuals
- **GSE43292**: Gene expression analysis of atherosclerotic plaque and intact arterial tissue

Data available from [NCBI GEO](https://www.ncbi.nlm.nih.gov/geo/).

## Troubleshooting

### Common Issues

**Issue**: Labels overlap on the plot
- **Solution**: The script uses `adjustText` to automatically prevent overlap. If issues persist, reduce the number of genes in `GENES_OF_INTEREST`.

**Issue**: File upload fails in Colab
- **Solution**: Ensure files are in TSV format with proper column names.

**Issue**: No significant genes found
- **Solution**: Check your threshold values. You may need to relax the `PVAL_THRESHOLD` or `LOG2FC_THRESHOLD`.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Contact

For questions or issues, please open an issue on GitHub or contact [jihong421@hanmail.net].

## Acknowledgments

- `adjustText` library for automatic label positioning
- GEO database for providing public datasets
