#-*- coding: utf-8 -*-

import os, math

# Série alternée de Leibniz
n = int(input('-->'))
total = 0
for k in range(n):
    total += pow(-1,k)/(2*k+1.0)
print ('Valeur trouvée:', 4*total, '\nValeur exacte', math.pi)

os.system("pause")
