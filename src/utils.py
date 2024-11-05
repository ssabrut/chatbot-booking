import time
import streamlit as st
from src.config.chain import executor

def get_response(prompt: str):
    """
    Generate a response for the given prompt and display a typing animation while processing.

    Parameters
    ----------
    prompt : str
        The input prompt for which the response is to be generated.

    Yields
    ------
    str
        Words of the generated response, one by one, with a delay between each word.

    Notes
    -----
    This function uses a placeholder to display a typing animation while the response is being generated.
    The typing animation is cleared once the response starts coming in.
    """
    typing_placeholder = st.empty()  # Create a placeholder for the typing message
    typing_placeholder.write("Thinking...")  # Display the typing message
    response = executor.invoke({"input": prompt})
    
    # Clear the typing message once the response starts coming in
    typing_placeholder.empty()
    for word in response["output"].split():
        yield word + " "
        time.sleep(0.05)