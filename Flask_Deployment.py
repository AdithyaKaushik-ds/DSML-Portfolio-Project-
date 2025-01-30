
from flask import Flask, request, jsonify
import pickle
import numpy as np

# Load the trained Linear Regression model
with open("gb_model.pkl", "rb") as file:
    model = pickle.load(file)

# Initialize Flask app
app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"message": "Welcome to the Insurance Cost Prediction API!"})

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get JSON data from request
        data = request.get_json()
        
        # Extract features from JSON
        features = [
            data.get("age"),
            data.get("bmi"),
            data.get("number_of_major_surgeries"),
            data.get("diabetes"),
            data.get("blood_pressure"),
            data.get("chronic_diseases"),
            data.get("history_of_cancer"),
            data.get("any_transplants"),
            data.get("known_allergies")
        ]
        
        # Convert to NumPy array
        input_features = np.array([features])
        
        # Make prediction
        prediction = model.predict(input_features)
        
        return jsonify({"estimated_premium": round(prediction[0], 2)})
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == '__main__':
    app.run(debug=True)
