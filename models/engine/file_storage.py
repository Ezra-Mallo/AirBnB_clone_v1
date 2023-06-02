#!/usr/bin/python3
import json
from models.base_model import BaseModel


class FileStorage:
    """
    Defines FileStorage class

    Attributes:
        __file_path = string, private, file name
        __objects = Dictionary, empty but will grow with value
    """
    __file_path = "file.json"
    __objects = {}

    def __init__(self):
        """Initialization"""
        pass

    def all(self):
        """
        returns the dictionary __objects
        """
        # return (FileStorage.__objects)
        return (self.__objects)

    def new(self, obj):
        """
        sets in __objects the obj with key <obj class name>.id
        """
        my_key = ("{}.{}".format(obj.__class__.__name__, obj.id))
        # FileStorage.__objects[my_key] = obj
        self.__objects[my_key] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        with open(FileStorage.__file_path, "w", encoding="utf-8") as file:
            dict_value = {key: value.to_dict() for key,
                          value in FileStorage.__objects.items()}
            """
            dict_value = {key: value.to_dict() for key,
                          value in self.__objects.items()}
            """
            json.dump(dict_value, file)

    def reload(self):
        """deserializes the JSON file to __objects
        (only if the JSON file (__file_path) exists; otherwise, do nothing.
        If the file doesn’t exist, no exception should be raised)"""
