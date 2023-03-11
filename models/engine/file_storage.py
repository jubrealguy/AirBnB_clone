#!/usr/bin/python3
"""
Store the dictionary representation to a JSON string in a JSON file
"""

from models.base_model import BaseModel
import json
import os


class FileStorage:
    """
    This class serializes instances to a JSON file and
    deserializes JSON file to instances
    """
    __file_path = "file.json"
    __objects = {}
    classes = {"BaseModel": BaseModel}

    def all(self):
        """ Returns dictionary object """
        return FileStorage.__objects

    def new(self, obj):
        """ sets a new formatted key and pair with
        the value then store in dictionary """
        k = obj.__class__.__name__ + '.' + obj.id
        FileStorage.__objects[k] = obj

    def save(self):
        """ serialization of objects """
        obj_file = {}
        for k, v in FileStorage.__objects.items():
            obj_file[k] = v.to_dict()

        with open(FileStorage.__file_path, 'w') as file:
            json.dump(obj_file, file)

    def reload(self):
        """ Deserializes the object (json to dict) """
        data = {}
        if os.path.isfile(FileStorage.__file_path):
            with open(FileStorage.__file_path, 'r') as file:
                data = json.load(file)

            for k, v in data.items():
                obj_classname, obj_id = k.split('.')
                class_name = FileStorage.classes[obj_classname]
                obj = class_name(**v)
                FileStorage.__objects[k] = obj

        else:
            return
