#!/usr/bin/python3
""" Unittests Base Model Module"""

import unittest
from datetime import datetime
from models import storage
from models.base_model import BaseModel
import json
import os
import pep8
import uuid


class Test_BaseModel(unittest.TestCase):
    """ Test Base Model Methods """

    def test_assert_docstring(self):
        """ Test docstring """
        self.assertTrue(len(BaseModel.__doc__) > 1)
        self.assertTrue(len(BaseModel.__init__.__doc__) > 1)
        self.assertTrue(len(BaseModel.__str__.__doc__) > 1)
        self.assertTrue(len(BaseModel.save.__doc__) > 1)
        self.assertTrue(len(BaseModel.to_dict.__doc__) > 1)

    def test_assert_uuid_version(self):
        """Test id unique and UUID version"""
        elm = BaseModel()
        street = BaseModel()
        self.assertNotEqual(elm.id, street.id)
        jason = uuid.UUID(elm.id, version=4)
        self.assertEqual(str(jason), elm.id, "Error: UUID no version 4")

    def test_assert_instn_attr(self):
        """ Test attributes exists """
        a = BaseModel()
        self.assertTrue(hasattr(a, 'id'))
        self.assertTrue(hasattr(a, 'created_at'))
        self.assertTrue(hasattr(a, 'updated_at'))

    def test_assert_instn_defs(self):
        """ Test methods exists """
        self.assertTrue(hasattr(BaseModel, "__init__"))
        self.assertTrue(hasattr(BaseModel, "__str__"))
        self.assertTrue(hasattr(BaseModel, "save"))

    def test_assert_is_instance(self):
        """ Test init instance is ok """
        model = BaseModel()
        self.assertIsInstance(model, BaseModel)

    def test_assert_str(self):
        """ Test str method is ok """
        model = BaseModel()
        c = model.__str__()
        d = model.id
        d1 = model.__dict__
        self.assertEqual(c, "[BaseModel] ({}) {}".format(d, d1))

    def test_assert_save(self):
        """Testing save function"""
        my_model = BaseModel()
        my_model.save()
        key = "BaseModel.{}".format(my_model.id)
        cmp = storage._FileStorage__elmects[key]
        self.assertEqual(my_model.id, cmp.id)
        self.assertTrue(os.path.isfile("file.json"))
        self.assertNotEqual(my_model.created_at, my_model.updated_at)

    def test_assert_to_dict(self):
        """ Test to_dict method """
        a = self.to_dict()
        self.assertIsInstance(a, dict)
        self.assertIsInstance(a['id'], str)
        self.assertIsInstance(a['updated_at'], str)
        self.assertIsInstance(a['created_at'], str)
        self.assertEqual(a['__class__'], self.__class__.__name__)


if __name__ == "__main__":
    unittest.main()
