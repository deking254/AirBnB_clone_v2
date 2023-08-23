#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, Float, ForeignKey, Table
from sqlalchemy.orm import relationship
class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = 'places'
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name =  Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True) 
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    amenity_ids = []
    reviews = relationship('Review', back_populates='place', cascade='all, delete-orphan')
    place_amenity = Table('place_amenity', Base.metadata,
    Column('place_id', String(60), ForeignKey('places.id'), primary_key=True, nullable=False),
    Column('amenity_id', ForeignKey('amenities.id'), primary_key=True, nullable=False))
    amenities = relationship('Amenity', secondary=place_amenity, back_populates='place_amenities', viewonly=False)

    @property
    def reviews(self):
        """returns the values in the reviews attribute"""
        from models import storage
        review_place = []
        """all_reviews = storage.all()
        for revew in all_reviews:
            if revew.id == self.id:
                review_place.append(revew)"""
        return (review_place)


    @property
    def amenities(self):
        """returns the values in the amenity_ids attribute"""
        amenties_place = []
        from models import storage
        all_objs = storage.all()
        for obj in all_objs:
            pass
    
    @amenities.setter
    def amenities(self, obj=None):
        """appends the ids to the class attribute amenity_ids"""
        if type(obj) == Amenity:
            self.amenity_ids.append(obj.id)
