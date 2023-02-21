#!/usr/bin/python3
""" This module defines the Base class in this project """

import json
import os

class Base():
    """
    This class is the "base" of all other classes in this project. The goal of
    it is to manage id attribute in all other classes and to avoid duplicating
    the same code

    Private Class Attributes:
        nb_objects (int):
            Incremented when a new object is instanziated

    """
    __nb_objects = 0

    def __init__(self, id=None):
        """ Constructor method """

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ Returns the JSON string representation of list_dictionaries """

        return json.dumps(list_dictionaries) if list_dictionaries is not None \
            else "[]"

    @staticmethod
    def from_json_string(json_string):
        """
        Returns the list of JSON representation, i.e an object of type list

        """
        if json_string is not None and json_string != []:
            json_list = json.loads(json_string)
        else:
            json_list = []

        return json_list

    @classmethod
    def save_to_file(cls, list_objs):
        """ Writes the JSON string representation to a file """

        list_dictionaries = []

        if list_objs is not None:
            for obj in list_objs:
                list_dictionaries.append(obj.to_dictionary())

        class_name = cls.__name__
        filename = f"{class_name}.json"
        list_objs_json = cls.to_json_string(list_dictionaries)

        with open(filename, 'w', encoding='utf-8') as f:
            f.write(list_objs_json)

    @classmethod
    def create(cls, **dictionary):
        """ Returns an instance with all attributes alrleady set """

        if cls.__name__ == 'Rectangle':
            dummy = cls(1, 1)
        elif cls.__name__ == 'Square':
            dummy = cls(1)
        else:
            return None

        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """ Returns a list of instances from a JSON file """

        filename = f"{cls.__name__}.json"
        if not os.path.exists(filename):
            return []

        objects_list = []
        with open(filename, 'r', encoding='utf-8') as f:
            dictionary_list = cls.from_json_string(f.read())
            for dict in dictionary_list:
                objects_list.append(cls.create(**dict))

        return objects_list
