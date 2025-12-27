from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd

model = joblib.load('traffic_accident_model.joblib')

app = FastAPI(title="Munchen Accident Forecast Model API")

class PredictionInput(BaseModel):
    year: int
    month: int

@app.post("/predict")
def predict_accidents(input_data: PredictionInput):
    features = pd.DataFrame({
        'JAHR': [input_data.year],
        'MONTH_NUM': [input_data.month]
    })
    
    prediction = model.predict(features)
    
    return {
        "prediction": int(prediction[0])
    }

@app.get("/")
def home():
    return {"message": "The model is working right now! /predict please post a post request."}