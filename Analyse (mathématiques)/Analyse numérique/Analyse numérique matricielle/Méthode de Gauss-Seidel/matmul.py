# -*- coding: utf-8 -*-

import os

# routines for multiplying matrices
import numpy


def mult_Ax(A, x):
    """ return the product of matrix A and vector x: Ax = b """

    # x is a vector
    if not x.ndim == 1:
        print("ERROR: x should be a vector")
        return None

    N = len(x)

    # A is square, with each dimension of length N
    if not (A.shape[0] == N and A.shape[1] == N):
        print("ERROR: A should be square with each dim of same length as x")
        return None

    # allocation the product array
    b = numpy.zeros((N), dtype=A.dtype)

    # each row of b is the product of the like row of A dotted with
    # the vector x
    for i in range(N):
        b[i] = numpy.dot(A[i, :], x)

    print(b)

    return b

os.system("pause")
