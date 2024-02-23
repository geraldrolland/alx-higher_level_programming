#!/usr/bin/python3

if __name__ == "__main__":
    from model_state import Base, State
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from sys import argv
    db = "mysql://{}:{}@localhost:3306/{}".format(argv[1], argv[2], argv[3])
    engine = create_engine(db, echo=False)
    Session = sessionmaker(bind=engine)
    se = Session()
    s = se.query(State).filter(State.name.like('%a%')).order_by(State.id).all()
    for state in s:
        print("{}: {}".format(state.id, state.name))
    se.close()
