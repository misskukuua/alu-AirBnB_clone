#!/usr/bin/python3
""" Unittests FileStorage Module"""

import unittest

import pep8

from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
import json
import os
import uuid


class TestFileStorage(unittest.TestCase):
    """ Test FileStorage obj Methods """

    def test_assert_stylepep8_amenity(self):
        """ Test for style model """
        style = pep8.StyleGuide(quiet=True)
        new = style.check_files(['models/engine/file_storage.py'])
        self.assertEqual(new.total_errors, 0, "Error pep8 base model")

    def test_assert_stylepep8_testsamenity(self):
        """ Test for style tests """
        s = pep8.StyleGuide(quiet=True)
        n = s.check_files(
            ['tests/test_models/test_engine/test_file_storage.py'])
        self.assertEqual(n.total_errors, 0, "Error pep8 tests")

    def test_assert_docstring(self):
        """ Test docstring """
        self.assertTrue(len(FileStorage.__doc__) > 1)
        self.assertTrue(len(FileStorage.all.__doc__) > 1)
        self.assertTrue(len(FileStorage.new.__doc__) > 1)
        self.assertTrue(len(FileStorage.save.__doc__) > 1)
        self.assertTrue(len(FileStorage.reload.__doc__) > 1)

    def test_assert_is_instance(self):
        """ Test init instance is ok """
        a = FileStorage()
        self.assertIsInstance(a, FileStorage)

    def test_assert_is_subclass(self):
        """ Test FileStorage is subclss BaseM """
        a = FileStorage()
        self.assertTrue(issubclass(self.a.__class__, BaseModel), True)

    def test_assert_args(self):
        """Test User have args"""
        a = FileStorage(8)
        self.assertEqual(type(a).__name__, "FileStorage")
        self.assertFalse(hasattr(a, "8"))

    def test_assert_save(self):
        """Test save method"""
        a = BaseModel()
        self.assertIsInstance(a, BaseModel)
        self.storage.new(a)
        self.storage.save()
        self.assertTrue(self.storage._FileStorage__file_path)
        self.assertTrue(self.storage._FileStorage__objects)
        self.assertTrue(os.path.isfile(self.storage._FileStorage__file_path))
        key = "BaseModel.{}".format(a.id)
        self.storage._FileStorage__objects = {}
        self.storage.reload()
        self.assertDictEqual(self.storage.all()[key].to_dict(), a.to_dict())


if __name__ == "__main__":
    unittest.main()
