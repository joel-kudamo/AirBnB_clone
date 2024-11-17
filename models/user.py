"""This module contains the User class for processing
user data"""
from datetime import datetime
import uuid
from models import storage
from base_model import BaseModel


class User(BaseModel):
    """This object inherits from the BaseModel class allowing
    user data """