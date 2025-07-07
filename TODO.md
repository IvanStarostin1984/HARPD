# TODO — Heart‑Attack Prediction (Logistic Regression)

Minimal guidance for the **OpenAI Codex 2025** agent.  
We must produce a runnable logistic‑regression solution that meets every requirement in the lecturer’s assignment (see `docs/original_assignment.md`) **within one day**.  
Where the assignment is silent, Codex may choose any reasonable implementation path (the simpler/cleaner – the better).

---

## 0  Setup (stage 1 of the run)
Codex should create this lightweight scaffold **before** writing any business logic:

.
├── data/ # keep raw data here (.csv if to be supplied manually after setup stage)
│ └── heart_attack_prediction_dataset.csv
├── outputs/ # evaluation artefacts (figures, reports, etc.)
├── src/ or notebooks/ # agent chooses
├── .codex/
│ └── setup.sh # installs extra deps if requirements.txt exists
├── AGENTS.md # soft prompt for tests / commands (optional stub)
├── TODO.md # this file – implementation guide
├── NOTES.md # running log of design decisions (auto‑append OK)
├── docs/
│ └── original_assignment.md # read‑only source of truth
└── README.md # quick‑start instructions

*Data and outputs directories have been created with `.gitkeep`. The dataset
file must be supplied manually as `data/heart_attack_prediction_dataset.csv`.*

yaml
Copy

*Feel free to adjust directory names if a clearer structure emerges, but keep the dataset path accurate (`data/…csv`).*

---

## 1  Environment
* Use **Python** (already on Codex base image).
* If additional packages are required, let Codex generate a `requirements.txt` and ensure `.codex/setup.sh` installs them (`pip install -r requirements.txt`).

---

## 2  Data
* CSV path (relative): **`data/heart_attack_prediction_dataset.csv`**  
  – supplied manually; **do not attempt to download**.

---

## 3  Pipeline (sequential tasks)

1. **Load & inspect** – echo shape, dtypes, basic summary.  
2. **Data quality check** – flag missing values / anomalies.  
3. **Pre‑process**  
   * Handle missing data (simple strategy is fine).  
   * Encode categoricals (one‑hot or ordinal).  
   * Scale / normalise numerics if solver benefits.  
4. **Partition** – train/test split **with stratification** and fixed seed.  
5. **Train** – fit a logistic‑regression classifier (solver & regularisation at agent’s discretion).  
6. **Evaluate** – output **accuracy, precision, recall, F1** and plot a confusion matrix.  
7. **Explainability** – print model coefficients *or* another quick feature‑importance view.  
8. **Persist outputs** – write metrics to console and save any plots / artefacts under `outputs/`.

---

## 4  Repo housekeeping (minimal)
* Main code may live in a single script (`src/heart_attack_prediction.py`) **or** divided into files – agent’s call.  
* Keep file count low; add only what’s necessary.  
* Update `README.md` with one‑command setup/run instructions.  
* Log key design choices in `NOTES.md` so the team can reuse them in the report.

---

## 5  File alignment policy
* `docs/original_assignment.md` → **single source of truth**. Do **not** edit this file.  
* `TODO.md` (this file) → implementation guide for Codex.  
* `AGENTS.md` → (optional) shell test blocks or lint rules; keep brief.  
* `NOTES.md` → ongoing notes; safe for Codex to append to.

---

## 6  Out‑of‑scope for this Codex run
Slides and the written report will be produced manually by the Presentation and Documentation roles.
