# Pathway Enrichment Validation in GSE Cardiometabolic Datasets

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.12+](https://img.shields.io/badge/python-3.12+-blue.svg)](https://www.python.org/downloads/)

Validation of AGE-RAGE signaling and lipid/atherosclerosis pathway enrichment in 
cardiometabolic disease transcriptomic datasets (GSE43292, GSE20950).

## Overview

This analysis validates the biological relevance of predicted therapeutic targets by 
evaluating pathway-level enrichment in disease-relevant transcriptomic datasets.

**Context**: Following network pharmacology prediction of Polygonum cuspidatum targets, 
this analysis validates whether AGE-RAGE signaling and lipid/atherosclerosis pathways 
are genuinely altered in disease contexts.

### Analysis Strategy

**1. Global KEGG Pathway Ranking**
- Genome-wide assessment of all KEGG pathways
- Determines relative importance of target pathways
- Provides unbiased context: "Among all biological processes, where do our pathways rank?"

**2. Targeted Statistical Validation**
- Fisher's exact test for specific pathways of interest:
  - AGE-RAGE signaling pathway in diabetic complications (KEGG:04933)
  - Lipid and atherosclerosis (KEGG:05417)
- Quantifies enrichment strength independent of global ranking
- Controls for experimental background

**3. Gene-Level Expression Profiling**
- Identifies which specific pathway genes are altered
- Reveals regulation direction (activation vs suppression)
- Demonstrates coordinated transcriptomic changes

---

## Validation Datasets

| Dataset | Disease Context | Comparison | Samples | Relevance |
|---------|----------------|------------|---------|-----------|
| **GSE43292** | Atherosclerosis | Plaque vs intact arterial tissue | 32 vs 32 | Validates lipid/atherosclerosis pathway |
| **GSE20950** | Metabolic dysfunction | Insulin-resistant vs insulin-sensitive adipose | 19 vs 20 | Validates AGE-RAGE/metabolic pathways |

**Rationale for Dataset Selection:**
- Independent patient cohorts (external validation)
- Disease-relevant tissues 
- Sufficient statistical power (n ≥ 15 per group)
- Available expression data with quality annotation

---

## Key Questions Addressed

1. **Are predicted pathways actually enriched in disease?**
   - Global ranking shows context among all pathways
   - Targeted test confirms statistical significance

2. **How strong is the enrichment?**
   - Odds ratios quantify effect size

3. **Which genes drive the enrichment?**
   - Gene-level heatmaps identify specific alterations
   - Regulation direction reveals pathway activation status

---

## Requirements

### Software
- Python 3.12 or higher
- Google Colab (recommended) or local Jupyter environment
- Web browser (for g:Profiler step)

### Python Dependencies
```bash
