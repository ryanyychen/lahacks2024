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
            gap="15vw",
            margin="5vh",
        )
    )