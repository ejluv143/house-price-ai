from flask import Flask, request, jsonify
from flask_cors import CORS
import pandas as pd
import joblib

app = Flask(__name__)
CORS(app)

model = joblib.load("house_price_model.pkl")


@app.route("/", methods=["GET"])
def home():
    return jsonify({
        "message": "Philippines House Price ML API is running"
    })


@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()

    size_sqm = float(data["size_sqm"])
    bedrooms = int(data["bedrooms"])
    location_score = int(data["location_score"])
    finish_level = data["finish_level"]
    cost_per_sqm = float(data["cost_per_sqm"])

    input_data = pd.DataFrame([{
        "size_sqm": size_sqm,
        "bedrooms": bedrooms,
        "location_score": location_score,
        "finish_level": finish_level,
        "cost_per_sqm": cost_per_sqm
    }])

    prediction = model.predict(input_data)[0]

    return jsonify({
        "estimated_price": round(prediction, 2)
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)