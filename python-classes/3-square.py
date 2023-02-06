#!/usr/bin/python3
"""This module defines a class Square"""


class Square:
    """
    A class used to represent a Square

    Attributes
    ----------
    __size: int
        The size of the square.

    Methods
    -------
    area()
        Returns the area of the square

    """

    def __init__(self, size=0):
        """
        Parameters
        ----------
        size: int
            The size of the square.

        Raises
        ------
        TypeError
            if the size provided is not an integer

        ValueError
            if the size provided is less than zero

        """

        if type(size) != int:
            raise TypeError("size must be an integer")

        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

    def area(self):
        """Returns the area of the square"""
        return self.__size ** 2
