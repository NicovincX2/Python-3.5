# -*- coding: utf-8  -*-

"""
    Function for generating the Proriol-Koornwinder-Dubiner-Owens 
    orthogonal polynomials and their derivatives on the triangle

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

    Last updated: Tue Sep 24 09:08:21 MDT 2013

"""




import orthopoly as op
import numpy as np

def pkdo(p,x,y):
    """
    Evaluate the Vandermonde matrix of PKDO polynomials up to order on the set of points (x,y) 
    as well as the Vandermondes containing the x and y derivatives of the polynomials
    """
    Nx = len(x)
    Np = (p+1)*(p+2)/2
    s = -np.ones(Nx)
    t = y
    dex = np.abs(y-1) > 1e-10
    s[dex] = 2*(1+x[dex])/(1-y[dex])-1

    # Vandermonde
    V = np.zeros((Nx,Np))

    # Derivative w.r.t. x
    Vx = np.zeros((Nx,Np))

    # Derivative w.r.t. y
    Vy = np.zeros((Nx,Np))

    ll = 0

    tfact0 = np.zeros(Nx)
    tfact  = np.ones(Nx)

    Ps = op.jacobi(p,0,0,s)
    Psder = op.jacobiD(p,0,0,s)
 
    for jj in range(p+1):

        Pt = op.jacobi(p+1,2*jj+1,0,t)
        Ptder = op.jacobiD(p+1,2*jj+1,0,t)

        for kk in range(p+1-jj):
            
            nfact = np.sqrt((jj+0.5)*(jj+kk+1))                
            V[:,ll] = nfact*Ps[:,jj]*Pt[:,kk]*tfact
            Vx[:,ll] = Psder[:,jj]*Pt[:,kk]
            Vy[:,ll] = Vx[:,ll]*(1+s)/2

            u = Ptder[:,kk]*tfact

            if jj>0:

                Vx[:,ll] *= nfact*tfact0
                Vy[:,ll] *= tfact0
                u -= 0.5*jj*Pt[:,kk]*tfact0

            Vy[:,ll] += Ps[:,jj]*u
            Vy[:,ll] *= nfact
              
            ll += 1
        
        tfact0 = tfact        
        tfact = tfact0*(1-t)/2

    return V,Vx,Vy
