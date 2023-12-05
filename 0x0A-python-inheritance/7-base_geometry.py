#!/usr/bin/python3


"""
This module 6-base_geometry defines the class BaseGeometry
"""


class BaseGeometry:
    """Defines a class BaseGeometry"""
    def area(self):
        """Raises an Exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate an integer"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
