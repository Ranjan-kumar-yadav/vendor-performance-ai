from fastapi import FastAPI
import joblib
import numpy as np

app = FastAPI()

model = joblib.load("vendor_model.pkl")
encoder = joblib.load("label_encoder.pkl")

@app.post("/predict-vendor")
def predict_vendor(data: dict):

    features = np.array([[
        data["total_orders"],
        data["accepted_orders"],
        data["avg_rating"],
        data["cancellation_rate"],
        data["complaints_count"]
    ]])

    prediction = model.predict(features)

    result = encoder.inverse_transform(prediction)

    return {
        "performance": result[0]
    }