from src.utils import get_response
from src.schema import Booking
import streamlit as st
import pandas as pd
import streamlit as st

def run():
    # Set the page configuration to always show the sidebar
    st.set_page_config(
        page_title="My App",
        page_icon="🧊",
        initial_sidebar_state="expanded"
    )
    
    st.title("🍽️ Restaurant Booking Assistant")

    # Initialize memory if not already in session state
    if 'messages' not in st.session_state:
        st.session_state.messages = []

    if 'booking' not in st.session_state:
        st.session_state.booking = Booking()

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

        with st.chat_message("assistant"):
            # Display assistant response in chat message container
            response = st.write_stream(get_response(prompt))

            # Add assistant response to chat history
            st.session_state.messages.append({"role": "assistant", "content": response})

    with st.sidebar:
        st.write("Current bookings:")
        df = pd.read_csv("data/bookings.csv")
        st.write(df)

if __name__ == "__main__":
    run()