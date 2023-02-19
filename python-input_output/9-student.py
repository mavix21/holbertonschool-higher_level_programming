#!/usr/bin/python3
"""This module defines the class Student"""


class Student:
    """Student class

    Public Instance Attributes:
        first_name: str
            Student's first name

        last_name: str
            Student's last name

        age: int
            Student's age

    Public Methods:
        to_json():
            Retrieves a dictionary of a Student instance

    """

    def __init__(self, first_name, last_name, age):
        """
        Parameters
            first_name (int): The first name of the student
            last_name (int): The last name of the student
            age (int): The age of the student

        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        Method that retrieves a dictionary representation of a Student instance

        Returns:
            Dictionary data structure of the attributes of the Student instance

        """
        return (self.__dict__)
