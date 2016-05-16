# -*- coding: utf-8 -*-

import os

'''
Pour un exercice de reconnaissance d'un filtre qui puisse jouer le rôle 
de dérivateur dans un certain intervalle de fréquences. On en génère un du 
premier ordre (passe-haut) et un du second ordre (passe-bande).
'''

from scipy import signal        # Pour les fonctions 'lti' et 'bode'
import numpy as np              # Pour np.logspace

# Ceci est un filtre passe-haut donc potentiellement dérivateur à BF

num = [0.01,0]                  # Polynôme au numérateur   (->    0.01*jw   )
den = [0.0099,1]                # Polynôme au dénominateur (-> 0.0099*jw + 1)

f = np.logspace(-1,4,num=200)   # L'intervalle de fréquences considéré (échelle log)
s1 = signal.lti(num,den)        # La fonction de transfert
f,GdB,phase = signal.bode(s1,f) # Fabrication automatique des données

from bode import diag_bode      # Pour générer le diagramme de Bode

# Appel effectif à la fonction dédiée.
diag_bode(f,GdB,phase,'PNG/S11_derivateur.png') 

# Ceci est un filtre passe-bande du second ordre (dérivateur à BF)

num2 = [0.01,0]                 # Numérateur   (->           0.01*jw         )
den2 = [10**-2,0.01,1]          # Dénominateur (-> 0.01*(jw)**2 + 0.01*jw + 1)

f = np.logspace(-1,4,num=200)   # Intervalle de fréquences en échelle log 
s2 = signal.lti(num2,den2)      # Fonction de transfert
f,GdB,phase = signal.bode(s2,f) # Fabrication des données
diag_bode(f,GdB,phase,'PNG/S11_derivateur2.png') # et du diagramme

os.system("pause")