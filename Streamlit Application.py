import streamlit as st
import pickle
import numpy as np

# Load the trained Linear Regression model
with open("lr_model.pkl", "rb") as file:
    model = pickle.load(file)

# Streamlit UI Design
st.set_page_config(page_title="Insurance Cost Prediction", page_icon="💰", layout="wide")

# Custom Styling
st.markdown("""
    <style>
    body {
        background-color: #f4f4f4;
    }
    .main-container {
        text-align: center;
        padding: 20px;
        background-color: white;
        border-radius: 10px;
        box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.1);
    }
    </style>
""", unsafe_allow_html=True)

# Main Header
st.markdown("<div class='main-container'>", unsafe_allow_html=True)
st.title("Insurance Cost Prediction")
st.markdown("### Predict your insurance premium based on health factors")
st.markdown("---")

# User Input Fields in Columns
col1, col2, col3 = st.columns(3)

with col1:
    age = st.number_input("📅 Age", min_value=18, max_value=100, value=30)
    bmi = st.number_input("⚖️ BMI", min_value=10.0, max_value=50.0, value=25.0)
    number_of_major_surgeries = st.selectbox("🩺 Number of Major Surgeries", [0, 1, 2, 3])

with col2:
    diabetes = st.selectbox("💉 Diabetes", [0, 1], format_func=lambda x: "Yes" if x == 1 else "No")
    blood_pressure = st.selectbox("❤️ Blood Pressure Problems", [0, 1], format_func=lambda x: "Yes" if x == 1 else "No")
    chronic_diseases = st.selectbox("🦠 Chronic Diseases", [0, 1], format_func=lambda x: "Yes" if x == 1 else "No")

with col3:
    history_of_cancer = st.selectbox("🧬 Family History of Cancer", [0, 1], format_func=lambda x: "Yes" if x == 1 else "No")
    any_transplants = st.selectbox("🔄 Any Transplants", [0, 1], format_func=lambda x: "Yes" if x == 1 else "No")
    known_allergies = st.selectbox("🌿 Known Allergies", [0, 1], format_func=lambda x: "Yes" if x == 1 else "No")

# Predict Button
if st.button("🔍 Predict Insurance Cost"):
    input_features = np.array([[age, bmi, number_of_major_surgeries, diabetes, blood_pressure, chronic_diseases, history_of_cancer, any_transplants, known_allergies]])
    prediction = model.predict(input_features)
    
    st.markdown("---")
    st.subheader("🔮 Predicted Insurance Cost")
    st.success(f" Estimated Cost: **{prediction[0]:,.2f}**")

st.markdown("</div>", unsafe_allow_html=True)
