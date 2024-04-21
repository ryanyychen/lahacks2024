"""Welcome to Reflex! This file outlines the steps to create a basic app."""

from rxconfig import config
from lahacks2024.login import login
from lahacks2024.register import register
from lahacks2024.homepage import homepage
from lahacks2024.create_lobby import create_lobby
from lahacks2024.userModel import User
import reflex as rx

# Global Styling
style = {
}

app = rx.App(style=style)
app.add_page(login, route="/login", title="Login")
app.add_page(register, route="/register", title="Register")
app.add_page(create_lobby, route="/", title="New Lobby")