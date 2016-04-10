#-*- coding: utf-8 -*-

import os

def eq2deg(A,B,C):
    from math import sqrt # Permet d'importer la fonction racine carré "sqrt(nombre)"
    D=B*B-4*A*C # On calcule delta, le discriminant, en fonction de A,B et C
    print ("Delta=",D) # On affiche la valeur de delta
    if D<0:
        print ("Il n'y a pas de solutions") # Lorsque delta est négatif, il n'existe pas de solutions
    if D==0:
        print ("Il existe une solution: x0 =", -B/2*A) # Lorsque delta est égale à 0, il existe une solution
    if D>0:
        x1 = (-B-sqrt(D))/2*A
        x2 = (-B+sqrt(D))/2*A
        print ("Il existe deux solutions: x1 =", x1, " et x2 =", x2) # Lorsque delta est positif,il y a deux solutions, X1 et X2

eq2deg(3,5,2)
eq2deg(10,20,5)
eq2deg(5,6,8)

os.system("pause")