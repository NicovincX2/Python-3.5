# -*- coding: utf-8 -*-

import os
import numpy as np
import scipy.optimize as so


def g(x):
    return np.log(x**2) - 2

x = so.newton(g, 1)
print('value of x:', x)
print('ln(x^2):', np.log(x**2))

os.system("pause")
