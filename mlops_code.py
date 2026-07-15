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

