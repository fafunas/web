import reflex as rx
from web.pages.dashboard import index
from web.pages.products import products
from web.pages.reports import reports
from web.pages.waitinglist import waitinglist
import web.styles.styles as styles
from rxconfig import config


app = rx.App(
    stylesheets=styles.STYLESHEETS,
    style=styles.BASE_STYLE,
)