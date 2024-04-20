from rxconfig import config
from lahacks2024.userModel import User
import reflex as rx
import bcrypt

class RegisterFormInputState(rx.State):
    form_data: dict = {}

    def handle_submit(self, form_data: dict):
        # Grab data from form
        self.form_data = form_data
        if (form_data["password"] == form_data["password_confirm"]):
            # Start new connection session to database
            with rx.session() as session:
                # Encrypt password before saving
                password = bcrypt.hashpw(form_data["password"].encode('utf-8'), bcrypt.gensalt())
                # Add new user object
                session.add(
                    User(
                        first_name=form_data["first_name"],
                        last_name=form_data["last_name"],
                        email=form_data["email"],
                        password=password,
                    )
                )
                # Commit changes to database
                session.commit()
        else:
            # Alert 'passwords do not match'
            return None

def register() -> rx.Component:
    return rx.center(
        rx.vstack(
            # HTML <form> tag
            rx.form.root(
                rx.heading("Register Account", size="9"),
                # HTML <table> for organizing
                rx.table.root(
                    rx.table.body(
                        rx.table.row(
                            rx.table.cell(
                                "First Name: ",
                            ),
                            rx.table.cell(
                                rx.input(
                                    name="first_name",
                                ),
                            ),
                        ),
                        rx.table.row(
                            rx.table.cell(
                                "Last Name: ",
                            ),
                            rx.table.cell(
                                rx.input(
                                    name="last_name",
                                ),
                            ),
                        ),
                        rx.table.row(
                            rx.table.cell(
                                "Email: ",
                            ),
                            rx.table.cell(
                                rx.input(
                                    name="email",
                                    placeholder="example@domain.com: ",
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
                        rx.table.row(
                            rx.table.cell(
                                "Confirm password: ",
                            ),
                            rx.table.cell(
                                rx.input(
                                    id="password_confirm",
                                ),
                            ),
                        ),
                    ),
                ),
                rx.button(
                        "Submit",
                        type="submit",
                ),
                align="center",
                justify="center",
                # Handle submit when submit button pressed
                on_submit=RegisterFormInputState.handle_submit,
            ),
            rx.button(
                "Back to Login",
                on_click=lambda: rx.redirect("/login")
            ),
            align="center",
            justify="center",
            spacing="7",
            font_size="1em",
        ),
        height="100vh",
    ),