#!/usr/bin/python3
"""
A class BaseModel to define all attributes and methods
for other classes
"""
import uuid
from datetime import datetime
import models

class BaseModel:
    """ Public instance attributes """
    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """ Returning an instance attribute of the class """
        return f"[{__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """ Updates the current date """
        self.updated_at = datetime.now()

    def to_dict(self):
        """ Returns dictionary containing key/values of instance """
        dict_info = dict(self.__dict__)
        dict_info['created_at'] = self.created_at.isoformat()
        dict_info['updated_at'] = self.updated_at.isoformat()
        dict_info['__class__'] = __class__.__name__
        return dict_info
