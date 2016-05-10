# -*- coding: utf-8 -*-

import os
from math import sin,pi,atan,sqrt
import numpy as np
import matplotlib.pyplot as plt

def sortie_filtree_brute(entree):
    T=np.arange(Tmin,Tmax,Te)
    s=np.zeros(len(T))
    e=np.zeros(len(T))
    k=1/(Te*bp) #coeff. redondant
    for n in range(1,len(T)):
        e[n]=entree(n*Te)
        s[n]=(e[n]+k*s[n-1])/(1+k)
    plt.plot(T,e,color='y')
    plt.plot(T,s)
    plt.show()

def sortie_filtree(t,Tmin,Te,bp):
    e=t[:,1]
    Tmax=Tmin+len(e)*Te
    T=np.arange(Tmin,Tmax,Te)
    s=np.zeros(len(T))
    k=1/(Te*bp) #coeff. redondant
    for n in range(1,len(T)):
        s[n]=(e[n]+k*s[n-1])/(1+k)
    plt.plot(T,e,color='y')
    plt.plot(T,t[:,2],color='g')
    plt.plot(T,s)
    plt.show()

def sortie_traitee(entree):
    T=np.arange(Tmin,Tmax,Te)
    s=np.zeros(len(T))
    e=np.zeros(len(T))
    k=1/(Te*bp) #coeff. redondant
    for n in range(1,len(T)):
        e[n]=entree(n*Te)
        s[n]=(e[n]+k*s[n-1])/(1+k)
    phi=-atan(pulsation/bp)
    decalage=phi/pulsation
    amplification=sqrt(1+(pulsation/bp)**2)
    plt.plot(T,e,color='y')
    plt.plot(T+decalage,amplification*s)
    plt.show()

def sinus_bruite(x):
    return sin(pulsation*x)+0.2*sin(10*pulsation*x)

Tmin=0
Tmax=1.001
Te=0.001
bp=.1
pulsation=1
t=np.loadtxt("Donnees_derivee_derivee-filtree.csv",delimiter=';')
#sortie_filtree_brute(sinus_bruite)
sortie_filtree(t,0,.001,500)
#sortie_traitee(sinus_bruite)

os.system("pause")