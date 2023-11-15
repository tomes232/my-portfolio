"""The chatbot page."""

from my_portfolio import styles
from my_portfolio.templates import template

import reflex as rx

from my_portfolio.components.chatbox import chatbox
   
@template(route="/chatbot", title="Chatbot")
def chatbot() -> rx.Component:
    return chatbox()