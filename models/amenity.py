#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Table
from sqlalchemy.orm import relationship
from models.place import Place
class Amenity(BaseModel, Base):
    """class definition for amenity"""
    __tablename__ = 'amenities'
    name = Column(String(128), nullable=False)
    place_amenities = relationship('Amenity', secondary=Place.place_amenity, back_populates='place_amenity')
