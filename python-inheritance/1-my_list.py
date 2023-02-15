#!/usr/bin/python3
""" This module defines a MyClass, that inherits from list """


class MyList(list):
    """
    This class inherits from list object type

    Public Instance Methods:
        print_sorted(self): Prints the list in ascending order

    """
    def print_sorted(self):
        """ Prints the list in my_list instance in ascending order """

        print(sorted(self))
