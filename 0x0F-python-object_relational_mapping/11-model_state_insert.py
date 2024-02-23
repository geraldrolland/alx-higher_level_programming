#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from model_state import Base, State
    db = "mysql://{}:{}@localhost:3306/{}".format(sys.argv[1], sys.argv[2], sys.argv[3])
    engine = create_engine(db, echo=False)
    Session = sessionmaker(bind=engine)
    session = Session()
    state = State(name="Louisiana")
    session.add(state)
    session.commit()
    state = session.query(State).filter(State.name == "Louisiana").first()
    print(state.id)
    session.close()

