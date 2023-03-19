#!/usr/bin/python3
""" Defines the class State """

from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from relationship_city import City, Base
import sys


class State(Base):
    """ State class that links to MySQL table states """
    __tablename__ = "states"
    id = Column(Integer, autoincrement=True, unique=True, primary_key=True,
                nullable=False)
    name = Column(String(128), nullable=False)

    cities = relationship("City", back_populates="state")


City.state = relationship("State", back_populates="cities")

if __name__ == "__main__":
    av = sys.argv
    conn = 'mysql+mysqldb://{}:{}@localhost/{}'.format(av[1], av[2], av[3])
    engine = create_engine(conn, pool_pre_ping=True)
    Base.metadata.create_all(engine)
