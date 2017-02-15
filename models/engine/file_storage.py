#!/usr/bin/python3
"""
Saving and reloading a file. Converting text to strings
in the saving process and then converting the strings
into objects when reloading the file.
"""
from datetime import datetime
import json
from os.path import isfile
import models


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
        for key in FileStorage.__objects.keys():
            if type(FileStorage.__objects[key]) is not dict:
                my_dict = FileStorage.__objects[key].to_json()
                new_cp.update({key: my_dict})
            else:
                new_cp.update({key: my_dict[key]})
                new_cp.update({'created_at': str(new_cp[key]['created_at'])})
                new_cp.update({'updated_at': str(new_cp[key]['updated_at'])})
        with open(FileStorage.__file_path, 'w', encoding="UTF-8") as my_file:
            json.dump(new_cp, my_file)

    def reload(self):
        """
        Opening a file in read only mode
        and converting the text back to objects
        """
        if isfile(FileStorage.__file_path):
            with open(FileStorage.__file_path, 'r', encoding="UTF-8") as File:
                load = json.load(File)
                for key in load.keys():
                    c_name = load[key]['__class__']
                    new_BM = self.__checker(load[key]['__class__'],
                                            (load[key]))
                    load.update({key: new_BM})

    def __checker(self, Class, key):
        """
        checks if class is valid and returns the result
        """
        from models.amenity import Amenity
        from models.base_model import BaseModel
        from models.city import City
        from models.place import Place
        from models.review import Review
        from models.state import State
        from models.user import User
        class_check = {"Amenity": Amenity, "BaseModel": BaseModel,
                       "City": City, "Place": Place, "Review": Review,
                       "State": State, "User": User}
        if Class not in class_check.keys():
            print("** class doesn't exist **")
            return None
        else:
            return class_check[Class]
