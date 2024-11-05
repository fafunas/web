import reflex as rx
from web.pages.dashboard import index
from web.pages.products import products
import web.styles.styles as styles
from rxconfig import config


app = rx.App(
    stylesheets=styles.STYLESHEETS,
    style=styles.BASE_STYLE,
)