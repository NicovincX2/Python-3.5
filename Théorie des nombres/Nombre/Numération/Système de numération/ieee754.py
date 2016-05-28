# -*- coding: utf-8 -*-

import os
from math import log2, floor
from bigfloat import *
# nécessite l'installation de la bibliothèque Debian libmpfr-dev
# et de la bibliothèque Python bigfloat


def petits2bits(x, nmax=50):
    """Renvoie nmax bits de l'écriture en base 2 du nombre x"""
    with precision(nmax + 10):  # permet de travailler en précision arbitraire
        bx = BigFloat(str(x))
        b2 = BigFloat('2')
        assert bx < 1, "Le nombre doit être de valeur absolue < 1"
        bin = ""
        k = 0
        while k < nmax:
            a = int(b2 * bx)
            bin += str(a)
            ba = BigFloat(str(a))
            bx = BigFloat(str(b2 * bx - ba))
            k += 1
        return '0:' + bin


def str_2_int(s):
    """Renvoie l'entier correspondant à la chaîne de bits s"""
    n = len(s) - 1
    ent = 0
    for bit in s:
        ent = ent * 2 + int(bit)
    return ent


def int_2_str(n, format):
    """Renvoie la chaîne de format bits correspondant à l'entier n"""
    s = ""
    k = n
    while k > 0:
        s += str(k % 2)
        k //= 2
    return '0' * (format - len(s)) + s[-1::-1]

# Comblez les True


def ieee(x, garde, l_expo=8, l_mant=23):
    """Simulation de la représentation d'un nombre selon la norme Ieee 754"""
    if x == 0:
        print('zéro')
        return '0 ' + '0' * l_expo + ' ' + '0' * l_mant
    extension = garde + l_mant + 1  # pour gérer les arrondis
    dec = 2**(l_expo - 1) - 1  # décalage
    ax = x if x >= 0 else -x  # valeur absolue
    signe = int(ax != x)  # bit de signe
    expo = int(floor(log2(ax)))
    # mantisse sur extension bits sous la forme 1.partie_frac
    mant = petits2bits(ax * 2.0**(-expo - 1), extension)[2:]
    if True:  # si la puissance dépasse le max, c'est l'infini
        print('infini')
        return True
    if True:  # si la puissance est inférieure à la puissance du plus petit -> 0
        print('zéro')
        return True
    if True:  # pour un normal, on retire le premier 1
        print('normal')
        print('ulp = 2**' + str(True))
        mantisse = True
    else:  # si le nombre est dénormalisé on prend ses extension premiers bits
        print('sous-normal')
        expo = True
        print('ulp = 2**' + str(True))
        mantisse = True
    distance = True  # on calcule de combien on dépasse le flottant inférieur
    if True:
        # on arrondit au supérieur
        mant_arr = int_2_str(str_2_int(mantisse[:l_mant]) + 1, l_mant)
        print('arrondi supérieur')
    else:
        if True:
            print('arrondi inférieur')
        else:
            print("pas d'arrondi")
        mant_arr = True  # sinon à l'inférieur ou pas d'arrondi
    print('les bits oubliés sont ' + str(True))
    return True


def toy7(x, garde):
    return ieee(x, garde, l_expo=3, l_mant=3)

x = 0.75
garde = 1
print(toy7(x, garde))

os.system("pause")
