import reflex as rx
from ..models.dashboardModel import ProductType, OrderType
from ..states.dashboardState import DashboardState
from ..styles.fonts import Font,FontWeight


def dashboardTable(order)->rx.Component:
    return rx.table.root(
    rx.table.header(
        rx.table.row(
            rx.table.column_header_cell("Numero Pedido",),
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
    border="1px solid black",
    padding="0.5em",
    
),
    
    
    
def show_product(product: ProductType)->rx.Component:
    return rx.hstack(
        rx.text(product.quantity),
        rx.spacer(),
        rx.text(product.name),
        rx.spacer(),
        rx.text(f"${product.price}"))


def show_order(order: OrderType)-> rx.Component:
    return rx.table.row(
        rx.table.cell(order.orders_num,
                      align="center",
                      font_weight=FontWeight.MEDIUM,),
        rx.table.cell(
            rx.foreach(order.productos, show_product)
        ),
        rx.table.cell(order.created_at),
        rx.table.cell(order.finish_time),
        rx.table.cell(f"${order.total}"),
        rx.table.cell(
            rx.hstack(
                rx.icon_button("check",
                               color="green",
                               background_color="white",
                               padding="0.5em",
                               border="1px solid black",
                               on_click=lambda: DashboardState.UpdateItem(order.id,"finish_time"),
                               ),
                rx.cond(order.finish_time!= None,
                        rx.icon_button("package-check",
                                       color="red",
                                       background_color="white",
                                       padding="0.5em",
                                       border="1px solid black",
                               on_click=lambda: DashboardState.UpdateItem(order.id, "pickUp_time")),
                        )
                
                
        )
        ),
       
    )