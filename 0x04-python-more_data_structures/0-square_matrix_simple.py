#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            k = map(lambda x: x**2, matrix[i])
            print("{}{}".format(k, ", " if j != len(matrix[i]) - 1 else ''), end='')
        print("{}".format(", " if i != len(matrix) else ''), end='')
