#!/usr/bin/python3

""" class BaseModel that defines all common attributes/methods """

import uuid
from datetime import datetime
import models


class BaseModel:
    """ Base Model class """

    def __init__(self, *args, **kwargs):
        """Initialization a new base model"""

        # form = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        if len(kwargs) != 0:
            for key, val in kwargs.items():
                if key == "self.created_at" or key == "self.updated_at":
                    val = datetime.fromisoformat(val)
                    setattr(self, key, val)
                    continue
                if key != '__class__':
                    setattr(self, key, val)
                else:
                    self.id = str(uuid.uuid4())
                    self.created_at = datetime.utcnow()
                    self.updated_at = datetime.utcnow()
                    models.storage.new(self)

    def save(self):
        """ Update with current time"""
        self.updated_at = datetime.today()
        models.storage.save()

    def to_dict(self):
        """return dictionary"""
        dict_example = self.__dict__.copy()
        dict_example['__class__'] = self.__class__.__name__
        dict_example['created_at'] = dict_example['created_at'].isoformat()
        dict_example['updated_at'] = dict_example['updated_at'].isoformat()
        return dict_example

    def __str__(self):
        """str should print class name, id, dict"""
        class_name = self.__class__.__name__
        class_dict = self.__dict__
        return "[{}] ({}) {}".format(class_name, self.id, class_dict)
