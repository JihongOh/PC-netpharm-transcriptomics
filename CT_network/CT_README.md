# Polygonum Cuspidatum Core-4 Compound-Target Network Preprocessing

## Overview

This repository contains Python code for preprocessing and generating compound-target association networks from the HERB 2.0 database. The workflow is designed for network pharmacology studies of *Polygonum cuspidatum* (虎杖), specifically focusing on the Core-4 bioactive compounds: **Resveratrol**, **Polydatin**, **Emodin**, and **Physcion**.

## Background

*Polygonum cuspidatum* (Huzhang) is a traditional Chinese medicinal herb with well-documented pharmacological properties. This analysis identifies molecular targets for its core bioactive compounds using data from:

- **HERB 2.0** (http://herb.ac.cn/v2): A comprehensive Chinese herbal medicine database
- **TCMSP 2.3**: Traditional Chinese Medicine Systems Pharmacology Database

The Core-4 compounds were selected based on:
1. Prior phytochemical studies
2. Well-established biological activities
3. Relevance to therapeutic mechanisms of *P. cuspidatum*

**Database Access Date**: 2026-01-21

## Methodology

### Target Identification (HERB 2.0)

Target proteins for each compound were identified using the following criteria:

1. **InChIKey Matching**: InChIKeys from TCMSP 2.3 were used to query corresponding targets in HERB 2.0
2. **Evidence Filtering**: Only targets supported by reference-mining evidence were retained
3. **Gene Symbol Standardization**: All gene symbols were standardized according to NCBI Gene nomenclature
4. **Deduplication**: Duplicate target entries were removed at preprocessing stage

### Data Processing Steps

```
Input (HERB 2.0 exports)
        ↓
[1] Parse compound-specific target files
        ↓
[2] Extract unique gene symbols
        ↓
[3] Remove duplicates
        ↓
[4] Standardize gene nomenclature
        ↓
[5] Generate network file & statistics
        ↓
Output (compound_target_network.csv)
```

## File Structure

```
├── compound_target_network_preprocessing.py  # Main preprocessing script
├── README.md                                  # This file
├── example_input/                             # Example input files
└── example_output/
    └── compound_target_network.csv           # Example output file
```

## Requirements

### Software
- Python 3.8+
- Google Colab (recommended) or local Python environment

### Python Dependencies
```
pandas>=1.3.0
openpyxl>=3.6.0
numpy>=1.21.0
```

Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

### In Google Colab (Recommended)

1. **Open the script in Google Colab**
   - Upload `compound_target_network_preprocessing.py` to Colab
   - Or copy-paste the code into a Colab cell

2. **Prepare input files**
   - Export target data from HERB 2.0 for each Core-4 compound
   - Expected file naming format:
     ```
     physcion_targets_HERB2.0.xlsx
     emodin_targets_HERB2.0.xlsx
     resveratrol_targets_HERB2.0.xlsx
     polydatin_targets_HERB2.0.xlsx
     ```
   - Ensure files contain a "Gene Symbol" or similar column

3. **Run the script**
   ```python
   from compound_target_network_preprocessing import CompoundTargetNetworkGenerator
   
   generator = CompoundTargetNetworkGenerator()
   network_df = generator.run()
   ```

4. **Download output**
   - The script automatically downloads `compound_target_network.csv`
   - File can also be manually downloaded from Colab file explorer

### Local Python Environment

```python
from compound_target_network_preprocessing import CompoundTargetNetworkGenerator

# Initialize generator
generator = CompoundTargetNetworkGenerator()

# Run preprocessing pipeline
network_df = generator.run(output_filename='compound_target_network.csv')

# Access results
print(f"Total pairs: {len(network_df)}")
print(network_df.head())
```

## Output Format

The output CSV file (`compound_target_network.csv`) contains:

| Column | Description |
|--------|-------------|
| compound | Standardized compound name (Physcion, Emodin, Resveratrol, Polydatin) |
| target | Gene symbol of the target protein |

### Example Output
```
compound,target
Physcion,TP53
Physcion,CASP3
Physcion,TNF
Emodin,TP53
Emodin,CASP3
Emodin,ESR1
Resveratrol,TP53
...
```

## Example Statistics Output

The preprocessing script generates the following statistics:

```
Network Statistics
======================================================================

Summary:
   Total compound-target pairs: 1,245
   Unique compounds: 4
   Unique targets: 487

Compound Distribution:
   Physcion: 325 targets
   Emodin: 298 targets
   Resveratrol: 412 targets
   Polydatin: 210 targets

Shared Targets (all 4 compounds):
   Count: 85
   Examples: TP53, CASP3, TNF, IL6, MAPK1, ...
```

## Limitations

1. **HERB 2.0 Completeness**: Network reflects available entries in HERB 2.0 as of 2025-01-21. Database updates may add or modify targets.

2. **InChIKey Accuracy**: Target matching depends on accurate InChIKey data in TCMSP 2.3. Manual verification recommended for critical targets.

3. **Evidence Filtering**: Only reference-mining supported targets included. Some experimentally validated targets may not be captured.

## Citation

If you use this code or data in your research, please cite:

```bibtex
@software{PC-netpharm-transcriptomics,
  author = {Jihong Oh},
  title = {Network Pharmacology and Transcriptome Analysis Reveal 
Potential Cardiometabolic Targets of Polygonum cuspidatum},
  year = {2026},
  url = {https://github.com/JihongOh/PC-netpharm-transcriptomics}
}
```

And acknowledge the database sources:

```
HERB 2.0: A high-throughput experiment- and reference-supported knowledgebase 
of herbal medicine-ingredient-target interactions

TCMSP 2.3: Traditional Chinese Medicine Systems Pharmacology Database and 
Analysis Platform
```

## Related Work

This preprocessing pipeline is part of a broader network pharmacology study investigating the therapeutic mechanisms of *Polygonum cuspidatum* using integrative computational methods.

## Contact & Support

For questions, suggestions, or issues:
- Open an issue on GitHub
- Contact: [jihong421@gmail.com]

## Version History

- **v1.0** (2026-01-21): Initial release
  - Core-4 compound target extraction from HERB 2.0
  - Deduplication and standardization
  - Statistics generation

## Acknowledgments

- HERB 2.0 database curators
- TCMSP database developers
- Network pharmacology research community
