from pydantic import Field
from typing import Optional
import reflex as rx
from datetime import datetime

class Product(rx.Base):
    id : Optional[str] = None
    start_time: datetime.now
    end_time: datetime
    status: bool = True