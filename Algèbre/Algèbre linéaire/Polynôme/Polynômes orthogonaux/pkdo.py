# -*- coding: utf-8 -*-

import os
import numpy as np


def pkdo(p, x, y):
    """
    Evaluate the Vandermonde matrix of PKDO polynomials up to order on the set of points (x,y) 
    """
    import orthopoly as op
    Nx = len(x)
    Np = (p + 1) * (p + 2) / 2
    s = -np.ones(Nx)
    t = y
    dex = np.abs(y - 1) > 1e-10
    s[dex] = 2 * (1 + x[dex]) / (1 - y[dex]) - 1

    # Vandermonde
    V = np.zeros((Nx, Np))

    # Derivative w.r.t. x
    Vx = np.zeros((Nx, Np))

    # Derivative w.r.t. y
    Vy = np.zeros((Nx, Np))

    ll = 0

    tfact0 = np.zeros(Nx)
    tfact = np.ones(Nx)

    Ps = op.jacobi(p, 0, 0, s)
    Psder = op.jacobiD(p, 0, 0, s)

    for jj in xrange(p + 1):

        Pt = op.jacobi(p + 1, 2 * jj + 1, 0, t)
        Ptder = op.jacobiD(p + 1, 2 * jj + 1, 0, t)

        for kk in xrange(p + 1 - jj):

            nfact = np.sqrt((jj + 0.5) * (jj + kk + 1))
            V[:, ll] = nfact * Ps[:, jj] * Pt[:, kk] * tfact
            Vx[:, ll] = Psder[:, jj] * Pt[:, kk]
            Vy[:, ll] = Vx[:, ll] * (1 + s) / 2

            u = Ptder[:, kk] * tfact

            if jj > 0:

                Vx[:, ll] *= nfact * tfact0
                Vy[:, ll] *= tfact0
                u -= 0.5 * jj * Pt[:, kk] * tfact0

            Vy[:, ll] += Ps[:, jj] * u
            Vy[:, ll] *= nfact

            ll += 1

        tfact0 = tfact
        tfact = tfact0 * (1 - t) / 2

    return V, Vx, Vy


if __name__ == '__main__':

    """ Check approximation error of PKDO basis """

    from triquad import triquad
    import sympy as sy
    import numpy as np

    x, y = sy.symbols('x,y')

    f = sy.sin(x - y)
    fx = sy.diff(f, x)
    fy = sy.diff(f, y)

    F = sy.lambdify([x, y], f, "numpy")
    Fx = sy.lambdify([x, y], fx, "numpy")
    Fy = sy.lambdify([x, y], fy, "numpy")

    # Order of quadrature
    p = 10

    # Order of polynomial space
    n = 9

    xq, yq, wq = triquad(p)

    np.set_printoptions(precision=4, linewidth=999)

    V, Vx, Vy = pkdo(n, xq, yq)

    # Check polynomials are orthonormal
    # print np.dot(V.T*wq,Vx)

    # Compute expansion coefficients
    fhat = np.dot(V.T, wq * F(xq, yq))

    # Evaluate approximating polynomial and x derivative on grid
    fpoly = np.dot(V, fhat)
    fxpoly = np.dot(Vx, fhat)
    fypoly = np.dot(Vy, fhat)

    # Print error
    print("Interpolation error = ", np.linalg.norm(F(xq, yq) - fpoly))
    print("x differentiation error = ", np.linalg.norm(Fx(xq, yq) - fxpoly))
    print("y differentiation error = ", np.linalg.norm(Fy(xq, yq) - fypoly))

os.system("pause")
