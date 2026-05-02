from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
import joblib

app = FastAPI(title='Student Performance Prediction API')
model = joblib.load('models/student_model.pkl')


class Student(BaseModel):
    attendance: int
    study_hours: int
    assignments_score: int
    quiz_score: int
    previous_grade: int
    lms_logins: int


@app.get('/')
def home():
    return {'message': 'API is running successfully'}


@app.post('/predict')
def predict(student: Student):
    data = pd.DataFrame([student.model_dump()])

    prediction = model.predict(data)[0]
    confidence = float(model.predict_proba(data).max())

    return {
        'prediction': prediction,
        'confidence': round(confidence * 100, 2)
    }