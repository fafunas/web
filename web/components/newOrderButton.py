import reflex as rx
from ..states.dashboardState import DashboardState
from ..models.product_model import Products
from ..components.productCard import ProductCard



def orderProduct(list_product)-> rx.Component:
    return rx.dialog.root(
    rx.dialog.trigger(rx.button("Nuevo Pedido")),
    rx.dialog.content(
        rx.dialog.title("Nuevo Pedido"),
        rx.dialog.description(
            "Complete los detalles del pedido",
            margin="2em"
        ),
        rx.form(
            rx.hstack(
                rx.foreach(
                    list_product,ProductCard
                )
            ),
            rx.hstack(
                 rx.flex(
                    rx.dialog.close(
                        rx.button(
                            "Cancelar",
                            color_scheme="gray",
                            variant="soft",
                        ),
                    ),
                    rx.dialog.close(
                        rx.button("Enviar", type="submit"),
                    ),
                    spacing="3",
                    margin_top="16px",
                    justify="end",
                ),
            ),
           # on_submit=lambda order: OrderDetailDialog(order),
            reset_on_submit=True,
            
        ),
    ),
   
)
