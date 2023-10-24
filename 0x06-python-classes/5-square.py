#!/usr/bin/python3
""" class square"""


class Square:
    """Square details"""

    def __init__(self, size=0):
        """initializes square"""
        self.size = size

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
        return ((self.__size)**2)

    def my_print(self):
        """print stuff"""
        for i in range(0, self.__size):
            [print("#", end="") for j in range(self.__size)]
            print("")
        if self.__size == 0:
            print("")
