import reflex as rx
from typing import Optional
from datetime import datetime
from bson import ObjectId
from sqlmodel import Field

def get_current_time():
    return datetime.now().replace(second=0, microsecond=0)

class Shift(rx.Model):
    id: Optional[ObjectId] = Field(default=None, alias="_id")
    shift_num: Optional[int] = None
    start_time: datetime = Field(default_factory=get_current_time)
    end_time: Optional[datetime] = None
    status: bool = True
    orders: int= Field(default=1)

