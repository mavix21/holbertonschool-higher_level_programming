#!/usr/bin/python3
""" This module defines the function from_json_string """

import json


def from_json_string(my_str):
    """ Returns an object represented by a JSON string

    Parameters:
        my_str (str):
            str to be deserialized

    Returns:
        The object (data structure) that results from deserializing
        my_str
    """

    return (json.loads(my_str))
