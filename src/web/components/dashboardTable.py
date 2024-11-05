import reflex as rx
from ..models.dashboardModel import ProductType, OrderType
from ..states.dashboardState import DashboardState


def dashboardTable(order)->rx.Component:
    return rx.table.root(
    rx.table.header(
        rx.table.row(
            rx.table.column_header_cell("Numero Pedido"),
            rx.table.column_header_cell("Producto"),
            rx.table.column_header_cell("Hora Pedido"),
            rx.table.column_header_cell("Hora Finalizado"),
            rx.table.column_header_cell("Total"),
            rx.table.column_header_cell("Acciones"),
        ),
    ),
    rx.table.body(
            rx.foreach(order, show_order)
        ),
    width="100%",
),
    
    
    
def show_product(product: ProductType)->rx.Component:
    return rx.hstack(
        rx.text(product.name),
        rx.text(product.quantity),
        rx.text(product.price))


def show_order(order: OrderType)-> rx.Component:
    return rx.table.row(
        rx.table.cell(order.orders_num),
        rx.table.cell(
            rx.foreach(order.productos, show_product)
        ),
        rx.table.cell(order.created_at),
        rx.table.cell(order.finish_time),
        rx.table.cell(order.total),
        rx.table.cell(
            rx.hstack(
                rx.icon_button("check",color="green",background_color="white",
                               on_click=lambda: DashboardState.UpdateItem(order.id,"finish_time"),
                               ),
                rx.cond(order.finish_time!= None,
                        rx.icon_button("package-check",color="red",background_color="white",
                               on_click=lambda: DashboardState.UpdateItem(order.id, "pickUp_time")),
                        )
                
                
        )
        )
    )