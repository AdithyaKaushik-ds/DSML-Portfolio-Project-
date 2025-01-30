# DSML-Portfolio-Project-
Insurance Cost Prediction

Problem Statement
Insurance companies need to accurately predict the cost of health insurance for individuals to
set premiums appropriately. However, traditional methods of cost prediction often rely on broad
actuarial tables and historical averages, which may not account for the nuanced differences
among individuals. By leveraging machine learning techniques, insurers can predict more
accurately the insurance costs tailored to individual profiles, leading to more competitive pricing
and better risk management.

Insurance Cost Prediction: Summary

Introduction

Insurance cost prediction is vital for risk management and fair premium pricing. This case study analyzes key factors affecting insurance premiums and evaluates machine learning models to identify the best predictor.

Dataset Overview

Demographics: Age, BMI, etc.

Health Indicators: Diabetes, Blood Pressure Problems, Chronic Diseases.

Medical History: Surgeries, Allergies, Family Cancer History.

Records: 1,338 entries with no missing values.

Key Insights from EDA

Age & Premium: Premiums increase significantly with age.

Health Factors: Diabetes, blood pressure issues, and surgeries contribute to higher costs.

BMI Influence: Categorized as Underweight, Normal, Overweight, and Obese to refine predictions.

Model Performance

Model

Train R²

Test R²

Linear Regression

0.72

0.68

Random Forest

0.98

0.85

GBM

0.97

0.87

XGBoost

0.98

0.90

XGBoost provided the highest accuracy, making it the preferred choice for deployment.

Recommendations

Use XGBoost for production deployment.

Focus on key features like age, BMI, and health indicators.

Regular model updates to adapt to new data.

Encourage preventive healthcare to lower overall insurance costs.

Conclusion

This study demonstrates how machine learning improves insurance cost prediction. A structured approach to data processing, feature engineering, and model evaluation ensures accuracy and efficiency, benefiting both insurers and policyholders.



