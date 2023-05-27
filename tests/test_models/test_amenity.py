#!/usr/bin/python3
"""Tests the Amenity class"""
import unittest
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """Tests the Amenity class"""

    def test_init(self):
        """Tests the initialization of the Amenity class"""

        amenity = Amenity()
        self.assertIsInstance(amenity, Amenity)
        self.assertIs(type(amenity), Amenity)
        self.assertTrue(issubclass(type(amenity), Amenity))
        self.assertEqual(amenity.name, "")
