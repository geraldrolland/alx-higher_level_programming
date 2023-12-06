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
        self.__width = width
        self.__height = height
        self.integer_validator("width", width)
        self.integer_validator("height", height)

    def integer_validator(self, name, value):
        """Validate an integer"""
        super().integer_validator(name, value)
