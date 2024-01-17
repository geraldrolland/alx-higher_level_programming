#!/usr/bin/python3


"""
This module defines the class Square
"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """Defines a class Square"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize the attribute of the object.
           args:
               size(int): size of a square
            x(int): position x
            y(int): position y
            id(int): value id
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Return th string representation of the square object"""
        f = "[Square] ({}) {}/{} - {}"
        return f.format(self.id, self.x, self.y, self.width)

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """assigns attributes to the instance"""
        if len(args) == 0:
            for key, value in kwargs.items():
                setattr(self, key, value)
            return
        my_keys = ["id", "size", "x", "y"]
        for key, value in zip(my_keys, args):
            setattr(self, key, value)

    def to_dictionary(self):
        """returns the dictionary representation of a Square"""
        return {"id": self.id, "x": self.x, "size": self.width, "y": self.y}
