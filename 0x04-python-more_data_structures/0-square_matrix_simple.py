#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for _list in matrix:
        new_matrix.append(list(map(lambda x: x**2, _list)))
    return (new_matrix)
