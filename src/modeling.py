"""
Model training utilities for UNSW-NB15.
"""

from sklearn.ensemble import RandomForestClassifier


def train_random_forest(X_train, y_train, random_state=42):
    """
    Train Random Forest classifier for intrusion detection.
    """
    model = RandomForestClassifier(
        n_estimators=200,
        random_state=random_state,
        class_weight="balanced",
        n_jobs=-1,
    )
    model.fit(X_train, y_train)
    return model

"""
Modeling module (documentation-only).

Model used:
- RandomForestClassifier
- class_weight="balanced"

Training approach (as implemented in the notebook):
- Preprocess features using a ColumnTransformer (scaling + one-hot encoding)
- Train the Random Forest on the preprocessed matrix
- Evaluate on a held-out test split

Source of truth:
- notebooks/01_capstone_unsw_nb15_full_analysis.ipynb
"""