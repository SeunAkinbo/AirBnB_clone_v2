#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from models.state import State
from models.place import Place

class City(BaseModel, Base):
    """ The city class, contains state ID and name """
    __tablename__ = "cities"

    name = Column("name", String(128), nullable=False)
    state_id = Column("state_id", String(60),
                      ForeignKey(State.id), nullable=False)
    places = relationship("Place", cascade='all, delete, delete-orphan',
                          backref="cities")
