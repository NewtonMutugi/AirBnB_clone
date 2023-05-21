#!/usr/bin/python3
"""Test for base_model"""

from datetime import datetime
import json
import unittest

from models.base_model import BaseModel
from uuid import UUID


class TestBaseModel(unittest.TestCase):
    """Test for BaseModel"""

    def __init__(self, *args, **kwargs):
        """ test constructor """
        super().__init__(*args, **kwargs)
        self.name = 'BaseModel'
        self.value = BaseModel

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
        self.name = 'BaseModel'
        self.value = BaseModel
        n = self.value()
        n.save()
        key = self.name + "." + n.id
        with open('file.json', 'r') as f:
            j = json.load(f)
            self.assertEqual(j[key], n.to_dict())

    def test_to_dict(self):
        """Test to_dict"""
        self.base.name = "Name"
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

    def test_kwargs(self):
        """Test kwargs"""
        self.base.name = "Person"
        self.base.my_number = 89
        self.base_json = self.base.to_dict()
        base2 = BaseModel(**self.base_json)
        self.assertEqual(self.base.id, base2.id)
        self.assertEqual(self.base.created_at, base2.created_at)
        self.assertEqual(self.base.updated_at, base2.updated_at)
        self.assertEqual(self.base.name, base2.name)
        self.assertEqual(self.base.my_number, base2.my_number)
        self.assertIsNot(self.base, base2)
        self.assertIsInstance(base2.created_at, datetime)
        self.assertIsInstance(base2.updated_at, datetime)

    def test_kwargs_empty(self):
        """Test kwargs empty"""
        base2 = BaseModel()
        base2.name = "Name"
        base2.my_number = 89
        base2_json = base2.to_dict()
        base3 = BaseModel(**base2_json)
        self.assertEqual(base2.id, base3.id)
        self.assertEqual(base2.created_at, base3.created_at)
        self.assertEqual(base2.updated_at, base3.updated_at)
        self.assertEqual(base2.name, base3.name)
        self.assertEqual(base2.my_number, base3.my_number)
        self.assertIsNot(base2, base3)
        self.assertIsInstance(base3.created_at, datetime)
        self.assertIsInstance(base3.updated_at, datetime)
