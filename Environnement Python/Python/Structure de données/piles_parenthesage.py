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

def afficher(p):
    pp=p.copy()
    pp.reverse()
    print(pp)

def tester(ep):    
    p = pile_vide()
    for j in range(len(ep)):
        if ep[j]=='(':
            empiler(j,p)
        elif ep[j]==')':
            if est_vide(p):
                return ") à l'indice "+str(j)+" n'est pas ouverte !"
            else:
                i=depiler(p)
                print("Couple ",i," ",j," correct")
    if est_vide(p):
        return 'Parenthésage OK'
    else:
        return "( à l'indice "+str(sommet(p))+" n'est pas refermée !"
                      
print(tester('(((())()))'))

os.system("pause")