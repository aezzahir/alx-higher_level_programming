#!/usr/bin/python3
"""
The class definition of a City.
"""

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from model_state import Base, State


class City(Base):
    """
    City Class mapped to cities Table
    """
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(128), nullable=True)
    state_id = Column(Integer, ForeignKey('states.id'))

    def __init__(self, name):
        self.name = name
