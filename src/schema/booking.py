from pydantic import BaseModel

class Booking(BaseModel):
    name: str = ""
    num_people: int = 0
    date: str = ""
    time: str = ""
    special_requests: str = ""