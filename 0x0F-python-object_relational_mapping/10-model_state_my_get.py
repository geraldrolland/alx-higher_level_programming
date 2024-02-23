#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from model_state import Base, State
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from sys import argv
    db = "mysql://{}:{}@localhost:3306/{}".format(argv[1], argv[2], argv[3])
    engine = create_engine(db, echo=False)
    Session = sessionmaker(bind=engine)
    session = Session()
    state = session.query(State).filter(State.name == (sys.argv[4],)).first()
    if state is not None:
        print(state.id)
    else:
        print("Not found")
    session.close()
