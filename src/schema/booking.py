from pydantic import BaseModel

class Booking(BaseModel):
    """
    Booking details for a reservation.

    Attributes
    ----------
    name : str
        The name of the person making the booking.
    num_people : int
        The number of people included in the booking.
    date : str
        The date of the booking.
    time : str
        The time of the booking.
    special_requests : str
        Any special requests or notes for the booking.
    """
    name: str = ""
    num_people: int = 0
    date: str = ""
    time: str = ""
    special_requests: str = ""