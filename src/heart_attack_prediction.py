import argparse
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

def parse_args() -> argparse.Namespace:
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(
        description="Heart Attack Risk Prediction via logistic regression"
    )
    parser.add_argument("--data", required=True, help="Path to dataset CSV")
    parser.add_argument("--out", required=True, help="Directory to store outputs")
    return parser.parse_args()


def load_data(path: str) -> pd.DataFrame:
    """Load dataset from CSV."""
    return pd.read_csv(path)


def preprocess(df: pd.DataFrame):
    """Split data and prepare features."""
    y = df["target"]
    X = pd.get_dummies(df.drop(columns=["target"]))
    return train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)


def train_model(X_train, y_train) -> LogisticRegression:
    """Train logistic regression model."""
    clf = LogisticRegression(max_iter=100)
    clf.fit(X_train, y_train)
    return clf


def evaluate_and_plot(model, X_test, y_test, out_dir: Path) -> None:
    """Evaluate model, print metrics and save confusion matrix."""
    y_pred = model.predict(X_test)
    acc = accuracy_score(y_test, y_pred)
    prec = precision_score(y_test, y_pred, zero_division=0)
    rec = recall_score(y_test, y_pred, zero_division=0)
    f1 = f1_score(y_test, y_pred, zero_division=0)
    print(f"Accuracy: {acc:.3f}")
    print(f"Precision: {prec:.3f}")
    print(f"Recall: {rec:.3f}")
    print(f"F1: {f1:.3f}")

    out_dir.mkdir(parents=True, exist_ok=True)
    ConfusionMatrixDisplay.from_predictions(y_test, y_pred)
    plt.tight_layout()
    fig_path = out_dir / "confusion_matrix.png"
    plt.savefig(fig_path)
    plt.close()


def main() -> None:
    args = parse_args()

    df = load_data(args.data)
    X_train, X_test, y_train, y_test = preprocess(df)
    model = train_model(X_train, y_train)
    evaluate_and_plot(model, X_test, y_test, Path(args.out))

    data_path = Path(args.data)
    if not data_path.is_file():
        print(f"Dataset not found: {data_path}", file=sys.stderr)
        sys.exit(1)

    print(f"Placeholder - dataset: {data_path}, output directory: {args.out}")

if __name__ == "__main__":
    main()
