"""chatbox component for the app."""

from my_portfolio import styles
from my_portfolio.state import State
#from my_portfolio import styles

import reflex as rx

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
    return rx.hstack(
        rx.input(
            placeholder="Ask me about my resume",
            on_change=State.set_question,
            style=styles.input_style,),
        rx.button(
            "Ask",
            on_click=State.answer, 
            style=styles.button_style),
    )

def chatbox() -> rx.Component:
    return rx.container(
        chat(),
        action_bar(),
    )
