import reflex as rx

class State(rx.State):
    users: list = []

    def add_user(self, form_data):
        name = form_data["Name"]
        location = form_data["Location"]
        self.users.append(name + ", " + location)
    
    def user_list(self):
        return self.users
    
        
def display_user_list():
        return rx.vstack(
            rx.foreach(State.users, rx.text),
        )

def create_lobby():
    return rx.vstack(
        rx.form.root(
            rx.text("Name: "),
            rx.input(name="Name"),
            rx.text("Location: "),
            rx.input(name="Location"),
            rx.button(
                "Add attendee",
                type="submit",
            ),
            on_submit=State.add_user,
        ),
        display_user_list(),
    )