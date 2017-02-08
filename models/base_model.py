#!/usr/bin/python3


from datetime import datetime
from uuid import uuid4
import json

class BaseModel():
    def __init__(self):
        self.id = str(uuid4())
        self.created_at = datetime.now().isoformat()

    def save(self):
        self.updated_at = datetime.now().isoformat()

    def to_json(self):
        self.__dict__.update({__class__: self.__class__.__name__})
        return (self.__dict__)

    def __str__(self):
        return("[{}] ({}) {}".format(self.__class__.__name__, str(self.id), self.__dict__))
