#!/usr/bin/python3
"""
Creating a class City and inherting from BaseModel
"""
from models.base_model import BaseModel


class City(BaseModel):
    """
    Creating public class attributes that
    can be accessed in subsequent methods.
    """
    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        """
        Initiating the class City to be able to accept arguments
        """
        if (args and type(args[0]) is dict):
            BaseModel.__init__(self, args[0])
        else:
            BaseModel.__init__(self)
