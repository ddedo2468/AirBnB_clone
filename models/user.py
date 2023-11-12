#!/usr/bin/python3
""" creating a user class from the base model """

from models.base_model import BaseModel


class User(BaseModel):
    """ Define the User class
    Attributes:
        email 'string' : the user email.
        password 'string' : the user password.
        first_name 'string' : first name.
        last_name 'string' : last name.
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
