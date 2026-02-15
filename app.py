# app.py
from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
import joblib

app = FastAPI(title="Customer Churn Prediction API")

# Load trained pipeline
pipeline = joblib.load("models/pipeline_model.pkl")

# Columns used during training
expected_cols = ['SeniorCitizen', 'tenure', 'MonthlyCharges', 'TotalCharges',
       'charge_per_tenure', 'is_month_to_month', 'gender_Male', 'Partner_Yes',
       'Dependents_Yes', 'PhoneService_Yes', 'MultipleLines_No phone service',
       'MultipleLines_Yes', 'InternetService_Fiber optic',
       'InternetService_No', 'OnlineSecurity_No internet service',
       'OnlineSecurity_Yes', 'OnlineBackup_No internet service',
       'OnlineBackup_Yes', 'DeviceProtection_No internet service',
       'DeviceProtection_Yes', 'TechSupport_No internet service',
       'TechSupport_Yes', 'StreamingTV_No internet service', 'StreamingTV_Yes',
       'StreamingMovies_No internet service', 'StreamingMovies_Yes',
       'Contract_One year', 'Contract_Two year', 'PaperlessBilling_Yes',
       'PaymentMethod_Credit card (automatic)',
       'PaymentMethod_Electronic check', 'PaymentMethod_Mailed check',
       'tenure_group_1-2yr', 'tenure_group_2-4yr', 'tenure_group_4-6yr']

# Define input data model
class ChurnInput(BaseModel):
    SeniorCitizen: int
    tenure: float
    MonthlyCharges: float
    TotalCharges: float
    charge_per_tenure: float
    is_month_to_month: int
    gender_Male: int = 0
    Partner_Yes: int = 0
    Dependents_Yes: int = 0
    PhoneService_Yes: int = 0
    

@app.post("/predict")
def predict_churn(data: ChurnInput):
    # Convert to DataFrame
    df = pd.DataFrame([data.dict()])

    # Add missing columns with 0
    for col in expected_cols:
        if col not in df.columns:
            df[col] = 0

    # Reorder columns to match training
    df = df[expected_cols]

    # Predict probability
    prob = pipeline.predict_proba(df)[:,1][0]
    prediction = pipeline.predict(df)[0]

    return {"churn_probability": float(prob), "churn_prediction": int(prediction)}
