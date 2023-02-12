#!/usr/bin/python3
""" This module defines the LockedClass Class """


class LockedClass:
    """
    Class with no class or object attribute that prevents
    the user from dinamically creating new instance attributes
    except if the new instance attribute is called 'first_name'

    """
    __slots__ = ['first_name']
