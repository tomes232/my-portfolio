"""chatbox component for the app."""

from my_portfolio import styles
from my_portfolio.state import State, models
from my_portfolio.components.loading_icon import loading_icon
#from my_portfolio import styles

import reflex as rx

def menu() -> rx.Component:
    return rx.vstack(
        rx.heading(State.model),
        rx.select(
            models,
            placeholder="Select a model",
            on_change=State.set_option,
            color_schemes="twitter",
        ))


def qa(question: str, answer: str) -> rx.Component:
    return rx.box(
        rx.box(rx.text(question, style=styles.question_style),
               text_align="right"),
        rx.box(rx.text(answer, style=styles.answer_style),
               text_align="left"),
        margin="1em",
    )
def chat() -> rx.Component:
   
    return rx.box(
        *[
            rx.foreach(
                State.chat_history,
                lambda messages: qa(messages[0], messages[1]),
            )

        ]
    )
def action_bar() -> rx.Component:
    return rx.box(rx.vstack(rx.form(
            rx.form_control(
            rx.hstack(
                rx.input(
                    placeholder="Ask me about my resume",
                    id="question",
                    _placeholder={"color": "#fffa"},
                    _hover={"border_color": styles.accent_color},
                    style=styles.input_style),
                    
                rx.button(
                    rx.cond(
                        State.processing,
                        loading_icon(height="1em"),
                        rx.text("Send"),
                    ),
                        type_="submit",
                        _hover={"bg": styles.accent_color},
                        style=styles.input_style,
                        color_scheme="facebook",
                    ),
                ),
            is_disabled=State.processing,
            ),
            on_submit=State.answer,
            reset_on_submit=True,
            width="100%",

            ),),)   

def chatbox() -> rx.Component:
    return rx.container(
        #menu(),
        rx.heading("Resume Chatbot"),
        chat(),
        action_bar(),
    )
