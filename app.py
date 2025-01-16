import streamlit as st
import pandas as pd
import joblib

# Load model
model = joblib.load('decision_tree_model.pkl')

# App title
st.title("Fitness Level Prediction App")

# User input
st.sidebar.header("Input Features")

def user_input_features():
    age = st.sidebar.slider("Age", 10, 80, 25)
    max_bpm = st.sidebar.slider("Max BPM", 100, 220, 180)
    avg_bpm = st.sidebar.slider("Avg BPM", 50, 150, 120)
    session_duration = st.sidebar.slider("Session Duration (hours)", 0.5, 3.0, 1.5)
    calories_burned = st.sidebar.slider("Calories Burned", 100, 1000, 500)
    workout_type = st.sidebar.selectbox("Workout Type", ["Cardio", "Strength", "Flexibility"])
    fat_percentage = st.sidebar.slider("Fat Percentage", 5, 50, 20)
    water_intake = st.sidebar.slider("Water Intake (liters)", 0.5, 5.0, 2.0)
    workout_frequency = st.sidebar.slider("Workout Frequency (days/week)", 1, 7, 4)
    bmi = st.sidebar.slider("BMI", 15.0, 40.0, 22.0)

    data = {
        "Age": age,
        "Max_BPM": max_bpm,
        "Avg_BPM": avg_bpm,
        "Session_Duration": session_duration,
        "Calories_Burned": calories_burned,
        "Workout_Type": workout_type,
        "Fat_Percentage": fat_percentage,
        "Water_Intake": water_intake,
        "Workout_Frequency": workout_frequency,
        "BMI": bmi
    }
    return pd.DataFrame([data])

input_df = user_input_features()

# Display user input
st.subheader("User Input:")
st.write(input_df)

# Prediction
if st.button("Predict Fitness Level"):
    prediction = model.predict(input_df)
    st.subheader("Prediction Result:")
    st.write(f"Predicted Fitness Level: {prediction[0]}")
