#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Table, Column, String, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship
from os import getenv
import models


place_amenity = Table("place_amenity", Base.metadata,
                      Column("place_id", String(60),
                             ForeignKey("places.id"),
                             primary_key=True,
                             nullable=False),
                      Column("amenity_id", String(60),
                             ForeignKey("amenities.id"),
                             primary_key=True,
                             nullable=False)
                      )


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = "places"
    
    city_id = Column("city_id", String(60), ForeignKey("cities.id"),
                     nullable=False)
    user_id = Column("user_id", String(60), ForeignKey("users.id"),
                     nullable=False)
    name = Column("name", String(128), nullable=False)
    description = Column("description", String(1024))
    number_rooms = Column("number_rooms", Integer, nullable=False, default=0)
    number_bathrooms = Column("number_bathrooms", Integer,
                              nullable=False, default=0)
    max_guest = Column("max_guest", Integer, nullable=False, default=0)
    price_by_night = Column("price_by_night", Integer,
                            nullable=False, default=0)
    latitude = Column("latitude", Float)
    longitude = Column("longitude", Float)
    amenity_ids = []

    if getenv("HBNB_TYPE_STORAGE") == "db":
        reviews = relationship("Review", cascade='all, delete, delete-orphan',
                               backref="place")

        amenities = relationship("Amenity",
                                 secondary= place_amenity,
                                 viewonly=False,
                                 back_populates="place_amenities") 
    else:
        @property
        def reviews(self):
            """ Returns list of reviews.id """
            records = models.storage.all()
            review_list = []
            output = []
            for item in records:
                review = item.replace('.', ' ')
                review = shlex.split(review)
                if review[0] == 'Review':
                   review_list.append(var[item])
            for item in review_list:
                if item.place_id == self.id:
                    output.append(item)
            return output

        @property
        def amenities(self):
            """Returns list of amenity_ids"""
            return self.amenity_ids

        @amenities.setter
        def amenities(self, obj=None):
            """Appends new amenity ids to the amenity_ids list"""
            if type(obj) is Amenity and obj.id not in self.amenity_ids:
                self.amenity_ids.append(obj.id)
