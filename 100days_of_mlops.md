## MIssion Critical Task
### Task 1
```__Objectives__:
Setting up a virutal enviroment is one of the first step in building a machine learning learning project.

The xFusionCorp Industries data science team needs a standardised Python environment for their new ML project. Set up a virtual environment with the required ML libraries on the controlplane host.

- Create a Python virtual environment named ml-env under /root/code/ using python3 -m venv.

- Activate the environment and install the following packages: numpy, pandas, scikit-learn, and matplotlib.

- Generate a requirements.txt file using pip freeze and save it at /root/code/requirements.txt.
```

### Solution
```
- virtual enviroment creation
python3 -m venv ml-env

- activate the virtual environment
source ml-env/bin/activate

- installing dependencies
pip install numpy scikit-learn matplotlib pandas
pip freeze > requirements.txt
```


### Task 2
```
Fixing the correct configuration for the jupyterlab configuration settings

Jupyter configuration file for the xFusionCorp Industries data science team

--- xFusionCorp team overrides (review before starting the server) ---
c.ServerApp.token = ''
c.ServerApp.password = ''
c.ServerApp.disable_check_xsrf = True
c.ServerApp.notebook_dir = '/root/notebooks/'
c.ServerApp.port = 8888
c.ServerApp.ip = '0.0.0.0'
```


### Task 3
``` Fixing the libraries in requirements.in for uv package manager
and compiling it to requirements/txt using this command

-libraries in the requirements.in
scikit-learn
mlflow
pandas
numpy
```
```
uv pip compile requirements.in -o requirements.txt
```

#### Task 4
The xFusionCorp Industries ML team enforces code quality with ruff and black on every pull request. The project at /root/code/fraud-detection/ currently fails both tools. Make it pass them.


The project at /root/code/fraud-detection/ contains a pyproject.toml and sample sources under src/.

The corrected project must meet the following requirements:

ruff and black are both configured with a line length of 120.
ruff lint rule selection includes E, F, W, and I, and is declared under [tool.ruff.lint] – The schema required by ruff 0.1 and later.
Running ruff check src/ from the project directory exits with status 0.
Running black --check src/ from the project directory exits with status 0.
Review the existing configuration and source files, and correct everything that prevents the two commands above from exiting cleanly.

ruff, black, and mypy are already installed.

#### Solution
- remove the unused import : import os
- modify the pyproject.toml file : set length for both black and ruff to 120, in the select add w and i to the errors
- final pyproject.toml should look like this-
```
    [project]
name = "fraud-detection"
version = "0.1.0"

[tool.ruff]
line-length = 120

[tool.ruff.lint]
select = ["E", "F", "W", "I"]

[tool.black]
line-length = 120
```

### Task 6
The xFusionCorp Industries deployment team needs the fraud-detection model code packaged as an installable Python distribution. A draft pyproject.toml exists at /root/code/fraud-detection/, but it does not build a wheel that meets the team's standard. Correct the file and produce a compliant package.


The project at /root/code/fraud-detection/ already contains the source code under src/fraud_detection/. The Python files are complete—you do not need to modify any of them.

The corrected pyproject.toml must satisfy every one of the following:

it declares a [build-system] section with requires = ["setuptools>=61.0", "wheel"] and build-backend = "setuptools.build_meta";
name is fraud_detection (the distribution name must match the module path under src/);
version is 0.1.0;
requires-python is >=3.10;
dependencies is ["scikit-learn", "pandas", "numpy"].
Review the existing pyproject.toml and correct everything that does not match the requirements above.

Build the package from the project directory:

   cd /root/code/fraud-detection
   python3 -m build

The build must produce a wheel named fraud_detection-0.1.0-*.whl under dist/.
The build package is already installed. Use python3 rather than python.

### Solution
- write this in the pyproject.toml file
```
[build-system]
requires = ["setuptools>=61.0", "wheel"]
build-backend = "setuptools.build_meta"

[project]
name = "fraud_detection"
version = "0.1.0"
description = "Fraud detection model for xFusionCorp Industries"
requires-python = ">=3.10"
dependencies = ["scikit-learn", "pandas", "numpy"]

[tool.setuptools.packages.find]
where = ["src"]
```

### Task 7
The xFusionCorp Industries ML team enforces code quality on every commit via pre-commit. A draft .pre-commit-config.yaml exists in the git repository at /root/code/fraud-detection/, but it does not match the team's standard and pre-commit run --all-files fails against it. Correct the configuration.


A git repository already exists at /root/code/fraud-detection/ with .pre-commit-config.yaml and process.py already tracked. pre-commit is installed system-wide.

The corrected configuration must declare the following five hooks so that pre-commit run --all-files executes every one of them:

trailing-whitespace, end-of-file-fixer, and check-yaml – All three sourced from the pre-commit/pre-commit-hooks repository, pinned to a current release;
ruff – Sourced from the astral-sh/ruff-pre-commit repository, pinned to a current release;
black – Sourced from the psf/black-pre-commit-mirror repository, pinned to a current release.
Every repository entry in the configuration must include a rev: field.

Review the existing .pre-commit-config.yaml and correct everything that prevents the hooks above from running.

Once the configuration is correct, register the hooks with git and run them against the tracked files:

   pre-commit install
   pre-commit run --all-files

Tip: pre-commit autoupdate queries each referenced repository and rewrites the rev: pins to the latest released tag. This is the standard way to discover current versions without looking them up by hand.

### Solution
```
repos:
  - repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v6.0.0
    hooks:
      - id: trailing-whitespace
      - id: end-of-file-fixer
      - id: check-yaml

  - repo: https://github.com/astral-sh/ruff-pre-commit
    rev: v0.15.15
    hooks:
      - id: ruff

  - repo: https://github.com/psf/black-pre-commit-mirror
    rev: 26.5.1
    hooks:
      - id: black
```
- use:
- ```
  pre-commit autoupddate
  ```
  To queries each referenced and pins to the latest released tag

### Task 8
- The xFusionCorp Industries ML platform team maintains a Cookiecutter template that new ML projects are generated from.
- A draft template exists at /root/code/mlops-template/, but it does not render. Correct the template and use it to generate a project.

- A Cookiecutter template exists at /root/code/mlops-template/. cookiecutter is installed system-wide.
- The corrected template must satisfy every one of the following:
- The cookiecutter.json declares four variables:
- project_name (default my-ml-project)
- author (default xFusionCorp)
- python_version (default 3.11)
- ml_framework with the choices sklearn, pytorch, and tensorflow
- The generated requirements.txt logic:
- Contains scikit-learn when ml_framework is sklearn
- Contains torch when ml_framework is pytorch
- Contains tensorflow when ml_framework is tensorflow
- The generated README.md content:
- Must reference both the project_name and the author from cookiecutter variables.
- The template directory structure {{cookiecutter.project_name}}/ must contain:
- Files: README.md and requirements.txt
- Directories: data/, models/, src/, and tests/
- Review the existing template in the VS Code explorer and correct everything that prevents it from rendering.
- Once the template renders, generate a project at /root/code/churn-model/:
  ```
   cookiecutter /root/code/mlops-template/ -o /root/code/ --no-input project_name=churn-model ml_framework=sklearn
  ```
The generated project must contain a requirements.txt listing scikit-learn and a README.md that mentions xFusionCorp.
```
This is the what is in the requirement.txt

{% if cookiecutter.ml_framework = 'sklearn' %}
scikit-learn
{% elif cookiecutter.ml_framework = 'pytorch' %}
torch
{% elif cookiecutter.ml_framework = 'tensorflow' %}
tensorflow
{% if cookiecutter.ml_framework = 'sklearn' %}
scikit-learn
{% elif cookiecutter.ml_framework = 'pytorch' %}
torch
{% elif cookiecutter.ml_framework = 'tensorflow' %}
tensorflow
```
### Solution
```
The two bugs summarised
FileBugFixrequirements.txt= instead of == in Jinja2 conditionsChange all = to ==requirements.txtNo closing {% endif %}Add {% endif %} at the end
```

### Task 10
- The xFusionCorp Industries ML team is adopting DVC so that datasets and model files are versioned separately from code.
- Initialise DVC inside the existing Git repository at /root/code/fraud-detection/ and record the initialisation in Git.

- A Git repository already exists at /root/code/fraud-detection/ with an initial commit.

- Initialise DVC inside that repository so that the standard .dvc/ control directory and .dvcignore file are created alongside the existing Git working tree.

- Stage every file that DVC produces during initialisation, and record them in a new Git commit with the message Initialize DVC.

- Once initialisation is complete, the DVC extension will detect the new .dvc/ directory and surface the DVC TRACKED section in the EXPLORER panel together with - a DVC indicator in the bottom status bar.

### Solution
```
- change into the project folder and initialize dvc
dvc init

- stage the files created from dvc init using git
git add .

- commit the changes
git commit -m "initialize DVC"
```

### Task 11
- A teammate has added the transactions dataset to the xFusionCorp Industries fraud-detection repository, but it was committed directly to Git instead of being tracked with DVC. Bring the repository in line with the team standard—every dataset under data/ must be tracked by DVC, not by Git.


- A project exists at /root/code/fraud-detection/ with DVC already initialised. The dataset data/raw/transactions.csv is currently tracked by Git, and the team standard requires DVC to own it instead.

- Stop Git from tracking the dataset without deleting it from disk.

- Track the same dataset with DVC so a .dvc pointer file is produced and data/raw/.gitignore excludes the dataset itself.

- Stage the new .dvc pointer and the new .gitignore, then record a Git commit with the message Track transactions dataset with DVC.

- Once tracking is moved to DVC, the DVC TRACKED section in the EXPLORER panel will list the dataset, confirming the extension recognises it as a DVC-managed file.

### Solution
```
# remove the file from git tracking but not from the disk
git rm --cached data/raw/transactions.csv

# add the file to dvc for dvc to track
dvc add data/raw/transactions.csv

# Stage the file created from dvc add about using git add
git add data/raw/transaction.csv.dvc data/raw/.gitignore

# commit the stage changes from git
git commit -m "Transactions dataset track with DVC"

# check the dvc folder to see it has been trakc
```
### Task 12
```
- The xFusionCorp Industries ML team uses SeaweedFS as the shared S3-compatible object store for DVC-tracked data.
- A .dvc/config already declares a remote called s3 for the fraud-detection project, but dvc push currently fails. Correct the configuration and push the tracked data into the SeaweedFS bucket.

- A project exists at /root/code/fraud-detection/ with DVC initialised and data/raw/transactions.csv already tracked.
- SeaweedFS is already running on the controlplane:
- S3 endpoint: http://localhost:8333
- Filer UI: open the SeaweedFS Filer button at the top of the lab (forwarded port 8888) – buckets are visible under /buckets/.
- Credentials: weedadmin / weedadmin123 (already set in .dvc/config)
- Bucket name: dvc-storage (already created and visible in the Filer UI under /buckets/dvc-storage)
- Review the existing .dvc/config and correct everything that prevents dvc push from succeeding. The remote called s3 must:
- point at the dvc-storage bucket using s3://;
- use the correct SeaweedFS S3 endpoint URL;
- be marked as the default remote.
- Push the tracked data. After the push, the dvc-storage bucket in the SeaweedFS Filer UI must contain at least one object under the files/md5/... prefix.

```


### Solution
- update the .dvc.config file
```
[core]
    remote = s3
['remote "s3"']
    url = s3://dvc-storage
    endpointurl = http://localhost:8333
    access_key_id = weedadmin
    secret_access_key = weedadmin123
```
### Task 13
```
- A new xFusionCorp Industries team member has cloned the fraud-detection repository onto a fresh machine.
- The DVC remote is already configured to point at the team's SeaweedFS bucket, but dvc pull is failing. Diagnose the cause, correct the configuration, and pull the dataset.


- A cloned project exists at /root/code/fraud-detection/ with DVC initialised, the data/raw/transactions.csv.dvc pointer file present, but the dataset itself missing from disk and from the local DVC cache.

- SeaweedFS is already running on the controlplane and the dataset has already been pushed to the dvc-storage bucket—open the SeaweedFS Filer button at the top of the lab and navigate to /buckets/dvc-storage/ to confirm that the object is there.

- S3 endpoint: http://localhost:8333
- Credentials: weedadmin / weedadmin123
- Review .dvc/config and correct everything that prevents dvc pull from authenticating against SeaweedFS.

- After the fix, the s3 remote must use:
- The access key (access_key_id) weedadmin
- The secret key (secret_access_key) weedadmin123.
- Pull the dataset. After the pull, data/raw/transactions.csv must be present on disk and its content must match the hash recorded in the .dvc pointer.
```

### Solution
```
- enter this in the .dvc.config file
[core]
    remote = s3

['remote "s3"']
    url = s3://dvc-storage
    endpointurl = http://localhost:8333
    access_key_id = weedadmin
    secret_access_key = weedadmin123

- then do dvc pull
```
### Task 14
```
- The xFusionCorp Industries ML team uses DVC pipelines to keep data processing reproducible.
- A draft dvc.yaml exists in the fraud-detection project, but dvc repro does not complete the full pipeline. Correct the pipeline definition so it runs cleanly end to end.


- A project exists at /root/code/fraud-detection/ with DVC initialised.
- Python scripts are at src/data/process_data.py and src/data/split_data.py; raw input is at data/raw/transactions.csv.
- Do not modify the Python files or the input data.

- The corrected pipeline must declare two stages with the following behaviour:

- process_data – Depends on data/raw/transactions.csv and src/data/process_data.py; produces data/processed/clean_transactions.csv.
- split_data – Depends on data/processed/clean_transactions.csv and src/data/split_data.py; produces data/processed/train.csv and data/processed/test.csv.
- Review the existing dvc.yaml and correct everything that prevents dvc repro from completing.

- After your changes, dvc repro must run end to end and dvc status must report no stale stages.

-Once the pipeline is valid, the DVC extension's PIPELINES section under the DVC view will list both stages and visualise the dependency graph between them.
```
### Solution
```
- update the content of the dvc.yaml with this
stages:
  process_data:
    cmd: python src/data/process_data.py
    deps:
      - data/raw/transactions.csv
      - src/data/process_data.py
    outs:
      - data/processed/clean_transactions.csv

  split_data:
    cmd: python src/data/split_data.py
    deps:
      - data/processed/clean_transactions.csv
      - src/data/split_data.py
    outs:
      - data/processed/train.csv
      - data/processed/test.csv

- on the terminal run - dvc repro
- dvc status
if the first command run without error you are good"
```
### Task 15
Day 15: Parameterize a DVC Pipeline

### Solution
```
- create the params.yml
add
n_estimators=200
```

### Task 16
```
    After training a model, the xFusionCorp Industries ML team requires DVC to surface model metrics through dvc metrics show. Although the fraud-detection pipeline successfully trains a model and generates a metrics.json file, DVC currently does not recognize this file as a metric. Ensure that the metrics.json file is properly configured to be recognized by DVC.


A project exists at /root/code/fraud-detection/ with a three-stage DVC pipeline (process_data, split_data, train). The train stage runs src/models/train.py, which writes the model to models/model.pkl and metrics to metrics.json. Do not modify the Python files.

Acceptance criteria:

The train stage in dvc.yaml declares metrics.json as a DVC metric output rather than a regular file output, with cache: false so the JSON lives in Git for diff history rather than in the DVC cache.
The pipeline has been reproduced so the metric registration takes effect, and dvc metrics show reports the accuracy and f1_score values from metrics.json.
Tip: once the metric is registered, dvc metrics diff compares its values across Git commits, which is useful when iterating on the model.
```
### Solution
```
Let me walk you through both the concept and the exact fix for this task.
The key concept
In DVC pipelines (dvc.yaml), each stage has outputs, and DVC treats them differently depending on how you declare them:
DeclarationPurposeWhere it livesouts:Regular output (data, models)DVC cache (.dvc/cache), tracked via .gitignoremetrics:Metric outputCan live in Git if cache: false, so you get diffable historyplots:Plot outputSimilar to metrics, for plot data
By default, anything under outs: — even a metrics.json — is just treated as a blob DVC caches. DVC has no idea it contains accuracy/f1_score fields you want to compare across commits. That's why dvc metrics show currently shows nothing: the file exists on disk, but DVC's pipeline graph doesn't know it's a metric.
Declaring it under metrics: with cache: false does two things:

Tells DVC "parse this as JSON and expose its keys via metrics show/diff."
Skips DVC caching it — instead it's just a normal file that Git tracks directly (since it's small, human-readable, and you want git diff-style history across commits, not binary cache storage).

Step-by-step fix
1. Look at the current dvc.yaml
bashcat /root/code/fraud-detection/dvc.yaml
You'll likely see the train stage looking something like:
yaml  train:
    cmd: python src/models/train.py
    deps:
      - src/models/train.py
      - data/processed/train.csv
    outs:
      - models/model.pkl
      - metrics.json
2. Edit the train stage — move metrics.json out of outs: and into a metrics: block with cache: false:
yaml  train:
    cmd: python src/models/train.py
    deps:
      - src/models/train.py
      - data/processed/train.csv
    outs:
      - models/model.pkl
    metrics:
      - metrics.json:
          cache: false
Notes:

models/model.pkl stays under outs: — it's a large binary artifact, belongs in DVC cache, not Git.
metrics.json moves to metrics: with cache: false — small JSON, belongs in Git, and DVC will parse it for metrics commands.

3. Reproduce the pipeline so DVC re-registers the stage outputs per the new config:
bashcd /root/code/fraud-detection
dvc repro
This reruns any stage whose deps/outs definition changed (here, just re-registers train since the DAG config changed — it may or may not literally re-execute train.py depending on whether DVC sees the cmd/deps as changed, but it will update dvc.lock to reflect metrics.json as a metric).
4. Verify it's recognized
bashdvc metrics show
Expected output showing something like:
Path            accuracy    f1_score
metrics.json    0.94        0.91
5. Commit the change (so it's real in Git, and so metrics.json's history is trackable going forward):
bashgit add dvc.yaml dvc.lock metrics.json
git commit -m "Register metrics.json as a DVC metric output"
Why this matters going forward (the tip in the task)
Once metrics.json is a proper metric:
bashdvc metrics diff HEAD~1
will show you exactly how accuracy/f1_score moved between commits — this is the core DVC workflow for tracking whether a model change improved or regressed performance, without needing a separate experiment tracker for simple cases.
If your metrics.json isn't showing up after dvc repro, double check:

Indentation in YAML (list item under metrics: needs the - metrics.json: then nested cache: false)
That dvc.lock actually got regenerated (cat dvc.lock and check the train stage's outs/metrics split)
Run dvc status to see if DVC thinks the pipeline is out of sync
```
### Task 17
```
The xFusionCorp Industries MLOps team needs every model training run to be reproducible, automatically tracked, and easy to compare so a chosen configuration can be promoted into version control. The fraud-detection pipeline is parameterized by max_depth, currently set shallow enough to underfit. Using DVC experiments, run three tracked experiments over different max_depth values, compare their recorded f1_score on the held-out test set, and promote the best-scoring run so its parameters, metrics, and model become the tracked workspace state.


A project exists at /root/code/fraud-detection/ with a parameterised DVC pipeline already in place. params.yaml declares n_estimators: 100 and max_depth: 4, and the baseline pipeline has been run once. src/models/train.py reads both parameters, trains the model, and evaluates it on the held-out test set, writing the real accuracy and f1_score to metrics.json. Do not modify the Python files.

Acceptance criteria:

Three DVC experiments have been run, each with a different value for max_depth across a reasonable range (for example 2, 6, and 12); each experiment retrains the model and produces a fresh metrics.json.
The experiment with the highest f1_score is applied to the workspace, so its max_depth, metrics.json, and models/model.pkl become the tracked state.
```
### Solution
```
Step 1: Confirm the baseline state
bash
cd /root/code/fraud-detection/
cat params.yaml
git status
You should see max_depth: 4, n_estimators: 100, and a clean-ish working tree (baseline pipeline already run/committed).
Step 2: Run three DVC experiments with different max_depth
DVC experiments let you override params on the fly without touching params.yaml or committing anything — each run is tracked in an internal experiments namespace.
bash
dvc exp run -S max_depth=2
dvc exp run -S max_depth=6
dvc exp run -S max_depth=12
Each of these will re-run the pipeline stages affected by max_depth (the training stage, and anything downstream like evaluation), producing a fresh metrics.json and models/model.pkl for that experiment — without disturbing your current workspace files until you decide to keep one.
Step 3: Compare the experiments
bash
dvc exp show --only-changed

This prints a table with columns for max_depth, n_estimators, accuracy, and f1_score for each experiment, so you can see at a glance which run scored highest on f1_score. (This is the same data the DVC extension's EXPERIMENTS view in the Activity Bar shows — worth opening if you're in VS Code, since it's easier to eyeball there.)
You're looking for the experiment name (something like exp-xxxxx) tied to whichever max_depth produced the best f1_score. Given underfitting at max_depth=4, it's likely — but not guaranteed — that a deeper tree (6 or 12) wins; don't assume, just read it off the table.
Step 4: Promote the winning experiment to the workspace
Once you've identified the best experiment name from dvc exp show:
bash
dvc exp apply <best-exp-name>
This overwrites your workspace with that experiment's params.yaml (max_depth), metrics.json, and models/model.pkl — exactly the tracked state the criteria ask for.
Step 5: Verify and persist
bash
cat params.yaml        # confirm max_depth matches the winning experiment
cat metrics.json        # confirm f1_score matches
git status               # see the modified files
git add params.yaml dvc.lock metrics.json models/model.pkl
git commit -m "Promote best max_depth from DVC experiments (highest f1_score)"
That last commit is what makes it "promoted into version control" — dvc exp apply only changes the workspace; committing locks it in as the new tracked baseline.

A couple of notes:

If dvc exp show output is hard to read in the terminal, dvc exp show --csv > experiments.csv and opening that is often easier for comparison.
If two experiments tie or are very close on f1_score, you may want to also glance at accuracy as a tiebreaker, but the task's stated criterion is strictly the highest f1_score.
```
### Task 18
The xFusionCorp Industries MLOps team versions datasets and models on separate Git branches so it can reproduce and roll between versions cleanly. Tag the current state as v1.0, create a v2-improved branch built on a newer dataset (which retrains the model), and confirm that switching back restores the original data and model.
A project exists at /root/code/fraud-detection/ with a working DVC pipeline (it processes the data and trains a model) and the baseline data/raw/transactions.csv already tracked.
An improved dataset has been pre-staged at /root/code/fraud-detection/data/raw/transactions_v2.csv and is visible in the file explorer. Do not delete this file.
Acceptance criteria:
On the main branch, the current state is tagged v1.0.
A branch named v2-improved holds the v2 state: the tracked dataset carries the contents of the v2 file (re-tracked with DVC), the pipeline has been re-run so models/model.pkl is retrained and versioned alongside the dataset, and the changes are committed.
Back on the main branch, the v1 dataset and model are restored on disk, matching the hashes recorded by the v1.0 tag. The DVC extension's DVC TRACKED section in the EXPLORER panel reflects the tracked dataset and model for the branch you currently have checked out. To compare the exact hashes recorded on each branch, use git show <ref>:dvc.lock or dvc status.

### Solution
So the "reproducibility" trick is:

Git commit/tag = a specific set of hashes → DVC checkout = materializes the actual files matching those hashes.

This is exactly why switching branches and running dvc checkout "restores" your old dataset and model — nothing is being copied back and forth manually, DVC is just re-linking the workspace to the cached blobs that match the hashes recorded in that branch's commit.
```
# Tag the current version
git tag v1.0
# create a new branch and checkout
git checkout -b v2-improved
# copy the new data on the old one
cp data/raw/transaction_v2.csv data/raw/transaction.csv
# retrack with dvc 
dvc add data/raw/transactions.csv
# run dvc repro
# commit the changes
git add data/raw/transactions.csv.dvc dvc.lock
git commit -m "Update to v2 dataset and retrain model"
# switch back to the main and restore back to v1
git checkout main
dvc checkout

```
### Task 19
Complete the xFusionCorp Industries fraud-detection production DVC pipeline. Three stages are already wired in `dvc.yaml`, two remain, and the pipeline must finish as a reproducible, SeaweedFS-backed, v1.0-tagged release.

A project exists at `/root/code/ml-pipeline/` with Git and DVC initialised. The `params.yaml` is in place and the `.dvc/config` is pre-configured to push to the SeaweedFS bucket `dvc-storage` at `http://localhost:8333`.
The `ingest`, `validate`, and `preprocess` stages are already declared in `dvc.yaml`, but one of them is misconfigured and prevents `dvc repro` from completing — run `dvc repro` to see it fail. The two scripts for the remaining stages are pre-staged at `/root/code/ml-pipeline/scripts-staging/train.py` and `scripts-staging/evaluate.py`, and belong in `scripts/`.
Acceptance criteria:

* The misconfigured existing stage is corrected so `dvc repro` can complete.
* Two further stages are declared in `dvc.yaml`:
   * `train` – Depends on the preprocessed dataset and `scripts/train.py`; reads `n_estimators`, `max_depth`, `test_size`, and `random_seed` from `params.yaml`; outputs `models/model.pkl` and `data/processed/test_split.csv`; declares `metrics.json` as a DVC metric with `cache: false`.
   * `evaluate` – Depends on `models/model.pkl`, `data/processed/test_split.csv`, and `scripts/evaluate.py`; outputs `reports/evaluation.json` declared with `cache: false`.
* The full pipeline has been reproduced, the cache pushed to the SeaweedFS remote, and the current state tagged `v1.0`.
* Every change is committed to Git so the release is fully captured.

Open the SeaweedFS Filer button at the top of the lab and navigate to `/buckets/dvc-storage/` to confirm that the bucket holds the pushed artefacts under the `files/md5/...` layout.


### Solution
- copy the train.py, evaluate.py from scripts-staging into script folder
- add train and evaluate stages to the dvc.yaml
- correct the output of the preprocess to data/preprocessed/clean.csv and not cleaned.csv
define this inside dvc.yaml
```
stages:
  ingest:
    cmd: python3 scripts/ingest.py
    deps:
      - scripts/ingest.py
      - data/raw/data.csv

  validate:
    cmd: python3 scripts/validate.py
    deps:
      - data/raw/data.csv
      - scripts/validate.py
    outs:
      - reports/validation.json:
          cache: false

  preprocess:
    cmd: python3 scripts/preprocess.py
    deps:
      - data/raw/data.csv
      - scripts/preprocess.py
    outs:
      - data/processed/clean.csv
  train:
    cmd: python3 scripts/train.py
    deps:
      - data/processed/clean.csv
      - scripts/train.py
    outs:
      - models/model.pkl
      - data/processed/test_split.csv
    params:
      - n_estimators
      - max_depth
      - test_size
      - random_seed
    metrics:
      - metrics.json:
          cache: false
  evaluate:
    cmd: python3 scripts/evaluate.py
    deps:
    - models/model.pkl
    - data/processed/test_split.csv
    - scripts/evaluate.py
    outs:
      - reports/evaluation.json:
          cache: false

```
- run the pipeline stages using the command below
```
dvc repro
```
- push it to the remote storage ( ensure you have configure this in the dvc.config)
```
dvc push
```

- stage and commit the changes
- tag the v1.0 -
```
git tag -a v1.0 -m "Fraud detection pipeline v1.0 release"
or
git tag v1.0
```


