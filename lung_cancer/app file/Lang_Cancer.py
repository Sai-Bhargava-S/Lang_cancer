# -*- coding: utf-8 -*-
"""
Created on Sat Mar  8 23:01:44 2025

@author: Sai Bhargava
"""
import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# Set page configuration
st.set_page_config(page_title="Health Assistant",
                   layout="wide",
                   page_icon="🧑‍⚕️")

# Loading the saved model
try:
    lung_cancer_model = pickle.load(open("C:/Users/Sai Bhargava/Desktop/lung_cancer/saved_files/lung_cancer_model.sav", 'rb'))
except Exception as e:
    st.error(f"Error loading model: {e}")

# Sidebar for navigation
with st.sidebar:
    selected = option_menu('Multiple Disease Prediction System',
                           ['Lung Cancer'],
                           menu_icon='hospital-fill',
                           icons=['lungs'],
                           default_index=0)

if selected == 'Lung Cancer':
    # Page title
    st.title('Lung Cancer Prediction using ML')

    # Getting the input data from the user
    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        Yellow_fingers = st.number_input('Yellow fingers (YES-2, NO-1)', min_value=1, max_value=2, step=1)

    with col2:
        Anxiety = st.number_input('Anxiety (YES-2, NO-1)', min_value=1, max_value=2, step=1)

    with col3:
        PeerPressure = st.number_input('Peer Pressure (YES-2, NO-1)', min_value=1, max_value=2, step=1)

    with col4:
        Chronic_Disease = st.number_input('Chronic Disease (YES-2, NO-1)', min_value=1, max_value=2, step=1)

    with col5:
        Fatigue = st.number_input('Fatigue (YES-2, NO-1)', min_value=1, max_value=2, step=1)

    with col1:
        Allergy = st.number_input('Allergy (YES-2, NO-1)', min_value=1, max_value=2, step=1)

    with col2:
        Wheezing = st.number_input('Wheezing (YES-2, NO-1)', min_value=1, max_value=2, step=1)

    with col3:
        Alcohol_Consuming = st.number_input('Alcohol Consuming (YES-2, NO-1)', min_value=1, max_value=2, step=1)

    with col4:
        Coughing = st.number_input('Coughing (YES-2, NO-1)', min_value=1, max_value=2, step=1)

    with col5:
        Swallowing_difficulty = st.number_input('Swallowing Difficulty (YES-2, NO-1)', min_value=1, max_value=2, step=1)

    with col1:
        Chest_pain = st.number_input('Chest Pain (YES-2, NO-1)', min_value=1, max_value=2, step=1)

    # Code for Prediction
    Lung_Cancer_prediction = None

    # Creating a button for Prediction    
    if st.button("Lung Cancer Test Result"):
        try:
            user_input = [
                Yellow_fingers, Anxiety, PeerPressure, Chronic_Disease, Fatigue,
                Allergy, Wheezing, Alcohol_Consuming, Coughing, Swallowing_difficulty, Chest_pain
            ]

            # Predict using the loaded model
            Lung_Cancer_prediction = lung_cancer_model.predict([user_input])

            if Lung_Cancer_prediction[0] == 0:
                st.success("The person does NOT have lung cancer.")
            else:
                st.error("The person has Lung Cancer.")
        except Exception as e:
            st.error(f"Error during prediction: {e}")
