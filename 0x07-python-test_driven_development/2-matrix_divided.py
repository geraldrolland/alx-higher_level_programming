#!/usr/bin/python3


def matrix_divided(matrix, div):
    """Return a new matrix divided by div"""
    if matrix == [] or not isinstance(matrix, list) or matrix is None:
        msg = "matrix must be a matrix (list of lists) of integers/floats"
        raise TypeError(msg)
    new_matrix = []
    if not isinstance(div, int) and not isinstance(div, float):
        msg = "matrix must be a matrix (list of lists) of integers/floats"
        raise TypeError(msg)
    elif div == 0:
        raise ZeroDivisionError("division by zero")
    else:
        size = len(matrix[0])
        for elem in matrix:
            if len(elem) != size:
                msg = "Each row of the matrix must have the same size"
                raise TypeError(msg)
            new_list = []
            for unit in elem:
                if not isinstance(unit, int) and not isinstance(unit, float):
                    msg1 = "(list of lists) of integers/floats"
                    msg = "matrix must be a matrix " + msg1
                    raise TypeError(msg)
                unit = round(unit / div, 2)
                new_list.append(unit)
            new_matrix.append(new_list)
        return new_matrix
