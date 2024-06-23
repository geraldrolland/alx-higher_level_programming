#!/usr/bin/python3

"""
This scripts create a state record with the name
Louisiana
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
    state = State(name="Louisiana")
    session.add(state)
    session.commit()
    state = session.query(State.id).filter(State.name == "Louisiana").one()
    print(state.id)
    session.close()
