#!/usr/bin/python3

"""Unittest for Review Class."""

import unittest

from models.review import Review
from models.base_model import BaseModel


class TestState(unittest.TestCase):
    """Test cases Review class."""

    def test_assert_is_instance(self):
        """test instance."""
        review = Review()
        self.assertIsInstance(review, Review)

    def test_is_class(self):
        """test is class"""
        review = Review()
        self.assertEqual(str(type(review)), "<class 'models.review.Review'>")

    def test_is_subclass(self):
        """test is_subclass."""
        review = Review()
        self.assertTrue(issubclass(type(review), BaseModel))

    def test_place_id(self):
        """Place id"""
        review = Review()
        self.assertEqual(review.place_id, "")

    def test_user_id(self):
        """user id"""
        review = Review()
        self.assertEqual(review.user_id, "")

    def test_place(self):
        """Place text"""
        review = Review()
        self.assertEqual(review.text, "")


if __name__ == "__main__":
    unittest.main()
