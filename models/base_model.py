#!/usr/bin/python3
"""

"""


from datetime import datetime
from uuid import uuid4
from models import storage
from time import strptime

class BaseModel():
    """

    """
    def __init__(self, *args, **kwargs):
        for arg in args:
            if arg is type(dict):
                self.__dict__ = arg
        self.id = str(uuid4())
        iso_time = str(datetime.now().isoformat())
        self.created_at = strptime(iso_time, '%Y-%m-%dT%H:%M:%S.%f')

    def save(self):
        self.updated_at = datetime.now().isoformat()

    def to_json(self):
        self.__dict__.update({__class__: self.__class__.__name__})
        return (self.__dict__)

    def __str__(self):
        return("[{}] ({}) {}".format(self.__class__.__name__,
                                     str(self.id), self.__dict__))
