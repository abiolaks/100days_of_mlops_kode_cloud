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

