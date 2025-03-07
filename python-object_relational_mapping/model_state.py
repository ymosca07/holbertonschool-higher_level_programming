#!/usr/bin/python3
"""
This module defines a State class that maps to the MySQL table 'states'.
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

# Création d'une instance de Base pour SQLAlchemy
Base = declarative_base()

class State(Base):
    """Class State that links to the MySQL table 'states'"""
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
