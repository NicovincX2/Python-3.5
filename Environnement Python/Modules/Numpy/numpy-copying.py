# -*- coding: utf-8 -*-

import os

# some examples on views and copies from the NumPy tutorial

import numpy as np


a = np.arange(12)

# assignments

print("assignments")

b = a   # no new object is created -- b and a point to the same object
print(b is a)

b.shape = 3, 4   # changes the shape of a too
print(a.shape)


print(a)
print(b)

b[1, 1] = -1    # changes a[1,1] too
print(a)


# views / shallow copy
print("views")

c = a[:]   # or c = a.view()

print(c is a)
print(c.base is a)

c.shape = 12

print(a)
print(c)


c[2] = 100.0
print(a)
print(c)


# deep copy
print("deep copying")

d = a.copy()

print(a)
print(d)

d[:, :] = 0.0

print(a)
print(d)

os.system("pause")
