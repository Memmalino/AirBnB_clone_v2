#!/usr/bin/python3
""" State Module for HBNB project """
import models
from os import getenv
from models.base_model import BaseModel
from models.base_model import Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

class State(BaseModel, Base):
    """This is the class for State
    Attributes:
        __tablename__: table name
        name: input name
        cities: relation to cities table
    """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("City", cascade="all, delete", backref="state")

    if env.get('HBNB_TYPE_STORAGE') != 'db':
        @property
        def cities(self):
            """get all cities with the current state id
            from filestorage
            """
            l = [
                v for k, v in models.storage.all(models.City).items()
                if v.state_id == self.id
            ]
            return (l)
