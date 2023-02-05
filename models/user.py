#!/usr/bin/python3

from models.base_model import BaseModel


class User(BaseModel):
    """Represent a user class
    """

    id = ""
    name = ""
    email = ""
    password = ""
    first_name = ""
    last_name = ""

