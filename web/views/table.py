import reflex as rx
from ..models.product_model import Products


def product_table(list_product: list[Products]) -> rx.Component:
    return rx.table.root(
        rx.table.header(
            rx.table.row(
                rx.table.column_header_cell("Producto"),
                rx.table.column_header_cell("Precio"),
                rx.table.column_header_cell("Accion")
            )
        ),
        rx.table.body(
            rx.foreach(list_product, row_table)
        )
    )
    
def row_table(product:Products)-> rx.Component:
    return rx.table.row(
        rx.table.cell(product.name),
        rx.table.cell(product.price),
        rx.table.cell(rx.hstack(
            rx.button("Eliminar"),
            rx.button("Editar")
        ))
    )
