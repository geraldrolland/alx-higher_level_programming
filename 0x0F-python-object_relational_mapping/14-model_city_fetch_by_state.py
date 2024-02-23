#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from model_state import Base, State
    from sqlalchemy.orm import sessionmaker
    from sqlalchemy import create_engine
    from model_city import City
    from sysy import argv
    db = "mysql://{}:{}@localhost:3306/{}".format(argv[1], argv[2], argv[3])
    engine = create_engine(db, echo=False)
    Session = sessionmaker(bind=engine)
    se = Session()
    s = se.query(City, State).join(State).order_by(City.id).all()
    for city, state in s:
        print("{}: ({}) {}".format(state.name, city.id, city.name))
    session.close()
