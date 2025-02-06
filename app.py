import streamlit as st
import nltk
from transformers import pipeline
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize


# Download necessary NLTK data
nltk.download('punkt')
nltk.download('stopwords')


chatbot = pipeline("text-generation", model="distilgpt2")

def healthcare_chatbot(user_input):
    if "symptom" in user_input:
        return "PLease consult Doctor for accurate advice"
    elif "appointment" in user_input:
        return "Would you like to schedule an appointment with Doctor? "
    elif "medication" in user_input:
        return "Prescribed medicines by a Doctor.."
    else:
        response = chatbot(user_input,max_length = 500,num_return_sequences=1)
        return response[0]['generated_text']  # output: array 0 index generated_text


def main():
    st.title("Healthcare Assistant Chatbot")
    user_input = st.text_input("How can I assist you today?")
    if st.button("submit"):
        if user_input:
            st.write("User :",user_input)
            with st.spinner("Processing your query, Please wait...."):
                    response=healthcare_chatbot(user_input)
            st.write("Healthcare Assistant : ",response)
        else:
            st.write("Please enter a message to get a response")


if __name__=="__main__":
    main()