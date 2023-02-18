#!/usr/bin/python3
""" This module defines the function write_file """


def write_file(filename="", text=""):
    """ Writes a given string to a text file

    Parameters:
        filename (str):
            name of the text file where text will be written to

        text (str):
            string that will be written to the text file filename
    """

    with open(filename, 'w', encoding="utf-8") as f:
        number_of_characters_written = f.write(text)

    return (number_of_characters_written)
