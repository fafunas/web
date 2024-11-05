import reflex as rx


def notification(message,color)-> rx.Component:
    return rx.callout(
    message,
    icon="triangle_alert",
    color_scheme=color,
    role="alert",
)

