#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from model_state import Base, State
    from sqlalchemy.orm import sessionmaker
    from sqlalchemy import create_engine
    from sys import argv
    db = "mysql://{}:{}@localhost:3306/{}".format(argv[1], argv[2], argv[3])
    engine = create_engine(db, echo=False)
    Session = sessionmaker(bind=engine)
    session = Session()
    state_list = session.query(State).filter(State.name.like('%a%')).all()
    if type(state_list) is list:
        for state in state_list:
            session.delete(state)
    if type(state_list) is State:
        session.delete(state_list)
    session.commit()
    session.close()
