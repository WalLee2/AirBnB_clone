#!/usr/bin/python3
"""
Creating a class: Place that inherits from BaseModel super class.
"""
from models.base_model import BaseModel


class Place(BaseModel):
    """
    Creating public class attributes that can be used in methods.
    """
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenities = []

    def __init__(self, *args, **kwargs):
        """Initiating the class"""
        if (args and type(args) is dict):
            BaseModel.__init__(self, args[0])
        else:
            BaseModel.__init__(self)
