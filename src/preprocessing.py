"""
Preprocessing utilities for UNSW-NB15.

This module mirrors preprocessing steps executed in the notebooks:
- Train/test split
- ColumnTransformer with scaling and encoding
"""

from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.model_selection import train_test_split


def build_preprocessor(numeric_features, categorical_features):
    """
    Create preprocessing pipeline used in model training.
    """
    return ColumnTransformer(
        transformers=[
            ("num", StandardScaler(), numeric_features),
            ("cat", OneHotEncoder(handle_unknown="ignore"), categorical_features),
        ]
    )


def split_data(X, y, test_size=0.2, random_state=42):
    """
    Split dataset into train and test sets.
    """
    return train_test_split(X, y, test_size=test_size, random_state=random_state, stratify=y)