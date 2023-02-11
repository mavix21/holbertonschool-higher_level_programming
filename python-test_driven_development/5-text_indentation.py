#!/usr/bin/python3
""" This module defines the function text_indentation """


def text_indentation(text):
    """ Prints a text with 2 new lines after each of these characters:
        '.', '?', and ':'

        Arguments:
            text (str): text to be printed

        Returns:
            nothing
    """

    if type(text) is not str:
        raise TypeError("text must be a string")

    symbols = ('.', '?', ':')
    symbol_printed = False
    for letter in text:
        if letter == " " and symbol_printed:
            continue

        if letter in symbols:
            print("{}\n".format(letter))
            symbol_printed = True
        else:
            print(letter, end="")
            symbol_printed = False
