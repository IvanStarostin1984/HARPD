# HARPD
ML logistic regression on Heart Attack Risk Prediction Dataset

This repo includes a tiny sample CSV under `tests/data/` used for automated
tests. To run the full pipeline on the real data you must supply
`data/heart_attack_prediction_dataset.csv` manually.

## Quick start

```bash
bash .codex/setup.sh && \
python src/heart_attack_prediction.py --data data/heart_attack_prediction_dataset.csv --out outputs/
```
