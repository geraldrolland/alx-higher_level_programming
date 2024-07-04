#!/usr/bin/python3

"""
this scripts list all city records from the cities
table with its corresponding state
"""

if __name__ == "__main__":
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from model_city import City
    from model_state import State, Base
    from sys import argv
    eng = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(argv[1], argv[2], argv[3]),
        pool_pre_ping=True
    )
    Session = sessionmaker(bind=eng)
    session = Session()
    cities = session.query(City).order_by(City.id).all()
    for city in cities:
        state = session.query(State).filter(State.id == city.state_id).one()
        print("{}: ({}) {}".format(state.name, city.id, city.name))
