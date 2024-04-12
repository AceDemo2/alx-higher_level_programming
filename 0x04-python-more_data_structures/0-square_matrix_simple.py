#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    k = []
    for i in range(len(matrix)):
        k[i] = (map(lambda x: x**2, matrix[i]))
    return (k)
