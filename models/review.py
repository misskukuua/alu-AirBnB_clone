#!/usr/bin/python3

from models.base_model import BaseModel

"""
Module Review
defines the Place class with a public attribute
'place_id', 'user_id', and 'text'
"""


class Review(BaseModel):
    """
    Review class
    """
    place_id = ""
    user_id = ""
    text = ""
