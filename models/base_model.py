#!/usr/bin/python3

""" class BaseModel that defines all common attributes/methods """

import uuid
from datetime import datetime
import models


class BaseModel:
    """ Base Model class """

    def __init__(self, *args, **kwargs):
        """Initialization a new base model"""

        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)
        else:
            for key, val in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    tform = "%Y-%m-%dT %H:%M:%S.%f"
                    val = datetime.strptime(kwargs[key], tform)
                if key != '__class__':
                    setattr(self, key, val)

    def save(self):
        """ Update with current time"""
        self.updated_at = datetime.today()
        models.storage.save()

    def to_dict(self):
        """method to create dict"""

        """method to create dict
        Return the dictionary of the BaseModel instance.
        """
        first_dict = self.__dict__.copy()
        first_dict["created_at"] = self.created_at.isoformat()
        first_dict["updated_at"] = self.updated_at.isoformat()
        first_dict["__class__"] = self.__class__.__name__
        return first_dict

    def __str__(self):
        """str should print class name, id, dict"""
        class_name = self.__class__.__name__
        class_dict = self.__dict__
        return "[{}] ({}) {}".format(class_name, self.id, class_dict)
