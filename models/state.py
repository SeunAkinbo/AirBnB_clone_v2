#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models import storage
from models.city import City
import shlex


class State(BaseModel, Base):
    """ State class
    Inherits:
        BaseModel, Base
    """
    __tablename__ = "states"
    name = Column("name", String(128), nullable=False)
    cities = relationship("City", cascade="all, delete, delete-orphan",
                          backref="state")

    @property
    def cities(self):
        data = storage.all()
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
