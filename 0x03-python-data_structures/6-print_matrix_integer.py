#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    """Print a matrix of integers."""
    for s in range(len(matrix)):
        for j in range(len(matrix[s])):
                print("{:d}".format(matrix[s][j]), end="")
                if j != (len(matrix[s]) - 1):
                    print(" ", end="")

        print("")
