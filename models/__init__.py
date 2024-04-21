#!/usr/bin/python3
"""This module initializes model package"""
from os import getenv

storage = getenv("HBNB_TYPE_STORAGE")

if storage == "db":
    from models.engine.db_storage import DBStorage
    storage_ = DBStorage()
else:
    from models.engine.file_storage import FileStorage
    storage_ = FileStorage()
storage_.reload()
