import reflex as rx
from ..models.order_model import ProductType, Order
from ..states.dashboardState import DashboardState
from ..styles.fonts import Font, FontWeight


def dashboardTable(order) -> rx.Component:
    return (
        rx.table.root(
            rx.table.header(
                rx.table.row(
                    rx.table.column_header_cell(
                        "Numero Pedido",
                    ),
                    rx.table.column_header_cell("Producto"),
                    rx.table.column_header_cell("Hora Pedido"),
                    rx.table.column_header_cell("Hora Finalizado"),
                    rx.table.column_header_cell("Total"),
                    rx.table.column_header_cell("Acciones"),
                ),
            ),
            rx.table.body(rx.foreach(order, show_order)),
            width="100%",
            border="1px solid black",
            padding="0.5em",
        ),
    )


def show_product(product: ProductType) -> rx.Component:
    return rx.hstack(
        rx.text(product.quantity),
       # rx.spacer(),
        rx.text(product.name),
        rx.spacer(),
        rx.flex(
            rx.text(f"${product.price}",align="center"),
            
        )
        
    )


def show_order(order: Order) -> rx.Component:
    return rx.table.row(
        rx.table.cell(
            rx.hstack(
                rx.box(
                    order.nro_order,
                    align="center",
                    font_weight=FontWeight.MEDIUM,
                ),
                rx.box(
                    rx.cond(
                        order.observation != "",
                        rx.tooltip(
                            rx.icon("eye"),
                            content=order.observation,
                        ),
                    ),
                ),
            )
        ),
        rx.table.cell(rx.foreach(order.productos, show_product),
                      align="left"),
        rx.table.cell(order.created_at),
        rx.table.cell(order.finish_time),
        rx.table.cell(f"${order.total}"),
        rx.table.cell(
            rx.hstack(
                rx.icon_button("printer",
                               on_click=lambda: DashboardState.test(order)),
                rx.icon_button(
                    "check",
                    color="white",
                    background_color="green",
                    padding="0.5em",
                    border="1px solid black",
                    on_click=lambda: DashboardState.UpdateItem(order.id, "finish_time"),
                ),
                rx.cond(
                    order.finish_time != None,
                    rx.icon_button(
                        "package-check",
                        color="white",
                        background_color="red",
                        padding="0.5em",
                        border="1px solid black",
                        on_click=lambda: DashboardState.UpdateItem(
                            order.id, "pickUp_time"
                        ),
                    ),
                ),
            )
        ),
    )
