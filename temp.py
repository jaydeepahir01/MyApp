# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# load the saved models
diabetes_model = pickle.load(open('/Users/jaydeepahir/Documents/Study/Internship/Intership Trained Classifier Model/diabetes_model.sav','rb'))
heart_diaseases_model = pickle.load(open('/Users/jaydeepahir/Documents/Study/Internship/Intership Trained Classifier Model/heart_model.sav','rb'))
parkinsons_model = pickle.load(open('/Users/jaydeepahir/Documents/Study/Internship/Intership Trained Classifier Model/pakinsons_model.sav','rb'))

# make a sidebar fro navigation 
with st.sidebar:
       selected = option_menu(
        'Multiple Disease Prediction System',
        ['Diabetes Prediction', 'Heart Disease Prediction', 'Parkinsons Prediction'],
        icons=['activity', 'heart', 'person'],
        default_index=0
    )
       
# diabetes prediction page
if selected == 'Diabetes Prediction':
    st.title('Diabetes Prediction using SVM')
    
    # input fields for diabetes prediction
    col1, col2 = st.columns(2)
    
    with col1:
        Pregnancies = st.text_input('Number of Pregnancies')
        Glucose = st.text_input('Glucose Level')
        BloodPressure = st.text_input('Blood Pressure Value')
        SkinThickness = st.text_input('Skin Thickness Value')
        
    with col2:
        Insulin = st.text_input('Insulin Level')
        BMI = st.text_input('BMI Value')
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function Value')
        Age = st.text_input('Age of the Person')

    # prediction button
    if st.button('Diabetes Test Result'):
        input_data = [Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]
        input_data_as_float = [float(i) for i in input_data]
        input_data_reshaped = [input_data_as_float]
        
        prediction = diabetes_model.predict(input_data_reshaped)
        
        if prediction[0] == 0:
            st.success('The person is not diabetic.')
        else:
            st.error('The person is diabetic.')

# heart diaseaes
if selected == 'Heart Disease Prediction':
    st.title('Heart Disease Prediction using SVM')
    
    # input fields for diabetes prediction
    col1, col2,col3= st.columns(3)
    
    with col1:
        age = st.text_input('Enter Age')
        sex = st.text_input('Enter Gender')
        cp = st.text_input('Enter Chest Pain Type (cp)')
        trestbps = st.text_input('Enter Resting Blood Pressure')
        thal = st.text_input('EnterThal')
        
    with col2:
        chol = st.text_input('Enter Cholesterol Level')
        fbs = st.text_input('Enter Fasting Blood Sugar')
        restecg = st.text_input('Resting ECG Results')
        thalach = st.text_input('Maximum Heart Rate Achieved')
    
    with col3:
        exang = st.text_input('Enter Exercise Induced Angina')
        oldpeak = st.text_input('Enter ST Depression Induced by Exercise')
        slope = st.text_input('Enter Slope of the Peak Exercise ST Segment')
        ca = st.text_input('Enter Number of Major Vessels Colored by Fluoroscopy')
        
    # prediction button
    if st.button('Diabetes Test Result'):
        input_data = [age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal]
        input_data_as_float = [float(i) for i in input_data]
        input_data_reshaped = [input_data_as_float]
        input_data_reshaped = heart_diaseases_scaler.transform(input_data_reshaped)
        prediction = heart_diaseases_model.predict(heart_diaseases_scaler.transform(input_data_reshaped))
        if prediction[0] == 0:
            st.success('The person does NOT have a heart disease.')
        else:
            st.error('The person HAS a heart disease.')

# parkinsons prediction page
if selected == 'Parkinsons Prediction':
    st.title('Parkinsons Prediction using SVM')
    
    # input fields for parkinsons prediction
    col1, col2 ,col3 ,col4= st.columns(4)
    with col1:
        fo = st.text_input('MDVP:Fo(Hz)')
        fhi = st.text_input('MDVP:Fhi(Hz)')
        flo = st.text_input('MDVP:Flo(Hz)')
        Jitter_percent = st.text_input('MDVP:Jitter(%)')
    with col2:
        Jitter_Abs = st.text_input('MDVP:Jitter(Abs)')
        RAP = st.text_input('MDVP:RAP')
        PPQ = st.text_input('MDVP:PPQ')
        DDP = st.text_input('Jitter:DDP')
    with col3:
        Shimmer = st.text_input('MDVP:Shimmer')
        Shimmer_dB = st.text_input('MDVP:Shimmer(dB)')
        APQ3 = st.text_input('Shimmer:APQ3')
        HNR = st.text_input('HNR')
    with col4:
        APQ5 = st.text_input('Shimmer:APQ5')
        APQ = st.text_input('MDVP:APQ')
        DDA = st.text_input('Shimmer:DDA')
        NHR = st.text_input('NHR')
    # prediction button
    if st.button('Parkinsons Test Result'):
        input_data = [fo, fhi, flo, Jitter_percent, Jitter_Abs, RAP, PPQ, DDP,
                      Shimmer, Shimmer_dB, APQ3, APQ5, APQ, DDA, NHR, HNR]
        input_data_as_float = [float(i) for i in input_data]
        input_data_reshaped = [input_data_as_float]
        
        prediction = parkinsons_model.predict(input_data_reshaped)
        
        if prediction[0] == 0:
            st.success('The person does not have Parkinsons disease.')
        else:
            st.error('The person has Parkinsons disease.')