# -*- coding: utf-8 -*-

import os


def dico_initial():
    d = [' ']
    for k in range(26):
        d.append(chr(65 + k))  # les majuscules
    return d


def indice(s, d):
    for k in range(len(d)):
        if d[k] == s:
            return k
    return -1


def compression(s):
    d = dico_initial()
    sortie = []
    mot = ''
    for c in s:
        if mot + c in d:
            mot += c
        else:
            sortie.append(indice(mot, d))
            d.append(mot + c)
            mot = c
    sortie.append(indice(mot, d))
    print(d)  # pour voir le dictionnaire
    return sortie


def decompression(L):
    d = dico_initial()
    mot = d[L[0]]
    sortie = mot
    for i in L[1:]:
        if i < len(d):
            entree = d[i]
        else:
            entree = mot + mot[0]
        sortie += entree
        d.append(mot + entree[0])
        mot = entree
    print(d)  # pour voir le dictionnaire
    return sortie


# s='ABABABABABAB'
s = 'LE LYCEE CLEMENCEAU DE NANTES RUE CLEMENCEAU A NANTES'
print(s)
L = compression(s)
print(L)
print(decompression(L))
print('Avant compression : ', len(s))
print('Après compression : ', len(L))
print('Taux de compression : ', round(100 * len(L) / len(s)), '%')

os.system("pause")
