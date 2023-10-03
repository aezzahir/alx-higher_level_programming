#!/usr/bin/python3
"""This module provides a function to divide a matrix by a number."""


def matrix_divided(matrix, div):
    """
    This function divides a matrix by a number.

    Args:
        matrix (list of list of int/float): The matrix to be divided.
    div (int, float): The number to divide the matrix by.

    Returns:
        list of list of int/float: The resulting matrix.
    """
    if not isinstance(matrix, list) or not ...
    all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix ...
                        (list of lists) of integers/floats")
    if not all(isinstance(num, (int, float)) for row in matrix for num in row):
        raise TypeError("matrix must be (list of lists) of integers/floats")
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(num / div, 2) for num in row] for row in matrix]
