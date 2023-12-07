#!/usr/bin/python3
"""define class MyInt"""


class MyInt(int):
    """
    MyInt class inherits from int with inverted == and != operators.
    """

    def __eq__(self, other):
        """
        Override the == operator to behave like the != operator.
        """
        return super().__ne__(other)

    def __ne__(self, other):
        """
        Override the != operator to behave like the == operator.
        """
        return super().__eq__(other)
