#!/usr/bin/python3
""" creating city class from the base model """

from models.base_model import BaseModel


class City(BaseModel):

    """ define the City class
    Attributes:
        state_id 'string' : the state id
        name 'string' : the city name
    """

    state_id = ""
    name = ""
