#!/usr/bin/python3
"""Defines the Place class"""
from models.base_model import BaseModel


class Place(BaseModel):
    """Represent a place class
    Attributes:
        city_id (str): The city id.
        user_id (str): The user id.
        name (str): The place name.
        description (str): The place description.
        number_rooms (int): The number of rooms.
        number_bathrooms (int): The number of bathrooms.
        max_guest (int): The maximum number of guests.
        price_by_night (int): The price by night.
        latitude (float): The place latitude.
        longitude (float): The place longitude.
        amenity_ids (list): A list of amenity ids.
    """

    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = float(0)
    longitude = float(0)
    amenity_ids = []
