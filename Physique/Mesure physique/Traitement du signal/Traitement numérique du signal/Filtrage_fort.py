# -*- coding: utf-8 -*-

import os
import numpy as np
import matplotlib.pyplot as plt

def X(t0,T,h):
    return np.arange(t0,t0+T,h)

def Y(t0,T,h,y0,Phi):
    t=X(t0,T,h)
    y=np.zeros(len(t))
    y[0]=y0
    for k in range(len(t)-1):
        y[k+1]=y[k]+h*Phi(k,t[k],y[k],h)
    return y

def F(k,t,y):
    return b*(eb[k]-y)

def Euler(k,t,y,h):
    return F(k,t,y)

def Heun(k,t,y,h):
    return (F(k,t,y)+F(k+1,t+h,y+h*F(k,t,y)))/2

donnees=np.loadtxt('Filtrage_fort.csv',delimiter=';')
n, p = np.shape(donnees)
t0, T = 0, 1
y0=0
t , h = np.linspace(t0,t0+T,num=n+1,retstep=True)
b=1000

eb=donnees[:,0] #données brutes
ef=donnees[:,1] #données filtrées

plt.grid()
plt.title('Comparaison des 2 méthodes à partir de données discrètes')
plt.xlabel('Valeurs de $t$')
plt.ylabel('Valeurs de $y$')
t=X(t0,T,h)
plt.plot(t,Y(t0,T,h,y0,Euler),'b:',linewidth=2,label='Euler')
plt.plot(t,Y(t0,T,h,y0,Heun),'y--',linewidth=2,label='Heun')
plt.plot(t,eb,'k-.',linewidth=3,label='Entrée brute')
plt.plot(t,ef,'k-',linewidth=1,label='Entrée filtrée')
plt.legend(loc=0)
plt.show()

os.system("pause")