import time
import streamlit as st
from src.config.chain import chain

def get_response(prompt: str):
    response = chain.predict(input=prompt)
    for word in response.split():
        yield word + " "
        time.sleep(0.05)

def run():
    st.title("🍽️ Restaurant Booking Assistant")

    # Initialize memory if not already in session state
    if 'messages' not in st.session_state:
        st.session_state.messages = []

    # Display chat messages from history on app rerun
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    if prompt := st.chat_input("Enter your message:"):
        # Display user message in chat message container
        with st.chat_message("user"):
            st.markdown(prompt)
            
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": prompt})

        # Display assistant response in chat message container
        with st.chat_message("assistant"):
            response = st.write_stream(get_response(prompt))

        # Add assistant response to chat history
        st.session_state.messages.append({"role": "assistant", "content": response})

if __name__ == "__main__":
    run()