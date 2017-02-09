#!/usr/bin/python3
"""

"""
import json
from os.path import isfile

class FileStorage():
    """

    """
    __objects = {}
    __file_path = "file.json"

    def all(self):
        return __objects

    def new(self, obj):
        self.__objects.update({obj.id: obj})

    def save(self):
        with open(__file_path, 'w', encoding="UTF-8") as my_file:
            json.dump(strftime(FileStorage.__objects), my_file)

    def reload(self):
        if isfile(FileStorage.__file_path):
            with open(FileStorage.__file_path, 'r') as myFile:
                return json.load(myFile)
