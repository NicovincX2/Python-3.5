# -*- coding: utf-8 -*-

import os
import numpy as np
from time import process_time

size = 200
iterations = 100

def mandelbrot_python(m, size, iterations):
    for i in range(size):
        for j in range(size):
            c = -2 + 3./size*j + 1j*(1.5-3./size*i)
            z = 0
            for n in range(iterations):
                if np.abs(z) <= 10:
                    z = z*z + c
                    m[i, j] = n
                else:
                    break

m = np.zeros((size, size))
mandelbrot_python(m, size, iterations)

import matplotlib.pyplot as plt

plt.imshow(np.log(m), cmap=plt.cm.hot,);
plt.xticks([]); plt.yticks([]);

top = process_time()
mandelbrot_python(m, size, iterations)
print(top-process_time())

import numba
from numba import jit, complex128

@jit(locals=dict(c=complex128, z=complex128))
def mandelbrot_numba(m, size, iterations):
    for i in range(size):
        for j in range(size):
            c = -2 + 3./size*j + 1j*(1.5-3./size*i)
            z = 0
            for n in range(iterations):
                if abs(z) <= 10:
                    z = z*z + c
                    m[i, j] = n
                else:
                    break

m = np.zeros((size, size))
mandelbrot_numba(m, size, iterations)

top = process_time()
mandelbrot_numba(m, size, iterations)
print(top-process_time())

"""
import cython

def mandelbrot_cython(int[:,::1] m,
                      int size,
                      int iterations):
    cdef int i, j, n
    cdef complex z, c
    for i in range(size):
        for j in range(size):
            c = -2 + 3./size*j + 1j*(1.5-3./size*i)
            z = 0
            for n in range(iterations):
                if z.real**2 + z.imag**2 <= 100:
                    z = z*z + c
                    m[i, j] = n
                else:
                    break

m = np.zeros((size, size))
mandelbrot_cython(m, size, iterations)

t3 = Timer(lambda: mandelbrot_cython(m, size, iterations))
t3.timeit()
"""

os.system("pause")
