# -*- coding: utf-8 -*-

import os
from pylab import *

a = 0
b = 8
m = (a + b) / 2

x = linspace(a, b, 101)

l0 = (x - m) / (a - m) * (x - b) / (a - b)
l1 = (x - a) / (m - a) * (x - b) / (m - b)
l2 = (x - a) / (b - a) * (x - m) / (b - m)

plot([a, m, b], zeros(3), "s")  # position des valeurs 0
plot([a, m, b], ones(3), "o")  # position des valeurs 1
plot(x, l0, label="l0")
plot(x, l1, label="l1")
plot(x, l2, label="l2")

title("Polynomes de Lagrange")
xlim(-1, 9)
ylim(-1, 2)
text(a, -0.1, "(a,0)", ha="center", va="top")
text(m, -0.1, "(m,0)", ha="center", va="top")
text(b, -0.1, "(b,0)", ha="center", va="top")
text(a, 1.05, "(a,1)", ha="center", va="bottom")
text(m, 1.05, "(m,1)", ha="center", va="bottom")
text(b, 1.05, "(b,1)", ha="center", va="bottom")
legend()
grid()

show()

os.system("pause")
