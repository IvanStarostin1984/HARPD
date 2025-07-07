import subprocess

from pathlib import Path

import pandas as pd


def test_pipeline(tmp_path: Path) -> None:
    data = pd.DataFrame(
        {
            "age": [63, 37, 41, 56, 57, 60],
            "sex": [1, 1, 0, 1, 0, 1],
            "cp": [3, 2, 1, 0, 0, 1],
            "trtbps": [145, 130, 130, 120, 120, 140],
            "chol": [233, 250, 204, 236, 354, 293],
            "output": [1, 1, 0, 1, 0, 0],
        }
    )
    csv_path = tmp_path / "data.csv"
    data.to_csv(csv_path, index=False)
    out_dir = tmp_path / "out"
    result = subprocess.run(
        [
            "python",
            "src/heart_attack_prediction.py",
            "--data",
            str(csv_path),
            "--out",
            str(out_dir),
        ],
        capture_output=True,
        text=True,
        check=True,
    )
    assert (out_dir / "confusion_matrix.png").exists()
    for metric in ["Accuracy", "Precision", "Recall", "F1"]:
        assert metric in result.stdout

import sys
from pathlib import Path

test_data = Path("tests/data/small_dataset.csv")


def test_main_runs_and_creates_confusion_matrix(tmp_path):
    out_dir = tmp_path / "outputs"
    cmd = [
        sys.executable,
        "src/heart_attack_prediction.py",
        "--data",
        str(test_data),
        "--out",
        str(out_dir),
    ]
    result = subprocess.run(cmd, capture_output=True, text=True, check=True)
    output = result.stdout
    assert "Accuracy:" in output
    assert "Precision:" in output
    assert "Recall:" in output
    assert "F1:" in output
    assert (out_dir / "confusion_matrix.png").exists()

