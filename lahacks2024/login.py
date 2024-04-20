from rxconfig import config
from lahacks2024.userModel import User
import reflex as rx

class LogInFormInputState(rx.State):
    form_data: dict = {}

    def handle_submit(self, form_data: dict):
        # Grab data from form
        self.form_data = form_data
        with rx.session() as session:
            # Query database and check email against password
            user = session.exec(User).filter(User.email == form_data["email"]).first()
            if user and user.password == form_data["password"]:
                # Redirect to homepage
                return rx.redirect("/")
            else:
                # Alert 'email or password incorrect'
                return None

input_style = {
    "margin-bottom": "5px",
}

def login() -> rx.Component:
    return rx.center(
        rx.vstack(
            rx.form.root(
                rx.heading("Log In", size="9"),
                rx.table.root(
                    rx.table.body(
                        rx.table.row(
                            rx.table.cell(
                                "Username: ",
                            ),
                            rx.table.cell(
                                rx.input(
                                    name="email",
                                    placeholder="email@domain.com",
                                ),
                            ),
                        ),
                        rx.table.row(
                            rx.table.cell(
                                "Password: ",
                            ),
                            rx.table.cell(
                                rx.input(
                                    name="password",
                                    type="password",
                                ),
                            ),
                        ),
                    ),
                ),
                rx.button(
                        "Log In",
                        type="submit",
                ),
                on_submit=LogInFormInputState.handle_submit,
            ),
            rx.button(
                "Register",
                on_click=lambda: rx.redirect("/register"),
            ),
            align="center",
            justify="center",
            spacing="7",
            font_size="1em",
        ),
        height="100vh",
    ),