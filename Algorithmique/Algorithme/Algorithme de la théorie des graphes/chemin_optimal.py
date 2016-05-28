# -*- coding: utf-8 -*-

import os
import numpy as np


def poids_min(M):
    n, p = np.shape(M)

    def cout(i, j):
        if i == n - 1 and j == p - 1:
            return M[i, j]
        if i == n - 1:
            return M[i, j] + cout(i, j + 1)
        if j == p - 1:
            return M[i, j] + cout(i + 1, j)
        return M[i, j] + min(cout(i + 1, j), cout(i, j + 1))
    return cout(0, 0)


def construire_tableaux():
    global M, cout, choix
    n, p = np.shape(M)
    cout = np.zeros((n, p))
    choix = np.zeros((n, p), dtype=np.str)
    cout[n - 1, p - 1] = M[n - 1, p - 1]
    choix[n - 1, p - 1] = ' '  # aucun choix !
    for j in range(p - 2, -1, -1):  # remplissage de la dernière ligne
        cout[n - 1, j] = cout[n - 1, j + 1] + M[n - 1, j]
        choix[n - 1, j] = '>'  # forcément vers la droite
    for i in range(n - 2, -1, -1):  # remplissage de la ligne i de droite à gauche
        cout[i, p - 1] = cout[i + 1, p - 1] + M[i, p - 1]
        choix[i, p - 1] = 'V'  # forcément vers le bas
        for j in range(p - 2, -1, -1):
            if cout[i + 1, j] < cout[i, j + 1]:
                cout[i, j] = cout[i + 1, j] + M[i, j]
                choix[i, j] = 'V'
            else:
                cout[i, j] = cout[i, j + 1] + M[i, j]
                choix[i, j] = '>'
    return cout[0, 0]


def chemin():
    n, p = np.shape(M)
    lst = [(0, 0)]
    i, j = 0, 0
    for k in range(n + p - 2):
        if choix[i, j] == 'V':
            i += 1
        else:
            j += 1
        lst.append((i, j))
    return lst

M = np.array([[1, 4, 6, 8, 2], [2, 4, 0, 2, 4], [3, 5, 0, 8, 9],
              [8, 0, 7, 6, 0], [0, 9, 5, 9, 1], [2, 7, 5, 5, 2]])

print(construire_tableaux())
print(cout)
print(choix)
print(chemin())

os.system("pause")
