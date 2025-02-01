import reflex as rx
from web.components.sidebar import sidebar
from web.components.product_button import product_button
from ..views.table import product_table
from ..states.productState import ProductState
from ..styles.fonts import Font
from ..styles.colors import TextColor
from ..styles.styles import Size



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
                rx.heading("Listado de Productos",
                           color=TextColor.HEADER,
                           font_size=Size.BIG,
                           margin=Size.MEDIUM)
            ),
            rx.hstack(product_button(),
            product_table(ProductState.products),),
            
            spacing="5",
        ),
            
    )