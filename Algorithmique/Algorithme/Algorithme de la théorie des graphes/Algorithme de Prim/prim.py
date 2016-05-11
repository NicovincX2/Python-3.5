# -*- coding: utf-8 -*-

import os

def p1(cx):
    return cx[0]

def p2(cx):
    return cx[1]

def cout(cx):
    return cx[2]

def inserer(cx,cxs):
    c=len(cxs)
    tri=[]
    k=0
    while k<c and cout(cx)<cout(cxs[k]):
        tri.append(cxs[k])
        k+=1
    tri.append(cx)
    for j in range(k,c):
        tri.append(cxs[k])
    return tri

def insererR(cx,cxs):
    if cxs==[] or cout(cx)<=cout(cxs[-1]):
        cxs.append(cx)
    else:
        fin=cxs[-1]
        cxs=insererR(cx,cxs[:-1])
        cxs.append(fin) 
    return cxs
    
def xor(b1,b2):
    return (b1 and not b2) or (b2 and not b1)

def cocycle1(pts,cxs):
    cc=[]
    for cx in cxs:
        if xor(p1(cx) in pts,p2(cx) in pts):
            cc.append(cx)
    return cc

def cocycle(pts,cxs):
    cc=[]
    for cx in cxs:
        if (p1(cx) in pts)^(p2(cx) in pts):
            cc=inserer(cx,cc)
    return cc

def construire(pts,cxs):
    pts_i=[pts[0]]
    cxs_i=[]
    for i in range(len(pts)-1):
        cx=cocycle(pts_i,cxs)[-1]
        if p1(cx) in pts_i:
            pts_i.append(p2(cx))
        else:
            pts_i.append(p1(cx))
        cxs_i.append(cx)
    return [pts_i,cxs_i]
        

pts=[1,2,3,4,5]
cxs=[(1,2,1),(1,3,1),(2,3,2),(2,4,1),(3,4,1),(4,5,2)]

print(construire(pts,cxs))

os.system("pause")