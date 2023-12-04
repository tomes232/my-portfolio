from my_portfolio import styles
from my_portfolio.state import State
#from my_portfolio import styles

import reflex as rx

def photo_change() -> rx.Component:
    #photo = "/" + State.photo
    print(State.photo)
    return rx.hstack(   rx.IconButton(aria_label="Change Photo", icon= rx.icon(tag="chevron_left"), on_click=State.change_photo_back),
        
                        rx.image(src=State.photo,   width="400px",
                            height="auto",
                            border_radius="200px 200px",
                            border="5px solid #555",
                            #box_shadow="lg",
                        ),

                        rx.IconButton(aria_label="Change Photo", icon= rx.icon(tag="chevron_right"), on_click=State.change_photo_forward)

                    )
