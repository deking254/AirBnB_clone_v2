#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=True)
    cities = relationship('City', back_populates='state', cascade='all, delete-orphan')

    @property
    def cities(self):
        """the getter for cities objects using filestorage"""
        return (self.cities)
