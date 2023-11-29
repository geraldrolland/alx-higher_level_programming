#!/usr/bin/python3


def print_square(size):
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
