# -*- coding: utf-8 -*-

import os


class Circle:

    def __init__(self, x0, y0, R):
        self.x0 = x0
        self.y0 = y0
        self.R = R

    def area(self):
        A = pi * self.R**2
        return A

    def plot(self, Rstar):
        if self.R < Rstar:
            color = 'b'
        else:
            color = 'r'
        alpha = linspace(0, 2 * pi, 100)
        fill(self.x0 + self.R * cos(alpha), self.y0 +
             self.R * sin(alpha), color=color, alpha=0.5)

data = loadtxt('circle_data.txt')
clist = []
for i in range(20):
    c = Circle(data[i, 0], data[i, 1], data[i, 2])
    clist.append(c)
areatot = 0.0
for c in clist:
    areatot += c.area()
    c.plot(1.0)
axis('scaled')
print('total area: ', areatot)

os.system("pause")
