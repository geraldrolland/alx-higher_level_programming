#!/usr/bin/python3


"""
This module defines the class Rectangle
"""


class Rectangle(BaseGeometry):

    """define a class Rectangle"""
    def __init__(self, width, height):
        """Initialize the attribute of the object
        args:
            width(int): width of the rectangle
            height(int): height of the rectangle
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def integer_validator(self, name, value):
        """Validate an integer"""
        super().integer_validator(name, value)
