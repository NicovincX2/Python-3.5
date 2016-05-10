# -*- coding: utf-8 -*-

import os
from math import exp,sin,atan,sqrt
import numpy as np
import matplotlib.pyplot as plt

def X(t0,T,h):
    return np.arange(t0,t0+T+h,h)

def Y(t0,T,h,y0,Phi):
    t=X(t0,T,h)
    y=np.zeros(len(t))
    y[0]=y0
    for k in range(len(t)-1):
        y[k+1]=y[k]+h*Phi(t[k],y[k],h)
    return y

def Euler(t,y,h):
    return F(t,y)

def Heun(t,y,h):
    return (F(t,y)+F(t+h,y+h*F(t,y)))/2

def RK4(t,y,h):
    a=F(t,y)
    b=F(t+h/2,y+h*a/2)
    c=F(t+h/2,y+h*b/2)
    d=F(t+h,y+h*c)
    return (a+2*b+2*c+d)/6

def F(t,y):
    return y

t0, T, h = 0, 5, 0.5 ; y0=1

plt.grid()
plt.title('Comparaison des 3 méthodes avec $h='+str(h)+'$')
plt.xlabel('Valeurs de $t$')
plt.ylabel('Valeurs de $y$')
t=X(t0,T,h)
plt.plot(t,Y(t0,T,h,y0,Euler),'b:',linewidth=2,label='Euler')
plt.plot(t,Y(t0,T,h,y0,Heun),'y--',linewidth=2,label='Heun')
plt.plot(t,Y(t0,T,h,y0,RK4),'r-',linewidth=2,label='RK4')
plt.plot(t,np.exp(t),'k-.',linewidth=3,label='Sol. exacte')
plt.legend(loc=0)
plt.savefig('Un_pas.eps')
plt.show()

os.system("pause")