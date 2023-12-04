"""The Solar Panel Detection page."""
from my_portfolio.templates import template
from my_portfolio.components.spd_format import spd


import reflex as rx


@template(route="/solar-panel-detection", title="Solar Panel Detection", image="/github.svg")
def solar_panel_detection() -> rx.Component:
    """The solar panel detection project page.

    Returns:
        The UI for the spd page.
    """
    return spd()
