import reflex as rx
from typing import Optional
from datetime import datetime
from bson import ObjectId
from sqlmodel import Field

def get_current_time():
    return datetime.now().replace(second=0, microsecond=0)

class ProductType(rx.Model):
    quantity: int
    price: float 
    name: str

class Order(rx.Model):
    id:Optional[ObjectId] = Field(default=None,alias="_id")
    created_at: datetime =Field(default_factory=get_current_time)
    finish_time: Optional[datetime]=None
    pickUp_time: Optional[datetime]=None
    total: int
    productos: list[ProductType]
    shift_num: Optional[ObjectId]=None
    nro_order: Optional[int] = Field(default=1)
    observation: Optional[str]
    payment: Optional[str]