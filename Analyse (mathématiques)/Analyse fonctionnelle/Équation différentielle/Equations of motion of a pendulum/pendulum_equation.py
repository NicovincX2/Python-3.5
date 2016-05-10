# -*- coding: utf-8 -*-

import os
from math import sin,pi
import numpy as np
import matplotlib.pyplot as plt

def X(t0,T,h):
    return np.arange(t0,t0+T+h,h)

def Y(t0,T,h,y0,Phi):
    t=X(t0,T,h)
    y=np.zeros((2,len(t)))
    y[:,0]=y0           
    for k in range(len(t)-1):
        y[:,k+1]=y[:,k]+h*Phi(t[k],y[:,k],h)
    return y[0,:]

def F(t,y):
    return np.array([y[1],G(t,y[0],y[1])])

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

def G(t,u,v):
    return -sin(u)

t0, T, h = 0, 30, 0.005
y0=[0.0, 2.0]

plt.grid()
plt.title('Comparaison des 3 méthodes avec $h='+str(h)+'$ \n Condition initiale : $['+str(u0)+','+str(v0)+']$')
plt.xlabel('Valeurs de $t$')
plt.ylabel('Valeurs de $y$')
t=X(t0,T,h)
plt.plot(t,Y(t0,T,h,y0,Euler),'b:',linewidth=2,label='Euler')
plt.plot(t,Y(t0,T,h,y0,Heun),'y--',linewidth=2,label='Heun')
plt.plot(t,Y(t0,T,h,y0,RK4),'r-',linewidth=2,label='RK4')
plt.legend(loc=0)
plt.savefig('Pendule1.eps')
plt.show()

os.system("pause")