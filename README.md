# 100days_kodekkloud_engineer
100 days of kode cloud engineering Challenge

### dvc commands

- dvc exp run -S max_depth=2 Runs the pipeline with max_depth overridden to 2, without editing params.yaml. Trains the model, evaluates it, and saves the result as a tracked "experiment" (not yet in your workspace or git history).
- dvc exp run -S max_depth=6	Same as above, but with max_depth=6. This is your second tracked experiment.
- dvc exp run -S max_depth=12	Same again, with max_depth=12. Your third tracked experiment.
- dvc exp show --only-changed	Prints a comparison table of all experiments — showing the params that changed (max_depth) alongside the metrics (accuracy, f1_score) for each run, so you can see which one performed best.
- dvc exp apply <best-exp-name>	Takes the experiment you pick (the one with the highest f1_score) and overwrites your actual workspace files — params.yaml, metrics.json, models/model.pkl — with that experiment's versions. This is the "promotion" step.
- git add params.yaml dvc.lock metrics.json 
