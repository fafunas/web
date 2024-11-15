import reflex as rx
from ..styles.colors import Color


def sidebar_item(
    text: str, icon: str, href: str, target: str ="_self"
) -> rx.Component:
    return rx.link(
        rx.hstack(
            rx.icon(icon),
            rx.text(text, size="4"),
            width="100%",
            padding_x="0.5rem",
            padding_y="0.75rem",
            align="center",
            style={
                "_hover": {
                    "bg": Color.CONTENT,
                    "color": Color.WHITE,
                },
                "border-radius": "0.5em",
            },
        ),
        href=href,
        target=target,
        underline="none",
        weight="medium",
        width="100%",
    )


def sidebar_items() -> rx.Component:
    return rx.vstack(
        sidebar_item("Dashboard", "layout-dashboard", "/#"),
        sidebar_item("Productos", "package-search", "/products"),
        sidebar_item("Informes", "book-text", "/reports"),
        sidebar_item("Panel espera", "square-arrow-out-up-right", "/waitinglist","_blank"),
        spacing="1",
        width="100%",
    )


def sidebar() -> rx.Component:
    return rx.box(
        rx.desktop_only(
            rx.vstack(
                rx.hstack(
                    rx.image(
                        src="/logo.png",
                        #width="2.25em",
                        height="auto",
                        border_radius="25%",
                    ),
                    align="center",
                    justify="start",
                    padding_x="0.5rem",
                    width="100%",
                ),
                sidebar_items(),
                spacing="5",
                padding_x="1em",
                padding_y="1.5em",
                bg=Color.PRIMARY,
                align="start",
                height="100vh",
                width="16em",
            ),
        ),
        rx.mobile_and_tablet(
            rx.drawer.root(
                rx.drawer.trigger(
                    rx.icon("align-justify", size=30)
                ),
                rx.drawer.overlay(z_index="5"),
                rx.drawer.portal(
                    rx.drawer.content(
                        rx.vstack(
                            rx.box(
                                rx.drawer.close(
                                    rx.icon("x", size=30)
                                ),
                                width="100%",
                            ),
                            sidebar_items(),
                            spacing="5",
                            width="100%",
                        ),
                        top="auto",
                        right="auto",
                        height="100%",
                        width="20em",
                        padding="1.5em",
                        bg=Color.PRIMARY,
                    ),
                    width="100%",
                ),
                direction="left",
            ),
            padding="1em",
        ),
    )