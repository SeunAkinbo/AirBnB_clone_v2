#!/usr/bin/python3
"""Module - db_storage"""

from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base
from models.state import State
from models.city import City


class DBStorage:
    """The database class that initiates all the methods"""
    __engine = None
    __session = None

    def __init__(self):
        username = getenv("HBNB_MYSQL_USER")
        password = getenv("HBNB_MYSQL_PWD")
        db_name = getenv("HBNB_MYSQL_DB")
        host = getenv("HBNB_MYSQL_HOST")
        env = getenv("HBNB_ENV")

        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(
                        username, passwordd, host, db_name),
                        pool_pre_ping=True))

        if env == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Queries current database with the classname
        Args:
            -cls
        """
        obj = {}
        if cls is not None:
            objs = self.__session.query(cls)
            for item in objs:
                key = "{}.{}".format(type(item).__name__, item.id)
                obj[key] = item
        else:
            obj_list = [User, State, City, Amenity, Place and Review]
            for cls_item in obj_list:
                items = self.__session.query(cls_item)
                for item in items:
                    key = "{}.{}".format(type(item).__name__, item.id)
                obj[key] = item
        return obj

    def new(self, obj):
        """Add the object to the current database"""
        self.__session.add(obj)

    def save(self):
        """Commits all changes to the databse"""
        self.__session.commit()

    def delete(self, obj=None):
        """Deletes obj from the database if not none"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """Creates tables in the database"""
        Base.metadata.create_all(self.__engine)
        sess_fctry = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(sess_fctry)
        self.__session = Session()

    def close(self):
        """Closes all sessions"""
        self.__session.close()
