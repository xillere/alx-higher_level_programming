#!/usr/bin/python3
""" class square"""


class Square:
    """Square details"""

    def __init__(self, size=0):
        """initializes square"""
        size.size = size

    @property
    def size(self):
        """retrieves size"""
        return (self.__size)

    @size.setter
    def size(self, value):
        """initializing a square


        Args:
        size (int): size of square
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """returns area"""
        return ((self.__self)**2)
