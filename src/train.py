import joblib
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score


FEATURES = [
    'attendance',
    'study_hours',
    'assignments_score',
    'quiz_score',
    'previous_grade',
    'lms_logins'
]


def train_model():
    df = pd.read_csv('data/processed/cleaned_student_data.csv')

    X = df[FEATURES]
    y = df['performance']

    X_train, X_test, y_train, y_test = train_test_split(
        X, y,
        test_size=0.2,
        random_state=42,
        stratify=y
    )

    model = RandomForestClassifier(
        n_estimators=300,
        random_state=42
    )

    model.fit(X_train, y_train)

    predictions = model.predict(X_test)
    accuracy = accuracy_score(y_test, predictions)

    print(f'Model Accuracy: {accuracy:.2%}')

    joblib.dump(model, 'models/student_model.pkl')
    print('Model saved successfully.')


if __name__ == '__main__':
    train_model()