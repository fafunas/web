import reflex as rx
from ..states.dashboardState import DashboardState


def shift_form()-> rx.Component:
    return rx.vstack(
        rx.heading("Nuevo turno"),
        rx.form(
            rx.vstack(
                rx.button("Iniciar Turno", type="submit"),
            ),
           # on_submit=FormState.handle_submit,
            reset_on_submit=True,
        ),
    )
    