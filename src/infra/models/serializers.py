
from pydantic import BaseModel

from datetime import date



class Newspapper(BaseModel):
    """model for newspapper"""
    header: str
    content: str
    img: str
    date_publish: date
    id: int

class Emails(BaseModel):
    """model for emails"""
    id: int
    email: str