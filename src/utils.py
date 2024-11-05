import time
import dateparser
import streamlit as st
from src.config.chain import executor
from rapidfuzz import fuzz, process

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

def format_relative_day(relative_day: str) -> str:
    reference_keywords = [
        "today", "tomorrow", "yesterday",
        "in", "next", "last", "ago", "before", "after",
        "the day after tomorrow", "the day before yesterday",
        "monday", "tuesday", "wednesday", "thursday",
        "friday", "saturday", "sunday", "week", "weeks",
        "month", "months"
    ]
    normalized_day = relative_day.strip().lower()
    best_match, score, _ = process.extractOne(normalized_day, reference_keywords, scorer=fuzz.WRatio) # best_match, score, index
    MATCH_THRESHOLD = 60

    if score < MATCH_THRESHOLD:
        raise f"Low confidence in interpreting '{relative_day}'. Attempting to parse directly."

    parsed_date = dateparser.parse(best_match)

    print(f"{best_match}: {parsed_date}")

    if parsed_date:
        return parsed_date.strftime('%Y-%m-%d')
    else:
        raise ValueError(f"Unable to parse the input: '{relative_day}'.")