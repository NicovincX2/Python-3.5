# -*- coding: utf-8 -*-

import os


def pile_vide():
    return []


def est_vide(p):
    return p == []


def sommet(p):
    return p[-1]


def empiler(s, p):
    p.append(s)
    return p


def depiler(p):
    return p.pop()


def afficher(p):
    pp = p.copy()
    pp.reverse()
    print(pp)

os.system("pause")
