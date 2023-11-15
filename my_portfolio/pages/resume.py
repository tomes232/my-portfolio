""" Page for my resume."""

from my_portfolio.templates import template


import reflex as rx

#shows pdf image of my resume
@template(route="/resume", title="Resume")
def resume() -> rx.Component:
    #return rx.container(
    #    rx.image(
    #    src="/resume.png",
    #    width="200%",
    #    height="100%",
    #    )
    #)
    return rx.image(
        src="/resume.png",
        width="200%",
        height="100%",
        )