# -*- coding: utf-8 -*-

import os
import numpy as np
import orthopoly as op


def triquad(n):
    """
        Compute the quadrature nodes and weights for integrating a
        function f(x,y) over a triangle with vertices {(-1,-1),(-1,1),(1,-1)}
    """
    alphax, betax = op.rec_jacobi(n, 0, 1)
    x, wx = op.gauss(alphax, betax)
    x = (1 + x) / 2
    wx = wx / 2

    alphat, betat = op.rec_jacobi(n, 0, 0)
    t, wt = op.gauss(alphat, betat)
    t = (1 + t) / 2
    wt = wt

    tt, xx = np.meshgrid(t, x)
    yy = xx * tt

    xx = 1 - 2 * xx
    yy = 2 * yy - 1

    ww = np.outer(wx, wt)

    xx = xx.flatten()
    yy = yy.flatten()
    ww = ww.flatten()

    return xx, yy, ww

if __name__ == '__main__':
    """
    Compute the integral of f(x,y) = exp(x+y) on the triangle with 
    vertices {(-1,-1),(-1,1),(1,-1)} using mapped Gauss quadrature 
    and compare the results with sympy

    """
    xq, yq, wq = triquad(6)

    import sympy as sy
    import numpy as np

    x, y = sy.symbols('x,y')
    Q = sy.integrate(sy.integrate(sy.exp(x + y), (y, -1, -x)), (x, -1, 1))

    print("sympy result = ", Q.evalf(12))
    print("Triangular Gauss quadrature result = ", sum(wq * np.exp(xq + yq)))

os.system("pause")
