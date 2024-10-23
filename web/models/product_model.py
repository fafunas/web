from pydantic import BaseModel, Field
import reflex as rx

class Products(rx.Base):
    name : str 
    price : int 
    status : bool = Field(default=True)