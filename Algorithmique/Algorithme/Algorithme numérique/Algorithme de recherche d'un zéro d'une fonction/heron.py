# -*- coding: utf-8 -*-

import os


def racine(a, xk, n):
    """
    Calcule une approximation de a à partir d'une première valeur par défaut xk
    On effectue n itérations de l'algorithme de Babylone (ou de Héron)
    """
    if n == 0:
        return xk
    else:
        return racine(a, (xk + a / xk) * 0.5, n - 1)

print(racine(2, 1, 100))

os.system("pause")
