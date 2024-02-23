#!/usr/bin/python3
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from sys import argv


db_uri = "mysql://{}:{}@localhost:3306/{}".format(argv[1], argv[2], argv[3])
eng = create_engine(db_uri, echo=False)
Session = sessionmaker()
session = Session(bind=eng)
state_list = session.query(State).order_by(State.id).all()
for state in state_list:
    print("{}: {}".format(state.id, state.name))
session.close()
