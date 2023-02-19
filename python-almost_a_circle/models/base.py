#!/usr/bin/python3
""" This module defines the Base class in this project """


class Base():
    """
    This class is the "base" of all other classes in this project. The goal of
    it is to manage id attribute in all other classes and to avoid duplicating
    the same code

    Private Class Attributes:
        nb_objects (int):
            Incremented when a new object is instanziated

    """
    __nb_objects = 0

    def __init__(self, id=None):
        """ Constructor method """

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
