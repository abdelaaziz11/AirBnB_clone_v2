#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.city import City
from os import getenv

STORAGE = getenv("HBNB_TYPE_STORAGE")


class State(BaseModel, Base):
    """ State class """

    __tablename__ = "states"
    if STORAGE == "db":
        name = Column(String(128), nullable=False)
        cities = relationship("City",
            backref="state",
            single_parent=True)
    else:
        name = ""
