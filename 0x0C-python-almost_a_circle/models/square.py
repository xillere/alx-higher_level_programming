#!/usr/bin/python3
'''square inheriting rectangle class'''
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    The Square class inherits from the Rectangle class
    """

    def __init__(self, size, x=0, y=0, id=None) -> None:
        """

        Args:
            size (int): lenght
            x (int): x
            y (int): y
            id (int): id
        """
        super().__init__(size, size, x, y, id)

    def __str__(self) -> str:
        """
        Returns:
            str: "[Square] (<id>) <x>/<y> - <width>".
        """
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    @property
    def size(self) -> int:
        """
        set/get the size of the square

        Returns:
            int: square size
        """
        return self.width

    @size.setter
    def size(self, value) -> None:
        """
        set/get the size of the square

        Args:
            value (int): new size of the square.
        """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        '''
        sets an argument to attribute.

        Args:
            args (int):
                        1 id attribute
                        2 size attribute
                        3 x attribute
                        4 y attribute

            kwargs (dict): Optional key/value
        '''
        attrs = ['id', 'size', 'x', 'y']
        if args:
            for i in range(len(args)):
                setattr(self, attrs[i], args[i])

        elif kwargs and len(kwargs) != 0:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        '''
        Returns square dictionary rep
        '''
        return {"id": self.id, "size": self.width,
                "x": self.x, "y": self.y}
