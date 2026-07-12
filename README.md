%%writefile README.md
# 🛡️ Account Takeover & Fraud Detection System

An interactive Machine Learning web application built with **Streamlit** and **K-Nearest Neighbors (KNN)** to detect suspicious user logins and account takeover attempts in real time.

## 📌 Key Features
- **Real-time Anomaly Detection**: Evaluates login parameters against normal vs. malicious user profiles.
- **Probabilistic Risk Scoring**: Displays exact prediction confidence percentages using `predict_proba`.
- **Feature Normalization**: Employs `StandardScaler` to accurately scale multi-dimensional session metrics.

## 📊 Parameters Analyzed
- **Login Attempts**: Number of login attempts in a session.
- **Session Duration**: Total length of session in seconds.
- **Pages Accessed**: Total pages viewed during activity.
- **Failed Logins**: Unsuccessful authentication attempts.

## 🛠️ Project Files
- `app.py` — Streamlit web interface code.
- `knn_model.pkl` — Trained KNN classifier object.
- `scaler.pkl` — Fitted StandardScaler object for feature normalization.
- `requirements.txt` — Python dependencies for deployment.

## 🚀 How to Run Locally
```bash
pip install -r requirements.txt
streamlit run app.py