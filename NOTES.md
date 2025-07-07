* 2025-07-07: Created `data/` and `outputs/` with `.gitkeep` files and updated
  `README.md` to note the dataset must be added manually and provide a one-line
  quick start command.

- 2025-07-07: Updated AGENTS.md shell block to mention that 
`.codex/setup.sh` installs packages from `requirements.txt` and created this script.

- 2025-07-07: Added .codex/setup.sh and requirements.txt to install pandas,
 scikit-learn, and matplotlib. Reason: create base environment 
 as described in TODO setup stage.

* 2025-07-07: added skeleton src/heart_attack_prediction.py 
parsing --data and --out and printing placeholder. 
Reason: initial CLI entry point per TODO.
* 2025-07-07: Renamed docs/original_assignment to docs/original_assignment.md and updated AGENTS references.

* 2025-07-07: Cleaned TODO.md by removing stray lines and updated status to reflect existing CLI skeleton. Next step is implementing logistic regression pipeline.

* 2025-07-08: Implemented preprocessing, train-test split with stratification,
  logistic regression model, metrics output, confusion matrix saving and tests.
  Reason: finish core pipeline per TODO and ensure quality with pytest.
* 2025-07-07: Implemented logistic regression pipeline and added tests with synthetic dataset to verify metrics and confusion matrix output.
* 2025-07-07: heart_attack_prediction.py exits with an error when the dataset file is missing. Updated README and AGENTS accordingly.
