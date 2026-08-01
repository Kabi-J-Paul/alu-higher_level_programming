#!/usr/bin/python3
"""Defines the City class.

This module maps the ``City`` class to the ``cities`` table of a MySQL
database, linked to the states table by a foreign key.
"""
from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import Base


class City(Base):
    """Represent a city stored in the cities table.

    It holds an auto generated primary key, a name and the id of the
    state the city belongs to.
    """

    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, autoincrement=True,
                nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
