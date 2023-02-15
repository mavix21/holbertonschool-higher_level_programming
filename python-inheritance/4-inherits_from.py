#!/usr/bin/python3
""" This module defines the function inherits_from(obj, a_class) """


def inherits_from(obj, a_class):
    """
    Checks if a given object is an instance of a class
    that inherited (directly or indirectly) from the
    specified class

    Parameters:
        obj (any):
            an object
        a_class (any):
            a class

    Returns:
        True, if the object is an instance of a class
        that inherited, directly or indirectly, from the
        specified class
        False otherwise

    """
    return issubclass(obj.__class__, a_class) \
        and obj.__class__ is not a_class
