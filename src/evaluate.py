import joblib
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import confusion_matrix, classification_report, accuracy_score
from sklearn.model_selection import train_test_split


FEATURES = [
    'attendance',
    'study_hours',
    'assignments_score',
    'quiz_score',
    'previous_grade',
    'lms_logins'
]


def evaluate_model():
    df = pd.read_csv('data/processed/cleaned_student_data.csv')

    X = df[FEATURES]
    y = df['performance']

    X_train, X_test, y_train, y_test = train_test_split(
        X, y,
        test_size=0.2,
        random_state=42,
        stratify=y
    )

    model = joblib.load('models/student_model.pkl')
    predictions = model.predict(X_test)

    accuracy = accuracy_score(y_test, predictions)
    print(f'Accuracy: {accuracy:.2%}')
    print(classification_report(y_test, predictions))

    cm = confusion_matrix(y_test, predictions)

    plt.figure(figsize=(8, 6))
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues')
    plt.title('Confusion Matrix')
    plt.xlabel('Predicted')
    plt.ylabel('Actual')
    plt.savefig('outputs/confusion_matrix.png')
    plt.show()


if __name__ == '__main__':
    evaluate_model()