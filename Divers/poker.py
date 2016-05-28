# -*- coding: utf-8 -*-

import os

from collections import Counter
from itertools import product, combinations, islice

# Liste des symboles des cartes
symboles = ['Trefle', 'Carreau', 'Coeur', 'Pique']

# Liste des valeurs dans un jeu de 32 cartes
vals_32 = ['Sept', 'Huit', 'Neuf', 'Dix', 'Valet', 'Dame', 'Roi', 'As']

# Ensemble des valeurs dans un jeu de 52 cartes
vals_52 = ['Deux', 'Trois', 'Quatre', 'Cinq', 'Six'] + vals_32


def jeu(vals):
    """Ensemble des cartes selon les valeurs choisies 2 -> As ou 7 -> As"""
    return product(vals, symboles)


def hauteur(carte):
    """Hauteur d'une carte. Une carte est un couple (valeur,symbole)"""
    return carte[0]


def couleur(carte):
    """Couleur d'une carte. Une carte est un couple (valeur,symbole)"""
    return carte[1]


def mains(vals):
    """Ensemble des sous-ensembles de jeu de cardinal 5 : c'est donc l'ensemble des mains de 5 cartes"""
    return combinations(jeu(vals), 5)


def hauteurs(main):
    """Liste des hauteurs d'une main"""
    return map(hauteur, main)


def couleurs(main):
    """Ensemble des couleurs d'une main"""
    return map(couleur, main)


def est_carre(main):
    """Teste si une main contient quatre cartes de même hauteur"""
    return 4 in Counter(hauteurs(main)).values()


def est_full(main):
    """Teste si une main contient trois cartes de même hauteur et deux d'une autre"""
    return {2, 3} == set(Counter(hauteurs(main)).values())


def est_double_paire(main):
    """Teste si une main contient 2 cartes de même hauteur et deux d'une autre"""
    return [1, 2, 2] == sorted(list(Counter(hauteurs(main)).values()))


def est_brelan(main):
    """Teste si une main contient 3 cartes de même hauteur"""
    return [1, 1, 3] == sorted(list(Counter(hauteurs(main)).values()))


def est_paire(main):
    """Teste si une main contient 2 cartes de même hauteur"""
    return [1, 1, 1, 2] == sorted(list(Counter(hauteurs(main)).values()))


def meme_couleur(main):
    """Teste si une main contient cinq cartes de même couleur"""
    return len(Counter(couleurs(main)).keys()) == 1


def suites(vals):
    """Ensemble d'ensembles de hauteurs de mains contenant une quinte"""
    return [set(islice(vals, k, k + 5, 1)) for k in range(len(vals) - 4)]


def est_quinte_32(main):
    """Teste si une main de 32 cartes contient une quinte avec des couleurs différentes"""
    return (set(hauteurs(main)) in suites(vals_32)) and not meme_couleur(main)


def est_quinte_52(main):
    """Teste si une main de 52 cartes contient une quinte avec des couleurs différentes"""
    return (set(hauteurs(main)) in suites(vals_52)) and not meme_couleur(main)


def est_couleur_32(main):
    """Teste si une main de 32 cartes contient une couleur qui n'est pas une quinte"""
    return not (set(hauteurs(main)) in suites(vals_32)) and meme_couleur(main)


def est_couleur_52(main):
    """Teste si une main de 52 cartes contient une couleur qui n'est pas une quinte"""
    return not (set(hauteurs(main)) in suites(vals_52)) and meme_couleur(main)


def est_flush_32(main):
    """Teste si une main de 32 cartes contient une couleur qui est une quinte"""
    return (set(hauteurs(main)) in suites(vals_32)) and meme_couleur(main)


def est_flush_52(main):
    """Teste si une main de 52 cartes contient une couleur qui est une quinte"""
    return (set(hauteurs(main)) in suites(vals_52)) and meme_couleur(main)


def compte_mains(test, vals):
    """Compte combien de fois le prédicat est vrai dans l'itérable"""
    return sum(map(test, mains(vals)))

os.system("pause")
