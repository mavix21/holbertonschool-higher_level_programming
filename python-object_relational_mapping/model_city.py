#!/usr/bin/python3
""" Defines the class City """

from sqlalchemy import ForeignKey, create_engine
from sqlalchemy import Column, Integer, String
from model_state import Base
import sys

states = Base.metadata.tables['states']


class City(Base):
    """ State class that links to MySQL table cities """
    __tablename__ = 'cities'
    id = Column(Integer, autoincrement=True, unique=True, primary_key=True,
                nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey(states.c.id), nullable=False)


if __name__ == '__main__':
    av = sys.argv
    conn = 'mysql+mysqldb://{}:{}@localhost/{}'.format(av[1], av[2], av[3])
    engine = create_engine(conn, pool_pre_ping=True)
    Base.metadata.create_all(engine)
