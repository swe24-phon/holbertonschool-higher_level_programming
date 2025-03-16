#!/usr/bin/python3
"""Script that prints the first State object from the database hbtn_0e_6_usa"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":
    # Check for correct number of arguments
    if len(sys.argv) != 3:
        print("Usage: {} username password".format(sys.argv[0]))
        sys.exit(1)

    # Create connection to MySQL server
    username, password = sys.argv[1], sys.argv[2]
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost:3306/test_7'.format(
            username, password
        ),
        pool_pre_ping=True
    )

    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)

    # Create a Session
    session = Session()

    # Query the first State object ordered by id
    first_state = session.query(State).order_by(State.id).first()

    # Print the result or "Nothing" if table is empty
    if first_state:
        print("{}: {}".format(first_state.id, first_state.name))
    else:
        print("Nothing")

    # Close the session
    session.close()
