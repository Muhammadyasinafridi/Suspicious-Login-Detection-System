import streamlit as st

st.markdown(
<style>
    /* 1. Makes the app layout clean and centered on screen */
    .main .block-container {
        max-width: 1000px;
        padding-top: 2rem;
    }

    /* 2. Styles big result numbers (Metrics) to be bold and dark blue */
    [data-testid="stMetricValue"] {
        font-size: 2.5rem;
        font-weight: bold;
        color: #1E3A8A;
    }

    /* 3. Styles metric labels (titles above the numbers) */
    [data-testid="stMetricLabel"] {
        font-size: 1.1rem;
        font-weight: 600;
        color: #4B5563;
    }

    /* 4. Makes primary buttons look clean with rounded corners */
    .stButton > button {
        border-radius: 8px;
        font-weight: bold;
    }
</style>
, unsafe_allow_html=True)



import warnings
import pandas as pd
import numpy as np
import joblib

#Hide the scikit-learn version mismatch warning in terminal
warnings.filterwarnings('ignore', category=UserWarning)



#Page Configuration
st.set_page_config(
    page_title="Account Takeover Detector",
    page_icon="🔒",
    layout="wide",
    initial_sidebar_state="collapsed"
)




#Load Model and Scaler

@st.cache_resource
def load_artifacts(): 
    Knn_model = joblib.load('knn_model.pkl')
    scaler = joblib.load('scaler.pkl')
    return Knn_model, scaler

Knn_model, scaler = load_artifacts()

#App Title & Subtitle
st.title("🔒 Suspicious Login Detection System")
st.write("Enter session parameters below to evaluate user activity risk.")
st.divider()

#Input Controls
col1, col2 = st.columns(2)

with col1:
    login_attempts = st.number_input("Login Attempts", min_value=0, value=0)
    session_duration = st.number_input("Session Duration (seconds)", min_value=0, value=120)

with col2:
    pages_accessed = st.number_input("Pages Accessed", min_value=0, value=0)
    failed_logins = st.number_input("Failed Logins", min_value=0, value=0)

st.divider()

#Prediction Button
if st.button("Predict User Activity Risk", type="primary", use_container_width=True):
    
    

# Passing Pandas DataFrame with original feature names
    feature_names = ["login_attempts", "session_duration", "pages_accessed", "failed_logins"] # Make sure these match your training dataset exact names!
    input_data = pd.DataFrame([[login_attempts, session_duration, pages_accessed, failed_logins]], columns=feature_names)

    scaled_data = scaler.transform(input_data)
    
    
    # Predict class and probability
    prediction = Knn_model.predict(scaled_data)[0]
    probabilities = Knn_model.predict_proba(scaled_data)[0]


## Display User Activity Results
    if prediction == 1:
        st.error("⚠️ **High Risk Detected!** This session is suspicious.")
    else:
        st.success("✅ ** Normal Activity:**  This session appears safe and authentic.")

# Show Risk Scores using Metrics
    m1, m2 = st.columns(2)
    m1.metric("Safe Probability", f"{probabilities[0]*100:.1f}%")
    m2.metric("Risk Probability", f"{probabilities[1]*100:.1f}%")
