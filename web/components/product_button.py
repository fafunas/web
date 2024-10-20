import reflex as rx
from ..states.productState import ProductState

def product_button()-> rx.Component:
    return rx.dialog.root(
        rx.dialog.trigger(
            rx.button(
                rx.icon("plus", size=26),
                rx.text("Agregar Producto",size="4"),
                size="3",
            ),
        ),
        rx.dialog.content(
            rx.hstack(
                rx.badge(
                    rx.icon(tag="package",size = 20),
                    color_scheme="blue",
                    radius="full",
                    padding="0.65rem"
                ),
                rx.vstack(
                    rx.dialog.title(" Agregar Producto")
                )
            ),
            rx.flex(
                rx.form(
                    rx.vstack(
                        rx.hstack(
                            rx.input(
                                placeholder="Producto",
                                name="name",
                                type="text",
                                required=True
                            ),
                            rx.input(
                                placeholder="Precio",
                                name="price",
                                type="number",
                                required=True
                            )
                        ),
                        rx.hstack(
                            rx.dialog.close(
                            rx.button(
                            "Agregar", type="submit",
                        )
                        ),
                        rx.dialog.close(
                            rx.button(
                                "Cancelar",
                                variant="soft",
                                color_scheme="gray",
                            )
                        )
                        )
                        
                        
                    ),
                   on_submit=ProductState.createProduct,  # Esto pasa los datos del formulario a handle_submit
                   #reset_on_submit=False
                )
            )
        )
    )