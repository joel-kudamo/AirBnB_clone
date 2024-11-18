#!/usr/bin/python3
"""This module initializes the folder as a package
and creates a unique FileStorage instance"""
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel

storage = FileStorage()
storage.reload()
