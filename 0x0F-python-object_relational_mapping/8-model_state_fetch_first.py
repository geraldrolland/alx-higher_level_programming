#!/usr/bin/python3
if __name__ == "__main__":
    from sqlalchemy import create_engine
    from model_state import Base, State
    from sqlalchemy.orm import sessionmaker
    from sys import argv
    db = "mysql://{}:{}@localhost:3306/{}".format(argv[1], argv[2], argv[3])
    eng = create_engine(db, echo=False)
    Session = sessionmaker()
    session = Session(bind=eng)
    my_state = session.query(State).filter(State.id == 1).first()
    if my_state is not None:
        print("{}: {}".format(my_state.id, my_state.name))
