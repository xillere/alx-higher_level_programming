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

    def to_json(self):
        """dictionary rep of the student"""
        return self.__dict__
