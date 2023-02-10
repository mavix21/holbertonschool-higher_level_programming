#!/usr/bin/python3
""" This module defines the function add_integer """


def add_integer(a, b=98):
    """
    Returns the sum of two integers

        Parameters:
        -----------

            a (int): an integer (or float) number
            b (int): another integer (or float) number

        Return:
        -------

            the sum of a and b
    """
    if isinstance(a, (int, float)):
        a = int(a)
    else:
        raise TypeError("a must be an integer")

    if isinstance(b, (int, float)):
        b = int(b)
    else:
        raise TypeError("a must be an integer")

    return a + b
