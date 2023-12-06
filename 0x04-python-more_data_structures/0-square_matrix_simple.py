#!/usr/bin/python3

def sqr(n):
    return n ** 2


def square_matrix_simple(matrix=[]):

    sqr_matrix = []
    for row in matrix:
        sqr_matrix.append(list(map(sqr, row)))
    return sqr_matrix
