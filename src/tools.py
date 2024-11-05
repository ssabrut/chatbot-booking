import streamlit as st
import dateparser
from rapidfuzz import fuzz, process
from langchain.tools import tool

@tool
def set_name(name: str = "") -> str:
    """
    Get the name of the user.

    If the name is not provided, ask for it until provided. Otherwise, store the name in the session state.

    Parameters
    ----------
    name : str, optional
        The name of the user. Default is an empty string.

    Returns
    -------
    str
        The name of the user.
    """
    st.session_state.booking.name = name
    if name != "":
        return name

@tool
def set_email(email: str = "") -> str:
    """
    Get the email of the user.

    If the email is not provided, ask for it until provided. Otherwise, store the email in the session state.

    Parameters
    ----------
    email : str, optional
        The email of the user. Default is an empty string.

    Returns
    -------
    str
        The email of the user.
    """
    st.session_state.booking.email = email
    if email != "":
        return email

@tool
def set_phone_number(phone_number: str = "") -> str:
    """
    Get the phone number of the user.

    If the phone number is not provided, ask for it until provided. Otherwise, store the phone number in the session state.

    Parameters
    ----------
    phone_number : str, optional
        The phone number of the user. Default is an empty string.

    Returns
    -------
    str
        The phone number of the user.
    """
    st.session_state.booking.phone_number = phone_number
    if phone_number != "":
        return phone_number

@tool
def set_number_of_people(num_people: int = 0) -> int:
    """
    Get the number of people for the booking.

    If the number is not provided, ask for it until provided. Otherwise, store the number in the session state.

    Parameters
    ----------
    num_people : int, optional
        The number of people for the booking. Default is 0.

    Returns
    -------
    int
        The number of people for the booking.
    """
    st.session_state.booking.num_people = num_people
    if num_people != 0:
        return num_people

@tool
def set_date(date: str = "") -> str:
    """
    Get the date for the booking.

    If the date is not provided, ask for it until provided. Otherwise, store the date in the session state.

    Parameters
    ----------
    date : str, optional
        The date for the booking. Default is an empty string.

    Returns
    -------
    str
        The date for the booking.
    """
    def format_relative_day(relative_day: str) -> str:
        """
        Parse a relative day expression and return an absolute date string.

        Parameters
        ----------
        relative_day : str
            The relative day expression to parse (e.g., 'tomorrow', 'next week').

        Returns
        -------
        str
            The absolute date in 'YYYY-MM-DD' format.

        Raises
        ------
        ValueError
            If unable to parse the input `relative_day`.

        Notes
        -----
        This function uses fuzzy matching to interpret `relative_day` and converts it into an absolute date.
        """
        reference_keywords = [
            "today", "tomorrow", "yesterday",
            "in", "next", "last", "ago", "before", "after",
            "the day after tomorrow", "the day before yesterday",
            "monday", "tuesday", "wednesday", "thursday",
            "friday", "saturday", "sunday", "week", "weeks",
            "month", "months"
        ]
        normalized_day = relative_day.strip().lower()
        best_match, score, _ = process.extractOne(normalized_day, reference_keywords, scorer=fuzz.WRatio)
        MATCH_THRESHOLD = 60

        if score < MATCH_THRESHOLD:
            raise f"Low confidence in interpreting '{relative_day}'. Attempting to parse directly."

        parsed_date = dateparser.parse(best_match)
        if parsed_date:
            return parsed_date.strftime('%Y-%m-%d')
        else:
            raise ValueError(f"Unable to parse the input: '{relative_day}'.")
    date = format_relative_day(date)
    st.session_state.booking.date = date
    if date != "":
        return date

@tool
def set_time(time: str = "") -> str:
    """
    Get the time for the booking.

    If the time is not provided, ask for it until provided. Otherwise, store the time in the session state in 24 hours format.

    Parameters
    ----------
    time : str, optional
        The time for the booking. Default is an empty string.

    Returns
    -------
    str
        The time for the booking.
    """
    st.session_state.booking.time = time
    if time != "":
        return time

@tool
def set_special_requests(special_requests: str = "") -> str:
    """
    Get the special requests for the booking.

    If the special requests are not provided, ask for them. Otherwise, store them in the session state.

    Parameters
    ----------
    special_requests : str, optional
        Special requests for the booking. Default is an empty string.

    Returns
    -------
    str
        The special requests for the booking.
    """
    st.session_state.booking.special_requests = special_requests
    if special_requests != "":
        return special_requests

@tool
def create_booking() -> str:
    """
    Create a booking for a restaurant reservation with complete details.

    Returns
    -------
    str
        Confirmation message indicating the booking was created.
    """
    print(st.session_state.booking)
    return "Booking created!"