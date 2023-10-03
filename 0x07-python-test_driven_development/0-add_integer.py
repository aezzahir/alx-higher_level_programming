#!/usr/bin/python3
"""
This module provides a function to add two numbers.
"""


def add_integer(a, b=98):
    """
    This function adds two numbers.

    Args:
        a (int, float): The first number.
    b (int, float, optional): The second number. Default is 98.

    Returns:
        int: The sum of a and b.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
