import sqlmodel
from rxconfig import config
import reflex as rx

class User(rx.Model, table=True):
    email: str = sqlmodel.Field(primary_key=True)
    password: str
    first_name: str
    last_name: str