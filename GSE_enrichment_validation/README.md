# Pathway Enrichment Assessment in Cardiometabolic Transcriptomic Datasets

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.12+](https://img.shields.io/badge/python-3.12+-blue.svg)](https://www.python.org/downloads/)

This repository contains scripts for global and targeted pathway over-representation analysis (ORA) in two independent cardiometabolic transcriptomic datasets (GSE43292 and GSE20950).

The workflow assesses enrichment of AGE-RAGE signaling and lipid/atherosclerosis pathways using differential expression results with experimental background correction.

---

## Overview

The analysis integrates three complementary approaches:

1. **Genome-wide KEGG pathway ranking** - Establishes pathway importance in global context
2. **Targeted Fisher's exact test** - Statistical validation of specific pathways
3. **Gene-level expression profiling** - Identifies individual gene alterations

These scripts reproduce the pathway validation analysis described in the manuscript. Results represent statistical enrichment assessment and do not constitute experimental validation of causal mechanisms.

---

## Datasets

| Dataset | Context | Comparison | Samples |
|---------|---------|------------|---------|
| GSE43292 | Atherosclerosis | Plaque vs intact artery | 32 vs 32 |
| GSE20950 | Insulin resistance | IR vs insulin-sensitive adipose | 19 vs 20 |

Public datasets were processed using GEO2R. DEGs were filtered using adjusted p < 0.01 and absolute log2FC > 0.58.

---

## Workflow

### Step 1: DEG Preprocessing
```bash
python step1_preprocess_deg.py
```

**Input**: GEO2R top table files (TSV format)

**Output**: QC-filtered gene lists and experimental background sets

Preprocessing steps:
- Remove NaN/ambiguous gene symbols
- Deduplicate probes (keep lowest adj.p per gene)
- Generate background and DEG files for g:Profiler

---

### Step 2: Global KEGG Enrichment

Performed via g:Profiler web interface: https://biit.cs.ut.ee/gprofiler/gost

**Settings**:
- Organism: Homo sapiens
- Statistical domain: Custom (upload background from Step 1)
- Data sources: KEGG only
- Significance: Benjamini-Hochberg FDR < 0.01

**Download**: Detailed results (CSV format)

---

### Step 3: Targeted Validation
```bash
python step2_validate_pathway_enrichment.py
```

**Input**: 
- Preprocessed stats files (Step 1)
- g:Profiler results (Step 2)

**Analysis**:
- Fisher's exact test for pathway enrichment
- Odds ratio calculation
- Gene-level expression summaries

**Output**:
- Global KEGG rankings (full tables)
- Integrated enrichment summary
- Gene expression heatmaps

All outputs correspond to Supplementary Tables and Figures referenced in the manuscript.

---

## Requirements

**Python**: 3.12 or higher
```bash
pip install -r requirements.txt
```

**Dependencies**:
```
pandas>=2.0.2
numpy>=2.0.2
matplotlib>=3.10.0
seaborn>=0.13.2
scipy>=1.16.3
```

---

## Key Output Files

| File | Description |
|------|-------------|
| KEGG_ORA_GSE43292_full.tsv | Complete global pathway ranking for GSE43292 |
| KEGG_ORA_GSE20950_full.tsv | Complete global pathway ranking for GSE20950 |
| Table_publication_ready.tsv | Integrated summary combining global and targeted results |
| Fig_enrichment_heatmap.png | Pathway enrichment visualization |
| Fig_gene_expression_KEGG_04933.png | AGE-RAGE pathway gene expression heatmap |
| Fig_gene_expression_KEGG_05417.png | Lipid pathway gene expression heatmap |

---

## Reproducibility

- **Database access**: 14 February 2026
- **g:Profiler**: (https://biit.cs.ut.ee/gprofiler/gost)

Results are reproducible with the listed software versions and database access date.

---


## Contact

**Jihong Oh**

Email: jihong421@gmail.com


