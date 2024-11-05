from sqlmodel import Field
import reflex as rx
from typing import Optional
from bson import ObjectId

class Products(rx.Base):
    id: Optional[ObjectId] = Field(default=None)
    name : str 
    price : int 
    status : bool = Field(default=True)