#!/usr/bin/python3
"""This module contains the city class for processing
city data"""
from models.base_model import BaseModel


class City(BaseModel):
    """This object inherits from the BaseModel class"""
    state_id = ""
    name = ""
    pass
