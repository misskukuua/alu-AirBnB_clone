#!/usr/bin/python3
"""Defines unittests for models/engine/file_storage.py."""

import unittest

import models
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
import os
import json


class TestFileStorage(unittest.TestCase):
    def setUp(self):
        self.storage = FileStorage()

    def tearDown(self):
        """Code to execute after tests are executed"""
        # Remove file.json if it exists
        try:
            os.remove("file.json")
        except IOError:
            pass

        # rename tmp.json from setUp() to file.json
        try:
            os.rename("tmp.json", "file.json")
        except IOError:
            pass

        FileStorage._FileStorage__objects = {}

    def test_all(self):
        self.assertEqual(type(self.storage.all()), dict)

    def test_new(self):
        test_model = BaseModel()
        self.storage.new(test_model)
        len_dict = len(self.storage.all())
        self.assertGreater(len_dict, 0)

    def test_instance(self):
        """ Check storage """
        self.assertIsInstance(models.storage, FileStorage)

