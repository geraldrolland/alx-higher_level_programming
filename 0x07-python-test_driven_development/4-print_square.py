#!/usr/bin/python3


"""
This is the docstring for module 4-print_square

This module provide the function print_square(...)
"""


def print_square(size):
    """Print the size of square using #.
    args:
	size(int): size of the square
    """
    if (isinstance(size, float) and size < 0) or size is None or \
            not isinstance(size, int):
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    else:
        i = 0
        while i < size:
            print(size * "#")
            i += 1
