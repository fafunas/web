import reflex as rx
from typing import Optional
from sqlmodel import Field

class Products(rx.Model, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name : str 
    price : int 
    status : bool 