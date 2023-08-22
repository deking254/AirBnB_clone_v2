#!/usr/bin/python3
""""the storage engne for the database"""
import os
from models.base_model import Base
from models.city import City
from models.state import State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker, scoped_session
class DBStorage:
    """the class definon for the storage engine"""
    __engine = None
    __session = None

    def __init__(self):
        """the inital function when DBstorage is initialized"""
        user = os.getenv("HBNB_MYSQL_USER", default="")
        passwd = os.getenv("HBNB_MYSQL_PWD", default="")
        host = os.getenv("HBNB_MYSQL_HOST", default="localhost")
        db = os.getenv("HBNB_MYSQL_DB", default="")
        other = os.getenv("HBNB_ENV")
        engine_def = 'mysql+mysqldb://{}:{}@{}/{}?charset=latin1'
        engne = engine_def.format(user, passwd, host, db)
        self.__engine = create_engine(engne, pool_pre_ping=True)
        if other == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """the function that queries the database for the cls entered"""
        objs = {}
        if cls == None:
            objs_arr = self.__session.query().all())
            for obj in objs_arr:
                objs.update(obj.to_dict()['__class__'] + '.' + obj.id: obj)
            return (objs)

        else:
            if cls == 'State':
                objs = {}
                objs_arr = self.__session.query(State).all()
            	for obj in objs_arr:
                	objs.update(obj.to_dict()['__class__'] + '.' + obj.id: obj)
            	return (objs)
            if cls == 'City':
                objs = {}
                objs_arr = self.__session.query(City).all()
                for obj in objs_arr:
                    objs.update(obj.to_dict()['__class__'] + '.' + obj.id: obj)
                return (objs)
            if cls == 'User':
                objs = {}
                objs_arr = self.__session.query(User).all()
                for obj in objs_arr:
                    objs.update(obj.to_dict()['__class__'] + '.' + obj.id: obj)
                return (objs)
            if cls == 'Amenity':
                objs = {}
                objs_arr = self.__session.query(Amenity).all()
                for obj in objs_arr:
                    objs.update(obj.to_dict()['__class__'] + '.' + obj.id: obj)
                return (objs)
            if cls == 'Place':
                objs = {}
                objs_arr = self.__session.query(Place).all()
                for obj in objs_arr:
                    objs.update(obj.to_dict()['__class__'] + '.' + obj.id: obj)
                return (objs)
            if cls == 'Review':
                objs = {}
                objs_arr = self.__session.query(Review).all()
                for obj in objs_arr:
                    objs.update(obj.to_dict()['__class__'] + '.' + obj.id: obj)
                return (objs)

    def new(self, obj):
        """add the object to the current database session"""
        self.all().update(obj.to_dict()['__class__'] + '.' + obj.id: obj})


    def save(self):
        """commit the changes made to current db session"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete from the current database session"""
        self.all().pop(obj.id);

    def reload(self):
        """create all tables and create session"""
        Base.metadata.create_all(self.__engine)
        self.__session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Scopped_sess = scoped_session(self.__session)
