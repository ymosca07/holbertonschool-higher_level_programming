#!/usr/bin/python3
""" DESC """
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from model_state import Base, State

Base = declarative_base()


class State(Base):
    """Class State mapping to 'states' table"""
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)