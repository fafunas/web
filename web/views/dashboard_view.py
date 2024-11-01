import reflex as rx
from web.components.card import card
from ..components.newOrderButton import orderProduct, orderForm
from ..components.dashboardTable import dashboardTable
from ..states.dashboardState import DashboardState
#from ..states.productState import ProductState
from ..models.product_model import Products




def dashboard(products:Products)-> rx.Component:
    return rx.vstack(
        rx.hstack(
            rx.button("Cerrar Turno",
                      on_click=DashboardState.getallOrders()),
            width="100%",
            justify="end"
            ),
            # Contenedor para los cards
            rx.hstack(
                card("loader", "En Preparacion", "yellow"),
                card("package", "Listo para retirar", "lightblue"),
                card("check", "Completadas", "green"),
                spacing="2em",
                justify="space-between",
                width="100%"
            ),
            rx.flex(
                rx.box(
                    orderProduct(products),
                    #orderForm(),
                    width="33%",
                    ),
                rx.box(
                    dashboardTable(),
                    width="67%",
                    ),
                width="100%",
                spacing="2",
            ),
            # Ajustes de margenes y alineación de los elementos en vertical
            spacing="2em",
            align="start",
            width="100%",
            padding="2em"
        ),