# Train Script
"""Train stage for the DVC experiments lab.

Trains a RandomForest fraud classifier using the hyperparameters declared
in params.yaml, then evaluates it on the held-out test split and writes
the real accuracy and f1_score to metrics.json. Because the metrics come
from a genuine evaluation, varying max_depth produces meaningfully
different scores, which is what makes comparing experiments worthwhile.
"""

import json
import os

import joblib
import pandas as pd
import yaml
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, f1_score

os.makedirs("models", exist_ok=True)

with open("params.yaml") as f:
    params = yaml.safe_load(f)

n_estimators = params["n_estimators"]
max_depth = params["max_depth"]

train = pd.read_csv("data/processed/train.csv")
test = pd.read_csv("data/processed/test.csv")


def features(df):
    X = df.drop(columns=["is_fraud", "transaction_id", "merchant"])
    return pd.get_dummies(X, columns=["category"])


X_train = features(train)
y_train = train["is_fraud"]

# Align the test columns to the training columns so one-hot categories
# that appear in only one split do not change the feature matrix shape.
X_test = features(test).reindex(columns=X_train.columns, fill_value=0)
y_test = test["is_fraud"]

model = RandomForestClassifier(
    n_estimators=n_estimators, max_depth=max_depth, random_state=42
)
model.fit(X_train, y_train)
joblib.dump(model, "models/model.pkl")

# Evaluate on the held-out test set so the metrics reflect real
# generalisation performance, not memorised training data.
preds = model.predict(X_test)
metrics = {
    "accuracy": round(accuracy_score(y_test, preds), 4),
    "f1_score": round(f1_score(y_test, preds, zero_division=0), 4),
}

with open("metrics.json", "w") as f:
    json.dump(metrics, f, indent=2)

print(f"max_depth={max_depth}, n_estimators={n_estimators}, metrics={metrics}")
# end

# Production Grade Data ingestion scirpt
import os
import pandas as pd

EXPECTED_COLUMNS = [
    "customer_id",
    "amount",
    "merchant",
    "is_fraud"
]

def load_and_validate_csv(file_path):
    # 1. File exists
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"{file_path} not found.")

    # 2. File not empty
    if os.path.getsize(file_path) == 0:
        raise ValueError("CSV file is empty.")

    # 3. Read file
    try:
        df = pd.read_csv(file_path)
    except Exception as e:
        raise ValueError(f"Unable to read CSV: {e}")

    # 4. DataFrame not empty
    if df.empty:
        raise ValueError("Dataset contains no rows.")

    # 5. Required columns
    missing = set(EXPECTED_COLUMNS) - set(df.columns)
    if missing:
        raise ValueError(f"Missing columns: {missing}")

    # 6. Duplicate rows
    if df.duplicated().any():
        print("Warning: Duplicate rows detected.")

    # 7. Missing values
    if df[EXPECTED_COLUMNS].isnull().any().any():
        raise ValueError("Required columns contain missing values.")

    return df


df = load_and_validate_csv("data/raw/data.csv")

print(
    f"Loaded {len(df)} rows and {len(df.columns)} columns successfully."
)
# End
### Evaluate script
import pandas as pd
import json
import joblib
import os
from sklearn.metrics import accuracy_score, f1_score, precision_score, recall_score

os.makedirs("reports", exist_ok=True)

model = joblib.load("models/model.pkl")
test = pd.read_csv("data/processed/test_split.csv")
y_test = test["is_fraud"]
X_test = test.drop(columns=["is_fraud"])

preds = model.predict(X_test)

report = {
    "accuracy": round(accuracy_score(y_test, preds), 4),
    "f1_score": round(f1_score(y_test, preds, zero_division=0), 4),
    "precision": round(precision_score(y_test, preds, zero_division=0), 4),
    "recall": round(recall_score(y_test, preds, zero_division=0), 4),
    "test_samples": len(y_test),
}

with open("reports/evaluation.json", "w") as f:
    json.dump(report, f, indent=2)

print(f"Evaluation: {report}")

## end

#mlflow code sample
"""
MLflow experiment logging — three TODO blocks below record a training
run with MLflow.

The model and data in this script are synthetic. A trivial
DummyClassifier stands in for a trained model so that the MLflow
logging calls have a real sklearn estimator to persist, and the
accuracy/F1 scores are computed from its predictions on a small fixed
fixture — not hardcoded. The purpose of the lab is to practise the
MLflow logging API, not to reason about model quality.

The three `# TODO` blocks inside the `mlflow.start_run()` context
are the only edits required.
"""
import numpy as np
import mlflow
import mlflow.sklearn
from sklearn.dummy import DummyClassifier
from sklearn.metrics import accuracy_score, f1_score

mlflow.set_tracking_uri("http://localhost:5000")

# Hyperparameters the run should record as MLflow parameters.
params = {"n_estimators": 100, "max_depth": 5, "random_state": 42}

# Synthetic "trained" model — a DummyClassifier fit on a small set of
# deterministic rows so it has valid internal state for
# mlflow.sklearn.log_model to serialise. No real learning takes place.
X_fit = np.array([[0.0], [1.0], [2.0], [3.0]])
y_fit = np.array([1, 1, 1, 0])
model = DummyClassifier(strategy="most_frequent").fit(X_fit, y_fit)

# Evaluation scores computed from the model's own predictions on the
# fixture above — deterministic and reproducible (accuracy 0.75,
# f1_score ~0.857), not fabricated constants.
preds = model.predict(X_fit)
accuracy = accuracy_score(y_fit, preds)
f1 = f1_score(y_fit, preds)

with mlflow.start_run():

    # TODO 1: log every entry in `params` as an MLflow parameter so that
    # n_estimators, max_depth, and random_state become searchable
    # parameters on this run.
    mlflow.log_params(params)


    # TODO 2: log `accuracy` and `f1` as MLflow metrics named
    # "accuracy" and "f1_score" respectively.
    mlflow.log_metric("accuracy", accuracy)
    mlflow.log_metric("f1_score", f1)


    # TODO 3: log the trained `model` as an MLflow sklearn model
    # artefact on this run.
    mlflow.sklearn.log_model(model, name="model")


    print(f"accuracy={accuracy}, f1_score={f1}")
#end


