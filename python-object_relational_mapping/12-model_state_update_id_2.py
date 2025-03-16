#!/usr/bin/python3
"""Updates the name of the State object with id = 2 to
'New Mexico' in the database hbtn_0e_6_usa"""
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
        state_to_update = session.query(State).filter_by(id=2).first()
        if state_to_update:
            state_to_update.name = "New Mexico"
            session.commit()
