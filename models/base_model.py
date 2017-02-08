#!/usr/bin/python3
import datetime
class BaseModel():
    def __init__(self, uuid="", name="anomyous"):
        self.uuid = uuid
        self.name = "anomyous"
        self.created_at = datetime.datetime.now()

    def save(self):
        self.updated_at = datetime.datetime.now()

    def __str__(self):
        return()

new = BaseModel()
print(new)
