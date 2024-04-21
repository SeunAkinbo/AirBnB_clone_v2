#!/usr/bin/python3
"""This module initializes model package"""
from os import getenv
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


storage = getenv("HBNB_TYPE_STORAGE")

if storage == "db":
    from models.engine.db_storage import DBStorage
    storage_ = DBStorage()
else:
    from models.engine.file_storage import FileStorage
    storage_ = FileStorage()
storage_.reload()
