#!/usr/bin/python3
""" This module defines the function print_square """


def print_square(size):
    """ Prints a square with the character '#'

        Arguments:
            size (int): size of the square

        Returns:
            nothing
    """
    if type(size) is float:
        if size < 0:
            raise TypeError("size must be an integer")
        else:
            size = int(size)
    elif type(size) is not int:
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")

    if size == 0:
        print()

    for i in range(size):
        print("#" * size)
