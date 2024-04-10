#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    for i in range(len(matrix)):
        k = list(map(lambda x: x**2, matrix[i]))
        print(list(k), end=', ' if i != len(matrix) - 1 else '')
