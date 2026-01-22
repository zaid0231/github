import streamlit as st
import numpy as np
import pandas as pd
from joblib import load

#page setup
st.set_page_config(
    page_title="Spam detection App",page_icon='📧', layout="wide")



# load the model
@st.cache_resource
def load_model():
    model_data = load('spam_detector.joblib')
    return model_data['model'], model_data['vectorizer']



# try is used to handle any potential errors during model loading
try:
     model,vectorizer = load_model() # load model and vectorizer

     # main UI 
     st.title("Spam Detection System")
     st.write(" Enter a message to classify it as Spam or Not Spam.")

     # input text area
     message = st.text_area("Message Input", height=100)         # Input area for user to enter message
     if st.button("Check Message", type='primary'): 
         if message:
            # preprocess and predict
            message = message.lower() # convert to lowercase
            message_vectorized = vectorizer.transform([message]) # vectorize the input message
            prediction = model.predict(message_vectorized) # get prediction
            probability = model.predict_proba(message_vectorized) # get prediction probabilities
            

            # display results

            st.write("----")
            col1, col2 = st.columns(2) # create two columns for better layout
            with col1: 
                if prediction[0] == "Spam":
                    st.error("The message is classified as: SPAM")  # st.error show error message in red box
                else:
                    st.success("The message is classified as: NOT SPAM") # st.success show success message in green box

            with col2:
                spam_prob = probability[0][1] if model.classes_[1] == "Spam" else probability[0][0]
                st.metric("Spam Probability", f"{spam_prob*100:.2f}%") # display spam probability as metric
            
            #show confidence bar
            st.write("Confidence score:")
            st.progress(spam_prob, text = "spam")
            st.progress(1 - spam_prob, text = "Ham")

         else:
            st.warning("Please enter a message to classify.") # st.warning show warning message in yellow box
            
            # example messages
            st.write("" \
            "**Example Messages:**\n" \
            "1. Congratulations! You've won a $1,000 Walmart gift card.\n" \
            "2. Important update regarding your account.\n" \
            "3. Get paid to work from home!\n")

except Exception as e:
    st.error(f"""Error loading model: {e}"
             please ensure :
                1. The 'spam_detector.joblib' file is in the correct directory.
                2.  The saved file contains both the model and the vectorizer.body
                3. All required package installed   
            """ )
    
    