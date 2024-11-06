import reflex as rx
from web.components.sidebar import sidebar
from ..components.shift_form import shift_form
from ..states.dashboardState import DashboardState
from ..views.dashboard_view import dashboard

@rx.page(
    title="Dashboard Cervesia",
    description="Festival Rico",
    on_load=DashboardState.on_load()
    
)

def index() -> rx.Component:
    return rx.hstack(
        sidebar(),
        rx.cond(
            DashboardState.shift_status,
            rx.flex(dashboard(DashboardState.products),
                    width="100%"),
            rx.box(
                rx.flex(
                    shift_form(),
                    align="center",
                    justify="center",
                ),
                width="100%",  
                display="flex",  # Configura el contenedor para usar flex
                alignItems="center",  # Centra verticalmente
                justifyContent="center",  # Centra horizontalmente
            ),
            
        ),
        spacing="0",
        width="100%",
    )