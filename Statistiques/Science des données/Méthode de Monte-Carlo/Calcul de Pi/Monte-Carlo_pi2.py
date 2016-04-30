#-*- coding: utf-8 -*-

# http://codes-sources.commentcamarche.net/source/41405-determination-approximative-de-pi-a-l-aide-de-la-methode-de-monte-carlo

##################################
#                                #
#   Programme : Monte Carlo.py   #
#   Crée par : Shakan972         #
#   Date de création : 7/02/07   #
#                                #
##################################

###################################################################################
#
#   Ce programme permet à l'aide de la méthode de Monte Carlo
#   de déterminer de manière approximative pi
#   Pour cela on trace un carré dans lequel figure un arc de cercle
#   Puis l'on génère une série de points de coordonnées (x,y) dans ce carré
#   Et à chaque fois le programme détermine si les points sont dans ou hors
#   de l'arc de cercle à l'aide du calcul se réferrant à cette méthode puis enfin
#   on fait le rapport du nombre de points dans le cercle (multiplié par 4)
#   avec le nombre de points total ce qui au final permet la détermination
#   approximative de pi.
#
###################################################################################

#Importation des bibliothèques

from tkinter import *
from random import *
import os

#Fonction permettant d'effectuer une pause

def stop():
    global flag
    flag=0

#Fonction permettant de démarrer le programme ou bien de le reprendre si il a été stoppé

def demarrer():
    global flag
    if flag==0:
        flag=1
        generateur_nbre_aleat()

#Cette fonction permet de différencier les points étant soit dans l'arc de cercle ou bien hors de l'arc de cercle
#La couleur du point tracé varie donc en fonction de la position du point dans le carré

def points_aleat(x,y):
    global pts_dans_cercle
    if (x-100)**2+(y-100)**2<90000:
        pts_dans_cercle=pts_dans_cercle+1
        can1.create_oval(x-2,y-2,x,y,fill='green')
    else:
        can1.create_oval(x-2,y-2,x,y,fill='red')

#Cette fonction permet le tirage de points de coordonnées aléatoires dans le cercle

def generateur_nbre_aleat():
    global x,y,pts_dans_cercle,pts_total,pi,flag
    x=randint(100,400)
    y=randint(100,400)
    points_aleat(x,y)
    pts_total+=1
    pi=float((pts_dans_cercle*4.)/(pts_total))
    result.configure(text = "Estimation de pi = "+str(pi))
    pts_cercle.configure(text= "Nombre de points dans le cercle = "+str(pts_dans_cercle))
    pts_tot.configure(text="Nombre de point total déjà placés = "+str(pts_total))
    if flag!=0:
        fen1.after(1,generateur_nbre_aleat)

#Programme principal

x=0
y=0
pts_dans_cercle=0
pts_total=0
pi=0
flag=0

fen1=Tk()
fen1.title("Détermination approximative de pi à l'aide de la méthode de Monte Carlo")
can1=Canvas(fen1,width=500,height=500)

can1.grid(row=0,column=0,columnspan=2)

#Création du carré et de l'arc de cercle figurant dans ce dernier

carre=can1.create_rectangle(100,100,400,400,width=1)

fra1=Frame(fen1)
fra1.grid(row=0,column=3,columnspan=2)

Button(fra1,text="Démarrer",command=demarrer).grid(row=1,column=0,pady=5)
Button(fra1,text="Arrêter",command=stop).grid(row=2,column=0,pady=5)
Button(fra1,text="Quitter",command=fen1.destroy).grid(row=3,column=0,pady=5)
result=Label(fen1)
result.grid(row=1,column=0,sticky=E)
pts_cercle=Label(fen1)
pts_cercle.grid(row=2,column=0,sticky=E)
pts_tot=Label(fen1)
pts_tot.grid(row=3,column=0,sticky=E)

fen1.mainloop()
os.system("pause")
