#!/usr/bin/python3
"""Adds the State object 'Louisiana' to the database hbtn_0e_6_usa"""
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
        new_state = State(name="Louisiana")
        session.add(new_state)
        session.commit()
        print(new_state.id)
