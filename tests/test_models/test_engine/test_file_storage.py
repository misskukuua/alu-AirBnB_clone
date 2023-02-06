#!/usr/bin/python3
import os
import unittest
from os import path
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage

""" testing the file storage"""


class TestCaseFileStorage(unittest.TestCase):
    """ class for test cases """

    def set_up(self):
        self.dir_path = 'file.json'
        self.our_model = FileStorage()

    def dispose_json(self):
        """ dispose json file """
        if path.exists(self.dir_path):
            os.remove(self.dir_path)

    def test_all(self):
        """ check type return by all function """
        self.assertEqual(type(self.our_model.all()), dict)

    def test_new(self):
        model = BaseModel()
        self.our_model.new(model)
        len_dict = len(self.our_model.all())
        self.assertGreater(len_dict, 0)

    def test_save(self):
        self.our_model.save()
        self.assertEqual(path.exists(self.dir_path), True)

    def test_reload(self):
        model = FileStorage()
        self.our_model.reload()
        len_dict = len(model.all())
        self.assertGreater(len_dict, 0)
