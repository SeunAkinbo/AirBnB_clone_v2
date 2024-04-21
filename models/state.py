#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from models.city import City
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from os import getenv
import models
import shlex


class State(BaseModel, Base):
    """ State class
    Inherits:
        BaseModel, Base
    """
    if getenv("HBNB_TYPE_STORAGE") == "db":
        __tablename__ = "states"
        name = Column("name", String(128), nullable=False)
        cities = relationship("City", cascade="all, delete, delete-orphan",
                              backref="state")
    else:
        @property
        def cities(self):
            data = models.storage.all()
            city_list = []
            output = []
            for key in data:
                city = key.replace('.', ' ')
                city = shlex.split(city)
                if (city[0] == 'City'):
                    city_list.append(data[key])
            for city in city_list:
                if city.state_id == self.id:
                    output.append(city)
            return output
