#!/usr/bin/python3
""" This module defines the Rectangle class """

from base import Base


class Rectangle(Base):
    """
    Rectangle class

    Private Instance Attributes:
        width (int):
            width of the rectangle instance
        heigth (int):
            height of the rectangle instance
        x (int):
            x position of the rectangle instance
        y (int):
            y position of the rectangle instance
        id (int):
            unique identifier for the rectangle instance

    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ Constructor method """

        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """ Getter method for width property """

        return self.__width

    @width.setter
    def width(self, value):
        """ Setter method for width property """

        self.__width = value

    @property
    def height(self):
        """ Getter method for height property """

        return self.__height

    @height.setter
    def height(self, value):
        """ Setter method for height property """

        self.__height = value

    @property
    def x(self):
        """ Getter method for x property """

        return self.__x

    @x.setter
    def x(self, value):
        """ Setter method for x property """

        self.__x = value

    @property
    def y(self):
        """ Getter method for y property """

        return self.__y

    @y.setter
    def y(self, value):
        """ Setter method for y property """

        self.__y = value
