#!/usr/bin/python3
"""This module contains the BaseModel class"""
from datetime import datetime
import uuid


class BaseModel:
    """This is the base class"""

    def __init__(self):
        """Initialize a new BaseModel with unique id and timestamps."""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at

    def __setattr__(self, name, value):
        """Automatically updates 'updated_at' when attributes change."""
        self.__dict__[name] = value
        if name != 'updated_at':
            self.__dict__["updated_at"] = datetime.now()

    def save(self):
        """Updates the updated_at timestamp"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """Convert instance to dictionary with ISO format timestamps."""
        new_dict = {}
        new_dict['__class__'] = self.__class__.__name__
        for key, value in self.__dict__.items():
            if key == "updated_at" or key == "created_at":
                new_dict[key] = str(value.isoformat())
            else:
                new_dict[key] = value

        return new_dict

    def __str__(self):
        """Return string representation of the instance."""
        return f'[{self.__class__.__name__}] ({self.id}) {self.__dict__}'
