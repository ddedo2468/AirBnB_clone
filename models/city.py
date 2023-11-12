#!/usr/bin/python3
""" creating city class from the base model """

from models.base_model import BaseModel


class City(BaseModel):
    """ define the City class """
    state_id = ""
    name = ""
