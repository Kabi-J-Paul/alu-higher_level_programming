#!/usr/bin/python3
"""Module that defines a student that can be saved and rebuilt."""


class Student:
    """Represent a student with a first name, a last name and an age."""

    def __init__(self, first_name, last_name, age):
        """Initialize a new Student.

        Args:
            first_name (str): the first name of the student.
            last_name (str): the last name of the student.
            age (int): the age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Return the dictionary description of the Student instance.

        Args:
            attrs (list): if it is a list of strings, only the attributes
                whose name is in that list are retrieved. Otherwise every
                attribute is retrieved.

        Returns:
            A dictionary of the selected attributes of the instance.
        """
        if type(attrs) is list and all(type(a) is str for a in attrs):
            return {k: v for k, v in self.__dict__.items() if k in attrs}
        return self.__dict__.copy()

    def reload_from_json(self, json):
        """Replace every attribute of the Student from a dictionary.

        Args:
            json (dict): keys are public attribute names and values are
                the new values of those attributes.
        """
        for key, value in json.items():
            setattr(self, key, value)
