#!/usr/bin/python3
"""Defines unittests for models/engine/file_storage.py."""

import unittest
from pathlib import Path

import models
from models.amenity import Amenity
from models.city import City
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
import os
import json

from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class TestFileStorage(unittest.TestCase):
    def setUp(self):
        self.storage = FileStorage()

    def tearDown(self):
        """Code to execute after tests are executed"""
        try:
            os.remove("file.json")
        except IOError:
            pass

        try:
            os.rename("tmp.json", "file.json")
        except IOError:
            pass

        FileStorage._FileStorage__objects = {}

    def test_all(self):
        self.assertEqual(type(self.storage.all()), dict)

    def test_instance(self):
        self.assertIsInstance(models.storage, FileStorage)


def save(self):
    with open(self.__file_path, 'w') as outfile:
        new_obj = {}
        for key, value in self.__objects.items():
            new_obj.update({key: value.to_dict()})
        json.dump(new_obj, outfile)


def reload(self):
    classes = {"Amenity": Amenity,
               "BaseModel": BaseModel,
               "City": City,
               "Place": Place,
               "Review": Review,
               "State": State,
               "User": User}
    my_file = Path(self.__file_path)
    if my_file.is_file():
        with open(self.__file_path) as json_file:
            loads = json.load(json_file)
            for key, value in loads.items():
                obj = classes[value["__class__"]](**value)
                self.__objects.update({key: obj})


if __name__ == '__main__':
    unittest.main()
