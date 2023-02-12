#!/usr/bin/python3
"""This module defines a class Rectangle"""


class Rectangle:
    """Rectangle class

    Private Instance Attributes:
        width: int
            Width of the rectangle

        height: int
            Height of the rectangle

    Public Class Attributes:
        number_of_instances: int
            Number of instances, incremented during
            each new instance instantation, decremented
            during each instance deletion

    Methods:
        area():
            Computes the area of the rectangle

        perimeter():
            Computes the perimeter of the rectangle

    """

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """
        Parameters
            width (int): The width of the rectangle
            height (int): The height of the rectangle

        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """ Getter method """

        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter method

        Parameters:
            value (int): The value of width to be set

        Raises:
            TypeError: if the width provided is not an integer

            ValueError: if the width provided is less than zero

        """

        if type(value) is not int:
            raise TypeError("width must be an integer")

        if value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @property
    def height(self):
        """ getter method """

        return self.__height

    @height.setter
    def height(self, value):
        """
        setter method

        Parameters:
            value (int): The value of height to be set

        Raises:
            TypeError: if the height provided is not an integer

            ValueError: if the height provided is less than zero

        """

        if type(value) is not int:
            raise TypeError("height must be an integer")

        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value

    def area(self):
        """
        Method that computes the area of the rectangle object

        Returns:
            The area of the rectangle

        """

        return (self.width * self.height)

    def perimeter(self):
        """
        Method that computes the perimeter of the rectangle object

        Returns:
            The perimeter of the rectangle, zero if either width or
            height is zero

        """

        if self.width == 0 or self.height == 0:
            perimeter = 0
        else:
            perimeter = 2 * (self.width + self.height)

        return perimeter

    def __str__(self):
        """
        Defines the string representation of the rectangle object

        Returns:
            A string representation of the rectangle with "#"

        """
        rectangle_string = ""

        if self.width == 0 or self.height == 0:
            return rectangle_string

        for i in range(self.height):
            if i > 0:
                rectangle_string += '\n'

            rectangle_string += "#" * self.width

        return rectangle_string

    def __repr__(self):
        """
        Defines the "formal" string representation of the rectangle object.

        Returns:
            A string representation of the rectangle to be able to recreate
            a new instance by using eval()

        """
        return f"Rectangle({self.width}, {self.height})"

    def __del__(self):
        """ Prints a message when the object is about to be deleted """

        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
