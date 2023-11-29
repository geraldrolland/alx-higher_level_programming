#!/usr/bin/python3


def add_integer(a, b=98):
    """""Return the addition of a and b"""

    if not isinstance(a, int) and not isinstance(a, float) or a is None:
        raise TypeError("a must be an integer")
    elif not isinstance(b, int) and not isinstance(b, float) or b is None:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
