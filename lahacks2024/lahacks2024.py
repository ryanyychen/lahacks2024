"""Welcome to Reflex! This file outlines the steps to create a basic app."""

from rxconfig import config
from lahacks2024.login import login
from lahacks2024.register import register
from lahacks2024.homepage import homepage
from lahacks2024.userModel import User
import reflex as rx

class State(rx.State):
    """The app state."""

# Global Styling
style = {
}

app = rx.App(style=style)
app.add_page(homepage, route="/", title="Homepage")
app.add_page(login, route="/login", title="Login")
app.add_page(register, route="/register", title="Register")