#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String


class User(BaseModel, Base):
    __tablename__ = "users"
    """This class defines a user by various attributes"""
    email = Column("email", String(128), nullable=False)
    password = Column("email", String(128), nullable=False)
    first_name = Column("email", String(128), nullable=False)
    last_name = Column("email", String(128), nullable=False)
