#!/usr/bin/python3


"""
This module defines a function pascal_triangle(n)
"""


def pascal_triangle(n):
    """Return a pascal triangle
    args:
        n(int): number of triangles
    """
    if n <= 0:
        return []
    if n == 1:
        return [[1]]
    if n == 2:
        return [[1], [1, 1]]
    my_list = [[1], [1, 1]]
    i = 2
    while i < n:
        sub_list = []
        sub_list.append(1)
        j = 0
        sum = 0
        while j + 1 < len(my_list[-1]):
            sum += my_list[-1][j] + my_list[-1][j + 1]
            sub_list.append(sum)
            sum = 0
            j += 1
        sub_list.append(1)
        my_list.append(sub_list)
        i += 1
    return my_list
