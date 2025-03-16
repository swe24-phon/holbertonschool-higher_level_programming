#!/usr/bin/python3
"""Defines the State class and creates the states table"""

from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import declarative_base, relationship
from model_city import City
import sys

Base = declarative_base()


class State(Base):
    """Represents a state for a MySQL database"""

    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
