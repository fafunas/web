import reflex as rx
from ..views.waitingListView import waiting


@rx.page(
    title="Lista de Espera",
    description="Lista de Espera",
   # on_load= WaitState.onload
)

def waitinglist()-> rx.Component:
    return waiting()
     
