#!/usr/bin/python3
""" This module defines the function matrix_divided """


def matrix_divided(matrix, div):
    """ Divides all elements of a given matrix by a given number

        Arguments:
            matrix (list): a list of lists (matrix) of integers/floats
            div (int/float): a number which the matrix will divided by

        Return:
            the result matrix
    """
    result_matrix = []
    result_row = []

    if type(div) != int and type(div) != float:
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    if not isinstance(matrix, (list)) or not matrix:
        raise TypeError("matrix must be a matrix (list of lists) of \
integers/floats")

    for sublist in matrix:
        if not isinstance(sublist, (list)):
            raise TypeError("matrix must be a matrix (list of lists) of \
integers/floats")
        for element in sublist:
            if type(element) != int and type(element) != float:
                raise TypeError("matrix must be a matrix (list of lists) of \
integers/floats")

    row_size = len(matrix[0])
    if len(matrix) > 1:
        for row in matrix[1:]:
            if len(row) != row_size:
                raise TypeError("Each row of the matrix must \
have the same size")

    for sublist in matrix:
        for element in sublist:
            result_row.append(round(element / div, 2))
        result_matrix.append(result_row[:])
        result_row.clear()

    return result_matrix
