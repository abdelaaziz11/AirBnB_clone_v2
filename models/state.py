#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.city import City
from os import getenv
import models

STORAGE = getenv("HBNB_TYPE_STORAGE")


class State(BaseModel, Base):
    """ State class """

    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("City", cascade="delete", backref="state")

    if STORAGE != "db":
        @property
        def cities(self):
            """ cities getter attribute """
            cit_lis = []
            all_cit = models.storage.all(City)
            for city in all_cit.values():
                if city.state_id == self.id:
                    cit_lis.append(city)
            return cit_lis
