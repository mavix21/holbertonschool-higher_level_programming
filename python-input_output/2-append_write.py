#!/usr/bin/python3
""" This module defines the function append_write """


def append_write(filename="", text=""):
    """ Appends a given string to a text file

    Parameters:
        filename (str):
            name of the text file where text will be appended to

        text (str):
            string that will be appended to the text file filename
    """

    with open(filename, 'a', encoding="utf-8") as f:
        number_of_characters_added = f.write(text)

    return (number_of_characters_added)
