#!/usr/bin/python3

""" class BaseModel that defines all common attributes/methods """
import uuid
from datetime import datetime
import models
from uuid import uuid4


def save(self):
    """ Update with current time """
    self.updated_at = datetime.today()
    storage.save()


def to_dict(self):


def __str__(self):

