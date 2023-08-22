#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Table
from sqlaclhemy import relationship
from models.place import place_amenity
class Amenity(BaseModel, Base):
    """class definition for amenity"""
    __tablename__ = 'amenities'
    name = Column(String(128), nullable=False)
    place_amenities = relationship('Amenity', secondary=place_amenity, back_populates='place_amenity')
