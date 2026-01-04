# src/ — Reusable Code (Project Modules)

This folder contains the modular Python code that mirrors the workflow implemented in the notebooks.
It is included to meet capstone rubric requirements for clean project structure and reproducibility.

## Files

- `preprocessing.py`
  - Preprocessing helpers (feature separation, encoders/scalers, pipeline utilities).
  - Mirrors the ColumnTransformer + OneHotEncoder + StandardScaler approach used in the notebooks.

- `modeling.py`
  - Model training helpers (Random Forest training, prediction utilities).
  - Mirrors the RandomForestClassifier setup used in the notebooks.

- `evaluation.py`
  - Evaluation helpers (accuracy, precision, recall, F1, ROC-AUC, classification report).
  - Includes plotting functions for Confusion Matrix and ROC Curve.

- `explainability.py`
  - SHAP explainability helpers (global and local explanations).
  - Mirrors the TreeExplainer + summary plot + waterfall plot logic used in the notebooks.

- `__init__.py`
  - Marks `src/` as a Python package so modules can be imported if needed.

## Note
The notebooks remain the primary “executable” artifacts.
The `src/` modules are included for structure and reuse (rubric-aligned), and can be imported if desired.