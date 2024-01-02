""" Page for my resume."""

from my_portfolio.templates import template

from my_portfolio.components.pdf_viewer import page, doc, worker, viewer


import reflex as rx

def resume() -> rx.Component:
    return rx.box(
        element="iframe",
        src="https://bit.ly/naruto-sage",
        border_color="red",
    )


#shows pdf image of my resume
@template(route="/resume", title="Resume")
def resume() -> rx.Component:
    return rx.box( worker(
            rx.box(
                      viewer(),
                        border="1px solid black",
                        border_radius="8px",
            ),
    ),)

        
    # return rx.box(
    #             rx.center(
    #                 doc(
    #                     page(),
    #                     ),
    #                     ),
    #             )