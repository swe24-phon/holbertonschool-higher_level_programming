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


if __name__ == "__main__":
    # Create an engine that connects to the MySQL server
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
            sys.argv[1], sys.argv[2], sys.argv[3]),
        pool_pre_ping=True
    )

    # Create all tables in the database
    Base.metadata.create_all(engine)
