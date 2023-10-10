#!/usr/bin/python3
"""
A  module for defining a student Class
"""


class Student:
    """
     class Student that defines a student
    """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if attrs is None:
            return self.__dict__
        else:
            dict = {}
            for attr in attrs:
                if hasattr(self, attr):
                    dict[attr] = getattr(self, attr)
            return (dict)
