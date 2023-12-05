#!/usr/bin/python3


"""
This module defines the class MyList
"""


class MyList(list):
    """Define a class MyList"""
    def print_sorted(self):
        """that prints the list, but sorted.
        args:
            no argument
        """
        my_sort = sorted(self)
        print(my_sort)
