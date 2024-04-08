#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix:
        for i in range(len(matrix)):
            if matrix[i]:
                for j in range(len(matrix[i])):
                    en = " " if j != len(matrix[i]) - 1 else "\n"
                    print("{:d}{}".format(matrix[i][j], en), end="")
            else:
                print("{}".format("\n"))
