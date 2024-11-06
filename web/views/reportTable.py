import reflex as rx
from ..components.searchDates import SearchDate
from reflex_ag_grid import ag_grid




def reportTable(items)-> rx.Component:
    return rx.vstack(
        SearchDate(),
        rx.hstack(
            ag_grid_simple(items),
            width="100%"
        ),
        width="100%"
        
    )
    
    
    
def ag_grid_simple(data):
    return ag_grid(
        id="ag_grid_basic_1",
        row_data=data,
        column_defs=column_defs,
        width="100%",
        height="60vh"
        
    )
    
column_defs = [
    ag_grid.column_def(field="created_at", header_name="Fecha"),
    ag_grid.column_def(field="shift", header_name="Turno"),
    ag_grid.column_def(field="order", header_name="N° Orden"),
    ag_grid.column_def(field="name", header_name="Producto"),
    ag_grid.column_def(field="quantity", header_name="Cantidad"),
    ag_grid.column_def(field="price", header_name="P. Unitario"),
    ag_grid.column_def(field="total", header_name="Total"),
]
