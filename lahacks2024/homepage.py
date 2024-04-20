from rxconfig import config
import reflex as rx

def homepage() -> rx.Component:
    # check for login status, if not logged in, redirect to /login
    return rx.center(
        rx.vstack(
            rx.heading("Welcome to Reflex!", size="9"),
            rx.text("Get started by editing"),
            rx.logo(),
            align="center",
            spacing="7",
            font_size="2em",
        ),
        height="100vh",
    )