from rxconfig import config
from lahacks2024.userModel import User
import reflex as rx

def process_login():
    # take credential and check database
    return None

def register() -> rx.Component:
    return rx.center(
        rx.theme_panel(),
        rx.vstack(
            rx.heading("Register Account", size="9"),
            rx.text("Enter details"),
            rx.input(placeholder="Username:"),
            rx.input(placeholder="Email:"),
            rx.input(placeholder="Password:"),
            rx.button(
                "Register",
                on_click=process_login(),
                size="4",
            ),
            rx.logo(),
            align="center",
            spacing="7",
            font_size="2em",
        ),
        height="100vh",
    )