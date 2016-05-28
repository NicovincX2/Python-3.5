# -*- coding: utf-8 -*-

import os

# Derive n fois


def derive(f, precision):
    """
    renvoie une approximation de la fonction dérivée de f
    avec un pas de dx qui est une puissance de 2
    """
    dx = 2**-precision
    return lambda x: (f(x + dx) - f(x)) / dx


def derive_n_fois1(f, precision, n):
    # version récursive du calcul de la dérivée n-eme
    assert n >= 0, "n doit être positif !"
    if n == 0:  # cas terminal
        return f  # f^(0) = f
    return derive(derive_n_fois1(f, precision, n - 1), precision)
    # f^(n) = derivée de f^(n - 1)


def derive_n_fois2(f, precision, nb_total_de_derivations):
    # avec  while
    assert nb_total_de_derivations >= 0, "nb de deriv doit être positif !"
    derivee_k_de_f = f
    nb_de_derivations = 0
    while nb_de_derivations < nb_total_de_derivations:
        derivee_k_de_f = derive(derivee_k_de_f, precision)
        nb_de_derivations += 1
    return derivee_k_de_f

os.system("pause")
