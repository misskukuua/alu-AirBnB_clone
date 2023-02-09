# #!/usr/bin/python3
# """Defines unittests for models/engine/file_storage.py."""
#
# import unittest
# from pathlib import Path
#
# import models
# from models.amenity import Amenity
# from models.city import City
# from models.engine.file_storage import FileStorage
# from models.base_model import BaseModel
# import os
# import json
#
# from models.place import Place
# from models.review import Review
# from models.state import State
# from models.user import User
#
#
# class TestFileStorage(unittest.TestCase):
#     def setUp(self):
#         self.storage = FileStorage()
#
#     def tearDown(self):
#         """Code to execute after tests are executed"""
#         try:
#             os.remove("file.json")
#         except IOError:
#             pass
#
#         try:
#             os.rename("tmp.json", "file.json")
#         except IOError:
#             pass
#
#         FileStorage._FileStorage__objects = {}
#
#     def test_all(self):
#         self.assertEqual(type(self.storage.all()), dict)
#
#     def test_instance(self):
#         self.assertIsInstance(models.storage, FileStorage)
#
#
# def save(self):
#     with open(self.__file_path, 'w') as outfile:
#         new_obj = {}
#         for key, value in self.__objects.items():
#             new_obj.update({key: value.to_dict()})
#         json.dump(new_obj, outfile)
#
#
# def reload(self):
#     classes = {"Amenity": Amenity,
#                "BaseModel": BaseModel,
#                "City": City,
#                "Place": Place,
#                "Review": Review,
#                "State": State,
#                "User": User}
#     my_file = Path(self.__file_path)
#     if my_file.is_file():
#         with open(self.__file_path) as json_file:
#             loads = json.load(json_file)
#             for key, value in loads.items():
#                 obj = classes[value["__class__"]](**value)
#                 self.__objects.update({key: obj})
#
#
# if __name__ == '__main__':
#     unittest.main()






# 2nd test base models
# #!/usr/bin/python3
# """ tests for our main base classes"""
#
# import io
# import unittest
# from time import sleep
#
# from models.base_model import BaseModel
#
#
# class TestCaseBaseModel(unittest.TestCase):
#
#     def setUp(self):
#         """ components for the test """
#         self.our_model = BaseModel()
#         self.our_model.name = "Our first model"
#         self.our_model.our_number = 20
#
#     def test_NumberAdded(self):
#         """test number added """
#         self.assertEqual(self.our_model.our_number, 20)
#
#     def test_classType(self):
#         """ testing class type """
#         self.assertEqual(self.our_model.__class__.__name__, 'BaseModel')
#
#     def test_toDict(self):
#         """ to dict returns a dictionary - checking the return type"""
#         self.assertEqual(type(self.our_model.to_dict()), dict)
#
#     def test_createdAt(self):
#         """ test if created at is a string that
#          can be found using created_at
#         """
#         our_model_json = self.our_model.to_dict()
#         self.assertEqual(type(our_model_json['created_at']), str)
#
#     def test_updatedAt(self):
#         """ testing if updated at is a string that can
#           be found using updated at
#          """
#         our_model_json = self.our_model.to_dict()
#         self.assertEqual(type(our_model_json['updated_at']), str)
#
#     def test_save(self):
#         """ testing if this updates the time """
#         old_time = self.our_model.to_dict()['updated_at']
#         sleep(2)
#         self.our_model.save()
#         self.assertNotEqual(self.our_model.to_dict()['created_at'],
#                             self.our_model.to_dict()['updated_at'])
#
#     def test_id(self):
#         """  id should remain the same at any time  """
#         self.our_model.save()
#         our_model_json = self.our_model.to_dict()
#         self.assertEqual(our_model_json['id'], self.our_model.__dict__['id'])
#
#     def test_str_(self):
#         """ test for string print function """
#         temporary_model = str(self.our_model)
#         self.assertEqual(temporary_model.split(" ")[0], "[BaseModel]")
#         self.assertEqual(temporary_model.split(" ")[1],
#                          "({})".format(self.our_model.id))
#         self.assertEqual(eval(temporary_model.split(" ")[2]), self.our_model.__dict__)
#
#     def test_sizeofDict(self):
#         """ is the dict the same length?  """
#         self.assertEqual(len(self.our_model.to_dict()),
#                          len(self.our_model.__dict__) + 1)


 #!/usr/bin/python3
# """Defines FileStorage class."""
# import json
# from models.base_model import BaseModel
# from models.user import User
# from models.state import State
# from models.city import City
# from models.place import Place
# from models.amenity import Amenity
# from models.review import Review
#
#
# class FileStorage:
#     """
#     Class FileStorage
#     Represent an abstracted storage test_engine.
#     It serializes instances to a JSON file and deserializes
#     JSON file to instance.
#     Attributes:
#         __file_path (str): Name of the file to save objects to.
#         __objects (dict): Dictionary of instantiated objects.
#     """
#     __file_path = 'file.json'
#     __objects = {}
#
#     def all(self):
#         """Return dictionary __objects."""
#         return self.__objects
#
#     def new(self, obj):
#         """Set in __objects obj with the  key <obj_class_name>.id"""
#         key = '{}.{}'.format(obj.__class__.__name__, obj.id)
#         self.__objects[key] = obj
#
#     def save(self):
#         """Serialize __objects to JSON file __file_path."""
#         object_dict = {}
#         for obj in self.__objects:
#             object_dict[obj] = self.__objects[obj].to_dict()
#         with open(self.__file_path, 'w') as file:
#             json.dump(object_dict, file)
#
#     def reload(self):
#         """
#         deserializes the JSON file to __objects (only if the JSON file
#         (__file_path) exists ; otherwise, do nothing. If the file does not
#         exist, no exception should be raised)
#         """
#
#         # add all import below to avoid circular dependencies
#         # eg. models imports file_storage, if file_storage imports models,
#         # it becomes circular
#
#
#         try:
#             with open(self.__file_path) as file:
#                 serialized_content = json.load(file)
#                 for item in serialized_content.values():
#                     class_name = item['__class__']
#                     self.new(eval(class_name + "(**" + str(item) + ")"))
#         except FileNotFoundError:
#             pass