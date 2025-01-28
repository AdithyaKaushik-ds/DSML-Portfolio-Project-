import streamlit as st
import pickle
import numpy as np

# Load the pre-trained XGBoost model
#with open("xgboost_model.pkl", "rb") as file:
   # model = pickle.load(file)

import joblib
model = joblib.load("xgboost_model.joblib")

# Streamlit App Title
st.title("Insurance Cost Prediction")
st.write("This app predicts insurance costs based on user inputs using a pre-trained XGBoost model.")

# Create a form for user input
with st.form("user_input_form"):
    st.subheader("Enter Your Details")

    # Collect user input for features
    age = st.number_input("Age", min_value=18, max_value=100, step=1, value=30, help="Enter the age of the individual.")
    sex = st.selectbox("Sex", options=["male", "female"], index=0, help="Select the gender of the individual.")
    bmi = st.number_input("BMI", min_value=10.0, max_value=50.0, step=0.1, value=25.0, help="Enter the Body Mass Index.")
    children = st.number_input("Number of Children", min_value=0, max_value=10, step=1, value=0, help="Enter the number of children.")
    smoker = st.selectbox("Smoker", options=["yes", "no"], index=1, help="Is the individual a smoker?")
    region = st.selectbox("Region", options=["northeast", "northwest", "southeast", "southwest"], help="Select the region of residence.")

    # Submit button inside the form
    submitted = st.form_submit_button("Predict")

# Process the input and make predictions if the form is submitted
if submitted:
    # Encode categorical features
    sex_encoded = 1 if sex == "male" else 0
    smoker_encoded = 1 if smoker == "yes" else 0
    region_mapping = {"northeast": 0, "northwest": 1, "southeast": 2, "southwest": 3}
    region_encoded = region_mapping[region]

    # Prepare input data for prediction
    input_data = np.array([[age, sex_encoded, bmi, children, smoker_encoded, region_encoded]])

    # Make prediction
    prediction = model.predict(input_data)

    # Display the result
    st.success(f"The predicted insurance cost is ${prediction[0]:,.2f}.")
