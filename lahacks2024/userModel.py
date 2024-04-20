from rxconfig import config
import reflex as rx

class User(rx.Model, table=True):
    email: str
    password: str
    first_name: str
    last_name: str