#!/usr/bin/python3
import datetime, uuid
class BaseModel():
    def __init__(self, uuid=, name="anomyous"):
        self.uuid = uuid
        self.name = "anomyous"
        self.created_at = "{}".format(datetime.datetime.now().isoformat())
        self.updated_at = "{}".format(datetime.datetime.now().isoformat())

	@setter.save
    def save(self):
        self.updated_at = datetime.datetime.now()

    def __str__(self):
        return("[{}] {} {}".format(type(self), self.uuid, BaseModel().__dict__))

new = BaseModel()
print(new)
