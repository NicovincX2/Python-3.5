# -*- coding: utf-8 -*-

import os
import random

# pour melanger les graphes...

def shuffle(G) :
    random.shuffle(G[0])
    for c in G[1].items() : 
        random.shuffle(c[1])

# pour completer les graphes NON orientes...
def completer_graphe_no(G) : 
    for x in G[0] : 
        for y in G[0][x] :
            if not x in G[0][y] : G[0][y].append(x)
  

# pour completer les graphes NON orientes VALUES...
def completer_graphe_nov(G) : 
    for x in G[0] : 
        for (y,d) in G[1][x] :
            if not (x,d) in G[1][y] : G[1][y].append((x,d))

# pour calculer le poids d'un ensemble d'aretes (q,d,q'):
def Poids(A) :
    res = 0
    for (x,d,y) in A :
        res = res + d
    return res

os.system("pause")

