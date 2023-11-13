#!/usr/bin/python3
'''class base'''
import csv
import json


class Base:
    '''
    Base class for other classes and sets up a private class attribute
    for counting the number of objects and a constructor for initializing
    instance ID values.

    Attributes:
        __nb_objects (int): The number of objects created for a class.
        id (int): The ID of an instance of a class.
    '''
    __nb_objects = 0

    def __init__(self, id=None) -> None:
        '''
        instantiation of id value

        Args:
            id (int): (optional) ID value for instance
        '''
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries) -> str:
        """returns JSON string rep of list_dictionaries.

        Args:
            list_dictionaries (list): list of dictionaries.
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """prints the JSON string rep of list_objs to file."""
        if list_objs is None:
            list_objs = []
        fname = cls.__name__ + ".json"
        with open(fname, "w") as f:
            json_rep = cls.to_json_string([obj.to_dictionary()
                                              for obj in list_objs])
            f.write(json_rep)

    @staticmethod
    def from_json_string(json_string):
        """
         that returns the list of the JSON string representation json_string

        Args:
            json_string (str): string representing list dictionaries
                                in JSON format.

        """
        if json_string is None or json_string == '[]':
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set."""
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                dum = cls(1, 1)
            elif cls.__name__ == "Square":
                dum = cls(1)
            dum.update(**dictionary)
            return dum

    @classmethod
    def load_from_file(cls):
        """Returns a list of instances from a JSON file."""
        fname = cls.__name__ + ".json"
        try:
            with open(fname, "r") as f:
            jstr = f.read()
        except FileNotFoundError:
            return []
        oblist = cls.from_json_string(jstr)
        instances = [cls.create(**obj) for obj in oblist]
        return instances
