import os
import pickle
import pandas as pd
from flask import Flask, render_template, request
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

app = Flask(__name__)

MODEL_PATH = "model/disease_model.pkl"
DATASET_PATH = "dataset/disease_dataset.csv"

# -------------------------------
# TRAIN MODEL (If not exists)
# -------------------------------
if not os.path.exists(MODEL_PATH):
    print("Training model...")

    data = pd.read_csv(DATASET_PATH)
    X = data.drop("disease", axis=1)
    y = data["disease"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)
    acc = accuracy_score(y_test, y_pred)
    print("Model Accuracy:", acc * 100)

    os.makedirs("model", exist_ok=True)
    pickle.dump(model, open(MODEL_PATH, "wb"))
    print("Model saved.")

else:
    print("Loading existing model...")

model = pickle.load(open(MODEL_PATH, "rb"))

# -------------------------------
# FLASK ROUTES
# -------------------------------

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    symptoms = [
        int(request.form['fever']),
        int(request.form['headache']),
        int(request.form['nausea']),
        int(request.form['cough']),
        int(request.form['fatigue'])
    ]

    prediction = model.predict([symptoms])[0]
    confidence = model.predict_proba([symptoms]).max() * 100

    return render_template(
        "result.html",
        prediction=prediction,
        confidence=round(confidence, 2)
    )

# -------------------------------
# RUN APP
# -------------------------------
if __name__ == "__main__":
    app.run(debug=True)
