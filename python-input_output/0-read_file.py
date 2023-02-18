#!/usr/bin/python3
""" This module defines the function read_file """


def read_file(filename=""):
    """ Reads from a text file and prints it to stdout

    Parameters:
        filename (str):
            name of the text file
    """

    with open(filename) as f:
        for line in f:
            print(line, end="")
