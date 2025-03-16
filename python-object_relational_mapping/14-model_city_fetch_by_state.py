#!/usr/bin/python3
"""
Prints all City objects from the database hbtn_0e_14_usa.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City


if __name__ == "__main__":
    # Check if the script is being run directly
    if __name__ == "__main__":
        # Get MySQL credentials and database name from command line arguments
        mysql_username = sys.argv[1]
        mysql_password = sys.argv[2]
        database_name = sys.argv[3]

        # Create engine
        engine = create_engine(
            'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
                mysql_username, mysql_password, database_name),
            pool_pre_ping=True
        )

        # Create a session
        Session = sessionmaker(bind=engine)
        session = Session()

        # Fetch all City objects and sort by cities.id
        cities = session.query(City).order_by(City.id).all()

        # Print the City objects in the specified format
        for city in cities:
            state_name = session.query(State.name).filter(
                State.id == city.state_id).scalar()
            print("{}: ({}) {}".format(state_name, city.id, city.name))

        # Close the session
        session.close()
