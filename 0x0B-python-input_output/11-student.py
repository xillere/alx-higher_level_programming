#!/usr/bin/python3
"""class Student."""


class Student:
    """student"""

    def __init__(self, first_name, last_name, age):
        """Initialize a new Student.

        Args:
            first_name (str): first name of student
            last_name (str): surname of the student
            age (int): age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """dictionary rep of the student

        If attrs is a list of strings, represents only those attributes
        included in the list.

        Args:
            attrs (list): (Optional) attributes
        """
        if (type(attrs) == list and
                all(type(item) == str for item in attrs)):
            return {i: getattr(self, i) for i in attrs if hasattr(self, i)}
        return self.__dict__

    def reload_from_json(self, json):
        """replaces attributes of the student

        Args:
            json (dict): the key and value
        """
        for key, value in json.items():
            setattr(self, key, value)
