"""The home page of the app."""

from my_portfolio import styles
from my_portfolio.templates import template
from my_portfolio.components.photo_change import photo_change
import reflex as rx
from my_portfolio.components.pdf_viewer import worker, viewer

def skills()-> rx.Component:
    """skills section of info page
    
        Returns:
          an rx.Component
    """

    data = [
    {
        "language": "Python",
        "A": 130,
        "fullMark": 150,
    },
    {
        "language": "C/C++",
        "A": 100,
        "fullMark": 150,
    },
    {
        "language": "Java",
        "A": 70,
        "fullMark": 150,
    },
    {
        "language": "Javascript",
        "A":20,
        "fullMark": 150,
    },
    {
        "language": "SQL",
        "A": 105,
        "fullMark": 150,
    },
    {
        "language": "HTML/CSS",
        "A": 40,
        "fullMark": 150,
    },
    ]

    return rx.box(
            rx.recharts.radar_chart(
            rx.recharts.radar(
                data_key="A",
                stroke="#8884d8",
                fill="#8884d8",
            ),
            rx.recharts.polar_grid(),
            rx.recharts.polar_angle_axis(data_key="language"),
            data=data,
        ),
            padding="2em",
            )


@template(route="/", title="Home", image="/github.svg")
def index() -> rx.Component:
    """The home page.

    Returns:
        The UI for the home page.
    """

    
    with open("aboutme.md", encoding="utf-8") as readme:
        content = readme.read()


    

    return rx.vstack(
                        rx.box(rx.center(rx.vstack(rx.heading("Welcome to My Portfolio", size='xl'),photo_change()))),
                        rx.divider(orientation="horizontal"),
                        rx.spacer(),
                        rx.spacer(),
                        rx.markdown(content, component_map=styles.markdown_style),
                        skills(),
                        rx.accordion(
                                        items=[
                                            ("My Info", rx.flex(
                                                        rx.vstack(
                                                        rx.box(
                                                            rx.span("Name: ", font_weight="bold"),
                                                            rx.span("Thomas Pickup"),
                                                            text_align="left"
                                                        ),
                                                        rx.box(
                                                            rx.span("Degree: ", font_weight="bold"),
                                                            rx.span("BSE computer science"),
                                                            text_align="left"
                                
                                                        ),
                                                        rx.box(
                                                            rx.span("Phone: ", font_weight="bold"),
                                                            rx.span("+914 356 7228"),
                                                            text_align="left"
                                                        ),
                                                        ),
                                                        rx.spacer(),
                                                            rx.vstack(
                                                            rx.box(
                                                                rx.span("Birthday: ", font_weight="bold"),
                                                                rx.span("March 7th 2000"),
                                                                text_align="left"
                                                            ),
                                                            rx.box(
                                                                rx.span("Experience: ", font_weight="bold"),
                                                                rx.span("2 Years"),
                                                                text_align="left"
                                                            ),
                                                            rx.box(
                                                                rx.span("Email: ", font_weight="bold"),
                                                                rx.span("tomes232@gmail.com"),
                                                                text_align="left"
                                                            ),
                                                        ),
                                                )),

                                                            
                                            ("Skills", skills()),
                                            ("Resume", rx.box(
                                                            rx.center(
                                                                worker(viewer()),
                                                            ),
                                                            height="1100px",
                                                            
                                                        ),),
                                                
                                        ],
                                        width="100%",
                                    )
    )


