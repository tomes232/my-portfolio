from my_portfolio import styles
from my_portfolio.state import State
#from my_portfolio import styles

import reflex as rx
def spd() -> rx.Component:
    return  rx.vstack(
        rx.heading("Solar Panel Detection", font_size="3em"),

        rx.video(

            url="https://youtu.be/dyFH9vZEw9s",
            width="800px",
            height="600px",
        ),
        notebook(),
    )

def notebook()-> rx.component:
    
    with open("solar-panel-detection.html", encoding="utf-8") as readme:
        content = readme.read()
    #return rx.cond(
    #    State.show_spd_notebook,
    #    rx.vstack(
    #        rx.box(
    #            rx.icon(tag="chevron_down"),
    #            rx.button("Jupyter Notebook ", variant="ghost", font_size="2em", on_click=State.change_spd_notebook),
    #            #position="fixed",
    #            #left="300px"
    #
    #
    #        ),
    #        rx.html(content)
    #    ),
    #    rx.vstack(
    #        rx.hstack(
    #            rx.icon(tag="chevron_up"),
    #            rx.button("Jupyter Notebook", variant="ghost", font_size="2em", on_click=State.change_spd_notebook),
    #            #position="fixed",
    #            #left="300px"
    #        ),
    #    )
    #)

    return rx.accordion(
        rx.accordion_item(
            rx.accordion_button(
                rx.heading("Jupyter Notebook", size="xl"),
                rx.accordion_icon(),
            ),
            rx.accordion_panel(
                rx.html(content),
            ),
        ),
        allow_toggle=True,
        width="100%",
        )