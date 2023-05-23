#!/usr/bin/python3
"""Tests the City class"""
import unittest
from models.city import City


class TestCity(unittest.TestCase):
    """Tests the City class"""

    def test_init(self):
        """Tests the init method"""
        city = City()
        self.assertIs(type(city.state_id), str)
        self.assertIs(type(city.name), str)
        self.assertEqual(city.state_id, "")
        self.assertEqual(city.name, "")
