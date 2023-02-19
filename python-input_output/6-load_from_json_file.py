#!/usr/bin/python3
""" This module defines the function load_from_json_file """

import json


def load_from_json_file(filename):
    """ Creates an object from a JSON file

    Parameters:

        filename (str):
            name of the file which contains the JSON to deserialize

    Returns:
        The object (data structure)
    """

    with open(filename, 'w', encoding="utf-8") as f:
        my_obj = json.load(f)

    return (my_obj)
