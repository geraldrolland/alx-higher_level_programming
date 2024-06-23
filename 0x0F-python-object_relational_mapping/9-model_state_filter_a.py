#!/usr/bin/python3

"""
This scripts list all state record that matches the
letter a
"""

if __name__ == "__main__":
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from model_state import State, Base
    from sys import argv
    eng = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(argv[1], argv[2], argv[3]),
        pool_pre_ping=True
    )
    Session = sessionmaker(bind=eng)
    session = Session()
    s = session.query(State).\
     filter(State.name.like("%a%")).order_by(State.id).all()
    for state in s:
        print("{}: {}".format(state.id, state.name))
