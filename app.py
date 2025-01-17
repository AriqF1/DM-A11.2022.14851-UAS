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

def check_abnormalities(inputs, normal_ranges):
    abnormalities = []
    # Pastikan mengambil nilai tunggal dari Series 'Age'
    if not (normal_ranges['Age'][0] <= inputs['Age'].iloc[0] <= normal_ranges['Age'][1]):
        abnormalities.append("Usia berada di luar rentang optimal untuk program kebugaran (18-60 tahun).")
    if not (normal_ranges['BMI'][0] <= inputs['BMI'].iloc[0] <= normal_ranges['BMI'][1]):
        abnormalities.append("BMI menunjukkan kondisi kekurangan berat badan atau kelebihan berat badan.")
    if not (normal_ranges['Resting_BPM'][0] <= inputs['Resting_BPM'].iloc[0] <= normal_ranges['Resting_BPM'][1]):
        abnormalities.append("Detak jantung saat istirahat (Resting BPM) berada di luar rentang normal (60-100 bpm).")
    if not (normal_ranges['Max_BPM'][0] <= inputs['Max_BPM'].iloc[0] <= normal_ranges['Max_BPM'][1]):
        abnormalities.append("Detak jantung maksimum (Max BPM) mungkin mengindikasikan potensi masalah kardiovaskular.")
    if not (normal_ranges['Avg_BPM'][0] <= inputs['Avg_BPM'].iloc[0] <= normal_ranges['Avg_BPM'][1]):
        abnormalities.append("Rata-rata detak jantung (Avg BPM) berada di luar rentang normal, yang dapat mengindikasikan aktivitas jantung yang tidak teratur.")
    if not (normal_ranges['Session_Duration'][0] <= inputs['Session_Duration (hours)'].iloc[0] <= normal_ranges['Session_Duration'][1]):
        abnormalities.append("Durasi sesi berada di luar rentang yang direkomendasikan (0,5-2,0 jam).")
    if not (normal_ranges['Calories_Burned'][0] <= inputs['Calories_Burned'].iloc[0] <= normal_ranges['Calories_Burned'][1]):
        abnormalities.append("Kalori yang terbakar terlalu rendah atau terlalu tinggi untuk sebuah sesi.")
    if not (normal_ranges['Fat_Percentage'][0] <= inputs['Fat_Percentage'].iloc[0] <= normal_ranges['Fat_Percentage'][1]):
        abnormalities.append("Persentase lemak tubuh berada di luar rentang sehat (10-30%).")
    if not (normal_ranges['Water_Intake'][0] <= inputs['Water_Intake (liters)'].iloc[0] <= normal_ranges['Water_Intake'][1]):
        abnormalities.append("Asupan air berada di bawah atau di atas jumlah harian yang direkomendasikan (2,0-3,7 liter).")
    if not (normal_ranges['Workout_Frequency'][0] <= inputs['Workout_Frequency (days/week)'].iloc[0] <= normal_ranges['Workout_Frequency'][1]):
        abnormalities.append("Frekuensi latihan terlalu rendah atau terlalu tinggi (3-6 hari per minggu).")
    return abnormalities


# Input dari pengguna
inputs = user_input_features()
if st.button('Cek'):

# Rentang normal
normal_ranges = {
    'Age': (18, 60),  # Rentang usia 
    'BMI': (18.5, 24.9),
    'Resting_BPM': (60, 100),
    'Max_BPM': (120, 220),
    'Avg_BPM': (70, 150),
    'Session_Duration': (0.5, 2.0),  # dalam jam
    'Calories_Burned': (200, 800),
    'Fat_Percentage': (10, 30),
    'Water_Intake': (2.0, 3.7),  # liter/hari
    'Workout_Frequency': (3, 6)  # hari/minggu
}

abnormalities = check_abnormalities(inputs, normal_ranges)

# Display user input
st.subheader("User Input:")
st.write(inputs)

# Prediksi
st.subheader("Peringatan Kesehatan:")
if abnormalities:
    for warning in abnormalities:
        st.warning(warning)
else:
    st.success("Kebugaran Tubuh Normal, Pertahankan..!!")

# Prediction using the loaded model
fitness_level = ""
if prediction[0] == 0:
    fitness_level = " Anda Pada Level Beginner,mulailah rutih berolahraga dan menjaga pola makan!"
elif prediction[0] == 1:
    fitness_level = "Anda Pada Level Intermediate dengan memiliki pengalaman olahraga yang cukup, terus pertahankan kebugaran Anda!"
elif prediction[0] == 2:
    fitness_level = "Anda Pada Level Advanced (kebugaran tinggi ) , tetap jaga intensitas latihan!"

# Display the fitness level as a message
st.subheader("Predicted Fitness Level:")
st.write(fitness_level)
