from rxconfig import config
from lahacks2024.userModel import User
import reflex as rx

def process_login():
    # take credential and check database
    return None

input_style = {
    "margin-bottom": "5px",
}

def login() -> rx.Component:
    return rx.center(
        rx.theme_panel(),
        rx.flex(
            rx.heading("Log in page", size="9"),
            rx.flex(
                rx.text("Username: "),
                rx.input(placeholder="Enter Username", style=input_style),
                align="center",
            ),
            rx.flex(
                rx.text("Password: "),
                rx.input(placeholder="Enter Password"),
                align="center",
            ),
            rx.button(
                "Log in",
                on_click=process_login(),
                size="4",
            ),
            rx.button(
                "Register",
                on_click=lambda: rx.redirect("/register"),
            ),
            align="center",
            spacing="7",
            font_size="2em",
            flex_direction="column",
        ),
        height="100vh",
    )