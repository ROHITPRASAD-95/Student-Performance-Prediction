ent_data(n=5000):
    np.random.seed(42)

    df = pd.DataFrame({
        'attendance': np.random.randint(50, 100, n),
        'study_houimport numpy as np
import pandas as pd


FEATURES = [
    'attendance',
    'study_hours',
    'assignments_score',
    'quiz_score',
    'previous_grade',
    'lms_logins'
]


def generate_studrs': np.random.randint(1, 12, n),
        'assignments_score': np.random.randint(40, 100, n),
        'quiz_score': np.random.randint(35, 100, n),
        'previous_grade': np.random.randint(45, 100, n),
        'lms_logins': np.random.randint(1, 40, n)
    })

    score = (
        0.25 * df['attendance'] +
        2.0 * df['study_hours'] +
        0.20 * df['assignments_score'] +
        0.25 * df['quiz_score'] +
        0.30 * df['previous_grade'] +
        0.50 * df['lms_logins']
    )

    df['performance'] = np.where(score >= 75, 'Pass', 'Fail')
    return df


if __name__ == '__main__':
    df = generate_student_data()
    df.to_csv('data/raw/student_performance.csv', index=False)
    print('Dataset saved successfully.')