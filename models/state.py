#!/usr/bin/python3
"""
Creating the class State and inheriting from BaseModel
"""
from models.base_model import BaseModel


class State(BaseModel):
    """
    Creating a public instance which can be accessed in subsequent methods
    """
    name = ""

    def __init__(self, *args, **kwargs):
        """
        Initiating the class State to be able to accept arguments
        """
        if (args and type(args) is dict):
            BaseModel.__init__(self, args[0])
        else:
            BaseModel.__init__(self)
