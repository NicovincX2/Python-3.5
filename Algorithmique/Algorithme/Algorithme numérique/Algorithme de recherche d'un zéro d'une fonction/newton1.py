# -*- coding: utf-8 -*-

import os
import numpy as np


def f(x):
    return 0.5 - np.exp(-x)


def fp(x):
    return np.exp(-x)


def newtonsmethod(func, funcp, xs, tol=1e-6, nmax=10):
    f = func(xs)
    for i in range(nmax):
        fp = funcp(xs)
        xs = xs - f / fp
        f = func(xs)
        print(xs, func(xs))
        if abs(f) < tol:
            print('tolerance reached in', i + 1, 'iterations')
            break
    if abs(f) > tol:
        print('Max number of iterations reached before convergence')
    return xs

print('starting at x=1')
xzero = newtonsmethod(f, fp, 1)
print('xzero,f(xzero) ', xzero, f(xzero))

print('starting at x=4')
xzero = newtonsmethod(f, fp, 4, nmax=40)
print('xzero,f(xzero) ', xzero, f(xzero))

xzero = newtonsmethod(np.sin, np.cos, 1)
print('starting point is x=1')
print('xzero,sin(xzero) ', xzero, np.sin(xzero))

xzero = newtonsmethod(np.sin, np.cos, 1.5)
print('starting point is x=1.5')
print('xzero,sin(xzero) ', xzero, np.sin(xzero))
print('xzero / pi ', xzero / np.pi)

os.system("pause")
