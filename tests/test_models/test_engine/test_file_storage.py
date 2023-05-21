#!usr/bin/python3
"""Unittest for FileStorage class"""

import unittest

from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models import storage


class TestFileStorage(unittest.TestCase):
    """Test for FileStorage class"""

    def test_all(self):
        """Test all method"""
        self.assertEqual(type(storage.all()), dict)
        # self.assertEqual(type(storage.all(BaseModel)), dict)
        obj1 = BaseModel()
        obj2 = BaseModel()
        obj3 = BaseModel()
        storage.new(obj1)
        storage.new(obj2)
        storage.new(obj3)
        # self.assertEqual(type(storage.all(BaseModel)), dict)
        key = obj1.__class__.__name__ + "." + obj1.id
        self.assertTrue(key in storage.all())
        key = obj2.__class__.__name__ + "." + obj2.id
        self.assertTrue(key in storage.all())
        key = obj3.__class__.__name__ + "." + obj3.id
        self.assertTrue(key in storage.all())

    def test_new(self):
        """Test new method"""
        base = BaseModel()
        storage.new(base)
        key = base.__class__.__name__ + "." + base.id
        self.assertEqual(storage.all()[key], base)

    def test_save(self):
        """Test save method"""
        base = BaseModel()
        base.save()
        key = base.__class__.__name__ + "." + base.id
        self.assertTrue(key in storage.all())

    def test_reload(self):
        """Test reload method"""
        base = BaseModel()
        base.save()
        storage.reload()
        key = base.__class__.__name__ + "." + base.id
        self.assertTrue(key in storage.all())
