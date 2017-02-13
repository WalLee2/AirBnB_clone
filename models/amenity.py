#!/usr/bin/python3
"""
Creating a class Amenity that inherits from BaseModel
"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    Creating a public class attribute that can be used in all methods
    """
    name = ""

    def __init__(self, *args, **kwargs):
        """
        Initiating the class Amenity to be able to accept arguments
        """
        if (args and type(args) is dict):
            BaseModel.__init__(self, args[0])
        else:
            BaseModel.__init__(self)
