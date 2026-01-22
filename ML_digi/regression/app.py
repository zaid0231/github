import streamlit as st
import numpy as np
import pandas as pd
from joblib import load

st.set_page_config(
    page_title="Blood Donation Prediction",page_icon='🩸', layout="wide")

# load the model

@st.cache_resource
def load_model():
    return load('blood_donation_model.joblib')
model=load_model()



# sidebar

with st.sidebar:
    st.title("Blood Donation Prediction System")
    page=st.radio('go to',['Prediction','About'])

if page == "Prediction":
    # Main Content
    st.title("Blood Donation Prediction System")
    st.write("------")

    #create two columnsn
    col1,col2= st.columns(2)

    with col1:
        st.subheader("Enter Donor Information")
        recency = st.slider("month since ladt donation",0,100,5)
        frequency = st.slider("Total Numbers Of Donations",0,50,1)
        monetory = st.slider("Total Blood Donated(c.c)",0,5000,150)
        time = st.slider("Months since first donation",0,200,10)

    with col2 :
        st.subheader("Current Values ")
        metrics_col1, metrics_col2 = st.columns(2)
        with metrics_col1:
            st.metric("Recency",f"{recency} months" )
            st.metric("frequency",f"{frequency} times")
        with metrics_col2:
            st.metric("Blood Volume",f"{monetory}c.c")
            st.metric("Time",f"{time} months")


    # prediction logic

    st.write("---")
    if st.button('predict Donation',type= 'primary'):
        with st.spinner("Processing . . ."):
            input_data= pd.DataFrame({
                'Recency':[recency],
                'Frequency': [frequency],
                'Monetary' : [monetory],
                'Time': [time]
            })

            prediction = model.predict(input_data)



            #Display results

            if prediction[0]==1:
                st.success('Likely to donate!')
            else:
                st.error("Unlikely to donate")