import reflex as rx
from ..models.product_model import Products


def ProductCard(item:Products)-> rx.Component:
    return rx.card(
        rx.flex(
            rx.form.field(
                rx.flex(
                    #rx.el.input(type="hidden",name=f"id_{item.id}",value=item.id.to(str)),
                    rx.text(item.name),
                    rx.form.control(
                        rx.input(
                            placeholder="Cantidad",
                            width="50px",
                            type="number",
                            name=f"quantity_{item.id}",
                            default_value="0",
                            required=True
                        ),
                        as_child=True
                    ),
                    direction="column",
                    spacing="1"
                )
            ),
            direction="column",
            spacing="3"
        ),
        size="4"
    )