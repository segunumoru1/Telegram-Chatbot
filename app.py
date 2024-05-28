import nltk
nltk.download('punkt')
from nltk.tokenize import word_tokenize
import streamlit as st
import json
from chatbot import predict_class, get_response


st.title("Telegram Chatbot Demo")

# Load the intents from the intents.json file
with open(r"telegram.json", 'r') as file:
    intents = json.load(file)

def main(intents):
    st.text("Enter your message:")
    message = st.text_input("", "")
    if st.button("Send"):
        intents_list = predict_class(message)
        response = get_response(intents_list, intents_json=intents)  # Pass intents dictionary
        st.text_area("Bot's Response:", response, height=200)

# Call the main function with the loaded intents dictionary
main(intents)