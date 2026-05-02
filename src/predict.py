import joblib
import pandas as pd


FEATURES = [
    'attendance',
    'study_hours',
    'assignments_score',
    'quiz_score',
    'previous_grade',
    'lms_logins'
]

model = joblib.load('models/student_model.pkl')


def predict_student(student_data):
    df = pd.DataFrame([student_data])
    df = df[FEATURES]

    prediction = model.predict(df)[0]
    probability = model.predict_proba(df).max()

    return prediction, probability


if __name__ == '__main__':
    sample = {
        'attendance': 85,
        'study_hours': 8,
        'assignments_score': 78,
        'quiz_score': 82,
        'previous_grade': 80,
        'lms_logins': 25
    }

    pred, prob = predict_student(sample)

    print(f'Prediction: {pred}')
    print(f'Confidence: {prob:.2%}')