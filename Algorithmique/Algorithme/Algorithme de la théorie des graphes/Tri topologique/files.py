# -*- coding: utf-8 -*-

def pile_vide():
    return []

def est_pile_vide(p):
    return p==[]

def sommet(p):
    return p[-1]

def empiler(s,p):
    p.append(s)
    return p

def depiler(p):
    return p.pop()

def file_vide():
    return [[],[]]

def est_file_vide(f):
    return est_pile_vide(f[0]) and est_pile_vide(f[1])

def suivant(f):
    if est_pile_vide(f[0]):
        while not est_pile_vide(f[1]):
            empiler(depiler(f[1]),f[0])
    return depiler(f[0])

def ajouter(c,f):
    empiler(c,f[1])
    return f

def afficher(f):
    file=f[0].copy()
    file.reverse()
    file.extend(f[1])
    print(file)

