#!/usr/bin/python3


"""
This is the module level docstring for 100-matrix_mul

This module provide matrix_mul(...) function
for the multiplication of two matrices

"""


def matrix_mul(m_a, m_b):
    """"Return the product of two given matrix m_a and m_b.
    args:
        m_a(list): first matrix
        m_b(list): second matrix
    """""
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    elif not isinstance(m_b, list):
        raise TypeError("m_b must be a list")
    elif m_a == [[]] or all(elem == [] for elem in m_a):
        raise ValueError("m_a can't be empty")
    elif m_b == [[]] or all(elem == [] for elem in m_b):
        raise ValueError("m_b can't be empty")
    else:
        for elem in m_a:
            if not isinstance(elem, list):
                raise ValueError("m_a must be a list of list")
            count_m_a = 0
            for item in elem:
                if type(item) not in [int, float]:
                    msg = "m_a should contain only integers or floats"
                    raise TypeError(msg)
                count_m_a += 1
                continue
            if count_m_a != len(m_a[0]):
                raise TypeError("each row of m_a must be of the same size")
            continue
        for elem in m_b:
            if not isinstance(elem, list):
                raise ValueError("m_b must be a list of list")
            count_m_b = 0
            for item in elem:
                if type(item) not in [int, float]:
                    msg = "m_b should contain only integers or floats"
                    raise TypeError(msg)
                count_m_b += 1
                continue
            if count_m_b != len(m_b[0]):
                raise TypeError("each row of m_b must be of the same size")
            continue
        if len(m_a[0]) != len(m_b):
            raise ValueError("m_a and m_b can't be multiplied")
        k = 0
        new_matrix = []
        while k < len(m_a):
            i = 0
            new_list = []
            while i < len(m_b[0]):
                j = 0
                sum = 0
                while j < len(m_b):
                    sum += m_b[j][i] * m_a[k][j]
                    j += 1
                new_list.append(sum)
                i += 1
            new_matrix.append(new_list)
            k += 1
        return new_matrix
