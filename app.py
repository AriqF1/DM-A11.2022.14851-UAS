import streamlit as st
import pandas as pd
import joblib

# Load model dan fitur
model = joblib.load('decision_tree_model.pkl')
feature_names = joblib.load('feature_names.pkl')

# App title
st.title("Fitness Level Prediction App")

# User input
st.sidebar.header("Input Features")

def user_input_features():
    # Input dari pengguna
    age = st.sidebar.slider("Age", 10, 80, 25)
    weight = st.sidebar.slider("Weight (kg)", 30, 150, 70)
    height = st.sidebar.slider("Height (m)", 1.0, 2.5, 1.75)
    max_bpm = st.sidebar.slider("Max BPM", 100, 220, 180)
    avg_bpm = st.sidebar.slider("Avg BPM", 50, 150, 120)
    resting_bpm = st.sidebar.slider("Resting BPM", 40, 100, 60)
    session_duration = st.sidebar.slider("Session Duration (hours)", 0.5, 3.0, 1.5)
    calories_burned = st.sidebar.slider("Calories Burned", 100, 1000, 500)
    fat_percentage = st.sidebar.slider("Fat Percentage", 5, 50, 20)
    water_intake = st.sidebar.slider("Water Intake (liters)", 0.5, 5.0, 2.0)
    workout_frequency = st.sidebar.slider("Workout Frequency (days/week)", 1, 7, 4)
    bmi = st.sidebar.slider("BMI", 15.0, 40.0, 22.0)
    
    gender = st.sidebar.selectbox("Gender", ["Male", "Female"])
    workout_type = st.sidebar.selectbox("Workout Type", ["Cardio", "Strength", "Flexibility"])
    experience_level = st.sidebar.selectbox("Experience Level", ["Beginner", "Intermediate", "Advanced"])

    # One-hot encoding untuk atribut kategorikal
    gender_male = 1 if gender == "Male" else 0
    workout_type_cardio = 1 if workout_type == "Cardio" else 0
    workout_type_strength = 1 if workout_type == "Strength" else 0
    experience_level_intermediate = 1 if experience_level == "Intermediate" else 0
    experience_level_advanced = 1 if experience_level == "Advanced" else 0

    # Data dalam format dictionary
    data = {
        'Age': age,
        'Weight (kg)': weight,
        'Height (m)': height,
        'Max_BPM': max_bpm,
        'Avg_BPM': avg_bpm,
        'Resting_BPM': resting_bpm,
        'Session_Duration (hours)': session_duration,
        'Calories_Burned': calories_burned,
        'Fat_Percentage': fat_percentage,
        'Water_Intake (liters)': water_intake,
        'Workout_Frequency (days/week)': workout_frequency,
        'BMI': bmi,
        'Gender_Male': gender_male,
        'Workout_Type_Cardio': workout_type_cardio,
        'Workout_Type_Strength': workout_type_strength,
        'Experience_Level_Intermediate': experience_level_intermediate,
        'Experience_Level_Advanced': experience_level_advanced
    }
    # Sesuaikan urutan kolom dengan model
    return pd.DataFrame([data]).reindex(columns=feature_names, fill_value=0)

# Input dari pengguna
input_df = user_input_features()

# Display user input
st.subheader("User Input:")
st.write(input_df)

# Prediksi
if st.button("Predict Fitness Level"):
    prediction = model.predict(input_df)
    st.subheader("Prediction Result:")
    st.write(f"Predicted Fitness Level: {prediction[0]}")
