"""The chatbot page."""

from my_portfolio import styles
from my_portfolio.templates import chat_template
from my_portfolio.components.pdf_viewer import worker, viewer


import reflex as rx

from my_portfolio.components.chatbox import chatbox
   
@chat_template(route="/chatbot", title="Resume Chatbot")
def chatbot() -> rx.Component:
    
    
    
    return rx.box( worker(viewer()),)
