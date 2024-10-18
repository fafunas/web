import reflex as rx
from typing import Optional

class Products(rx.Model, table=True):
    name : str 
    price : int 
    status : bool 