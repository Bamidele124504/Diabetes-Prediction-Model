# -*- coding: utf-8 -*-
"""
Created on Tue Sep 26 13:07:12 2023

@author: KANKE LCDO
"""
import numpy as np
import pickle
import streamlit as st

#loading the saved model
loaded_model=pickle.load(open('trained_model.sav','rb'))

#creating A function for prediction
def diabetes_prediction(input_data):
    
    #change the input to numpy array
    data=np.array(input_data)
    
    #reshape the numpy array because we are predicting for just one instance or data point
    input_data_reshaped=data.reshape(1, -1)
    
    prediction=loaded_model.predict (input_data_reshaped)
    print(prediction)
    
    if (prediction [0]==0):
        return 'this person is Not Diabetic'
    else :
        return 'this person is Diabetic.see A Doctor'
    #this now is for the web page
def main():
    #given A Title
    st.title('Diabetes prediction web App')
    
    #getting inputs from the user
    
    Pregnancies = st.text_input('Number of Pregnancies')
    Glucose = st.text_input('Glucose level')
    BloodPressure = st.text_input('Blood Pressure Value')
    SkinThickness= st.text_input('Skin Thickness Value')
    Insulin = st.text_input('Insulin Level')
    BMI = st.text_input('Body Mass Index Level')
    DiabetesPedigreeFunction = st.text_input('Diabetes pedigree Function Value')
    Age = st.text_input('age of the person')
    
    #code for prediction
    diagnosis = ''
    
    #creating A function for prediction
    
    if st.button('Diabets Test Result'):
        dignosis = diabetes_prediction([Pregnancies,Glucose,BloodPressure,SkinThickness,
                                      Insulin,BMI,DiabetesPedigreeFunction,Age])
        
    st.success(diagnosis)
     
     
if __name__=='__main__':
         main()
         
