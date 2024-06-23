#!/usr/bin/python3

"""
This scripts get a state record that matches the
id parsed as the fourth commandline argument
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
    state = session.query(State.id).filter(State.name==argv[4]).one_or_none()
    if state is not None:
        print(state.id)
    else:
        print("Not found")
