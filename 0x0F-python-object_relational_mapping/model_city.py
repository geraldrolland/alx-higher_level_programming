#!/usr/bin/python2

"""
This scripts create the table City
"""

from model_state import Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String, Integer, ForeignKey


class City(Base):
    __tablename__ = "cities"
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128))
    state_id = Column(Integer, ForeignKey("states.id"))
