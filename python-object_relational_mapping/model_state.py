#!/usr/bin/python3
"""Defines the State class and the declarative Base.

This module maps the ``State`` class to the ``states`` table of a
MySQL database using SQLAlchemy.
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """Represent a state stored in the states table.

    It holds an auto generated primary key and the name of the state.
    """

    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, autoincrement=True,
                nullable=False)
    name = Column(String(128), nullable=False)
