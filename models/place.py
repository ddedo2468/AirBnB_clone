#!/usr/bin/python3
""" creating a place class from the base model """

from models.base_model import BaseModel


class Place(BaseModel):
    """ Define the Place class
    Attributes:
        city_id 'string' : City id.
        user_id 'string' : User id.
        name 'string' : the place name.
        description 'string' : the describtion of place.
        number_rooms 'int' : the number of rooms.
        number_bathrooms 'int' : The number of bathrooms.
        max_guest 'int' : the max number of guests.
        price_by_night 'int' : the price for night.
        latitude 'float' : lat pos of place.
        longitude 'float' : long pos of place.
        amenity_ids 'list' : the ids list.
    """

    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
