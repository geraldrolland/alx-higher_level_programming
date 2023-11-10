#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    squared_matrix = []
    i = 0
    for elem in matrix:
        mat = list(map(lambda x: x ** 2, elem))
        squared_matrix.append(mat)
    return squared_matrix
