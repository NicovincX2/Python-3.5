# -*- coding: utf-8 -*-

import os

'''
Simple illustration de la notion de battements par superposition de deux ondes 
sinusoïdales de pulsation proches.
'''

import numpy as np
import matplotlib.pyplot as plt


t  = np.linspace(0,10,1000)    # Echantillonnage en temps
w1 = 25                        # La pulsation du premier signal
w2 = w1*1.04                   # La pulsation du second  signal
S1 = np.cos(w1*t)              # Le premier signal proprement dit
S2 = np.cos(w2*t)              # Le second  signal proprement dit
S3 = S1+S2                     # La somme des deux

plt.subplot(211)               # La figure du dessus contient
plt.title('Illustration de la notion de battements')
plt.plot(t,S1)                 # le premier signal et
plt.plot(t,S2)                 # le second  signal.
plt.ylabel('Deux cosinus')
plt.subplot(212)               # La figure du dessous
plt.plot(t,S3)                 # contient leur somme
plt.ylabel('et leur somme')
plt.xlabel('Temps')            
plt.savefig('PNG/S03_battements.png')

os.system("pause")