import subprocess
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
