#!/usr/bin/python3
""" This module defines the function is_kind_of_class(obj, a_class) """


def is_kind_of_class(obj, a_class):
    """
    Checks if a given object is an instance of the specified class
    or if the object is an instance of a class that inherited from
    the specified class

    Parameters:
        obj (any):
            an object
        a_class (any):
            a class

    Returns:
        True, if the object is an instance of either the specified class
        or a class that inherited from it
        False otherwise

    """
    return isinstance(obj, a_class)
