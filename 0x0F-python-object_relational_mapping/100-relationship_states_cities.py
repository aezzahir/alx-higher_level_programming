#!/usr/bin/python3
"""
Add the State object “Louisiana” to the database
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
    my_state = State("California")
    my_city = City("San Francisco")
    my_state.cities.append(my_city)
    session.add(my_state)
    session.commit()
    print(my_state.id)
