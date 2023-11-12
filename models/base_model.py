#!/usr/bin/python3
""" BaseModel the parent class """

from uuid import uuid4
import models
from datetime import datetime


class BaseModel:
    """ define BaseModel class """

    def __init__(self, *args, **kwargs):
        """ the class constructor """

        format_time = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()
        if len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    self.__dict__[key] = datetime.strptime(value, format_time)
                else:
                    self.__dict__[key] = value
        else:
            models.storage.new(self)

    def __str__(self):
        """ print strint repr for the objs """

        new_str = ("[{}] ({}) {}".format(self.__class__.__name__,
                                         self.id, self.__dict__))
        return new_str

    def save(self):
        """ update the last time obj edited at """

        self.updated_at = datetime.today()
        models.storage.save()

    def to_dict(self):
        """ return a dictionary of baseModel instances"""

        nw_dictionary = self.__dict__.copy()
        nw_dictionary["created_at"] = self.created_at.isoformat()
        nw_dictionary["updated_at"] = self.updated_at.isoformat()
        nw_dictionary["__class__"] = self.__class__.__name__
        return nw_dictionary
