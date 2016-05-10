# -*- coding: utf-8 -*-

import os

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
    return []

def est_file_vide(f):
    return f==[]

def suivant(f):
    s=f[0]
    for k in range(1,len(f)):
        f[k-1]=f[k]
    f.pop()
    return s

def ajouter(c,f):
    f.append(c)
    return f

def afficher(f):
    print(f)

f=file_vide()
ajouter(1,f)
afficher(f)
ajouter(2,f)
afficher(f)
print(suivant(f))
afficher(f)
ajouter(3,f)
afficher(f)

os.system("pause")