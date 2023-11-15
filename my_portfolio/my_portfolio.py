"""Welcome to Reflex!."""

from my_portfolio import styles

# Import all the pages.
from my_portfolio.pages import *

import reflex as rx

# Create the app and compile it.
app = rx.App(style=styles.base_style)
app.compile()
