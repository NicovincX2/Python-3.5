# -*- coding: utf-8 -*-

import os

# integration numerique par la methode des rectangles avec alpha = a

from pylab import *

xmin = 0
xmax = 3 * pi / 2
nbx = 20
nbi = nbx - 1  # nombre d'intervalles

x = linspace(xmin, xmax, nbx)
y = cos(x)
plot(x, y, "bo-")

integrale = 0
for i in range(nbi):
    integrale = integrale + y[i] * (x[i + 1] - x[i])
    # dessin du rectangle
    x_rect = [x[i], x[i], x[i + 1], x[i + 1], x[i]]  # abscisses des sommets
    y_rect = [0, y[i], y[i], 0, 0]  # ordonnees des sommets
    plot(x_rect, y_rect, "r")
print("integrale =", integrale)

show()

os.system("pause")
