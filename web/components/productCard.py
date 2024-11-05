import reflex as rx
from ..models.product_model import Products


def ProductCard(item:Products)-> rx.Component:
    return rx.card(
    rx.flex(
        rx.form.field(
            rx.flex(
                rx.el.input(type="hidden",name=f"price_{item.id}",value=item.price.to(str)),
                rx.el.input(type="hidden",name=f"name.{item.id}",value=item.name),
                rx.text(item.name, align="center"),
                rx.form.control(
                    rx.input(
                        placeholder="Cantidad",
                        width="40px",
                        type="number", 
                        name=f"quantity_{item.id}",
                        default_value="0",
                        required=True
                    ),
                    as_child=True
                ),
                direction="column",
                align="center",
                justify="center",
                spacing="4",
            ),
            direction="column"
        ),
        direction="column",
        align="center",
        justify="center",
        width="100%"
    ),
    size="4"
)