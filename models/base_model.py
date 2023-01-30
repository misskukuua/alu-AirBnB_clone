#!/usr/bin/python3

""" class BaseModel that defines all common attributes/methods """

import uuid
from datetime import datetime
import models
from uuid import uuid4


class BaseModel:
    pass

    def __init__(self):
        self.updated_at = None

    def save(self, storage=None):
        """ Update with current time """
        self.updated_at = datetime.today()
        storage.save()

    def to_dict(self):
        """method to create dict"""
        first_dict = self.__dict__



    def __str__(self):
