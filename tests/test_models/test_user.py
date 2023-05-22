#!/usr/bin/python3
"""Unittest for User class"""

import datetime
import unittest

from models.user import User


class TestUser(unittest.TestCase):
    """Test cases for User"""

    def test_user(self):
        """Test for User class"""
        u = User()
        self.assertIsInstance(u, User)
        self.assertTrue(hasattr(u, "email"))
        self.assertTrue(hasattr(u, "password"))
        self.assertTrue(hasattr(u, "first_name"))
        self.assertTrue(hasattr(u, "last_name"))
        self.assertEqual(u.email, "")
        self.assertEqual(u.password, "")
        self.assertEqual(u.first_name, "")
        self.assertEqual(u.last_name, "")
        self.assertTrue(hasattr(u, "id"))
        self.assertTrue(hasattr(u, "created_at"))
        self.assertTrue(hasattr(u, "updated_at"))
        self.assertTrue(type(u.id), str)
        self.assertTrue(type(u.created_at), datetime.datetime)
        self.assertTrue(type(u.updated_at), datetime.datetime)
