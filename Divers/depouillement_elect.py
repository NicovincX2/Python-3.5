# -*- coding: utf-8 -*-

import os

def gagnant_tour1(a):
    n=len(a)
    majorite=1+n//2
    for i in range(n//2):
        score=1
        for j in range(i+1,n):
            if a[j]==a[i]:
                score+=1
        if score>=majorite:
            return a[i]
    return -1
    
def gagnant_tour1_bis(a):
    n=len(a)
    m=n//2
    for i in range(m):
        if a[i+m]==a[i]:
            return a[i]
        i+=1
    return -1

def gagnants_tour2v1(a):
    n=len(a)
    score=[0]*n 
    score_max=0
    for i in range(n):
    # on commence par déterminer l'indice du premier qui a voté pour a[i] 
        i_min=0
        while a[i_min]!=a[i]:
            i_min+=1
        # on ajoute 1 vote dans la bonne pile de bulletins
        score[i_min]+=1;
        # on en profite pour tenir à jour le meilleur score 
        if score[i_min]>score_max:
            score_max=score[i_min]
    gagnants=[]
    for i in range(n):
        if score[i]==score_max:
            gagnants.append(a[i])
    return gagnants

def gagnants_tour2(a):
    n=len(a)
    score_max=0
    for i in range(n):
        score=1
        for j in range(i+1,n):
            if a[j]==a[i]:
                score+=1
        if score>score_max:
            score_max=score
    gagnants=[]
    for i in range(n):
        score=1
        for j in range(i+1,n):
            if a[j]==a[i]:
                score+=1
        if score==score_max:
            gagnants.append(a[i])
    return gagnants
    
def gagnants_tour2_bis(a):
    n=len(a)
    score_max=0
    d=0
    while d<n:
        f=d
        while f<n and a[f]==a[d]:
            f+=1
        if f-d>score_max:
            score_max=f-d
        d=f;
    gagnants=[]
    d=0
    while d<n:
        f=d
        while f<n and a[f]==a[d]:
            f+=1
        if f-d==score_max:
            gagnants.append(a[d])
        d=f
    return gagnants

def gagnant_tour1_ter(a):
    n=len(a)
    i=0
    candidat=a[0]
    nb=1
    j=1
    while j<n:
        if a[j]==candidat:
            nb+=1
        j+=1; #à ce stade, nb occurrences de candidat dans a[i:j] 
        if j<n and 2*nb<=j-i:
            i=j
            candidat=a[i]
            nb=1
            j=i+1 
    # On regarde si candidat est majoritaire ou pas 
    score=0
    for j in range(n):
        if a[j]==candidat:
            score+=1
    if 2*score>n:
        return candidat 
    else:
        return -1

#print(gagnants_tour2([0,2,2,3,2,3,3,5,0]))
        
#print(gagnants_tour2_bis([1,1,1,1,2,2,2,2,3]))

print(gagnant_tour1_ter([0,2,2,3,2,0,2,0,2]))

os.system("pause")