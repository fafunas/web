import reflex as rx

from ..components.sidebar import sidebar
from ..styles.fonts import Font
from ..styles.colors import TextColor
from ..styles.styles import Size
from ..states.reportState import ReportState
from ..views.reportTable import reportTable




@rx.page(
    title="Resportes",
    description="Reportes de pedidos",
    #on_load= ReportState.onload
)

def reports()-> rx.Component:
    return rx.hstack(
        sidebar(),
        rx.vstack(
            rx.heading("Reportes",
                       color=TextColor.HEADER,
                       font_size=Size.BIG,
                       margin=Size.MEDIUM),
            rx.hstack(
            reportTable(ReportState.data),
            width="100%"
        ),
            width="100%"
        ),
        width="100%"
    )