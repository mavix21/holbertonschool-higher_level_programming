#!/usr/bin/python3
"""This module defines the class Rectangle"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ Rectangle class that inherits from BaseGeometry """

    def __init__(self, width, height):
        """ Instantation method """

        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height

    def __str__(self):
        """ String representation of an instance """

        return f"[Rectangle] {self.__width}/{self.__height}"
