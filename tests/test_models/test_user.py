#!/usr/bin/python3

"""Unittest for User."""

import unittest

from models.user import User

from models.base_model import BaseModel

class TestUser(unittest.TestCase):
    """Test user class."""

    def test_instance(self):
        """test instance."""
        u = User()
        self.assertIsInstance(u, User)

    def test_is_class(self):
        """test instance."""
        u = User()
        self.assertEqual(str(type(u)), "<class 'models.u.User'>")

    def test_is_subclass(self):
        """test is_subclass."""
        u = User()
        self.assertTrue(issubclass(type(u), BaseModel))

    def test_id(self):
        """test id"""
        our_user = User()
        self.assertIsNotNone(our_user.id)

    def test_email(self):
        """test email"""
        our_user = User()
        self.assertEqual(our_user.email, "")
        our_user.email = "airbnb@mail.com"
        self.assertEqual(our_user.email, "airbnb@mail.com")

    def test_password(self):
        """test password"""
        our_user = User()
        self.assertEqual(our_user.password, "")
        our_user.password = "root"
        self.assertEqual(our_user.password, "root")

    def test_first_name(self):
        """test first name"""
        our_user = User()
        self.assertEqual(our_user.first_name, "")
        our_user.first_name = "Betty"
        self.assertEqual(our_user.first_name, "Betty")

    def test_last_name(self):
        """test last name"""
        our_user = User()
        self.assertEqual(our_user.last_name, "")
        our_user.last_name = "Bar"
        self.assertEqual(our_user.last_name, "Bar")

if __name__ == "__main__":
    unittest.main()
