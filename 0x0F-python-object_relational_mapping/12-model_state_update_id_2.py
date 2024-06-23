#!/usr/bin/python3

"""
This scripts updates the name of the state record with
the id 2
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
    state = session.query(State).filter(State.id == 2).one_or_none()
    state.name = "New Mexico"
    session.add(state)
    session.commit()
    session.close()
