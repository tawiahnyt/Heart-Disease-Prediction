# -*- coding: utf-8 -*-
"""
Created on Fri Dec 20 14:43:12 2024

@author: Eunice
"""

import numpy as np
import pickle
import streamlit as st

# Loading the saved model
loaded_model = pickle.load(open('models/heart_disease_model.sav', 'rb'))

# Function to make the prediction
def heart_prediction(input_data):
    input_data_as_numpy_array = np.asarray(input_data)
    reshaped_input_data = input_data_as_numpy_array.reshape(1, -1)

    prediction = loaded_model.predict(reshaped_input_data)

    print(prediction)

    if prediction[0] == 0:
        return 'The person does not have heart disease'
    else:
        return 'The person has heart disease'


# Main function for Streamlit app
def main():
    # Display title
    st.title('Heart Disease Prediction Input Form')

    # Descriptive text for each input
    st.write("Please enter the values for the following attributes:")

    # 1. Age: Numeric input
    age = st.number_input("Age (in years)", min_value=1, max_value=120, step=1)

    # 2. Sex: Binary input (1 for Female, 0 for Male)
    sex = st.radio("Sex", options=[1, 0], format_func=lambda x: "Male" if x == 0 else "Female")

    # 3. Chest Pain Type: Dropdown (Nominal with values 1-4)
    chest_pain_type = st.selectbox("Chest Pain Type", options=[1, 2, 3, 4], format_func=lambda x: {
        1: "Typical angina",
        2: "Atypical angina",
        3: "Non-anginal pain",
        4: "Asymptomatic"
    }[x])

    # 4. Resting Blood Pressure: Numeric input (mm Hg)
    resting_bp_s = st.number_input("Resting Blood Pressure (in mm Hg)", min_value=50, max_value=200, step=1)

    # 5. Serum Cholesterol: Numeric input (mg/dl)
    cholesterol = st.number_input("Serum Cholesterol (in mg/dl)", min_value=100, max_value=500, step=1)

    # 6. Fasting Blood Sugar: Binary input (1 for >120 mg/dl, 0 for <=120 mg/dl)
    fasting_blood_sugar = st.radio("Fasting Blood Sugar", options=[0, 1], format_func=lambda x: "> 120 mg/dl" if x == 1 else "<= 120 mg/dl")

    # 7. Resting ECG: Dropdown (Nominal with values 0, 1, 2)
    resting_ecg = st.selectbox("Resting Electrocardiogram Results: ", options=[0, 1, 2], format_func=lambda x: {
        0: "Normal",
        1: "ST-T wave abnormality",
        2: "Ventricular hypertrophy"
    }[x])

    # 8. Maximum Heart Rate Achieved: Numeric input (71-202 bpm)
    max_heart_rate = st.number_input("Maximum Heart Rate Achieved (bpm)", min_value=71, max_value=202, step=1)

    # 9. Exercise Induced Angina: Binary input (0 for No, 1 for Yes)
    exercise_angina = st.radio("Exercise Induced Angina", options=[0, 1], format_func=lambda x: "No" if x == 0 else "Yes")

    # 10. Oldpeak: Numeric input (Depression of ST segment)
    oldpeak = st.number_input("Oldpeak (ST Depression)", min_value=-10.0, max_value=10.0, step=0.1)

    # 11. ST Slope: Dropdown (Nominal with values 0, 1, 2)
    ST_slope = st.selectbox("Slope of the Peak Exercise ST Segment", options=[0, 1, 2], format_func=lambda x: {
        0: "Upsloping",
        1: "Flat",
        2: "Downsloping"
    }[x])

    # Code for Prediction
    diagnosis = ''

    # Button to trigger prediction
    if st.button('Predict'):
        diagnosis = heart_prediction([age, sex, chest_pain_type, resting_bp_s, cholesterol, fasting_blood_sugar,
                                        resting_ecg, max_heart_rate, exercise_angina, oldpeak, ST_slope])

    # Display the result
    st.success(diagnosis)


if __name__ == '__main__':
    main()
