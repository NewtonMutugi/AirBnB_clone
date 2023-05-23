#!/usr/bin/python3
"""Tests the state class"""
import unittest
from models.state import State


class TestState(unittest.TestCase):
    """Tests the state class"""

    def test_init(self):
        """Tests the init method"""
        state = State()
        self.assertIs(type(state.name), str)
        self.assertEqual(state.name, "")
