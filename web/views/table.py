import reflex as rx
from ..models.product_model import Products
from ..states.productState import ProductState



def product_table(list_product: list[Products]) -> rx.Component:
    return rx.table.root(
        rx.table.header(
            rx.table.row(
                rx.table.column_header_cell("Productos"),
                rx.table.column_header_cell("Precio"),
                rx.table.column_header_cell("Accion")
            )
        ),
        rx.table.body(
            rx.foreach(list_product, row_table),
           )
    )


def row_table(product:Products)-> rx.Component:
    return rx.table.row(
        rx.table.cell(product.name),
        rx.table.cell(f"$ {product.price}"),
        rx.table.cell(rx.hstack(
            dialogUpdate(product),
            dialogDelete(product),
            
        ))
    )


def dialogDelete(item)-> rx.Component:
    return rx.dialog.root(
        rx.dialog.trigger(
            rx.button(
                rx.icon("trash",size=20),
                rx.text("Eliminar")
            )
        ),
        rx.dialog.content(
            rx.dialog.title(
                rx.heading(
                    "¿Esta seguro que desea eliminar el producto?"
                )
            ),
            rx.dialog.description(
                item.name
            ),
            rx.flex(
                rx.dialog.close(
                    rx.button(
                        "Cancel",
                        variant="soft",
                        color_scheme="gray",
                        ),
                    ),
                rx.dialog.close(
                    rx.button(
                        "Eliminar",
                        type="submit",
                        on_click= lambda: ProductState.deleteProduct(item),
                        ),
                    ),
                spacing="3",
                justify="end",
                ),
            )
        )
    
def dialogUpdate(item)-> rx.Component:
    return rx.dialog.root(
        rx.dialog.trigger(
            rx.button(
                rx.icon("pencil",size=20),
                rx.text("Editar")
            ),
        ),
        rx.dialog.content(
            rx.dialog.title("Editar Producto"),
            rx.flex(
                rx.form.root(
                    rx.text(
                "Descipcion",
                as_="div",
                size="2",
                margin_bottom="4px",
                weight="bold",
            ),
                    rx.el.input(type="hidden",name="id",value=item["id"].to(str)),
                    rx.input(
                        default_value=item.name,
                        name="name",
                        disabled=True
                    ),
                    rx.text(
                "Precio",
                as_="div",
                size="2",
                margin_bottom="4px",
                weight="bold",
                
            ),
            rx.input(
               default_value=item.price.to(str),
               name="price",
               type="number"
            ),
            rx.flex(
                rx.dialog.close(
                    rx.button(
                        "Cancel",
                        variant="soft",
                        color_scheme="gray",
                        ),
                    ),
                rx.dialog.close(
                    rx.button(
                        "Actualizar",
                        type="submit",
                        ),
                    ),
                spacing="3",
                justify="end",
                ),
            on_submit=ProductState.updateProduct,
            direction="column",
            spacing="3",
                )
            
        ),
            
        )
        
    )
    