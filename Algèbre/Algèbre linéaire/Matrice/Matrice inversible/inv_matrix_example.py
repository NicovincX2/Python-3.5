# -*- coding: utf-8 -*-

""""
    This program calculates the inverse of a matrix by many ways.
    Marina von Steinkirch, spring/2013 (based on Mike Zingale's codes)
"""

import numpy as npy
from scipy import linalg 
from inverseGauss import inverseGauss
from inverseNewton import inverseNewton
import os

def main():
    A = npy.array([ [4, 3, 4, 10], [2, -7, 3, 0], [-2, 11, 1, 3], [3, -4, 0, 2] ], dtype=npy.float64)
    
    
    print "\nInverse matrix calculated by the Numpy API:"
    AinvNpy = linalg.inv(A)
    print "NumPy: A . Ainv = \n", npy.dot(A, AinvNpy)
    print "NumPy: Ainv = \n", AinvNpy
    
    print "\nInverse matrix calculated by the Gauss method:"    
    AinvGauss = inverseGauss(A)
    print "Gauss: A . Ainv = \n", npy.dot(A, AinvGauss)
    print "Gauss: Ainv = \n", AinvGauss
    
    print "\nInverse matrix calculated by the Newton method:"
    AinvNewton, error, nIter = inverseNewton(A)
    print "Newtow: A . Ainv = \n", npy.dot(A, AinvNewton)
    print "Newtow: Ainv = \n", AinvNewton
    print "Number of iterations: ", nIter
    print "Error from Numpy API results: ", error
    
    print "\nDone!"

if __name__ == "__main__":
    main()

os.system("pause")