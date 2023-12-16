#!/usr/bin/python3
"""
Improved State Class 'Relationship'
"""

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
Base = declarative_base()


class State(Base):
    """
    Improved State Class Mapped to states Table
    """
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(128), nullable=True)
    cities = relationship("City", back_populates="state")

    def __init__(self, name):
        self.name = name
