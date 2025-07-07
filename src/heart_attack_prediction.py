"""Run a logistic regression pipeline on the heart attack dataset."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path
from typing import Tuple

import matplotlib.pyplot as plt
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    ConfusionMatrixDisplay,
    accuracy_score,
    f1_score,
    precision_score,
    recall_score,
)
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler


def parse_args() -> argparse.Namespace:
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(
        description="Heart Attack Risk Prediction with logistic regression",
    )
    parser.add_argument("--data", required=True, help="Path to dataset CSV")
    parser.add_argument("--out", required=True, help="Output directory")
    return parser.parse_args()


def load_dataset(path: str) -> pd.DataFrame:
    """Load CSV into a DataFrame."""
    return pd.read_csv(path)


def split_xy(df: pd.DataFrame) -> Tuple[pd.DataFrame, pd.Series]:
    """Return features and target column."""
    target = "output" if "output" in df.columns else "target"
    if target not in df.columns:
        target = df.columns[-1]
    X = df.drop(columns=target)
    y = df[target]
    return X, y


def make_preprocessor(X: pd.DataFrame) -> ColumnTransformer:
    """Return a ColumnTransformer for numeric and categorical features."""
    cat_cols = X.select_dtypes(include=["object", "category"]).columns
    num_cols = X.select_dtypes(exclude=["object", "category"]).columns
    num_pipe = Pipeline(
        [("imputer", SimpleImputer(strategy="median")), ("scaler", StandardScaler())]
    )
    cat_pipe = Pipeline(
        [
            ("imputer", SimpleImputer(strategy="most_frequent")),
            ("onehot", OneHotEncoder(handle_unknown="ignore")),
        ]
    )
    return ColumnTransformer([("num", num_pipe, num_cols), ("cat", cat_pipe, cat_cols)])


def build_pipeline(X: pd.DataFrame) -> Pipeline:
    """Create a pipeline with preprocessing and logistic regression."""
    preprocessor = make_preprocessor(X)
    return Pipeline(
        [
            ("prep", preprocessor),
            ("clf", LogisticRegression(max_iter=1000, solver="liblinear")),
        ]
    )


def evaluate(
    model: Pipeline, X_test: pd.DataFrame, y_test: pd.Series, out_dir: Path
) -> None:
    """Print metrics and save confusion matrix."""

    preds = model.predict(X_test)
    acc = accuracy_score(y_test, preds)
    prec = precision_score(y_test, preds, zero_division=0)
    rec = recall_score(y_test, preds, zero_division=0)
    f1 = f1_score(y_test, preds, zero_division=0)
    print(f"Accuracy: {acc:.3f}")
    print(f"Precision: {prec:.3f}")
    print(f"Recall: {rec:.3f}")
    print(f"F1: {f1:.3f}")

    out_dir.mkdir(parents=True, exist_ok=True)
    ConfusionMatrixDisplay.from_predictions(y_test, preds)
    plt.tight_layout()
    fig_path = out_dir / "confusion_matrix.png"
    plt.tight_layout()
    plt.savefig(fig_path)
    plt.close()


def main() -> None:
    args = parse_args()
    data_path = Path(args.data)
    if not data_path.is_file():
        print(f"Dataset not found: {data_path}", file=sys.stderr)
        sys.exit(1)

    df = load_dataset(data_path)
    X, y = split_xy(df)
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, stratify=y, random_state=42
    )
    pipe = build_pipeline(X_train)
    pipe.fit(X_train, y_train)
    evaluate(pipe, X_test, y_test, Path(args.out))


if __name__ == "__main__":
    main()
