# Telco Customer Churn Analysis Dashboard

## Why Does Churn Matter Financially?

Customer churn is one of the most critical metrics for subscription-based businesses, especially telecom:

- **Cost of acquisition vs. retention**: Acquiring a new customer costs **5–7× more** than retaining an existing one.  
- **Revenue impact**: Churn directly reduces recurring revenue and affects accurate forecasting.  
- **Lifetime value (LTV)**: Retaining high-value customers increases their lifetime contribution.  
- **Operational efficiency**: Understanding churn helps optimize marketing spend on retention campaigns.  

> Reducing churn is **more profitable than acquiring new customers**, making churn prediction a strategic priority.

---

## Business Context

A telecom company is losing customers. Our main objectives are:  

1. **Predict churn** – Identify customers likely to leave.  
2. **Explain churn drivers** – Understand which features contribute most to churn.  
3. **Recommend retention strategies** – Target high-risk customers.  
4. **Estimate financial impact** – Quantify potential revenue saved and net profit.

---

## Key Observations

### We Observed:

- **Churners have low tenure** – Most customers leave within the first 6 months.  
- **Churners have higher monthly charges** – Indicates a potential value-price mismatch.  
- **Month-to-month contracts seem expensive** – Easy to leave due to zero switching costs.  

**Critical Failures Identified:**

1. Weak onboarding → low-tenure churn.  
2. Value-price mismatch → high-paying customers leave.  
3. Zero switching cost → month-to-month contracts allow easy exit.  

**Recommended Fixes:**  

- Strengthen early engagement.  
- Improve value delivery for high-tier clients.  
- Offer retention incentives beyond contract terms.  

---

## Model Performance & Threshold Strategy

- Initial **recall**: 0.54 → insufficient for business needs.  
- By adjusting **classification threshold** from 0.5 to 0.35:  
  - Recall increased to 0.72 → 374 × 0.72 ≈ 269 churners caught (previously 202).  
  - Additional churners saved: 67 → 67 × $960 = $64,320 potential revenue saved.  
  - Precision dropped to 0.55 → more non-churners targeted, acceptable for financial impact.  

> **Key principle**: Catch more churners even if precision drops slightly → saving customers directly impacts revenue.  

- You can also experiment with thresholds **0.30, 0.40, 0.45** to maximize net profit.  

---

## Financial Simulation Guidelines

- **If Net Profit > 0 → deploy model**  
- **If Net Profit < 0 → adjust threshold**  
- **Retention campaign assumptions**:  
  - Cost per targeted customer: $20  
  - Retention success rate: 30%  
  - Customer monthly value: $80 × 12 months = $960  

---
**Customer Churn Analysis – Key Insights**  

- **Overall churn rate**: ~26%  
- **High-risk segment**: Month-to-month contracts + low tenure + high monthly charges  

**ML Model Performance (threshold = 0.35)**:  

- ROC-AUC: 0.84  
- Recall for churners: 0.72  

**Financial Simulation**:  

- Targeted campaign: 487 customers  
- Expected saved churners: 81  
- Revenue saved: $77,472  
- Campaign cost: $9,740  
- Net profit: $67,732  

**Recommendations**:  

- Offer incentives for month-to-month high-paying customers in first 6 months.  
- Consider pricing review for high monthly charges.  
- Monitor churn trends monthly and adjust campaign threshold for maximum ROI.  

---

## Visualizations

### 1️ SHAP Feature Importance (Global)
<img width="1088" height="450" alt="newplot" src="https://github.com/user-attachments/assets/fc7b24cf-14c5-4295-b382-07830e709dff" />

### 2️ Churn Probability Distribution
<img width="1462" height="586" alt="image" src="https://github.com/user-attachments/assets/f7b74801-d18e-4a82-8774-82ba01bcdf55" />

### 3️ Top 100 High-risk customers heatmap
<img width="1088" height="450" alt="newplot" src="https://github.com/user-attachments/assets/7823af19-e657-4b61-8f84-1be228698465" />

### 4 SHAP per Customer
<img width="1088" height="450" alt="newplot" src="https://github.com/user-attachments/assets/f166b587-61e2-4d96-bc3e-04df400e94a7" />

### 5 Net Profit vs Threshold
<img width="1088" height="450" alt="newplot" src="https://github.com/user-attachments/assets/5b664be4-b7ec-40fa-8850-7c1efc51ac69" />


---
---

## Deployment Architecture (API + Multi-Container Setup)

To make the solution production-ready and scalable, the model was deployed using a modern API-based architecture:

- **FastAPI backend** serves the trained churn prediction model as a REST API (`/predict` endpoint).
- **Streamlit frontend** provides an interactive user interface for financial simulation and churn analysis.
- **Multi-container Docker setup** separates frontend and backend services using Docker Compose.
- Containers communicate internally via Docker network (service-to-service communication).
- Environment variables are used for flexible configuration between local and containerized environments.

### Architecture Overview

User → Streamlit Frontend → FastAPI Backend → Trained ML Model
This architecture enables:

- Clean separation of concerns (UI vs. model inference)
- Independent backend scalability
- Production-ready deployment
- Cloud portability (AWS / GCP / Azure ready)



