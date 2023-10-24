#!/usr/bin/python3

"""Square class"""


class Square:
    """square"""

    def __init__(self, size=0):
        """Initializes square.

        Args:
            size (int): The size
        """
        self.size = size

    @property
    def size(self):
        """return size"""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return area"""
        return ((self.__size)**2)

    def __eq__(self, other):
        """=="""
        return self.area() == other.area()

    def __ne__(self, other):
        """not equal"""
        return self.area() != other.area()

    def __lt__(self, other):
        """smaller than"""
        return self.area() < other.area()

    def __le__(self, other):
        """smaller equal"""
        return self.area() <= other.area()

    def __gt__(self, other):
        """bigger than"""
        return self.area() > other.area()

    def __ge__(self, other):
        """bigger equal"""
        return self.area() >= other.area()
