#!/usr/bin/python3
""" class square"""


class Square:
    """Square details"""

    def __init__(self, size=0):
        """initializing a square


        Args:
        size (int): size of square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """ gets area of square

        Return: area of square"""
        return ((self.__size)**2)
