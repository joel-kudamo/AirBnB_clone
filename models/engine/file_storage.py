#!/usr/bin/python3
"""This module contains the FileStorage"""
import json


class FileStorage:
    """This Filestorage allows for serializing and 
    deserializing instances into a JSON file
    """

    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """Returns the path to json file where json objects will be stored"""
        return self.__file_path

    def new(self, obj):
        """saves the object to the dictionary with a unique key"""
        if isinstance(obj, object) and isinstance(obj.id, str):
            self.__objects[f"{obj.__class__.__name__}.{obj.id}"]

    def save(self):
        pass

    def reload(self):
        """deserializes the JSON file to __objects if JSON file exists"""




