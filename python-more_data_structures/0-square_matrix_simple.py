#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    row = []

    for i in matrix:
        for j in i:
            row.append(j ** 2)
        n = row[:]
        new_matrix.append(n)
        row.clear()

    return new_matrix
