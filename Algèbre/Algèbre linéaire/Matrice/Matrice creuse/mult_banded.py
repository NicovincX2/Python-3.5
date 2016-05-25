# -*- coding: utf-8  -*-

"""
    Multiplication ny a banded matrix using the same representation as
    scipy.linalg.solve_banded

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

    Created: Sat Oct 19 00:11:30 MDT 2013

"""

import os
import numpy as np
from scipy.linalg import solve_banded

def mult_banded(l_and_u,ab,x):

    n = len(x)

    pos = lambda j:j*(j>0)

    # Number of lower and upper diagonals
    l,u = l_and_u

    # Total number of bands     
    m = l+u+1

    # Number of zeros on the left
    zl = [pos(u-k) for k in range(m)]   
    
    # Number of zeros on the right
    zr = [pos(k-u) for k in range(m)]

    # Locations of nonzero elements in ab by row
    loc = [range(zl[k],n-zr[k]) for k in range(m)]

    def pad(k,v): return np.hstack((np.zeros(zr[k]),v,np.zeros(zl[k])))
    
    return sum([pad(k,ab[k,loc[k]]*x[loc[k]]) for k in range(m)])


if __name__ == '__main__':

    u = 2
    l = 4
    m = u+l+1
    n = 10

    ab = np.random.randn(m,n)
    x = np.random.randn(n)
    b = mult_banded((l,u),ab,x)
    y = solve_banded((l,u),ab,b)

    print(x-y)

os.system("pause")