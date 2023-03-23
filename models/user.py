#!/usr/bin/python3

"""
A module that defines the ORM class for User table
"""
from models.base_model import Base, BaseModel
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class User(BaseModel, Base):
    """
    Defines attributes for User table
    """
    __tablename__ = 'users'

    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128), nullable=True)
    last_name = Column(String(128), nullable=True)
    places = relationship(
            'Place', backref='user', cascade='all, delete, delete-orphan')
    reviews = relationship(
            'Review', backref='user', cascade='all, delete, delete-orphan')