from dataclasses import dataclass
from typing import Tuple, Dict, Any, Optional

import numpy as np
import matplotlib.pyplot as plt

from sklearn.metrics import (
    accuracy_score, precision_score, recall_score, f1_score,
    roc_auc_score, classification_report,
    ConfusionMatrixDisplay, RocCurveDisplay
)


@dataclass
class EvalResult:
    metrics: Dict[str, float]
    y_pred: np.ndarray
    y_proba: np.ndarray
    report: str


def safe_proba_positive_class(model, X, positive_class_index: int = 1) -> np.ndarray:
    """
    Returns P(class=1) safely for binary classifiers.
    """
    proba = model.predict_proba(X)
    # proba shape: (n, 2) for binary
    if proba.ndim == 2 and proba.shape[1] >= 2:
        return proba[:, positive_class_index]
    # fallback (shouldn't happen in normal sklearn binary classifiers)
    return proba.ravel()


def compute_metrics(model, X_test, y_test) -> Dict[str, float]:
    y_pred = model.predict(X_test)
    y_proba = safe_proba_positive_class(model, X_test)

    return {
        "accuracy": float(accuracy_score(y_test, y_pred)),
        "precision": float(precision_score(y_test, y_pred)),
        "recall": float(recall_score(y_test, y_pred)),
        "f1": float(f1_score(y_test, y_pred)),
        "roc_auc": float(roc_auc_score(y_test, y_proba)),
    }


def print_report(model, X_test, y_test, labels: Tuple[str, str] = ("Normal", "Attack")) -> str:
    y_pred = model.predict(X_test)
    rep = classification_report(y_test, y_pred, target_names=list(labels))
    print(rep)
    return rep


def plot_confusion_matrix(y_true, y_pred, labels: Tuple[str, str] = ("Normal", "Attack"), title: str = ""):
    ConfusionMatrixDisplay.from_predictions(
        y_true, y_pred,
        display_labels=list(labels),
        cmap="Blues"
    )
    if title:
        plt.title(title)
    plt.tight_layout()
    plt.show()


def plot_roc_curve(y_true, y_proba, title: str = "", name: str = "Classifier"):
    RocCurveDisplay.from_predictions(y_true, y_proba, name=name)
    if title:
        plt.title(title)
    plt.tight_layout()
    plt.show()


def evaluate_model(
    model,
    X_test,
    y_test,
    labels: Tuple[str, str] = ("Normal", "Attack"),
    model_name: str = "Model"
) -> EvalResult:
    """
    One-call evaluation wrapper:
    - predicts y_pred and y_proba
    - computes metrics
    - generates classification report text
    """
    y_pred = model.predict(X_test)
    y_proba = safe_proba_positive_class(model, X_test)

    metrics = {
        "accuracy": float(accuracy_score(y_test, y_pred)),
        "precision": float(precision_score(y_test, y_pred)),
        "recall": float(recall_score(y_test, y_pred)),
        "f1": float(f1_score(y_test, y_pred)),
        "roc_auc": float(roc_auc_score(y_test, y_proba)),
    }

    report = classification_report(y_test, y_pred, target_names=list(labels))

    return EvalResult(metrics=metrics, y_pred=y_pred, y_proba=y_proba, report=report)