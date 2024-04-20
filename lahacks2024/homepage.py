from rxconfig import config
import reflex as rx

def profile():
    return rx.text("RC")

def homepage() -> rx.Component:
    # check for login status, if not logged in, redirect to /login
    return rx.center(
        rx.hstack(
            rx.vstack(
                rx.box(
                    rx.hstack(
                        profile(),
                        rx.text("Ryan Chen"),
                    ),
                    rx.text("XXX@gmail.com"),
                    padding="1em",
                    border_width="5px",
                ),
            ),
            rx.vstack(

                rx.box(
                    rx.heading("Lobbies"),
                    padding="1em",
                ),
                rx.box(
                    rx.text("LA Hacks"),
                    rx.hstack(
                        rx.text("id: xxxxxxxxx"),
                        rx.text("4/19/2024"),
                    ),
                    rx.text("XXX@gmail.com"),
                    padding="1em",
                    border_width="5px",
                ),
                rx.box(
                    rx.text("LA Hacks"),
                    rx.hstack(
                        rx.text("id: xxxxxxxxx"),
                        rx.text("4/19/2024"),
                    ),
                    rx.text("XXX@gmail.com"),
                    padding="1em",
                    border_width="5px",
                ),
                rx.box(
                    rx.text("LA Hacks"),
                    rx.hstack(
                        rx.text("id: xxxxxxxxx"),
                        rx.text("4/19/2024"),
                    ),
                    rx.text("XXX@gmail.com"),
                    padding="1em",
                    border_width="5px",
                ),
            ),
            rx.chakra.popover(
                rx.chakra.popover_trigger(
                    rx.chakra.button("Popover Example")
                ),
                rx.chakra.popover_content(
                    rx.center(
                        rx.box(
                            rx.heading("Create Lobby"),
                            rx.text("Name"),
                            rx.input(),
                            rx.text("Description"),
                            rx.input(),
                            rx.text("Date"),
                            rx.input(),
                            rx.text("Time"),
                            rx.input(),
                            rx.button("Create"),
                            padding="1em",
                            border_width="5px",
                        ),
                        padding="5em",
                    ),
                ),
            ),
            gap="15vw",
            margin="5vh",
        ),
    )