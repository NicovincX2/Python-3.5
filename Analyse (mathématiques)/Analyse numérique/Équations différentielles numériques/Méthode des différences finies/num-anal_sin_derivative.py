# -*- coding: utf-8 -*-

import os
import matplotlib
import numpy as np


def nderiv(y, x):
    "Finite difference derivative of the function f"
    n = len(y)
    d = zeros(n, 'd')  # assume double
    # Use centered differences for the interior points, one-sided differences
    # for the ends
    for i in range(1, n - 1):
        d[i] = (y[i + 1] - y[i - 1]) / (x[i + 1] - x[i - 1])
    d[0] = (y[1] - y[0]) / (x[1] - x[0])
    d[n - 1] = (y[n - 1] - y[n - 2]) / (x[n - 1] - x[n - 2])
    return d

x = np.linspace(0, 2 * pi)
dsin = nderiv(sin(x), x)
plot(x, dsin, label='numerical')
plot(x, cos(x), label='analytical')
title("Comparison of numerical and analytical derivatives of sin(x)")
legend()

os.system("pause")
