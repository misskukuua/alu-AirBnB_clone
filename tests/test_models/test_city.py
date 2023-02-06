#!/usr/bin/python3
""" Unittest for test_city """

import unittest

from models.base_model import BaseModel
from models.city import City


class TestCity(unittest.TestCase):
    """Test cases for the City class"""

    def test_assert_is_instance(self):
        """ Test init instance is ok """
        c = City()
        self.assertIsInstance(c, City)

    def test_is_subclass(self):
        """test is_subclass."""
        c = City()
        self.assertTrue(issubclass(type(c), BaseModel))

    def test_is_class(self):
        """test instance."""
        c = City()
        self.assertEqual(str(type(c)), "<class 'models.c.City'>")

    def test_state_id(self):
        """ Test field attributes of user """
        c = City()
        self.assertTrue(type(c.state_id) == str)

    def test_name(self):
        """ Test field attributes of user """
        c = City()
        self.assertTrue(type(c.name) == str)


if __name__ == "__main__":
    unittest.main()
