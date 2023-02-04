""" Test for Amenity """

import unittest
from models.amenity import Amenity
from models.base_model import BaseModel


class AmenityTest(unittest.TestCase):
    """tests for amenities"""

    def test_assert_is_instance(self):
        """ Test init instance is ok """
        a = Amenity()
        self.assertIsInstance(a, Amenity)

    def test_assert_is_subclass(self):
        """ Test amenity is subclass BaseModel """
        a = Amenity()
        self.assertTrue(issubclass(a.__class__, BaseModel), True)

    def test_class_attr(self):
        a = Amenity()
        self.assertIs(type(a.name), str)
        self.assertFalse(bool(getattr(a, "name")))


if __name__ == "__main__":
    unittest.main()
