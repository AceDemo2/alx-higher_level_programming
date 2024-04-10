#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            k = list(map(lambda x: x**2, matrix[i]))
            print(k, end=', ' if j != len(matrix[i]) - 1 else '')
