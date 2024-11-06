import reflex as rx

class ProductType(rx.Model):
    quantity: int
    price: float 
    name: str

class OrderType(rx.Model):
    id: str
    orders_num: int
    total: float
    shift: int
    created_at: str  # Store datetime as string
    finish_time: str | None
    pickUp_time: str | None
    productos: list[ProductType]