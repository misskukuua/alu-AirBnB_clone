# #!/usr/bin/python3
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
# import os
# import unittest
# from os import path
# from models.base_model import BaseModel
# from models.engine.file_storage import FileStorage
#
# """ testing the file storage"""
#
#
# class TestCaseFileStorage(unittest.TestCase):
#     """ class for test cases """
#
#     def set_up(self):
#         self.dir_path = 'file.json'
#         self.our_model = FileStorage()
#
#     def dispose_json(self):
#         """ dispose json file """
#         if path.exists(self.dir_path):
#             os.remove(self.dir_path)
#
#     def test_all(self):
#         """ check type return by all function """
#         self.assertEqual(type(self.our_model.all()), dict)
#
#     def test_new(self):
#         model = BaseModel()
#         self.our_model.new(model)
#         len_dict = len(self.our_model.all())
#         self.assertGreater(len_dict, 0)
#
#     def test_save(self):
#         self.our_model.save()
#         self.assertEqual(path.exists(self.dir_path), True)
#
#     def test_reload(self):
#         model = FileStorage()
#         self.our_model.reload()
#         len_dict = len(model.all())
#         self.assertGreater(len_dict, 0)
#
#
# if __name__ == '__main__':
#     unittest.main()

# #!/usr/bin/python3
# """Test Suite for FileStorage in models/file_storage.py"""
# import os.path
# import unittest
#
# import models
# from models.engine.file_storage import FileStorage
# from models.base_model import BaseModel
# from models.user import User
# from models.state import State
# from models.amenity import Amenity
# from models.city import City
# from models.review import Review
# from models.place import Place
#
#
# class TestFileStorage(unittest.TestCase):
#     """TestFilesStorage"""
#
#     def setUp(self):
#         """ condition to test file saving """
#         with open("test.json", 'w'):
#             FileStorage._FileStorage__file_path = "test.json"
#             FileStorage._FileStorage__objects = {}
#
#     def tearDown(self):
#         """ destroys created file """
#         FileStorage._FileStorage__file_path = "file.json"
#         try:
#             os.remove("test.json")
#         except FileNotFoundError:
#             pass
#
#     def test_class_doc(self):
#         """ check for documentation """
#         self.assertTrue(len(FileStorage.__doc__) > 0)
#
#     def test_method_docs(self):
#         """ check for method documentation """
#         for func in dir(FileStorage):
#             self.assertTrue(len(func.__doc__) > 0)
#
#     def test_all(self):
#         """ Test method all from filestorage """
#         my_obj = FileStorage()
#         my_dict = my_obj.all()
#         self.assertTrue(type(my_dict) == dict)
#
#     def test_new(self):
#         """ Tests method new for filestorage """
#         my_obj = FileStorage()
#         new_obj = BaseModel()
#         my_obj.new(new_obj)
#         my_dict = my_obj.all()
#         key = "{}.{}".format(type(new_obj).__name__, new_obj.id)
#         self.assertTrue(key in my_dict)
#
#     def test_empty_reload(self):
#         """ Empty reload function """
#         my_obj = FileStorage()
#         new_obj = BaseModel()
#         my_obj.new(new_obj)
#         my_obj.save()
#         my_dict1 = my_obj.all()
#         os.remove("test.json")
#         my_obj.reload()
#         my_dict2 = my_obj.all()
#         self.assertTrue(my_dict2 == my_dict1)
#
#     def test_save(self):
#         """ Tests the save method for filestorage """
#         my_obj = FileStorage()
#         new_obj = BaseModel()
#         my_obj.new(new_obj)
#         my_dict1 = my_obj.all()
#         my_obj.save()
#         my_obj.reload()
#         my_dict2 = my_obj.all()
#         for key in my_dict1:
#             key1 = key
#         for key in my_dict2:
#             key2 = key
#         self.assertEqual(my_dict1[key1].to_dict(), my_dict2[key2].to_dict())
#
#     def test_instance(self):
#         """ Check storage """
#         self.assertIsInstance(models.storage, FileStorage)
#
#
# if __name__ == '__main__':
#     unittest.main()
