#!/usr/bin/python3
"""This module contains the Review class for processing
Review data"""
from models.base_model import BaseModel


class Review(BaseModel):
    """This object inherits from the BaseModel class"""
    place_id = ""
    user_id = ""
    text = ""