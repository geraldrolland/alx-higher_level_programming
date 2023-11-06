#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for lst in matrix:
        for elem in lst:
            print("{}".format(elem), end=" " if elem != lst[-1] else "")
        print()
