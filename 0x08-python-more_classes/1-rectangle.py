#!/usr/bin/python3


"""
This is the module docstring for 1-rectangle

This module define a class Rectangle
"""


class Rectangle:
    """Define a class Rectangle"""

    def __init__(self, width=0, height=0):
        """Initialize the attribute of the object.
        args:
            width(int): width of Rectangle
            height(int): height of Rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
