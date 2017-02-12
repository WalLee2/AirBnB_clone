#!/usr/bin/python3
"""
Review class inheriting from a super class BaseModel
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """
    Creating public class attributes and defining an __init__ method.
    """
    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        """Initiating the Review class"""
        if (args and type(args) is dict):
            BaseModel.__init__(self, args[0])
        else:
            BaseModel.__init__(self)
