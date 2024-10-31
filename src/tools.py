from langchain.tools import tool

@tool
def create_booking(
    name: str = "",
    number_of_people: int = 0,
    date: str = "",
    time: str = "",
    special_requests: str = "",
):
    """Create a booking for a restaurant reservation."""
    return f"Booking created for {name} for {number_of_people} people on {date} at {time}. Special requests: {special_requests}."

tools = [create_booking]