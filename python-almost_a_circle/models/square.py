#!/usr/bin/python3
""" This module defines the Square class """

from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Square class

    Private Instance Attributes:
        size (int):
            size of the square instance
        x (int):
            x position of the rectangle instance
        y (int):
            y position of the rectangle instance
        id (int):
            unique identifier for the rectangle instance

    """

    def __init__(self, size, x=0, y=0, id=None):
        """ Constructor method """

        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """ Getter for size property """
        return self.width

    @size.setter
    def size(self, value):
        """ Setter for size property """

        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """ Assigns an argument to each attribute """

        attrs = ("id", "size", "x", "y")
        if args:
            for kw, value in zip(attrs, args):
                setattr(self, kw, value)
        elif kwargs:
            for kw, value in kwargs.items():
                setattr(self, kw, value)

    def __str__(self):
        """ Returns the string representation of the square instance """

        return f"[{self.__class__.__name__}] ({self.id}) {self.x}/{self.y} \
- {self.width}"
