# streamlit_app.py
import streamlit as st
import requests

st.title("Customer Churn Prediction")

# User inputs
SeniorCitizen = st.selectbox("Senior Citizen", [0,1])
tenure = st.number_input("Tenure (months)", min_value=0, max_value=72, value=12)
MonthlyCharges = st.number_input("Monthly Charges", min_value=0.0, value=70.0)
TotalCharges = st.number_input("Total Charges", min_value=0.0, value=840.0)
charge_per_tenure = st.number_input("Charge per Tenure", min_value=0.0, value=70.0)
is_month_to_month = st.selectbox("Month-to-Month Contract", [0,1])
gender_Male = st.selectbox("Gender Male", [0,1])
Partner_Yes = st.selectbox("Partner", [0,1])
Dependents_Yes = st.selectbox("Dependents", [0,1])
PhoneService_Yes = st.selectbox("Phone Service", [0,1])

# Button to predict
if st.button("Predict Churn"):
    # Prepare data
    payload = {
        "SeniorCitizen": SeniorCitizen,
        "tenure": tenure,
        "MonthlyCharges": MonthlyCharges,
        "TotalCharges": TotalCharges,
        "charge_per_tenure": charge_per_tenure,
        "is_month_to_month": is_month_to_month,
        "gender_Male": gender_Male,
        "Partner_Yes": Partner_Yes,
        "Dependents_Yes": Dependents_Yes,
        "PhoneService_Yes": PhoneService_Yes
    }

    # Call FastAPI backend
    response = requests.post("http://churn_backend:8000/predict", json=payload)


    if response.status_code == 200:
        result = response.json()
        st.write(f"Churn Probability: {result['churn_probability']:.2f}")
        st.write(f"Churn Prediction (0=No, 1=Yes): {result['churn_prediction']}")
    else:
        st.error("Error predicting churn. Check backend logs.")
