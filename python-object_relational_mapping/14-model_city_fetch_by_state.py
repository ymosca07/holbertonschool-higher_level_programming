#!/usr/bin/python3
"""Doc string"""


from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City

if __name__ == "__main__":
    engine = create_engine(
        f"mysql+mysqldb://{argv[1]}:{argv[2]}@localhost:3306/{argv[3]}",
        pool_pre_ping=True
    )

    Session = sessionmaker(bind=engine)
    session = Session()

    results = session.query(State.name, City.id, City.name)\
        .join(City, State.id == City.state_id)\
        .order_by(City.id)\
        .all()

    for state_name, city_id, city_name in results:
        print(f"{state_name}: ({city_id}) {city_name}")
