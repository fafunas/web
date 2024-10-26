import reflex as rx
from web.components.sidebar import sidebar
from ..components.shift_form import shift_form
from ..states.dashboardState import DashboardState
from ..views.dashboard_view import dashboard

@rx.page(
    title="Dashboard Cervesia",
    description="Festival Rico"
    
)

def index() -> rx.Component:
    return rx.hstack(
        sidebar(),
        rx.cond(
            DashboardState.shift_status,
            rx.box(dashboard()),
            rx.box(
                rx.flex(
                    shift_form(),
                    align="center",
                    justify="center",
                ),
                width="100%",  # Anchura completa de la pantalla
                height="100vh",  # Altura completa de la ventana
                display="flex",  # Configura el contenedor para usar flex
                alignItems="center",  # Centra verticalmente
                justifyContent="center",  # Centra horizontalmente
            )
        ),
        spacing="0",
        width="100%",
    )