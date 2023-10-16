#!/usr/bin/python3

"""
This is the Base Class
"""
import json


class Base:
    """This is the Base Class"""

    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Return the JSON string representation
        """
        if not list_dictionaries or list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Save the Json reprasentaion in a file
        """
        my_list = []
        for instance in list_objs:
            my_list.append(instance.to_dictionary())
        my_list = cls.to_json_string(my_list)
        with open("{}.json".format(cls.__name__), mode="w") as Myfile:
            Myfile.write(my_list)
