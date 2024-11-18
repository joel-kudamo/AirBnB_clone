#!/usr/bin/python3
"""This module contains the User class for processing
user data"""
from models.base_model import BaseModel


class User(BaseModel):
    """This object inherits from the BaseModel class allowing
    user data """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
    pass
