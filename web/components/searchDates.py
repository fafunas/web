import reflex as rx
from ..states.reportState import ReportState


def SearchDate()->rx.Component:
    return rx.hstack(
        rx.form.root(
            rx.hstack(
                rx.input(
                    placeholder="Desde",
                    type="date",
                    name="from",
                    required=True
                ),
                rx.input(
                    placeholder="Hasta",
                    type="date",
                    name="to",
                    required=True
                ),
                rx.button(
                    "Buscar",
                    type="submit"
                )
                
            ),
            on_submit=ReportState.fillTable
            
        )
       
    )