#!/usr/bin/python3
"""Defines the City class"""
from models.base_model import BaseModel


class City(BaseModel):
    """Represent a city class
    Attributes:
        state_id (str): The state id.
        name (str): The city name.
    """

    state_id = ""
    name = ""
