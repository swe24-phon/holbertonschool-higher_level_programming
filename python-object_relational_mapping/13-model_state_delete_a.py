#!/usr/bin/python3
"""Deletes all State objects with a name containing
the letter 'a'
from the database hbtn_0e_6_usa"""
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from model_state import Base, State
import sys


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: {} <mysql_username> <mysql_password> "
              "<database_name>".format(sys.argv[0]))
        sys.exit(1)

    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
            mysql_username, mysql_password, database_name),
        pool_pre_ping=True)

    Base.metadata.create_all(engine)

    with Session(engine) as session:
        # Query and delete State objects where contains 'a'
        states_to_delete = session.query(State).filter
        (State.name.like('%a%')).all()
        for state in states_to_delete:
            session.delete(state)
        session.commit()
