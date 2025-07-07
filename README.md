# HARPD
ML logistic regression on Heart Attack Risk Prediction Dataset

The dataset file `data/heart_attack_prediction_dataset.csv` must be supplied
manually.
If the file is missing, running the pipeline exits with a clear error message.

## Quick start

```bash
bash .codex/setup.sh && \
python src/heart_attack_prediction.py --data data/heart_attack_prediction_dataset.csv --out outputs/
```
