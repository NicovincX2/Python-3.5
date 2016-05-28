# -*- coding: utf-8 -*-


"""
    Class for generating 2D finite element matrices

    Copyright (C) 2013 Greg von Winckel

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.

    Created: Sun May 26 11:26:58 MDT 2013

"""


import numpy as np
import matplotlib.pyplot as plt
import matplotlib.tri as tri
import os
from scipy.sparse import csr_matrix
from scipy.sparse.linalg import spsolve


class femmat2d(object):
    """ This object is created using a triangulation and produces
        the various matrices needed for a finite element calcuation
        as well as specifyin which grid points are on the interior
        and which are on the boundary.

        This version of the code supports piecewise linear variable "reaction"
        coefficients and piecewise constant "diffusion" coefficients  """

    def __init__(self, triang):
        self.tri = triang.triangles
        self.x = triang.x
        self.y = triang.y
        self.nbr = triang.neighbors
        self.nvert = len(self.x)       # Number of grid points (vertices)
        self.nel = len(self.tri)     # Number of elements (triangles)

        # Determine which points are on the boundary and which are in the
        # interior
        self.bpt = set(self.tri.flat[np.flatnonzero(triang.neighbors == -1)])
        self.ipt = set(np.arange(self.nvert)).difference(self.bpt)

        # Vertices of reference triangle
        S = np.array(((-1, -1), (1, 0), (0, 1)))

        # Coefficients of mapping from reference to target elements
        # A1 = (a11,a21), A2 = (a12,a22)
        A1 = np.dot(x[self.tri], S)
        A2 = np.dot(y[self.tri], S)
        self.Adet = A1[:, 0] * A2[:, 1] - A1[:, 1] * A2[:, 0]

        # Coefficients of inverse mapping
        Ap1 = np.c_[A2[:, 1], -A1[:, 1]] / self.Adet.reshape(self.nel, 1)
        Ap2 = np.c_[-A2[:, 0], A1[:, 0]] / self.Adet.reshape(self.nel, 1)

        # Basic matrix types on the reference element
        self.M = np.array(((2, 1, 1), (1, 2, 1), (1, 1, 2))) / 24.0
        self.Kxx = np.array(((1, -1, 0), (-1, 1, 0), (0, 0, 0))) / 2.0
        self.Kxy = np.array(((1, 0, -1), (-1, 0, 1), (0, 0, 0))) / 2.0
        self.Kyy = np.array(((1, 0, -1), (0, 0, 0), (-1, 0, 1))) / 2.0
        self.Phi1 = np.array(((6, 2, 2), (2, 2, 1), (2, 1, 2))) / 120.0
        self.Phi2 = np.array(((2, 2, 1), (2, 6, 2), (1, 2, 2))) / 120.0
        self.Phi3 = np.array(((2, 1, 2), (1, 2, 2), (2, 2, 6))) / 120.0

        # Compute all of the elemental stiffness and mass matrices
        self.cxx = (Ap1[:, 0]**2 + Ap1[:, 1]**2) * self.Adet
        self.cxy = (Ap1[:, 0] * Ap2[:, 0] + Ap1[:, 1] * Ap2[:, 1]) * self.Adet
        self.cyy = (Ap2[:, 0]**2 + Ap2[:, 1]**2) * self.Adet

        # Indices of the nonzero elements in the assembled matrices
        self.rows = np.array(map(lambda s: np.outer(np.ones(3), self.tri[s]),
                                 range(self.nel))).flatten("C")
        self.cols = np.array(map(lambda s: np.outer(self.tri[s], np.ones(3)),
                                 range(self.nel))).flatten("C")

    def getInteriorPoints(self):
        return list(self.ipt)

    def getBoundaryPoints(self):
        return list(self.bpt)

    def assemble_Mtype(self, v=None, order=0):
        """ Corresponds to the weak form (phi_j,v*phi_k) where 
           if order = 0, v has the same length as the number of elements
           if order = 1, v has the same length as the number of vertices """

        if v is None:

            Mel = np.kron(self.Adet, self.M)
        else:
            if order is 0:
                Mel = np.kron(self.Adet * v, self.M)
            else:
                Mel = np.kron(v[self.tri[:, 0]] * self.Adet, self.Phi1) + \
                    np.kron(v[self.tri[:, 1]] * self.Adet, self.Phi2) + \
                    np.kron(v[self.tri[:, 2]] * self.Adet, self.Phi3)

        M = csr_matrix((Mel.flatten("F"), (self.rows, self.cols)))
        return M

    def assemble_Ktype(self, v=None):
        """ Corresponds to the weak form v*(grad[phi_j],\grad[phi_k]) where
            v should have the same length as the number of elements """

        if v is None:

            Kel = np.kron(self.cxx, self.Kxx)   + \
                np.kron(self.cxy, self.Kxy)   + \
                np.kron(self.cxy, self.Kxy.T) + \
                np.kron(self.cyy, self.Kyy)

        else:
            Kel = np.kron(v * self.cxx, self.Kxx)   + \
                np.kron(v * self.cxy, self.Kxy)   + \
                np.kron(v * self.cxy, self.Kxy.T) + \
                np.kron(v * self.cyy, self.Kyy)

        K = csr_matrix((Kel.flatten("F"), (self.rows, self.cols)))
        return K


if __name__ == '__main__':

    # number of grid points per dimension
    n = 100

    q = np.linspace(-2, 2, n)

    # Create tensor product grid of x,y coordinates and column stack them as
    # vectors
    x, y = map(lambda s: s.flatten(), np.meshgrid(q, q))

    # Create triangle mesh
    t = tri.Triangulation(x, y)

    fem = femmat2d(t)

    # Compute centroids of elements
    xc = np.mean(x[t.triangles], 1)
    yc = np.mean(y[t.triangles], 1)

    # Number of elements
    Nel = t.triangles.shape[0]

    # Number of vertices
    Nvert = len(x)

    # Variable "diffusion" coefficient (piecewise constant)
    u = np.ones(Nel)

    dex = np.where((xc > 0) & (yc > 0))
    u[dex] = 2

    # Variable "reaction" coefficient (piecesise linear)
    v = np.exp(x - y)

    f = 50 * np.sin(np.pi * (y + x))

    M = fem.assemble_Mtype()
    V = fem.assemble_Mtype(v, 1)
    U = fem.assemble_Ktype(u)
    A = U + V
    F = M * f

    i = fem.getInteriorPoints()
    b = fem.getBoundaryPoints()

    xb = x[b]
    yb = y[b]

    psi = np.zeros(Nvert)

    # Bounday forcing term
    g = np.zeros(Nvert)
#    g[b] = np.sin(np.pi*xb)

    # Dirichlet problem
#    psi[i] = spsolve(A[i,:][:,i],F[i]-A[i,:][:,b]*g[b])

    # Neumann problem
    psi = spsolve(A, F - g)

    # Plot solution
    plt.tricontourf(t, psi, 50)
    plt.show()

os.system("pause")
