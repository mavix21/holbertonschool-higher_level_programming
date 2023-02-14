#!/usr/bin/python3
""" This module defines the function lookup(obj)"""


def lookup(obj):
    """
    Returns the list of available attributes and methods of a
    given object

    Parameters:
        obj (any):
            object whose attributes and methods we want to lookup

    Returns:
        A list of attributes and methods

    """
    return dir(obj)
