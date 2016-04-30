# -*- coding: utf-8 -*-

import os

class Triangle:
    def __init__(self, x0y0, x1y1, x2y2, color='b'):
        self.x0y0 = x0y0
        self.x1y1 = x1y1
        self.x2y2 = x2y2
        self.x = array([ self.x0y0[0], self.x1y1[0], self.x2y2[0] ])
        self.y = array([ self.x0y0[1], self.x1y1[1], self.x2y2[1] ])
        self.color = color
    def __repr__(self):
        return 'Triangle with corners:'+str(self.x0y0)+str(self.x1y1)+str(self.x2y2)
    def area(self):
        A = 0.5 * abs( (self.x[0]-self.x[2])*(self.y[1]-self.y[0]) - 
                       (self.x[0]-self.x[1])*(self.y[2]-self.y[0]) )
        return A
    def plot(self):
        fill(self.x, self.y, color=self.color)

tlist = []  # Start with an empty list
t1 = Triangle( (0,1), (5,0), (3,3), 'b' )
tlist.append(t1)  # Add t1 to the list
t2 = Triangle( (3,4), (1,6), (-2,3), 'r' )
tlist.append(t2)
t3 = Triangle( (8,-1), (6,4), (2,6), 'g' )
tlist.append(t3)
for t in tlist:
    t.plot()
axis('scaled')

areatot = 0.0
for t in tlist:
    areatot += t.area()
print 'total area: ',areatot

os.system("pause")

