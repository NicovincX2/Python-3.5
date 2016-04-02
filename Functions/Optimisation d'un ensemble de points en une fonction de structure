# -*- coding: utf-8 -*-

# http://kmdb.pagesperso-orange.fr/_src/_python/_formation_2010/python_formation_exemples_optimisation.html

import os

# Minimiser le résidu formé par la différence entre une fonction de structure donnée et un ensemble de points issus d’expérimentations.

import numpy as np

# donnees = np.loadtxt('donnees-moindrescarres.dat',skiprows=1)
t , yb = donnees[:,0] , donnees[:,1]

plot(t,yb,'bo')
grid(True)
xlabel(r'$t$',size=20)
ylabel(r'$\tilde{y}$',size=20)
title(r'Donn\'{e}es exp\'{e}rimentales',size=18)

def y(t,p):
    """Exponentielle decroissante."""
    return p[0]*np.exp(-p[1]*t)

def residu(p):
    """Residu."""
    return y(t,p)-yb


LM = op.leastsq(residu,[1.0,1.0],full_output=1)
LM[0]
LM[1]
LM[2]['nfev']

os.system("pause")
