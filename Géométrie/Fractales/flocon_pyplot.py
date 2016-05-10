# -*- coding: utf-8 -*-

import os
from matplotlib import pyplot as plt
from math import sqrt
import numpy as np

k=0.5/sqrt(3)
xm=100
seuil=3

def flocon(a,b):
    d=sqrt((b[0]-a[0])**2+(b[1]-a[1])**2)
    if d<seuil:
        plt.plot([a[0],b[0]],[a[1],b[1]],'k-')
    else:
        a1=(2*a+b)/3
        a3=(a+2*b)/3
        a2=(a+b)/2+k*np.array([a[1]-b[1],b[0]-a[0]])
        flocon(a,a1)
        flocon(a1,a2)
        flocon(a2,a3)
        flocon(a3,b)

a=np.array([0,0])
b=np.array([xm,0])
c=np.array([xm/2,-xm*sqrt(3)/2])
plt.axes().set_aspect('equal')
plt.axes().set_xticks([])
plt.axes().set_yticks([])
flocon(a,b)
flocon(b,c)
flocon(c,a)
#plt.subplots_adjust(0.02,0.02,0.98,0.98,0.2,0.2)
plt.show()

os.system("pause")