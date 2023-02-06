#!/usr/bin/python3
"""This module defines a class Square"""


class Square:
    """
    A class used to represent a Square

    Attributes
    ----------
    __size: int
        The size of the square

    Methods
    -------
    area()
        Returns the area of the square

    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Parameters
        ----------
        size: int
            The size of the square

        position: tuple of 2 positive integers
            Coordinates of the square

        """

        self.size = size
        self.position = position

    @property
    def size(self):
        """Getter method"""

        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter Method

        Parameters
        ----------
        value: int
            The value of size to be set

        Raises
        ------
        TypeError
            if the size provided is not an integer

        ValueError
            if the size provided is less than zero

        """

        if type(value) != int:
            raise TypeError("size must be an integer")

        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    @property
    def position(self):
        """Getter method"""

        return self.__position

    @position.setter
    def position(self, value):
        """
        Setter Method

        Parameters
        ----------
        value: tuple of two integers
            The coordinates of the square

        Raises
        ------
        TypeError
            if the value provided is not a tuple of two integers

        """

        if type(value) != tuple or len(value) != 2 or \
                not all(isinstance(i, int) and i >= 0 for i in value):
            raise TypeError("position must be a tuple of 2 positive integers")

        self.__position = value

    def area(self):
        """Returns the area of the square"""

        return self.__size ** 2

    def my_print(self):
        """Prints the square"""

        if self.__size == 0:
            print()
        else:
            for i in range(self.__position[1]):
                print()
            for i in range(self.__size):
                print(" " * self.__position[0], end="")
                print("#" * self.__size)
