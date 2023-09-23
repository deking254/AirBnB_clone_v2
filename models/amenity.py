#!/usr/bin/python3

"""
Amenity Module for HBNB project.
Defines the Amenity class that represents an amenity data set.
"""

import os
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base


class Amenity(BaseModel, Base):
    """
    Represents an amenity data set.
    """
    __tablename__ = 'amenities'
    
    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        name = Column(String(128), nullable=False)
    else:
        name = ''
