#!/usr/bin/python3
"""Tests the Place class"""

import unittest
from models.place import Place


class TestPlace(unittest.TestCase):
    """Tests the Place class"""

    def test_init(self):
        """Tests the init method"""
        place = Place()
        self.assertIs(type(place.city_id), str)
        self.assertIs(type(place.user_id), str)
        self.assertIs(type(place.name), str)
        self.assertIs(type(place.description), str)
        self.assertIs(type(place.number_rooms), int)
        self.assertIs(type(place.number_bathrooms), int)
        self.assertIs(type(place.max_guest), int)
        self.assertIs(type(place.price_by_night), int)
        self.assertIs(type(place.latitude), float)
        self.assertIs(type(place.longitude), float)
        self.assertIs(type(place.amenity_ids), list)
        self.assertEqual(place.city_id, "")
        self.assertEqual(place.user_id, "")
        self.assertEqual(place.name, "")
        self.assertEqual(place.description, "")
        self.assertEqual(place.number_rooms, 0)
        self.assertEqual(place.number_bathrooms, 0)
        self.assertEqual(place.max_guest, 0)
        self.assertEqual(place.price_by_night, 0)
        self.assertEqual(place.latitude, 0.0)
        self.assertEqual(place.longitude, 0.0)
        self.assertEqual(place.amenity_ids, [])
