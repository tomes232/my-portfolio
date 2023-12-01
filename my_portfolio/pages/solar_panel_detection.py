"""The Solar Panel Detection page."""
from my_portfolio.templates import template

import reflex as rx


@template(route="/solar-panel-detection", title="Solar Panel Detection", image="/github.svg")
def solar_panel_detection() -> rx.Component:
    """The solar panel detection project page.

    Returns:
        The UI for the spd page.
    """
    return rx.vstack(
        rx.heading("Solar Panel Detection", font_size="3em"),

        rx.video(

            url="https://youtu.be/dyFH9vZEw9s",
            width="800px",
            height="600px",
        ),
    )
