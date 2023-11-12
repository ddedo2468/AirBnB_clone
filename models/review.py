#!/usr/bin/python3
""" creating a review class from the base model """

from models.base_model import BaseModel


class Review(BaseModel):
    """Define the review class
    Attributes:
        place_id 'str' : Place id.
        user_id 'str' : the User id.
        text 'string' : the customer review.
    """

    place_id = ""
    user_id = ""
    text = ""
