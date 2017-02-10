#!/usr/bin/python3
"""
Super class that all other objects inherit from.
"""
from datetime import datetime, date
from uuid import uuid4


class BaseModel():
    """
    __init__ method: handles input from other methods that call BaseModel

    save method: Updates the current time with a datetime object and calls
    FileStorage method to update the dictionary

    to_json method: copies, updates, returns dictionary the key value pairs

    __str__ method: returns class name, id, and a dictionary
    """
    def __init__(self, *args, **kwargs):
        formatt = '%Y-%m-%d %H:%M:%S.%f'
        switch = 0
        for arg in args:
            if type(arg) is dict:
                switch = 1
                self.created_at = datetime.strptime(arg["created_at"], formatt)
                self.updated_at = datetime.strptime(arg["updated_at"], formatt)
                self.__dict__ = arg
        if switch == 0:
            self.created_at = datetime.now()
            self.id = str(uuid4())
            from models.__init__ import storage
            storage.new(self)

    def save(self):
        self.updated_at = datetime.now()
        from models.__init__ import storage
        storage.save()

    def to_json(self):
        new = self.__dict__.copy()
        new.update({"__class__": self.__class__.__name__})
        new.update({"created_at": str(self.created_at)})
        new.update({"updated_at": str(self.updated_at)})
        return (new)

    def __str__(self):
        return ("[{}] ({}) {}".format(
            self.__class__.__name__, self.id, self.__dict__)
        )
