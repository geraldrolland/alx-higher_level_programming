#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix == [[]]:
        print()
        return
    for lst in matrix:
        for elem in lst:
            if elem == lst[-1]:
                print("{}".format(elem), end = "")
                break
            print("{:d}".format(elem), end = " ")
        print()
