#!/usr/bin/python3
"""This module defines the class Square"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ Square class that inherits from Rectangle """

    def __init__(self, size):
        """ Instantation method """

        super().__init__(size, size)
