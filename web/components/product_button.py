import reflex as rx
from ..states.productState import ProductState


def product_button() -> rx.Component:
    return rx.dialog.root(
        rx.dialog.trigger(
            rx.button(
                rx.icon("plus", size=26),
                rx.text("Agregar Producto", size="4"),
                size="3",
            ),
        ),
        rx.dialog.content(
            rx.dialog.title("Agregar Producto"),
            rx.dialog.description("Agregar un nuevo producto a la lista"),
            # rx.hstack(
            #     rx.badge(
            #         rx.icon(tag="package", size=20),
            #         color_scheme="blue",
            #         radius="full",
            #         padding="0.65rem",
            #     ),
            #     rx.vstack(rx.dialog.title(" Agregar Producto")),
            # ),
            rx.form(
                rx.flex(
                    rx.vstack(
                        rx.input(placeholder="Producto", name="name", required=True),
                        rx.input(placeholder="Precio", name="price", required=True),
                        rx.flex(
                            rx.dialog.close(
                                rx.button("Cancel", variant="soft", color_scheme="gray")
                            ),
                            rx.dialog.close(rx.button("Agregar", type="submit")),
                            spacing="3",
                            justify="end",
                        ),
                    ),
                    
                ),
                on_submit=ProductState.createProduct,
                reset_on_submit=False,
            ),
        ),
    )
