#!/usr/bin/python3
"""This module contains the FileStorage"""
import json
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State


class FileStorage:
    """This Filestorage class allows for serializing and
    deserializing instances into a JSON file
    """

    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """Returns the dictionary __objects where all instances
        are stored"""
        return self.__objects

    def new(self, obj):
        """saves the object to the dictionary with a unique key"""
        if isinstance(obj, object) and isinstance(obj.id, str):
            self.__objects[f"{obj.__class__.__name__}.{obj.id}"]\
                    = obj

    def save(self):
        """serializes __objects to json string and writes to __file_path"""
        json_objects = {}
        for key, obj in self.__objects.items():
            json_objects[key] = obj.to_dict()
        if len(self.__file_path) != 0:
            with open(f"{self.__file_path}", "w", encoding="utf-8") as f:
                json.dump(json_objects, f, indent=2)

    def reload(self):
        """deserializes the JSON file to __objects if JSON file exists"""
        try:
            with open(f"{self.__file_path}", "r", encoding="utf-8") as f:
                objs = json.load(f)

            for key, value in objs.items():
                class_name = value["__class__"]
                obj = eval(class_name)(**value)
                self.__objects[key] = obj
        except json.decoder.JSONDecodeError:
            pass
        except (OSError, FileNotFoundError):
            pass
