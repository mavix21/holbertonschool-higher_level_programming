#!/usr/bin/python3
""" This module defines the function to_json_string """

import json


def to_json_string(my_obj):
    """ Returns the JSON representation of an object (string)

    Parameters:
        my_obj (obj):
            object to be serialized

    Returns:
        The JSON string representation of the given object
    """

    return (json.dumps(my_obj))
