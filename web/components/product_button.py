import reflex as rx
from ..states.productState import ProductState


def product_button() -> rx.Component:
    return rx.form(
                rx.flex(
                    rx.vstack(
                        rx.input(placeholder="Producto", name="name", required=True),
                        rx.input(placeholder="Precio", name="price", required=True),
                        rx.flex(
                           
                            rx.button("Agregar", type="submit"),
                            spacing="3",
                            justify="end",
                        ),
                    ),
                    
                ),
                on_submit=ProductState.createProduct,
                reset_on_submit=False,
            ),
