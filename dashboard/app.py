import streamlit as st
import pandas as pd
import joblib
import plotly.express as px
import plotly.io as pio

pio.templates.default = 'plotly_dark'

model = joblib.load('models/student_model.pkl')

st.set_page_config(
    page_title='Student Performance Predictor',
    page_icon='🎓',
    layout='wide'
)

st.title('🎓 Student Performance Prediction System')
st.markdown('Predict student academic success using Machine Learning.')

col1, col2 = st.columns(2)

with col1:
    attendance = st.slider('Attendance (%)', 50, 100, 85)
    study_hours = st.slider('Study Hours', 1, 12, 8)
    assignments_score = st.slider('Assignment Score', 40, 100, 78)

with col2:
    quiz_score = st.slider('Quiz Score', 35, 100, 82)
    previous_grade = st.slider('Previous Grade', 45, 100, 80)
    lms_logins = st.slider('LMS Logins', 1, 40, 25)

if st.button('Predict Performance'):
    sample = pd.DataFrame([{
        'attendance': attendance,
        'study_hours': study_hours,
        'assignments_score': assignments_score,
        'quiz_score': quiz_score,
        'previous_grade': previous_grade,
        'lms_logins': lms_logins
    }])

    prediction = model.predict(sample)[0]
    confidence = model.predict_proba(sample).max()

    st.success(f'Prediction: {prediction}')
    st.info(f'Confidence: {confidence:.2%}')

    fig = px.bar(
        x=sample.columns,
        y=sample.iloc[0].values,
        title='Student Feature Analysis'
    )
    st.plotly_chart(fig, use_container_width=True)