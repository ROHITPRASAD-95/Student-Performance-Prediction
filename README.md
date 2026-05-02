🎓 Student Performance Prediction System
A Machine Learning project that predicts whether a student will pass or fail based on academic performance, attendance, study habits, and LMS engagement.

🚀 Features
Synthetic dataset generation
Data preprocessing pipeline
Random Forest classification
Model evaluation and visualization
FastAPI REST API
Interactive Streamlit dashboard
Feature importance analysis

🛠️ Tech Stack
Python
Pandas
NumPy
Scikit-Learn
Matplotlib
Seaborn
Plotly
Streamlit
FastAPI
📂 Project Structure
Student-Performance-Prediction/├── data/├── notebooks/├── src/├── api/├── dashboard/├── models/├── outputs/├── images/├── requirements.txt├── README.md└── main.py

▶️ Run the Project
Train Model
python main.py
Start FastAPI Server
uvicorn api.app:app --reload
Launch Dashboard
streamlit run dashboard/app.py

📊 Model Features
Attendance
Study Hours
Assignment Score
Quiz Score
Previous Grade
LMS Logins
🎯 Prediction Output
Pass / Fail
Confidence Score
Student Performance Analysis

📈 Sample Results
Accuracy: ~99%
Real-time predictions
Interactive visualizations
API-ready deployment

🌐 API Endpoint
POST /predict
Example JSON:
{  "attendance": 85,  "study_hours": 8,  "assignments_score": 78,  "quiz_score": 82,  "previous_grade": 80,  "lms_logins": 25}

🖥️ Dashboard Highlights
Interactive sliders
Instant predictions
Confidence meter
Feature visualization

👨‍💻 Author
Rohit Kumar
