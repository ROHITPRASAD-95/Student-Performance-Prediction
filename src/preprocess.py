import pandas as pd


FEATURES = [
    'attendance',
    'study_hours',
    'assignments_score',
    'quiz_score',
    'previous_grade',
    'lms_logins',
    'performance'
]


def preprocess_data():
    df = pd.read_csv('data/raw/student_performance.csv')

    df.drop_duplicates(inplace=True)
    df = df[FEATURES]

    df.to_csv('data/processed/cleaned_student_data.csv', index=False)
    print('Preprocessing complete.')


if __name__ == '__main__':
    preprocess_data()