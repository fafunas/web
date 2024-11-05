import reflex as rx
from web.components.sidebar import sidebar
from web.components.product_button import product_button
from ..components.callout import notification
from ..views.table import product_table
from ..states.productState import ProductState



@rx.page(
    title="Dashboard Cervesia",
    description="Productos",
    on_load= ProductState.get_all_products
    
)

def products()-> rx.Component:
    return rx.hstack(
        sidebar(),
        rx.vstack(
            rx.hstack(
                rx.heading("Listado de Productos")
            ),
            product_button(),
            product_table(ProductState.products),
            spacing="5",
        ),
            
    )