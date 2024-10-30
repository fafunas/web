import reflex as rx
from typing import Optional
from datetime import datetime
from bson import ObjectId
from sqlmodel import Field

def get_current_time():
    return datetime.now().replace(second=0, microsecond=0)

class Order(rx.Model):
    id:Optional[ObjectId] = Field(default=None,alias="_id")
    created_at: datetime =Field(default_factory=get_current_time)
    finish_time: Optional[datetime]=None
    total: int
    items : list