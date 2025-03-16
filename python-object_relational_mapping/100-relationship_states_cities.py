#!/usr/bin/python3
""" creates the State “California” with the City “San Francisco”
    from the database hbtn_0e_100_usa
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from relationship_state import State, Base
from relationship_city import City

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = Session(bind=engine)

    california = State(name="California")
    san_francisco = City(name="San Francisco")
    california.cities.append(san_francisco)

    Session.add(california)
    Session.commit()

    Session.close()