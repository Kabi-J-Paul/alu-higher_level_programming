#!/usr/bin/python3
"""Base module.

This module defines the ``Base`` class, the parent of every other class
in this project. It manages the ``id`` attribute of all instances and
provides the JSON serialization and deserialization helpers.
"""
import json


class Base:
    """Base class managing the id attribute of all derived classes.

    It keeps a private counter of the number of instances created so
    that every object receives a unique id when none is given.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize a new Base with the given id, or an automatic one."""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return the JSON string representation of a list of dictionaries."""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Write the JSON representation of a list of objects to a file."""
        filename = "{}.json".format(cls.__name__)
        if list_objs is None:
            list_objs = []
        list_dictionaries = [obj.to_dictionary() for obj in list_objs]
        with open(filename, "w") as a_file:
            a_file.write(cls.to_json_string(list_dictionaries))

    @staticmethod
    def from_json_string(json_string):
        """Return the list of dictionaries held by a JSON string."""
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Return an instance with all its attributes already set."""
        if cls.__name__ == "Square":
            dummy = cls(1)
        else:
            dummy = cls(1, 1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """Return a list of instances loaded from the class JSON file."""
        filename = "{}.json".format(cls.__name__)
        try:
            with open(filename, "r") as a_file:
                list_dictionaries = cls.from_json_string(a_file.read())
                return [cls.create(**d) for d in list_dictionaries]
        except FileNotFoundError:
            return []
