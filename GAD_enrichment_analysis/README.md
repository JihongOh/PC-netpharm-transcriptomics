# GAD Disease Enrichment Visualization

Visualization of GAD (Genetic Association Database) disease enrichment analysis results from DAVID Bioinformatics Resources.

![Python](https://img.shields.io/badge/python-3.7+-blue.svg) ![License](https://img.shields.io/badge/license-MIT-green.svg)

## Example Outputs

### Figure 3: GAD enrichment analysis dot plot
![Example 3](/Figure3_GAD_DotPlot.png)


##  Features

-  **Automatic duplicate removal** - Keeps most significant result (lowest P-value)
- **Disease categorization** - Color-coded by functional category
-  **Cross-platform** - Works in Google Colab and local Python
-  **Clean formatting** - Converts complex terms: `Disease| context | drug` → `Disease (context; drug)`


##  Workflow

### Step 1: Generate GAD Enrichment Results from DAVID

1. **Go to DAVID website**: https://davidbioinformatics.nih.gov/
    
2. **Upload your gene list**:
    
    - Click "Shortcut to DAVID Tools"
    - Click "Upload" tab
    - Paste your gene list (one gene per line)
    - Select identifier type (e.g., "OFFICIAL_GENE_SYMBOL")
3. **Select species**:
    
    - Select taxonomy: `Homo sapiens (Human)`
    - Click "Submit List"
4. **Get GAD enrichment results**:
    
    - Click "Functional Annotation Chart"
    - Find "GAD_DISEASE" section
    - Click "Download File" → Select **CSV format**
    - Save the CSV file

### Step 2: Visualize with This Script

Use the downloaded CSV file with this script to create publication-quality figures.

##  Quick Start

### Google Colab (Easiest)

```python
# 1. Copy gad_enrichment_plot.py to Colab
# 2. Run the script
# 3. Upload your CSV when prompted
# 4. Download the result automatically
```

### Local Python

```bash
# Install dependencies
pip install pandas numpy matplotlib

# Run with your data
python gad_enrichment_plot.py path/to/your_GAD_results.csv
```

##  Input Format

CSV file from DAVID GAD enrichment analysis containing:

**Required columns:**

- `Term`: Disease name
- `Count`: Number of associated genes
- `P-Value`: Raw p-value
- `Benjamini`: Adjusted p-value (Benjamini-Hochberg FDR)

**Example:**

```csv
Category,Term,Genes,Count,List Total,Pop Hits,Pop Total,P-Value,Benjamini,...
GAD_DISEASE,lung cancer,29.87%,89,276,516,12919,2.73e-56,1.48e-52,...
GAD_DISEASE,colorectal cancer,25.84%,77,276,426,12919,1.29e-49,2.33e-46,...
```

##  Configuration

Edit these variables in the script to customize output:

```python
TOP_N = 10              # Number of diseases to display
DPI = 300               # Output resolution (increase for publication)
OUTPUT_FILENAME = 'Figure3_GAD_DotPlot.png'
```

**Adjust font sizes:**

```python
ax.tick_params(axis='y', labelsize=13)  # Y-axis labels (disease names)
ax.set_xlabel(..., fontsize=13)         # X-axis label
```

##  Methodology

### Duplicate Removal

When multiple entries exist for the same disease (case-insensitive):

- **Method**: Keep entry with lowest P-value (most significant)
- **Rationale**: Standard practice in enrichment analysis to ensure conservative and reliable results

**Example:**

```
lung cancer (P=2.73e-56) ✓ kept
lung cancer (P=3.86e-53) ✗ removed
```

### Disease Term Formatting

Complex terms with multiple contexts are reformatted for clarity:

```
Input:  Type 2 Diabetes| edema | rosiglitazone
Output: Type 2 Diabetes (edema; rosiglitazone)
```

### Disease Categories

Automatic classification into 9 functional categories:

- **Cancer** - Malignancies and neoplasms
- **Metabolic** - Diabetes, obesity, lipid disorders
- **Cardiovascular** - Heart disease, atherosclerosis
- **Kidney** - Renal diseases
- **Neurodegenerative** - Alzheimer's, Parkinson's
- **Autoimmune/Inflammatory** - MS, arthritis
- **Respiratory** - Asthma, COPD
- **Infectious** - Viral, bacterial diseases
- **Bone/Skeletal** - Bone density, osteoporosis

##  License
MIT License - See [LICENSE](https://claude.ai/chat/LICENSE) for details

##  Contact

For questions or issues:

- Open an issue on GitHub
- Email: jihong421@gmail.com

##  Acknowledgments

- [DAVID Bioinformatics Resources](https://davidbioinformatics.nih.gov/) for enrichment analysis tools
- [GAD (Genetic Association Database)](https://geneticassociationdb.nih.gov/) for disease-gene associations
