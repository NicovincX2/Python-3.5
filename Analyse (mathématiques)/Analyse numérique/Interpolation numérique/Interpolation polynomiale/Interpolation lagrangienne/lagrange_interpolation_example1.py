# -*- coding: utf-8 -*-

import os
from pylab import *

a = 0
b = 8
m = (a + b) / 2
# valeurs de la fonction en a, m, et b
ya = 4
ym = 8
yb = -6

x = linspace(a, b, 101)

l0 = (x - m) / (a - m) * (x - b) / (a - b)
l1 = (x - a) / (m - a) * (x - b) / (m - b)
l2 = (x - a) / (b - a) * (x - m) / (b - m)
P = ya * l0 + ym * l1 + yb * l2

plot([a, m, b], zeros(3), "s")  # position des valeurs 0
plot([a, m, b], [ya, ym, yb], "o")  # position des valeurs de f
plot(x, P)

title("Interpolation de Lagrange")
xlim(-1, 9)
ylim(-8, 10)
text(a, -0.5, "(a,0)", ha="center", va="top")
text(m, -0.5, "(m,0)", ha="center", va="top")
text(b, -0.5, "(b,0)", ha="center", va="top")
text(a, ya + 0.05, "(a,f(a))", ha="right", va="bottom")
text(m, ym + 0.2, "(m,f(m))", ha="left", va="bottom")
text(b, yb - 0.4, "(b,f(b))", ha="left", va="top")
grid()

show()

os.system("pause")
