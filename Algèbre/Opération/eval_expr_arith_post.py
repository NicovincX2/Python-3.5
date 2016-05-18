# -*- coding: utf-8 -*-

import os

def pile_vide():
    return []

def est_vide(p):
    return p==[]

def sommet(p):
    return p[-1]

def empiler(s,p):
    p.append(s)
    return p

def depiler(p):
    return p.pop()


def eval_avec_controle(eap):
    symbols=eap.split()
    p = pile_vide()
    for s in symbols:
        if s == '+':
            if est_vide(p):
                return 'Pas assez de nombres'
            a=depiler(p)
            if est_vide(p):
                return 'Pas assez de nombres'
            b=depiler(p)
            empiler(int(a)+int(b),p)
        elif s == '*':
            if est_vide(p):
                return 'Pas assez de nombres'
            a=depiler(p)
            if est_vide(p):
                return 'Pas assez de nombres'
            b=depiler(p)
            empiler(int(a)*int(b),p)
        else:
            try:
                empiler(int(s),p)
            except ValueError:
                return 'Erreur de saisie'
    a=depiler(p)
    if est_vide(p):
        return a
    else:
        return 'Trop de nombres'
          
def controler(eap):
    symbols=eap.split()
    poids = 0
    for s in symbols:
        if s=='+' or s=='*':
            if poids<2:
                return 'Pas assez de nombres'
            else:
                poids-=1
        else:
            try:
                x=int(s)
            except ValueError:
                return 'Erreur de saisie'
            else:
                poids+=1
    if poids>1:
        return 'Trop de nombres'
    elif poids<1:
        return 'Pas assez de nombres'
    else:
        return 'Syntaxe correcte'

def evaluer(eap):
    symbols=eap.split()
    p = pile_vide()
    for s in symbols:
        if s == '+':
            a=depiler(p)
            b=depiler(p)
            empiler(int(a)+int(b),p)
        elif s == '*':
            a=depiler(p)
            b=depiler(p)
            empiler(int(a)*int(b),p)
        else:
            empiler(int(s),p)
    return depiler(p)

#print(eval_avec_controle('3 4 + 8 *'))
print(controler('3 4 + 8 *'))
print(evaluer('3 4 + 8 *'))

os.system("pause")