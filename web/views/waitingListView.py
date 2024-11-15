import reflex as rx
from ..styles.styles import Size
from ..states.LocalState import LocalState

def waiting() -> rx.Component:
    return rx.vstack(
        rx.grid(
            rx.vstack(
                rx.heading(
                    "En Preparación",
                    text_align="center",
                    font_size=Size.VERY_BIG,
                    width="100%",
                    margin="30px 0px",
                    padding="15px",
                    border_bottom="2px solid black"
                ),
                rx.flex(
                    rx.cond(
                        LocalState.enprep,
                        rx.foreach(
                            LocalState.enprep,
                            lambda x: orderitem(x, "red")
                        ),
                    ),
                    flex_wrap="wrap",
                    direction="row",  # Cambiamos a dirección de fila para centrar columnas
                    align="center",  # Centramos el contenido en la dirección horizontal
                    width="100%",
                    height="calc(100% - 80px)",
                    overflow_y="auto",
                    padding="10px",
                    gap="75px",
                    style={
                        "display": "grid",
                        "gridAutoFlow": "column",  # Las columnas se llenan una por una
                        "gridTemplateRows": "repeat(auto-fill, 120px)",  # Filas automáticas
                        "justifyContent": "center"
                    }
                ),
                width="100%",
                height="100%"
            ),
            rx.vstack(
                rx.heading(
                    "Para Retirar",
                    text_align="center",
                    font_size=Size.VERY_BIG,
                    width="100%",
                    padding="15px",
                    margin="30px 0px",
                    border_bottom="2px solid black"
                ),
                rx.flex(
                    rx.cond(
                        LocalState.ready,
                        rx.foreach(
                            LocalState.ready,
                            lambda x: orderitem(x, "green")
                        )
                    ),
                    flex_wrap="wrap",
                    direction="row",
                    align="center",
                    width="100%",
                    height="calc(100% - 80px)",
                    overflow_y="auto",
                    padding="10px",
                    gap="75px",
                    style={
                        "display": "grid",
                        "gridAutoFlow": "column",
                        "gridTemplateRows": "repeat(auto-fill, 120px)",
                        "justifyContent": "center"
                    }
                ),
                width="100%",
                height="100%"
            ),
            columns="2",
            width="100%",
            height="calc(100vh - 100px)",
            gap="0"
        ),
        width="100%",
        height="100vh",
        overflow="hidden"
    )

def orderitem(x: rx.Var[int], color: str) -> rx.Component:
    return rx.center(
        rx.text(
            x,
            font_size=Size.EXTRA_BIG,
            color=color,
            font_weight="bold",
            
        ),
        width="100px",
        height="100px"
    )
