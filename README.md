# Credit-Card-Fraud-Detection


**Author:** Rutendo 



## Project Overview

This project implements a machine learning pipeline to detect fraudulent credit card transactions. It covers data preprocessing, handling class imbalance using SMOTE, feature scaling, training and tuning multiple models (Logistic Regression, Random Forest, XGBoost), and model evaluation.
The final model is saved for deployment and integrated into a Flask web application for real-time fraud prediction.



## Dataset

The dataset (`creditcard_2023.csv`) contains anonymized transaction features (`V1` to `V28`), transaction amount, and a target variable `Class` where:
- `0` = Normal transaction
- `1` = Fraudulent transaction



## Key Features

- Exploratory Data Analysis with Pandas and Seaborn
- Class imbalance handling with SMOTE
- Feature scaling using StandardScaler
- Model training: Logistic Regression, Random Forest, XGBoost, and Voting Ensemble
- Hyperparameter tuning using GridSearchCV
- Threshold tuning via Precision-Recall curves to optimize F1-score
- Model and scaler saved with `joblib` for reuse
- Export of predictions to CSV for Power BI integration

****Files****
- creditcard_2023.csv — Dataset file

- fraud_detection_model.pkl — Saved trained model

- scaler.joblib — Saved scaler for feature transformation

- app.py — Flask app for real-time predictions

- templates/ — HTML templates for Flask

- requirements.txt — Python dependencies

- README.md — This file


  

**Installation Instructions**


**Clone the repository:**


git clone https://github.com/yourusername/credit-card-fraud-detection.git
cd credit-card-fraud-detection


**Create and activate a virtual environment:**


python -m venv venv
source venv/bin/activate   # On Windows use: venv\Scripts\activate


**Install required libraries:**


pip install -r requirements.txt

Launch the notebook or start the Flask app as described above.



**MIT License**


Copyright (c) 2025 Rutendo Simango

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights 
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell 
copies of the Software, and to permit persons to whom the Software is 
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included 
in all copies or substantial portions of the Software.







