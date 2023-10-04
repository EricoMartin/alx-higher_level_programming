#!/usr/bin/python3
""" The 2-matrix_divided Module """


def matrix_divided(matrix, div):
    """
        def matrix_divided(matrix, div)

        Args:
            matrix: a list of lists of integers or floats
            div: a number (integer or float)

        Returns:
            a new matrix
    """
    length = 0

    if type(matrix) is not list:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    for block in matrix:    # matrix is a list
        if type(block) is not list:
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        
        for element in block:
            if type(element) is not int and type(element) is not float:
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

        if len(block) != prev_len and prev_len != 0:
            raise TypeError("Each row of the matrix must have the same size")
        prev_len = len(block)

    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(elem / div, 2) for elem in row] for row in matrix]
