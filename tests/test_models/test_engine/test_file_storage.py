#!/usr/bin/python3
"""Test Suite for FileStorage in models/file_storage.py"""
import os.path
import unittest

import models
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.amenity import Amenity
from models.city import City
from models.review import Review
from models.place import Place


class TestFileStorage(unittest.TestCase):
    """TestFilesStorage"""

    def setUp(self):
        """ condition to test file saving """
        with open("file.json", 'w'):
            FileStorage._FileStorage__file_path = "file.json"
            FileStorage._FileStorage__objects = {}

    def tearDown(self):
        """ destroys created file """
        FileStorage._FileStorage__file_path = "file.json"
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_class_doc(self):
        """ check for documentation """
        self.assertTrue(len(FileStorage.__doc__) > 0)

    def test_method_docs(self):
        """ check for method documentation """
        for func in dir(FileStorage):
            self.assertTrue(len(func.__doc__) > 0)

    def test_all(self):
        """ Test method all from filestorage """
        my_obj = FileStorage()
        my_dict = my_obj.all()
        self.assertTrue(type(my_dict) == dict)

    def test_new(self):
        """ Tests method new for filestorage """
        my_obj = FileStorage()
        new_obj = BaseModel()
        my_obj.new(new_obj)
        my_dict = my_obj.all()
        key = "{}.{}".format(type(new_obj).__name__, new_obj.id)
        self.assertTrue(key in my_dict)

    def test_empty_reload(self):
        """ Empty reload function """
        my_obj = FileStorage()
        new_obj = BaseModel()
        my_obj.new(new_obj)
        my_obj.save()
        my_dict1 = my_obj.all()
        os.remove("test.json")
        my_obj.reload()
        my_dict2 = my_obj.all()
        self.assertTrue(my_dict2 == my_dict1)

    def test_save(self):
        """ Tests the save method for filestorage """
        my_obj = FileStorage()
        new_obj = BaseModel()
        my_obj.new(new_obj)
        my_dict1 = my_obj.all()
        my_obj.save()
        my_obj.reload()
        my_dict2 = my_obj.all()
        for key in my_dict1:
            key1 = key
        for key in my_dict2:
            key2 = key
        self.assertEqual(my_dict1[key1].to_dict(), my_dict2[key2].to_dict())

    def test_instance(self):
        """ Check storage """
        self.assertIsInstance(models.storage, FileStorage)


if __name__ == '__main__':
    unittest.main()
