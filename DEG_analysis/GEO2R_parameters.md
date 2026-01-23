# GEO2R Differential Expression Analysis Parameters

This document describes the parameters and settings used for differential
expression analyses performed using GEO2R
(https://www.ncbi.nlm.nih.gov/geo/geo2r/).

---

## Datasets

### GSE43292
- Tissue column:
  - Atheroma plaque
  - Macroscopically intact tissue

### GSE20950
- Metabolic status column:
  - Insulin sensitive
  - Insulin resistance

---

## Analysis Method

- Differential expression method: limma
- Multiple testing correction: Benjamini–Hochberg (FDR)
- Log2 transformation: auto-detect
- Precision weights (voom): enabled
- Force normalization: disabled
- Platform annotation: NCBI generated

---

## Significance Thresholds

- Adjusted p-value (FDR): < 0.01
- Absolute log2 fold change: > 0.58

---

## Output Processing

- Full differential expression result tables were downloaded using the
  "Download full table" option in GEO2R.
- Downloaded tables were further preprocessed using custom Python scripts
  to remove ambiguous probes, harmonize gene symbols, and apply consistent
  significance thresholds.

---

## Data

- Download date: Jan 23, 2026

---

## Notes

- GEO2R performs limma-based differential expression analysis on normalized
  expression values provided by GEO.
- No additional normalization or statistical modeling was performed outside
  GEO2R.
