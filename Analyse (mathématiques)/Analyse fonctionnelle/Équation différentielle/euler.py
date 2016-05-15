# -*- coding: utf-8 -*-

import os
from pygal import *
 
def listeEuler(f,x0,y0,pas,n):
    x,y,L = x0,y0,[]
    for k in range(n):
        L += [(x,y)]
        x += pas
        y += pas * f(x,y)
    return L
 
def euler(f,x0,y0,xf,n):
    pas = (xf - x0) / n
    courbe  = XY()
    courbe.title = "Methode d Euler"
    courbe.add("Solution approchee",listeEuler(f,x0,y0,pas,n))
    courbe.render_to_file("courbeEulerPython.svg")

os.system("pause")

