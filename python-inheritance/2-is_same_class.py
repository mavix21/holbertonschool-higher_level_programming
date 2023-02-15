#!/usr/bin/python3
""" This module defines the function is_same_class(obj, a_class) """


def is_same_class(obj, a_class):
    """
    Checks if a given object is exactly an instance of the specified class

    Parameters:
        obj (any):
            an object
        a_class (any):
            a class

    Returns:
        True, if the object is exactly an instance of the specified class
        False otherwise

    """
    return obj.__class__ is a_class
