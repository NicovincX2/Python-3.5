# -*- coding: utf-8 -*-

import os

'''
Un filtre "bizarre" dont il faut trouver la fonction de transfert sachant 
qu'il est du premier ordre.
'''

from scipy import signal  # Pour lti et bode
import numpy as np       # Pour l'échantillonnage

num = [0.001, 10.1]       # Numérateur   (-> 0.001*jw + 10.1)
den = [0.0101, 1]         # Dénominateur (-> 0.0101*jw + 1  )


# Extraction des données
f = np.logspace(0, 6, num=200)
s1 = signal.lti(num, den)
f, GdB, phase = signal.bode(s1, f)

# Et préparation du diagramme
from bode import diag_bode
diag_bode(f, GdB, phase, 'PNG/S11_filtre_bizarre.png')

os.system("pause")
