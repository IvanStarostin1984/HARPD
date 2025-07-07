"""Run a logistic regression pipeline on the heart attack dataset."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

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
from sklearn.preprocessing import StandardScaler


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Heart Attack Risk Prediction")
    parser.add_argument("--data", required=True, help="Path to dataset CSV")
    parser.add_argument("--out", required=True, help="Directory to store outputs")
    return parser.parse_args()


def load_data(path: Path) -> pd.DataFrame:
    return pd.read_csv(path)


def prepare_data(df: pd.DataFrame):
    X = df.drop(columns=df.columns[-1])
    y = df[df.columns[-1]]
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    return train_test_split(X_scaled, y, test_size=0.2, random_state=42, stratify=y)


def train_model(X_train, y_train) -> LogisticRegression:
    model = LogisticRegression(max_iter=1000, solver="liblinear")
    model.fit(X_train, y_train)
    return model


def evaluate(model: LogisticRegression, X_test, y_test, out_dir: Path) -> None:
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

    df = load_data(data_path)
    X_train, X_test, y_train, y_test = prepare_data(df)
    model = train_model(X_train, y_train)
    evaluate(model, X_test, y_test, Path(args.out))


if __name__ == "__main__":  # pragma: no cover - entry point
    main()
