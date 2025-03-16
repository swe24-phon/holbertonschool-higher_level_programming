#!/usr/bin/python3
"""Defines the State class and creates the states table"""

from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import relationship
import sys
from sqlalchemy import ForeignKey
from base import Base


class State(Base):
    """Represents a state for a MySQL database"""

    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
    cities = relationship("City", back_populates="state",
                          cascade="all, delete-orphan")
