#!/usr/bin/python3


"""
This module defines the class Rectangle
"""


from models.base import Base


class Rectangle(Base):

    """Defines the class Base"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize the attribute of the object.
        args:
            width(int): width of the rectangle
            height(int): height of the rectangle
            x(int): coordinate x
            y(int): coordinate y
            id(int): value of object
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Return the area of the rectangle"""
        return self.__width * self.__height

    def display(self):
        """print the string representation of the object"""
        for i in range(self.__y):
            print()
        for i in range(self.__height):
            print((self.__x * " ") + self.__width * "#")

    def __str__(self):
        """Return string representation of the object"""
        f = "[Rectangle] ({}) {}/{} - {}/{}"
        s = f.format(self.id, self.x, self.y, self.width, self.height)
        return s

    def update(self, *args, **kwargs):
        """assigns an argument to each attribute"""
        if len(args) == 0:
            for key, value in kwargs.items():
                setattr(self, key, value)
            return
        my_keys = ["id", "width", "height", "x", "y"]
        for key, value in zip(my_keys, args):
            setattr(self, key, value)

    def to_dictionary(self):
        """ returns the dictionary representation of a Rectangle:"""
        my_dict = {
            "x": self.x,
            "y": self.y,
            "id": self.id,
            "height": self.height,
            "width": self.width
            }
        return my_dict
