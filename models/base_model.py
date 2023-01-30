#!/usr/bin/python3

""" class BaseModel that defines all common attributes/methods """

import uuid
from datetime import datetime
import models
from uuid import uuid4


class BaseModel:
    """ Base Model class """

    def __init__(self, *args, **kwargs):
        """Initialization a new base model"""

        tform = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()

    def save(self, storage=None):
        """ Update with current time"""
        self.updated_at = datetime.today()
        models.storage.save()

    def to_dict(self):
        """method to create dict
        Return the dictionary of the BaseModel instance.
        """
        first_dict = self.__dict__.copy()
        first_dict["__class__"] = self.__class__.__name__

    def __str__(self):
        """str should print class name, id, dict"""
        class_name = self.__class__.__name__
        class_dict = self.__dict__
        return "[{}] ({}) {}".format(class_name, self.id, class_dict)
