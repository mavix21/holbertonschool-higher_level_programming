#!/usr/bin/python3
""" This module defines the function pascal_triangle """


def pascal_triangle(n):
    """
    Creates a list representation of the Pascal's triangle

    Parameters:
        n (int):
            Pascal's triangle number of rows

    Returns:
        A list of lists of integers representing the Pascal's
        triangle of n
    """

    pascal_list = []

    if n <= 0:
        return pascal_list

    prev_row = [1]

    for i in range(n):
        new_row = [1]

        for j in range(i):
            if j + 1 < i:
                new_row.append(prev_row[j] + prev_row[j + 1])

        if i > 0:
            new_row.append(1)

        pascal_list.append(new_row[:])
        prev_row = new_row[:]

    return pascal_list
