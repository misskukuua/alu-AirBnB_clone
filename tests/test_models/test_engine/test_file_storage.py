#!/usr/bin/python3
import os
import unittest
from os import path

import models
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
import json

""" testing the file storage"""


class TestCaseFileStorage(unittest.TestCase):
    """ class for test cases """

    def set_up(self):
        self.dir_path = 'file.json'
        self.our_model = FileStorage()

    def test_objects(self):
        """Test objects is a dictionary"""
        self.assertTrue(hasattr(FileStorage, "_FileStorage__objects"))
        self.assertEqual(dict, type(FileStorage._FileStorage__objects))

    def test_file_path(self):
        self.assertTrue(hasattr(FileStorage, "_FileStorage__file_path"))
        self.assertEqual(str, type(FileStorage._FileStorage__file_path))

    def test_instance(self):
        """test instance."""
        self.assertIsInstance(self.our_model, FileStorage)

    def tearDown(self):
        """Dispose json """
        try:
            os.remove(self.dir_path)
        except FileNotFoundError:
            pass
        try:
            os.rename(self.dir_path, "tmp")
        except FileNotFoundError:
            pass
        FileStorage._FileStorage__objects = {}

    def test_all(self):
        """ check type return by all function """
        self.assertEqual(type(self.our_model.all()), dict)

    def test_new(self):
        model = BaseModel()
        models.storage.new(model)
        self.assertNotEqual(FileStorage._FileStorage__objects, {})
        obj = (model.__class__.__name__ + '.' +
               model.id)
        self.assertIn(obj, FileStorage._FileStorage__objects.keys())

    # def test_new(self):
    #     model = BaseModel()
    #     self.our_model.new(model)
    #     len_dict = len(self.our_model.all())
    #     self.assertGreater(len_dict, 0)

    def test_save(self):
        self.our_model.save()
        self.assertEqual(path.exists(self.dir_path), True)

    def test_reload_no_file(self):
        self.assertRaises(FileNotFoundError, models.storage.reload())

    def test_reload_with_arg(self):
        with self.assertRaises(TypeError):
            models.storage.reload(None)

    # def test_reload(self):
    #     model = FileStorage()
    #     self.our_model.reload()
    #     len_dict = len(model.all())
    #     self.assertGreater(len_dict, 0)
