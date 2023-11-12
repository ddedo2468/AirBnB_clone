#!/usr/bin/python3
""" defining the BaseModel and its correspondent methods """

import models
from datetime import datetime
from uuid import uuid4


class BaseModel:
""" Base Class """
   def __init__(self, *args, **kwargs):
        """ initializing object """
        time_format = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()
        if len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "created_at" or k == "updated_at":
                    self.__dict__[k] = datetime.strptime(v, time_format)
                else:
                    self.__dict__[k] = v
        else:
            models.storage.new(self)

    def __str__(self):
    """ printing the string representation """
      new = (f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}")
       return new

    def save(self):
    """ updating the object with the latest time """
      self.updated_at = datetime.today()
       models.storage.save()

    def to_dict(self):
    """ returns the dictionary of the BaseModel instances """
      new_dict = self.__dict__.copy()
       new_dict["created_at"] = self.created_at.isoformat()
        new_dict["updated_at"] = self.updated_at.isoformat()
        new_dict["__class__"] = self.__class__.__name__
        return new_dict
