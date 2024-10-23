from pydantic import Field
from typing import Optional
import reflex as rx

class Product(rx.Base):
    id : Optional[str] = None
    start: str
    end: str