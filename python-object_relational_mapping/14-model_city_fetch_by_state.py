#!/usr/bin/python3
"""Script that prints all City objects from the database"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: {} username password database".format(sys.argv[0]))
        sys.exit(1)

    username, password, dbname = sys.argv[1], sys.argv[2], sys.argv[3]
    
    # Create engine and session
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        username, password, dbname
    ))
    
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query cities joined with states
    results = session.query(City, State)\
        .filter(City.state_id == State.id)\
        .order_by(City.id).all()

    # Print results
    for city, state in results:
        print("{}: ({}) {}".format(state.name, city.id, city.name))

    session.close()
