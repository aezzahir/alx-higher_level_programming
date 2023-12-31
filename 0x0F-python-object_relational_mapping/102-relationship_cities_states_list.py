#!/usr/bin/python3
"""
List all State objects, and corresponding City objects,
contained in the database
"""
import sys
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)

    Base.metadata.create_all(engine)
    Session = sessionmaker()
    Session.configure(bind=engine)
    session = Session()
    cities = session.query(City, State).filter(
            State.id == City.state_id).order_by(City.id).all()
    for city, state in cities:
        print("{}: {} -> {}".format(city.id, city.name, state.name))
    session.close()
