from flask import Blueprint, render_template, request
import joblib
import numpy as np

main = Blueprint('main', __name__)
model = joblib.load("fraud_detection_model.pkl")
scaler = joblib.load("scaler.joblib")

@main.route('/', methods=['GET', 'POST'])
def home():
    prediction = None
    if request.method == 'POST':
        features = [float(request.form.get(col)) for col in request.form]
        scaled_features = scaler.transform([features])
        proba = model.predict_proba(scaled_features)[0][1]
        prediction = "Fraud" if proba >= 0.5 else "Not Fraud"
    return render_template("index.html", prediction=prediction)
