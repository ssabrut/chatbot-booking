from langchain.tools import tool
import streamlit as st

@tool
def set_name(name: str = "") -> str:
    """
    Get the name of the user.

    If the name is not provided, ask for it. Otherwise, store the name in the session state.

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
def set_number_of_people(num_people: int = 0) -> int:
    """
    Get the number of people for the booking.

    If the number is not provided, ask for it. Otherwise, store the number in the session state.

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

    If the date is not provided, ask for it. Otherwise, store the date in the session state.

    Parameters
    ----------
    date : str, optional
        The date for the booking. Default is an empty string.

    Returns
    -------
    str
        The date for the booking.
    """
    st.session_state.booking.date = date
    if date != "":
        return date

@tool
def set_time(time: str = "") -> str:
    """
    Get the time for the booking.

    If the time is not provided, ask for it. Otherwise, store the time in the session state.

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

tools = [set_name, set_number_of_people, set_date, set_time, set_special_requests, create_booking]