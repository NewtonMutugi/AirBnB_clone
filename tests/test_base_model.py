#!/usr/bin/python3
"""Test for base_model"""

from datetime import datetime
import unittest

from models.base_model import BaseModel
from uuid import UUID


class TestBaseModel(unittest.TestCase):
    """Test for BaseModel"""

    def setUp(self):
        """Set up test methods"""
        self.base = BaseModel()

    def test_id(self):
        """Test id"""
        self.assertTrue(hasattr(self.base, "id"))
        self.assertIsInstance(self.base.id, str)
        self.assertNotEqual(self.base.id, "")
        self.assertEqual(type(UUID(self.base.id)), UUID)

    def test_created_at(self):
        """Test created_at"""
        self.assertTrue(hasattr(self.base, "created_at"))
        self.assertIsInstance(self.base.created_at, datetime)

    def test_updated_at(self):
        """Test updated_at"""
        self.assertTrue(hasattr(self.base, "updated_at"))
        self.assertIsInstance(self.base.updated_at, datetime)

    def test_str(self):
        """Test __str__"""
        self.assertEqual(str(self.base),
                         "[{}] ({}) {}".format(
            self.base.__class__.__name__, self.base.id, self.base.__dict__))

    def test_save(self):
        """Test save"""
        self.base.save()
        self.assertNotEqual(self.base.created_at, self.base.updated_at)

    def test_to_dict(self):
        """Test to_dict"""
        self.base.name = "Holberton"
        self.base.my_number = 89
        self.base_json = self.base.to_dict()
        self.assertEqual(self.base_json["id"], self.base.id)
        self.assertEqual(self.base_json["__class__"],
                         self.base.__class__.__name__)
        self.assertEqual(self.base_json["created_at"],
                         self.base.created_at.isoformat())
        self.assertEqual(self.base_json["updated_at"],
                         self.base.updated_at.isoformat())
        self.assertEqual(self.base_json["name"], self.base.name)
        self.assertEqual(self.base_json["my_number"], self.base.my_number)
        self.assertEqual(type(self.base_json["created_at"]), str)
        self.assertEqual(type(self.base_json["updated_at"]), str)
