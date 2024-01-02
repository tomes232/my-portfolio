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


def ai_intro() -> rx.Component:
    return rx.box( rx.box(rx.text("Hi, I am an AI assistant here to answer any questions you have about Tommy's resume.", style=styles.answer_style),
                text_align="left"),
                margin="1em",
            )


def qa(question: str, answer: str) -> rx.Component:
    return rx.box(
        rx.box(rx.text(question, style=styles.question_style),
               text_align="right"),
        rx.box(rx.text(answer, style=styles.answer_style),
               text_align="left"),
        margin="1em",
    )
def chat() -> rx.Component:
   
    return rx.vstack(rx.box(
        *[        
            ai_intro(),    
            rx.foreach(
                State.chat_history,
                lambda messages: qa(messages[0], messages[1]),
            )

        ]

    ),
        py="8",
        flex="1 1 auto",
        width="100%",
        max_w="3xl",
        padding_x="4",
        align_self="center",
        overflow_x="hidden",
        overflow_y="auto",
        padding_bottom="5em",
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

def chatbox_header() -> rx.Component:
    """Chatbot header.

    Returns:
        The chatbot header component.
    """
    return rx.hstack( rx.breadcrumb(
                    rx.breadcrumb_item(
                    rx.image(
                        src="/pickup-logo.svg",
                        height="3em",
                        border_radius="3em 3em",

                    ),                 
                    ),
                    rx.breadcrumb_item(
                        rx.heading("ReflexGPT", size="md"),
                    ),
    ),)


def sidebar_header() -> rx.Component:
    """Sidebar header.

    Returns:
        The sidebar header component.
    """
    return rx.hstack(
        # The logo.
        rx.image(
            src="/pickup-logo.svg",
            height="4em",
            border_radius="4em 4em",

        ),
        rx.spacer(),
        # Link to my linkedin.
        rx.link(
            rx.center(
                rx.image(
                    src="/linkedin.svg",
                    height="3em",
                    padding="0.2em",
                ),
                box_shadow=styles.box_shadow,
                bg="transparent",
                border_radius=styles.border_radius,
                _hover={
                    "bg": styles.accent_color,
                },
            ),
            href="https://www.linkedin.com/in/thomas-pickup-986778186",
        ),

        # Link to Tomes232 GitHub repo.
        rx.link(
            rx.center(
                rx.image(
                    src="/github.svg",
                    height="3em",
                    padding="0.5em",
                ),
                box_shadow=styles.box_shadow,
                bg="transparent",
                border_radius=styles.border_radius,
                _hover={
                    "bg": styles.accent_color,
                },
            ),
            href="https://github.com/tomes232",
        ),
        width="100%",
        border_bottom=styles.border,
        padding="1em",
    )

def chatbox() -> rx.Component:
    return rx.container(
        #menu(),
        rx.heading("Resume Chatbot"),
        #rx.spacer(),
        chat(),
        action_bar(),
    )


def sidebar_footer() -> rx.Component:
    """Sidebar footer.

    Returns:
        The sidebar footer component.
    """
    return rx.hstack(
        rx.spacer(),
        rx.link(
            rx.text("Home"),
            href="/",
        ),
        rx.link(
            rx.text("Docs"),
            href="https://github.com/tomes232/chatbot-api",
        ),
        width="100%",
        border_top=styles.border,
        padding="1em",
    )


def chatbox_sidebar() -> rx.Component:
     return rx.box(
        rx.vstack(
            sidebar_header(),
            rx.heading("ResumeGPT", size="md"),
            #rx.spacer(),
            chat(),
            action_bar(),
            sidebar_footer(),
            height="100dvh",
        ),
        display=["none", "none", "block"],
        min_width=styles.sidebar_width,
        height="100%",
        position="sticky",
        top="0px",
        border_right=styles.border,
    )

