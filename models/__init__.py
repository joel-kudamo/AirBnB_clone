"""This module initializes the folder as a package and creates a unique FileStorage instance"""
from models.engine.file_storage import FileStorage


storage = FileStorage
storage.reload()