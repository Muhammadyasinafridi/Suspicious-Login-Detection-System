import streamlit as st
import joblib
import numpy as np

# Page setup
st.set_page_config(page_title="Security Anomaly Detector", page_icon="🛡️")

# Load saved model and scaler
@st.cache_resource
def load_artifacts():
    model = joblib.load('knn_model.pkl')
    scaler = joblib.load('scaler.pkl')
    return model, scaler

try:
    knn, scaler = load_artifacts()

    st.title("🛡️ Suspicious Login Detection System")
    st.write("Enter session parameters to evaluate account activity risk using KNN.")
    st.divider()

    col1, col2 = st.columns(2)
    with col1:
        login_attempts = st.number_input("Login Attempts", min_value=1, max_value=50, value=2)
        session_duration = st.number_input("Session Duration (sec)", min_value=1, max_value=3600, value=20)
    with col2:
        pages_accessed = st.number_input("Pages Accessed", min_value=1, max_value=1000, value=15)
        failed_logins = st.number_input("Failed Logins", min_value=0, max_value=50, value=0)

    st.divider()

    if st.button("Analyze Activity Risk", type="primary", use_container_width=True):
        input_features = np.array([[login_attempts, session_duration, pages_accessed, failed_logins]])
        scaled_features = scaler.transform(input_features)

        prediction = knn.predict(scaled_features)[0]
        probabilities = knn.predict_proba(scaled_features)[0]

        normal_prob = probabilities[0] * 100
        suspicious_prob = probabilities[1] * 100

        if prediction == 0:
            st.success(f"✅ **Normal User Activity** (Confidence: {normal_prob:.1f}%)")
        else:
            st.error(f"🚨 **Suspicious Activity Flagged!** (Confidence: {suspicious_prob:.1f}%)")

        col_a, col_b = st.columns(2)
        col_a.metric("Normal Class Probability", f"{normal_prob:.1f}%")
        col_b.metric("Suspicious Class Probability", f"{suspicious_prob:.1f}%")

except Exception as e:
    st.error(f"Error loading model files: {e}")
    st.info("Make sure 'knn_model.pkl' and 'scaler.pkl' are saved in your Colab files!")
    col_b.metric("Suspicious Class Probability", f"{suspicious_prob:.1f}%")
