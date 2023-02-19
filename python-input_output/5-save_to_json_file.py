#!/usr/bin/python3
""" This module defines the function save_to_json_file """

import json


def save_to_json_file(my_obj, filename):
    """ Writes the JSON representation of a given object to a text file

    Parameters:
        my_obj (any):
            Object (data structure)

        filename (str):
            name of the file which the JSON will be written to
    """

    with open(filename, 'w+', encoding="utf-8") as f:
        f.write(json.dumps(my_obj))
