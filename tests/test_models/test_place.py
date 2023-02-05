#!/usr/bin/python3
"""Unittest for Place"""

import unittest
from models.place import Place
from models.base_model import BaseModel


class TestPlaceClass(unittest.TestCase):
    """Test Place class"""

    def test_is_a_subclass_of_basemodel(self):
        self.place = Place()
        self.assertTrue(issubclass(type(self.place), BaseModel))

    def test_instance(self):
        """test instance."""
        p = Place()
        self.assertIsInstance(p, Place)

    def test_class_attrs(self):
        """Unittests for testing instantiation of the Place class."""
        self.place = Place()

        self.assertIs(type(self.place.name), str)
        self.assertIs(type(self.place.city_id), str)
        self.assertIs(type(self.place.user_id), str)
        self.assertIs(type(self.place.description), str)
        self.assertIs(type(self.place.number_bathrooms), int)
        self.assertIs(type(self.place.max_guest), int)
        self.assertIs(type(self.place.number_rooms), int)
        self.assertIs(type(self.place.price_by_night), int)
        self.assertIs(type(self.place.latitude), float)
        self.assertIs(type(self.place.longitude), float)
        self.assertIs(type(self.place.amenity_ids), list)


if __name__ == "__main__":
    unittest.main()
