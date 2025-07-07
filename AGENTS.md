# Agent Guidelines – Heart‑Attack Prediction (Logistic Regression)
# This is preliminary version to be analysed and modified if necessary.
This file tells **OpenAI Codex 2025** what to do every time it starts an
iteration inside this repository. Keep it short; add only statements
that actively steer the agent.

---

## 1  Quick health‑check (runs each iteration)

shell: |
  # 1. Set up Python environment (installs `requirements.txt` if present).
  bash .codex/setup.sh

  # 2. Execute the end‑to‑end pipeline if the dataset is present.
  if [ -f data/heart_attack_prediction_dataset.csv ]; then
    python src/heart_attack_prediction.py \
           --data data/heart_attack_prediction_dataset.csv \
           --out  outputs/
  else
    echo "Dataset missing: place data/heart_attack_prediction_dataset.csv" >&2
  fi

  # 3. (Optional, fast) style gates – skip gracefully if tools absent.
  if command -v ruff >/dev/null 2>&1;  then ruff check src tests;  fi
  if command -v black >/dev/null 2>&1; then black --check src tests; fi

**Pass criteria**

* Script exits **0**.
* Stdout contains the four core metrics  
  *(accuracy, precision, recall, F1)*.
* Confusion‑matrix PNG (or SVG) is written to `outputs/`.

---

## 2  Coding rules (condensed)

1. **PEP 8**   +  **Black** (line length = 88) + 4‑space indent.  
2. ≤ 20 logical lines per function; minimise nesting.  
3. Never hard‑code absolute paths – always reference `data/` and `outputs/`.  
4. Log every design choice in **NOTES.md** (date‑stamped bullet).  
5. Touch only the files you need; avoid repo churn.
6. When creating tasks for each task choose separate set of files to work on in parallel to avoid conflicts. The only files that allow parallel work on are TODO.md and NOTES.md in case of adding information only.
---

## 3  File roles

| Path                                        | Purpose                                 |
|---------------------------------------------|-----------------------------------------|
| `src/heart_attack_prediction.py`            | End‑to‑end ML pipeline *you may decide to break it into several files)                  |
| `data/heart_attack_prediction_dataset.csv`  | Raw dataset (read‑only)                 |
| `outputs/`                                  | Metrics, plots, confusion matrix        |
| `.codex/setup.sh`                           | Install packages from `requirements.txt` |
| `README.md`                                 | Quick‑start instructions                |
| `TODO.md` / `NOTES.md`                      | Work plan / engineering log (append‑only)|
Original_assignment.md and .csv dataset are single sources of truth and are not to be changed.
Original assignment is to be implemented in simplest way fully aligned with original assignment.
You may create additional folders/files in repo if necessary.
You may change AGENTS.md/TODO.md/NOTES.md contents if necessary.
---

## 4  Clean exit checklist

The agent may mark a task **done** when:

* `python src/heart_attack_prediction.py` finishes without error,
  writes metrics & the confusion‑matrix figure to `outputs/`,
  and prints the metric values to stdout.
* `README.md` includes a one‑command quick‑start
  (clone → setup → run).
* `requirements.txt` lists every import that is **not** in the
  Python standard library.

*End of file*
