#!/usr/bin/python3
"""File storage module"""

from datetime import datetime
import json
import os.path
from models.base_model import BaseModel
from models.user import User


def attributes(self, classname):
    """Returns the valid attributes and their types for classname."""
    attributes = {
        "BaseModel":
                 {"id": str,
                  "created_at": datetime,
                  "updated_at": datetime},
        "User":
                 {"email": str,
                  "password": str,
                  "first_name": str,
                  "last_name": str},
        "State": {"name": str},
        "City": {"state_id": str, "name": str},
        "Amenity": {"name": str},
        "Place": {"city_id": str,
                  "user_id": str,
                  "name": str,
                  "description": str,
                  "number_rooms": int,
                  "number_bathrooms": int,
                  "max_guest": int,
                  "price_by_night": int,
                  "latitude": float,
                  "longitude": float,
                  "amenity_ids": list},
    }
    return attributes[classname]


class FileStorage:
    """Serializes instances to a JSON file and deserializes JSON file to
    instances"""

    __file_path = "file.json"
    __objects = {}

    def classes(self):
        """Returns a dictionary of valid classes and their references."""
        from models.base_model import BaseModel
        from models.user import User
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review

        classes = {"BaseModel": BaseModel,
                   "User": User,
                   "State": State,
                   "City": City,
                   "Amenity": Amenity,
                   "Place": Place,
                   "Review": Review}
        return classes

    def all(self):
        """Returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""

        FileStorage.__objects[obj.__class__.__name__ + "." + obj.id] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)"""

        new_dict = {}
        for key, value in FileStorage.__objects.items():
            new_dict[key] = value.to_dict()
        with open(FileStorage.__file_path, "w") as f:
            json.dump(new_dict, f)
            return

    def reload(self):
        """Deserializes the JSON file to __objects"""

        if os.path.isfile(FileStorage.__file_path):
            with open(FileStorage.__file_path, "r") as f:
                new_dict = json.load(f)
                for key, value in new_dict.items():
                    class_name = value["__class__"]
                    obj = self.classes()[class_name](**value)
                    FileStorage.__objects[key] = obj
        else:
            pass
