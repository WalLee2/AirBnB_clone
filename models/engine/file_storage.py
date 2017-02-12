#!/usr/bin/python3
"""
Saving and reloading a file. Converting text to strings
in the saving process and then converting the strings
into objects when reloading the file.
"""
from datetime import datetime
import json
from os.path import isfile


class FileStorage():
    """
    all method: Returns the object

    new method: updates the dictionary id

    save method: Serializes, or converts Python objects into JSON strings.
    reload method: Deserializes, or converts JSON strings
    into Python objects.
    """
    __objects = {}
    __file_path = "file.json"

    def all(self):
        """
        Returning the dictionary
        """
        return FileStorage.__objects

    def new(self, obj):
        """
        Updating a dictionary
        """
        self.__objects.update({obj.id: obj})

    def save(self):
        """
        Updating a dictionary and writing to a file in string format
        """
        new_cp = {}
        for key in FileStorage.__objects:
            if type(FileStorage.__objects[key]) is not dict:
                new_cp.update({key: FileStorage.__objects[key].to_json()})
            else:
                new_cp.update({key: FileStorage.__objects[key]})
                new_cp.update({'created_at': str(new_cp[key]['created_at'])})
                new_cp.update({'updated_at': str(new_cp[key]['updated_at'])})
        with open(FileStorage.__file_path, 'w', encoding="UTF-8") as my_file:
            json.dump(new_cp, my_file)

    def reload(self):
        """
        Opening a file in read only mode and converting the text back to objects
        """
        if isfile(FileStorage.__file_path):
            with open(FileStorage.__file_path, 'r', encoding="UTF-8") as File:
                FileStorage.__objects = json.load(File)
                from models.base_model import BaseModel
                for key in FileStorage.__objects.keys():
                    new_BM = BaseModel(FileStorage.__objects[key])
                    FileStorage.__objects.update({key: new_BM})
