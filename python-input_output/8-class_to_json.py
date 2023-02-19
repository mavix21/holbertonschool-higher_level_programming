#!/usr/bin/python3
""" This module defines the function class_to_json """


def class_to_json(my_obj):
    """ Returns the dictionary representation of an object

    Parameters:
        my_obj (obj):
            object

    Returns:
        A dictionary of the attributes of the given object
    """

    return (my_obj.__dict__)
