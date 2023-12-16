#!/usr/bin/python3
"""
 prints the State object with the name passed as argument from the database
"""
import sys
from model_state import Base, State

from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    search = sys.argv[4]
    Base.metadata.create_all(engine)
    Session = sessionmaker()
    Session.configure(bind=engine)
    session = Session()
    state = session.query(State).filter_by(name=search).first()
    if state:
        print("{}".format(state.id))
    else:
        print("Not found")
