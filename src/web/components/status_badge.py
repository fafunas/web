import reflex as rx

def _badge(status: str):
    badge_mapping = {
        "Completeda": ("check", "Completeda", "green"),
        "En Preparacion": ("loader", "En Preparacion", "yellow"),
        "Listo Para Retirar": ("package", "Listo Para Retirar", "blue"),
    }
    icon, text, color_scheme = badge_mapping.get(status, ("loader", "En Preparacion", "yellow"))
    return rx.badge(
        rx.icon(icon, size=16),
        text,
        color_scheme=color_scheme,
        radius="large",
        variant="surface",
        size="2",
    )

def status_badge(status: str):
    return rx.match(
        status,
        ("Completeda", _badge("Completeda")),
        ("En Preparacion", _badge("En Preparacion")),
        ("Listo Para Retirar", _badge("Listo Para Retirar")),
        _badge("En Preparacion"),
    )