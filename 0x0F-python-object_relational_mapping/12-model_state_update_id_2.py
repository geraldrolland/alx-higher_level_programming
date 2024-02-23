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
    state = session.query(State).filter(State.id == 2).first()
    state.name = "New Mexico"
    session.add(state)
    session.commit()
    session.close()
