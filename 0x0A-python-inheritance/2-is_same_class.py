#!/usr/bin/python3
"""This module contains a function to check if an object is
exactly an instance of a specified class"""


def is_same_class(obj, a_class):
    """
    Returns True if the object is exactly an instance of the
    specified class ; otherwise False.
    """
    return type(obj) is a_class
