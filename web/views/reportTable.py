import reflex as rx
from reflex_ag_grid import ag_grid



column_defs = [
    ag_grid.column_def(field="orders_num"),
    ag_grid.column_def(field="total"),
    ag_grid.column_def(field="shift"),
    ag_grid.column_def(field="created_at"),
    ag_grid.column_def(field="finish_time"), 
    ag_grid.column_def(field="pickUp_time")
]

def agGridTable(data):
    return ag_grid(
        id="ag_grid_basic_1",
        row_data=data,  # Your list of dictionaries goes here
        column_defs=column_defs,
        width="100%",
    )