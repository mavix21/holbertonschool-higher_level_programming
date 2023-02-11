#!/usr/bin/python3
""" This module defines the function say_my_name """


def say_my_name(first_name, last_name=""):
    """ Prints "My name is <first name> <last name>

        Arguments:
            first name (string): user's first name
            lasst name (string): user's last name

        Returns:
            nothing
    """
    if type(first_name) != str:
        raise TypeError("first_name must be a string")

    if type(last_name) != str:
        raise TypeError("last_name must be a string")

    print(f"My name is {first_name} {last_name}")
