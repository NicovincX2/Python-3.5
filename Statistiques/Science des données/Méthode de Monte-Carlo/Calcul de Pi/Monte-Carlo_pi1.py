#-*- coding: utf-8 -*-

"""
Méthode de Monte-Carlo
Soit C un cercle de centre O(x;y) et de rayon r. Un point M de coordonnées (a;b) appartient à C si et seulement si (a–x)^2+(b–y)^2=r^2.
Ici nous avons un cercle trigonométrique (le cercle dont le centre est l'origine du repère et dont le rayon vaut 1), donc (a–x)^2+(b–y)^2=r^2 devient a^2+b^2=1.
Soit un point M de coordonnées (a, b), où 0<a<1 et 0<b<1. On tire aléatoirement les valeurs de a et b.
Le point M appartient au disque de centre (0,0) de rayon 1 si et seulement si a^2+b^2<=1. La probabilité que le point M appartienne au disque est π/4.
En faisant le rapport du nombre de points dans le disque au nombre de tirages, on obtient une approximation du nombre π/4 si le nombre de tirages est grand.
L'aire du carré vaut (R)^2 soit 1. L'aire du quart de cercle vaut (Pi*R^2)/4 soit Pi/4.
En choisissant N points aléatoires (à l'aide d'une distribution uniforme) à l'intérieur du carré, la probabilité que ces points se trouvent aussi dans le quart de cercle est:
p=(aire du cercle)/(aire du carré)=Pi/4
Soit n, le nombre points effectivement dans le cercle, il vient alors:
p=n/N=Pi/4 d'où  Pi=4*(n/N)
"""
import os
import random
import math
import matplotlib.pyplot as plt

x_inner, y_inner = [], []
x_outer, y_outer = [], []
for i in range(100000):
    a, b = random.uniform(-1., 1.), random.uniform(-1., 1.)
    length = math.sqrt(a**2 + b**2)
    if length < 1:
        x_inner.append(a)
        y_inner.append(b)
    else:
        x_outer.append(a)
        y_outer.append(b)
plt.scatter(x_inner, y_inner, c='red', marker='.', s=200)
plt.scatter(x_outer, y_outer, c='blue', marker='.', s=200)
print('La valeur de pi approchée :', 4 * len(x_inner) /
      float(len(x_inner) + len(x_outer)), '\nLa valeur de pi exacte :', math.pi)
plt.axis('equal')
plt.savefig('Monte-Carlo_pi_color.png')
plt.show()

os.system("pause")
