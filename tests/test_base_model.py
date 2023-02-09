#!/usr/bin/python3

""" tests for our main base classes"""
import io
import unittest
from time import sleep

from models.base_model import BaseModel


class TestCaseBaseModel(unittest.TestCase):

    def setUp(self):
        """ components for the test """
        self.our_model = BaseModel()
        self.our_model.name = "Our first model"
        self.our_model.our_number = 20

    def test_NumberAdded(self):
        """test number added """
        self.assertEqual(self.our_model.our_number, 20)

    def test_classType(self):
        """ testing class type """
        self.assertEqual(self.our_model.__class__.__name__, 'BaseModel')

    def test_toDict(self):
        """ to dict returns a dictionary - checking the return type"""
        self.assertEqual(type(self.our_model.to_dict()), dict)

    def test_createdAt(self):
        """ test if created at is a string that
         can be found using created_at
        """
        our_model_json = self.our_model.to_dict()
        self.assertEqual(type(our_model_json['created_at']), str)

    def test_updatedAt(self):
        """ testing if updated at is a string that can
          be found using updated at
         """
        our_model_json = self.our_model.to_dict()
        self.assertEqual(type(our_model_json['updated_at']), str)

    def test_save(self):
        """ testing if this updates the time """
        old_time = self.our_model.to_dict()['updated_at']
        sleep(2)
        self.our_model.save()
        self.assertNotEqual(self.our_model.to_dict()['created_at'],
                            self.our_model.to_dict()['updated_at'])

    def test_id(self):
        """  id should remain the same at any time  """
        self.our_model.save()
        our_model_json = self.our_model.to_dict()
        self.assertEqual(our_model_json['id'], self.our_model.__dict__['id'])

    def test_str_(self):
        """ test for string print function """
        temporary_model = str(self.our_model)
        self.assertEqual(temporary_model.split(" ")[0], "[BaseModel]")
        self.assertEqual(temporary_model.split(" ")[1],
                         "({})".format(self.our_model.id))
        self.assertEqual(eval(temporary_model.split(" ")[2]), self.our_model.__dict__)

    def test_sizeofDict(self):
        """ is the dict the same length?  """
        self.assertEqual(len(self.our_model.to_dict()),
                         len(self.our_model.__dict__) + 1)

#
# from models.base_model import BaseModel
#
# my_model = BaseModel()
# my_model.name = "My First Model"
# my_model.my_number = 89
# print(my_model)
# my_model.save()
# print(my_model)
# my_model_json = my_model.to_dict()
# print(my_model_json)
# print("JSON of my_model:")
# for key in my_model_json.keys():
#     print("\t{}: ({}) - {}".format(key, type(my_model_json[key]),
#                                    my_model_json[key]))
