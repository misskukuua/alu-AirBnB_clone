#!/usr/bin/python3

"""
Class that defines all common attributes/methods for other classes
"""

from uuid import uuid4
from datetime import datetime
import models

class BaseModel:
    """
    The base class for all classes
    """
    def __init__(self, *args, **kwargs):
        """Initialize the base model"""
        if kwargs.__len__() > 0:
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                    setattr(self, key, value)
                    continue
                if key != '__class__':
                    setattr(self, key, value)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.utcnow()
            self.updated_at = datetime.utcnow()
            # models.storage.new(self)

    def __str__(self):
        """ String should print class name, self.id and self.__dict__"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        
        """
        updates the public instance attribute 'updated_at' with the current datetime
        """
        self.updated_at = datetime.utcnow()
        models.storage.save()

    def to_dict(self):
        """returns a dictionary containing all keys/values of __dict__ of the instance"""
        current_dict = self.__dict__.copy()
        current_dict['__class__'] = self.__class__.__name__
        current_dict['updated_at'] = current_dict['updated_at'].isoformat()
        current_dict['created_at'] = current_dict['created_at'].isoformat()
        return current_dict
