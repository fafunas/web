import reflex as rx
from web.components.card import card
from ..components.newOrderButton import orderProduct, orderForm
from ..components.dashboardTable import dashboardTable
from ..states.dashboardState import DashboardState
from ..models.product_model import Products




def dashboard(products:Products)-> rx.Component:
    return rx.vstack(
        rx.hstack(
            rx.button("Cerrar Turno",
                      on_click=DashboardState.closeShift
                      ),
            width="100%",
            justify="end"
            ),
            # Contenedor para los cards
            rx.hstack(
                card("loader", "En Preparacion", "yellow",rx.cond(DashboardState.statusCards["active"],DashboardState.statusCards["active"],0)),
                card("package", "Listo para retirar", "lightblue",rx.cond(DashboardState.statusCards["ready"], DashboardState.statusCards["ready"],0)),
                card("check", "Completadas", "#2A7E3B",rx.cond(DashboardState.statusCards["total"],DashboardState.statusCards["total"],0)),
                spacing="1",
                align="center",  
                justify="between",
                width="100%"
            ),
            rx.flex(
                rx.box(
                    orderProduct(products),
                    #orderForm(),
                    width="33%",
                    ),
                rx.box(
                    dashboardTable(DashboardState.orderTable),
                    width="67%",
                    ),
                width="100%",
                spacing="2",
            ),
            # Ajustes de margenes y alineación de los elementos en vertical
            spacing="2",
            align="start",
            width="100%",
            padding="2em"
        ),