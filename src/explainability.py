"""
Explainability utilities using SHAP.

This module mirrors SHAP-based explainability used in the notebooks.
"""

import shap


def compute_shap_values(model, X_sample):
    """
    Compute SHAP values for a trained tree-based model.
    """
    explainer = shap.TreeExplainer(model)
    shap_values = explainer.shap_values(X_sample)
    return shap_values


def plot_global_importance(shap_values, X_sample):
    """
    Plot global feature importance using SHAP.
    """
    shap.summary_plot(shap_values, X_sample, show=True)