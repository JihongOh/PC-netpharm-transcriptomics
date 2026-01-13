# GAD Disease Enrichment Visualization

Publication-quality visualization of GAD (Genetic Association Database) disease enrichment analysis results from DAVID Bioinformatics Resources.

![Python](https://img.shields.io/badge/python-3.7+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

## 🎯 Features

- ✅ **Automatic duplicate removal** - Keeps most significant result (lowest P-value)
- ✅ **Disease categorization** - Color-coded by functional category
- ✅ **Cross-platform** - Works in Google Colab and local Python
- ✅ **Clean formatting** - Converts complex terms: `Disease| context | drug` → `Disease (context; drug)`
- ✅ **Publication-ready** - High-resolution output (300 DPI)

## 📊 Example Output

![Example](example_output/Figure3_example.png)

*Top 10 most significantly enriched diseases with automatic categorization and clean formatting.*

## 🚀 Quick Start

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
python gad_enrichment_plot.py path/to/your_data.csv
```

## 📥 Input Format

CSV file from DAVID GAD enrichment analysis with these columns:
- `Term`: Disease name
- `Count`: Number of associated genes
- `P-Value`: Raw p-value
- `Benjamini`: Adjusted p-value (FDR)

## ⚙️ Configuration

Edit these variables in the script:

```python
TOP_N = 10              # Number of diseases to display
DPI = 300               # Output resolution
OUTPUT_FILENAME = 'Figure3_GAD_DotPlot.png'
```

## 📖 Documentation

- **[GUIDE.md](GUIDE.md)** - Detailed usage instructions
- **[GITHUB_UPLOAD_GUIDE.md](GITHUB_UPLOAD_GUIDE.md)** - How to upload to GitHub

## 🔬 Methodology

### Duplicate Removal
When multiple entries exist for the same disease (case-insensitive):
- **Method**: Keep entry with lowest P-value (most significant)
- **Rationale**: Standard practice in enrichment analysis
- **Reference**: Khatri et al. (2012) PLoS Comput Biol

### Disease Categories

Automatic classification into 9 categories:
- Cancer
- Metabolic  
- Cardiovascular
- Kidney
- Neurodegenerative
- Autoimmune/Inflammatory
- Respiratory
- Infectious
- Bone/Skeletal

## 📚 Citation

If you use this tool in your research, please cite:

**DAVID:**
```
Huang da W, Sherman BT, Lempicki RA. 
Systematic and integrative analysis of large gene lists using DAVID bioinformatics resources. 
Nat Protoc. 2009;4(1):44-57.
```

**Multiple testing correction:**
```
Benjamini Y, Hochberg Y. 
Controlling the false discovery rate: a practical and powerful approach to multiple testing. 
J R Stat Soc Series B Methodol. 1995;57(1):289-300.
```

## 📝 License

MIT License - See [LICENSE](LICENSE) for details

## 🤝 Contributing

Contributions welcome! Please open an issue or submit a pull request.

## 📧 Contact

For questions or issues:
- Open an issue on GitHub
- Email: your.email@example.com

## 🙏 Acknowledgments

- DAVID Bioinformatics Resources for enrichment analysis tools
- GAD (Genetic Association Database) for disease-gene associations
