# 🧬 MRSA Biofilm Surveillance Dashboard

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.15863612.svg)](https://doi.org/10.5281/zenodo.15863612)
[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/release/python-390/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.45.0+-red.svg)](https://streamlit.io)
[![ORCID](https://img.shields.io/badge/ORCID-0000--0003--2070--2811-green.svg)](https://orcid.org/0000-0003-2070-2811)

An AI-driven genomic surveillance and mechanistic inference system for high-biofilm MRSA lineages.

## 🎯 Project Overview

This dashboard demonstrates key components of an advanced research project focusing on methicillin-resistant *Staphylococcus aureus* (MRSA) biofilm formation. The project aims to:

1. **Identify genetic determinants** of high-biofilm MRSA clones
2. **Decode regulatory circuitry** governing the planktonic→sessile switch
3. **Deploy real-time surveillance** & therapeutic-prioritisation
4. **Analyze RNA dynamics** & design RNA-based interventions

## 🚀 Features

- **Phylogenetic visualization** of MRSA lineages with biofilm risk overlay
- **Biofilm risk scoring** based on genomic markers
- **Geographic distribution** mapping of high-risk strains
- **Therapeutic coverage calculator** for phage and peptide therapies
- **RNA stability analysis** for regulatory mechanisms
- **RNA-targeting interventions** design and evaluation
- **Interactive file upload** for new MRSA genome analysis

## 🛠️ Installation

### Prerequisites
- Python 3.9 or higher
- pip package manager

### Setup

1. Clone the repository:
```bash
git clone https://github.com/mojo8787/Genom2.git
cd Genom2
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the application:
```bash
streamlit run app.py
```

4. Open your browser and navigate to `http://localhost:8501`

## 📊 Dashboard Components

### 1. Main Dashboard
- Project overview and metrics
- Sample phylogenetic tree with biofilm risk overlay
- Biofilm formation distribution analysis

### 2. Genomic Determinants
- GWAS results visualization
- Machine learning models for biofilm prediction
- Feature importance analysis

### 3. Regulatory Circuits
- Regulatory network visualization
- Gene expression pathway analysis
- Mobile genetic element impact assessment

### 4. Surveillance Dashboard
- Real-time tracking of high-biofilm MRSA lineages
- Geographic distribution mapping
- Therapeutic recommendations

### 5. RNA Dynamics
- RNA stability analysis
- Antisense oligonucleotide design
- CRISPR-Cas13 targeting evaluation

## 🧪 Usage

### Analyzing New MRSA Genomes

1. Navigate to the main dashboard
2. Use the file uploader to submit FASTA or FASTQ files
3. View analysis results across multiple tabs:
   - Sequence information
   - Biofilm formation prediction
   - Phage therapy coverage
   - RNA-based intervention targets

### Exploring Existing Data

Use the sidebar navigation to explore:
- **Genomic Determinants**: ML models and GWAS results
- **Regulatory Circuits**: Network analysis and pathway visualization
- **Surveillance**: Geographic tracking and therapeutic prioritization
- **RNA Dynamics**: Stability analysis and intervention design

## 🔬 Scientific Background

This project addresses the critical challenge of MRSA biofilm formation, which contributes to:
- Increased antibiotic resistance
- Persistent infections
- Healthcare-associated complications

By combining genomic surveillance with mechanistic inference, the dashboard enables:
- Early detection of high-biofilm strains
- Targeted therapeutic interventions
- RNA-based treatment strategies

## 📁 Project Structure

```
Genom2/
├── app.py                 # Main Streamlit application
├── requirements.txt       # Python dependencies
├── pyproject.toml        # Project configuration
├── utils/                # Utility modules
│   ├── data_loader.py    # Data loading functions
│   ├── visualization.py  # Plotting and visualization
│   ├── ml_models.py      # Machine learning models
│   ├── phage_calculator.py # Therapeutic calculations
│   └── rna_analysis.py   # RNA dynamics analysis
├── pages/                # Additional Streamlit pages
├── data/                 # Sample datasets
└── .streamlit/          # Streamlit configuration
```

## 🤝 Contributing

This project is developed for research purposes in antimicrobial resistance and genomic surveillance. For collaboration opportunities or questions, please contact the project author.

## 📄 License

This project is developed for research purposes in computational biology and antimicrobial resistance.

## 👨‍🔬 Author

**Dr. Almotasem Bellah Younis, PhD**
- Website: [almotasem-younis.netlify.app](https://almotasem-younis.netlify.app)
- Project: Mechanistic AI: Decoding Mobile Genetic Elements as Master Regulators of MRSA Biofilms for Precision Therapy
- Research Focus: Advanced genomic surveillance and antimicrobial resistance

## 🎯 Research Impact

This dashboard demonstrates the integration of:
- **Genomic surveillance** for pathogen monitoring
- **Machine learning** for predictive modeling
- **Network analysis** for mechanistic understanding
- **RNA dynamics** for therapeutic targeting
- **Interactive visualization** for scientific communication

---

*Developed as part of advanced research in MRSA biofilm formation and therapeutic intervention strategies.* 