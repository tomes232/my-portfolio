"""The settings page."""

from my_portfolio.templates import template

import reflex as rx


@template(route="/blog", title="Blog")
def blog() -> rx.Component:
    """The settings page.

    Returns:
        The UI for the settings page.
    """
    return rx.vstack(
        rx.heading("Blog", font_size="3em"),
        rx.text("Feature coming soon!"),
    )
