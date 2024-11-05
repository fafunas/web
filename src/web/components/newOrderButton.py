import reflex as rx
from ..states.dashboardState import DashboardState
from ..models.product_model import Products
from ..models.order_model import Order
from ..components.productCard import ProductCard



def orderProduct(list_product)-> rx.Component:
    return rx.form(
            rx.grid(
                rx.foreach(
                    list_product,ProductCard
                ),
                columns="4",
                spacing="3",
                width="100%"
            ),
            rx.hstack(
                 rx.flex(
                    rx.button("Enviar", type="submit"),
                    spacing="3",
                    margin_top="16px",
                    justify="end",
                ),
            ),
            orderForm(),
            on_submit=DashboardState.handle_submit,
            reset_on_submit=True,
        ),



def orderForm() -> rx.Component:
    return rx.dialog.root(
        rx.dialog.content(
            rx.dialog.title("Resumen de Orden"),
            rx.dialog.description(
                "Favor de confirmar la order",
                size="2",
            ),
            rx.table.root(
                rx.table.header(
                    rx.table.row(
                        rx.table.column_header_cell("Item"),
                        rx.table.column_header_cell("Cantidad"),
                    )
                ),
                rx.table.body(
                    rx.foreach(
                        DashboardState.productconfirm,
                        lambda x: rx.table.row(
                            rx.table.cell(rx.text(x["name"])),
                            rx.table.cell(rx.text(x["quantity"])),
                        )
                    )
                )
            ),
            rx.text(
                DashboardState.order_data.total),
            
            rx.flex(
                rx.dialog.close(
                    rx.button(
                        "Cancel",
                        variant="soft",
                        color_scheme="gray",
                        on_click=DashboardState.closeDialog
                    ),
                ),
                rx.dialog.close(
                    rx.button("Agregar"),
                    on_click=DashboardState.createOrder
                ),
                spacing="3",
                margin_top="16px",
                justify="end",
            ),
        ),
        open=DashboardState.openedDialog,
    )
    
    
    
def row_table(item)-> rx.Component:
    return rx.table.row(
        rx.table.cell(item.name),
        rx.table.cell(item.price),
       )
    