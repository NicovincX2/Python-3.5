# -*- coding: utf-8 -*-

import os
import scipy as sp
import scipy.linalg

def gauss_legendre(n):
    k=sp.arange(1.0,n)       
    a_band = sp.zeros((2,n)) 
    a_band[1,0:n-1] = k/sp.sqrt(4*k*k-1) 
    x,V=sp.linalg.eig_banded(a_band,lower=True) 
    w=2*sp.real(sp.power(V[0,:],2)) 
    return x, w

os.system("pause")