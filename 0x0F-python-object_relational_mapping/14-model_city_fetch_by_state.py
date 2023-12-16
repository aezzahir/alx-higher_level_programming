#!/usr/bin/python3
"""
Print all City objects from the database
"""
import sys
from model_state import Base, State
from model_city import City
from sqlalchemy import (create_engine)
from sqlalchemy import asc
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker()
    Session.configure(bind=engine)
    session = Session()
    cities = session.query(State.name, City.id, City.name).join(
            City, State.id == City.state_id).order_by(State.id, City.id)
    for city in cities:
        print("{}: ({}) {}".format(city[0], city[1], city[2]))
