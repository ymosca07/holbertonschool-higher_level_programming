#!/usr/bin/python3
"""Doc string"""


from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine(
        f"mysql+mysqldb://{argv[1]}:{argv[2]}@localhost:3306/{argv[3]}",
        pool_pre_ping=True
    )

    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(State)\
        .filter(State.name.like('%a%'))\
        .order_by(State.id)\
        .all()

    for state in states:
        print(f"{state.id}: {state.name}")
