<<<<<<< HEAD
# erecongco-capstone-unsw-nb15
Capstone Project
=======
# Explainable & Fair Intrusion Detection (UNSW-NB15)

## Overview
This project implements an explainable and fairness-aware intrusion detection system using the UNSW-NB15 dataset.  
It combines high-performance machine learning models with SHAP explainability and post-hoc fairness auditing to support trustworthy AI-driven security decisions.

The project was developed as a capstone demonstrating end-to-end ML workflow: data analysis, modeling, explainability, fairness evaluation, and stakeholder communication.

---

## Dataset
- **Source:** UNSW-NB15 Network Intrusion Dataset  
- **Records:** 82,332  
- **Features:** 45 original features (numeric + categorical)  
- **Target:**  
  - `0` = Normal traffic  
  - `1` = Attack traffic  

---

## Project Structure

```text
ERECONGCO-CAPSTONE-UNSW-NB15/
├── data/                      # Dataset files or pointers
├── notebooks/                 # Jupyter notebooks (analysis + technical slides)
│   ├── 01_capstone_unsw_nb15_full_analysis.ipynb
│   └── 02_technical_presentation_slides.ipynb
├── src/                       # Reusable preprocessing and modeling code
├── outputs/                   # Figures, metrics, intermediate results
├── reports/                   # Final reports and presentations
│   └── business_presentation_explainable_ids.pptx
├── README.md
└── requirements.txt

## Presentations

- **Technical Presentation (Jupyter Slides):**
  `notebooks/02_technical_presentation_slides.ipynb`

- **Business-Facing Presentation (PowerPoint):**
  `reports/business_presentation_explainable_ids.pptx`
>>>>>>> 2b0b9d8 (Initial commit: project structure, notebooks, and documentation)
