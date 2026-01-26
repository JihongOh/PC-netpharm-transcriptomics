# PC Network Pharmacology & Transcriptomics

Analysis scripts and notebooks for network pharmacology and transcriptomic analyses of *Polygonum cuspidatum* (PC, 虎杖, 호장근), including compound-target network construction, DEG preprocessing, enrichment analyses, and visualization.

---

## Associated Manuscript

The code in this repository supports the analyses presented in the manuscript:

**"Network pharmacology and transcriptomic integration reveals potential cardiometabolic regulatory mechanisms of *Polygonum cuspidatum*"**

---

## Data Sources

Publicly available transcriptomic datasets were obtained from the Gene Expression Omnibus (GEO):
- **GSE43292**: Atherosclerotic plaque vs. intact arterial tissue
- **GSE20950**: Insulin-resistant vs. insulin-sensitive subcutaneous adipose tissue

Differential expression analyses were performed using GEO2R (limma-based), and full result tables were further processed using custom Python scripts.

---

## Repository Structure

```
PC-netpharm-transcriptomics/
│
├── README.md                          # Main repository documentation
├── LICENSE                            # MIT License
│
├── CT_network/                        # Compound-Target Network Analysis
│   ├── CT_README.md                   # Network construction documentation
│   ├── Compound_target_network_preprocessing.ipynb
│   ├── input_files/                   # Raw compound-target data
│   └── output_files/                  # Processed network files
│
├── KEGG_analysis/                     # KEGG Pathway Analysis
│   ├── README.md                      # KEGG pathway analysis guide
│   ├── kegg_hub_genes_plot.py        # Hub gene visualization
│   ├── kegg_top10_plot.py            # Top 10 pathways visualization
│   ├── Figure2A_example.png          # Example output
│   └── Figure2B_example.png          # Example output
│
├── GAD_enrichment_analysis/           # Gene-Disease Association Analysis
│   ├── README.md                      # GAD enrichment documentation
│   ├── GAD_enrichment_plot.ipynb     # Disease association analysis
│   └── Figure3_GAD_DotPlot.png       # Example output
│
└── DEG_analysis/                      # Differential Expression Gene Analysis
    ├── DEG_analysis_README.md         # Overview of DEG workflow
    ├── GEO2R_parameters.md            # GEO2R analysis parameters
    │
    ├── Volcano_Plot_Analysis.ipynb    # Volcano plot generation
    ├── Volcano_plot_README.md         # Volcano plot documentation
    │
    ├── Venn_diagram_Overlap_analysis.ipynb  # PC-DEG overlap analysis
    ├── Venndiagram_README.md          # Venn diagram documentation
    │
    ├── DotPlot_Cardiometabolic_GSE20950_GSE43292_PC.ipynb
    └── Dotplot_README.md              # KEGG pathway dot plot documentation
```

---

## Analysis Workflow

### 1. Compound-Target Network Construction (`CT_network/`)

Build and preprocess compound-target interaction networks for PC's core-4 bioactive compounds (Polydatin, Resveratrol, Emodin, Physcion).

**Key Steps:**
- Data collection from multiple databases
- Network preprocessing and validation
- Target degree calculation
- Network file generation

**Usage:**
```bash
cd CT_network
# Open Compound_target_network_preprocessing.ipynb in Colab
```

📖 See: `CT_README.md`

---

### 2. KEGG Pathway Analysis (`KEGG_analysis/`)

Identify enriched KEGG pathways and visualize hub genes in pathway networks.

**Key Outputs:**
- Hub gene networks (Figure 2A)
- Top 10 enriched pathways (Figure 2B)

**Usage:**
```bash
cd KEGG_analysis
python kegg_hub_genes_plot.py
python kegg_top10_plot.py
```

📖 See: `KEGG_analysis/README.md`

---

### 3. Gene-Disease Association Analysis (`GAD_enrichment_analysis/`)

Analyze disease associations of PC target genes using GAD (Genetic Association Database).

**Key Outputs:**
- Disease enrichment dot plots (Figure 3)
- Cardiovascular and metabolic disease associations

**Usage:**
```bash
cd GAD_enrichment_analysis
# Open GAD_enrichment_plot.ipynb in Colab
```

📖 See: `GAD_enrichment_analysis/README.md`

---

### 4. DEG Analysis & Visualization (`DEG_analysis/`)

Comprehensive differential expression analysis and multi-dataset comparison.

#### 4a. Data Preparation
- Download DEG data from GEO using GEO2R
- Follow parameters in `GEO2R_parameters.md`

#### 4b. Volcano Plot Analysis
Visualize differential gene expression with publication-ready volcano plots.

**Features:**
- Automated data preprocessing
- Statistical filtering (adj.P.Val < 0.01, |log2FC| > 0.58)
- Gene-of-interest labeling
- High-resolution output (300 DPI)

**Usage:**
```bash
cd DEG_analysis
# Open Volcano_Plot_Analysis.ipynb in Colab
```

📖 See: `Volcano_plot_README.md`

#### 4c. Venn Diagram Overlap Analysis
Identify shared genes between PC targets and DEGs from both datasets.

**Features:**
- 3-way Venn diagram (PC targets ∩ GSE20950 ∩ GSE43292)
- Target degree calculation
- Overlap tables with fold change and significance
- Excel output with formatted supplement tables

**Usage:**
```bash
cd DEG_analysis
# Open Venn_diagram_Overlap_analysis.ipynb in Colab
```

📖 See: `Venndiagram_README.md`

#### 4d. KEGG Pathway Dot Plot
Compare cardiometabolic pathway enrichment across datasets.

**Features:**
- Dual-dataset comparison
- Color-coded by significance
- Point size proportional to gene count
- Cardiometabolic pathway focus

**Usage:**
```bash
cd DEG_analysis
# Open DotPlot_Cardiometabolic_GSE20950_GSE43292_PC.ipynb in Colab
```

📖 See: `Dotplot_README.md`

---

## Quick Start

```bash
# Clone the repository
git clone https://github.com/JihongOh/PC-netpharm-transcriptomics.git
cd PC-netpharm-transcriptomics

# Navigate to desired analysis folder
cd CT_network          # OR
cd KEGG_analysis       # OR
cd GAD_enrichment_analysis  # OR
cd DEG_analysis

# Follow the README in each folder for specific instructions
```

---

## Requirements

### Python Packages
```
pandas>=1.3.0
numpy>=1.21.0
matplotlib>=3.4.0
matplotlib-venn>=0.11.6
adjustText>=0.8
openpyxl>=3.0.9
```

### Installation
```bash
pip install pandas numpy matplotlib matplotlib-venn adjustText openpyxl
```

### Platform
- **Recommended**: Google Colab (no local installation required)
- **Alternative**: Local Jupyter Notebook or Python environment

---

## Key Datasets

| Dataset | Description | Tissue Type | Comparison |
|---------|-------------|-------------|------------|
| **GSE20950** | Metabolic dysfunction | Subcutaneous adipose tissue | Insulin-resistant vs Insulin-sensitive |
| **GSE43292** | Vascular pathology | Arterial tissue | Atheroma plaque vs Intact tissue |

---

## Citation

If you use this code in your research, please cite:

```bibtex
@article{oh2025pc,
  title={Network pharmacology and transcriptomic integration reveals potential cardiometabolic regulatory mechanisms of Polygonum cuspidatum},
  author={Oh, Jihong et al.},
  journal={[Biomedicines]},
  year={2026},
  doi={Under review}
}
```

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## Contact

For questions or issues, please open an issue on GitHub or contact:
- **Author**: Jihong Oh
- **Email**: [jihong421@gmail.com]

---

## Acknowledgments

- NCBI GEO for providing public transcriptomic datasets
- Network pharmacology databases for compound-target predictions
- Open-source Python community for analysis tools
