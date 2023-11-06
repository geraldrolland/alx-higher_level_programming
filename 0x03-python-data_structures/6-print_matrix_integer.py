#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix == [[]]:
        print()
        return
    for lst in matrix:
        last_elem = lst[-1]
        for elem in lst:
            txt = "{}"
            if last_elem == elem:
                print(txt.format(elem), end="")
                break
            print(txt.format(elem), end=" ")
        print()
