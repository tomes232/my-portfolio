""" Page for my resume."""

from my_portfolio.templates import template

from my_portfolio.components.pdf_viewer import page, doc, worker, viewer


import reflex as rx



#shows pdf image of my resume
@template(route="/resume", title="Resume")
def resume() -> rx.Component:
    return rx.box(
            rx.center(
                worker(viewer()),
            ),
            height="750px",
        )
    # return rx.box(
    #             rx.center(
    #                 doc(
    #                     page(),
    #                     ),
    #                     ),
    #             )