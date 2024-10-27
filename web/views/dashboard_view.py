import reflex as rx
from web.components.card import card
from ..states.dashboardState import DashboardState


def dashboard()-> rx.Component:
    return rx.vstack(
        rx.hstack(
    rx.button("Cerrar Turno",
              on_click=DashboardState.closeShift()),
    width="100%",
    justify="end"
),
            # Contenedor para los cards
            rx.hstack(
                card("loader", "En Preparacion", "yellow"),
                card("package", "Listo para retirar", "lightblue"),
                card("check", "Completadas", "green"),
                spacing="2em",
                justify="space-between",
                width="100%"
            ),
            # Margen entre los cards y la tabla
            rx.box(height="2em"),  # Para crear espacio entre los elementos
            # Contenedor para la tabla (centrado)
            rx.heading("TABLA", text_align="center"),
            rx.box(
                # Aquí se pondría la tabla (ejemplo de tabla vacía por ahora)
                rx.table.root(
    rx.table.header(
        rx.table.row(
            rx.table.column_header_cell("Numero Pedido"),
            rx.table.column_header_cell("Hora Pedido"),
            rx.table.column_header_cell("Hora Finalizado"),
            rx.table.column_header_cell("Total"),
            rx.table.column_header_cell("Observaciones"),
            rx.table.column_header_cell("Acciones"),
        ),
    ),
    rx.table.body(
        rx.table.row(
            rx.table.row_header_cell("Danilo Sousa"),
            rx.table.cell("danilo@example.com"),
            rx.table.cell("Developer"),
        ),
        rx.table.row(
            rx.table.row_header_cell("Zahra Ambessa"),
            rx.table.cell("zahra@example.com"),
            rx.table.cell("Admin"),
        ),
        rx.table.row(
            rx.table.row_header_cell("Jasper Eriks"),
            rx.table.cell("jasper@example.com"),
            rx.table.cell("Developer"),
        ),
    ),
    width="100%",
),
                width="100%",
                padding="1em",
                border="1px solid lightgray",
                border_radius="md",
                box_shadow="md"
            ),
            # Ajustes de margenes y alineación de los elementos en vertical
            spacing="2em",
            align="start",
            width="100%",
            padding="2em"
        ),