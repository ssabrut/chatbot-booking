import streamlit as st
from src.config.chain import chain

def run():
    st.title("Chatbot Booking")
    user_input = st.text_input("Enter your message:", key="input")
    
    if user_input:
        print(chain.predict(input=user_input))

if __name__ == "__main__":
    run()