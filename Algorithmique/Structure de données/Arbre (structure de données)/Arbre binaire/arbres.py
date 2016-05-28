# -*- coding: utf-8 -*-

import os


def est_vide(a):
    return a == []


def arbre_vide():
    return []


def cons(e, g, d):
    return [e, g, d]


def contenu(a):
    return a[0]


def f_g(a):
    return a[1]


def f_d(a):
    return a[2]


def hauteur(a):
    if est_vide(a):
        return -1
    else:
        return 1 + max(hauteur(f_d(a)), hauteur(f_g(a)))


def parcours_infixe(a):
    if est_vide(a):
        return ''
    elif est_vide(f_g(a)) and est_vide(f_d(a)):
        return str(contenu(a))
    else:
        return '(' + parcours_infixe(f_g(a)) + contenu(a) + parcours_infixe(f_d(a)) + ')'


def parcours_postfixe(a):
    if est_vide(a):
        return ''
    elif est_vide(f_g(a)) and est_vide(f_d(a)):
        return str(contenu(a))
    else:
        return parcours_postfixe(f_g(a)) + ' ' + parcours_postfixe(f_d(a)) + ' ' + contenu(a)

a = [1, [2, [], [3, [4, [], []], []]], []]
print(hauteur(a))

a = ['-', ['+', [3, [], []], ['x', [5, [], []], ['+', [7, [], []], [2, [], []]]]],
     ['+', [4, [], []], ['x', [8, [], []], [9, [], []]]]]
print(parcours_infixe(a))
print(parcours_postfixe(a))

os.system("pause")
