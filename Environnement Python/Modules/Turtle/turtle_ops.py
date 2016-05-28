#-*- coding: utf-8 -*-

# http://codes-sources.commentcamarche.net/source/48466-turtle-operations-de-base-et-fractales

# Importation de la librairie Turtle #####################################
from turtle import *
import os
#########################################################################

# Dessin d'un trait #####################################################


def Trait(x, y, n):                                                       #
    #(x,y) sont les coordonnées du point de départ.                     #
    # n est la taille du trait                                          #
    up()                                                                #
    goto(x, y)                                                           #
    down()                                                              #
    forward(n)                                                          #
#########################################################################

# Dessin d'un carré #####################################################


def Carre(x, y, n):                                                      #
    #(x,y) sont les coordonnées du coin supérieur gauche.               #
    # n est la taille d&#8217;un coté                                   #
    up()                                                                #
    goto(x, y)                                                           #
    down()                                                              #
    for i in range(4):                                                 #
        forward(n)                                                      #
        left(90)                                                        #
#########################################################################

# Dessin d'un triangle ##################################################


def Triangle(longueur, x, y, orientation):                                 #
    #Cette fonction dessine un triangle équilatéral.                    #
    #longueur est la longueur d'un coté.                                #
    #(x,y) sont les coordonnées du coin gauche.                         #
    #orientation=1 pour un triangle tourné vars le haut                 #
    #orientation=-1 pour un triangle tourné vars le base                #
    up()                                                                #
    goto(x, y)  # On positionne le curseur                                 #
    down()                                                              #
    for i in range(0, 3):  # On trace les trois cotés du triangle         #
        forward(longueur)                                               #
        left(orientation * 120)  # Un triangle équilatéral a 3 angles de 60°#
#########################################################################

# Dessin d'une étoile ###################################################


def Etoile(longueur, x, y):                                               #
    #Cette fonction dessine une étoile avec la fonction triangle        #
    #longueur est la longueur d'un coté.                                #
    #l'axe (x) est l'axe horizontale sur lequel repose l'étoile         #
    #l'axe(y) est l'axe vertical sur lequel repose l'étoile             #
    #couleur est la couleur du dessin.                                  #
    h = sqrt(3) * longueur / 2                                                #
    #h est la hauteur d'un triangle équilatéral,                        #
    #
    Triangle(longueur, x, y + h / 3, 1)
    Triangle(longueur, x, y + h, -1)                                         #
    #Ainsi on obtient une étoile parfaitement symétrique                #
    up()                                                                #
    goto(x, y + longueur)                                                  #
    down()                                                              #
#########################################################################

# Dessin d'un polygone régulier #########################################


def Poly(x, y, n, c):                                                      #
    #(x,y) sont les coordonnées du coin supérieur gauche.               #
    # n est la taille d&#8217;un coté                                   #
    # c est le nombre de cotés                                          #
    up()                                                                #
    goto(x, y)                                                           #
    down()                                                              #
    angle = 360 / c                                                         #
    for i in range(c):                                                 #
        forward(n)                                                      #
        right(angle)                                                    #
#########################################################################

# Dessin d'un cercle ####################################################


def Cercle(x, y, r):                                                     #
    # (x,y) sont les coordonnées du haut du cercle                      #
    # r est son rayon                                                   #
    Poly(x, y, 1, 360)                                                     #
#########################################################################

# Dessin de fractales ###################################################


def Dessin(Chaine, n, x, X0, Y0):                                       #
    for i in range(0, len(Chaine)):                                      #
        if Chaine[i] == 'A':                                              #
            forward(n)                                                  #
        elif Chaine[i] == '+':                                            #
            right(x)                                                    #
        elif Chaine[i] == '-':                                            #
            left(x)                                                     #


def Substitution(Chaine, regle):                                        #
    #Cette fonction va remplacer 'A' dans la chaine par la regle.       #
    C2 = str()                                                            #
    #C2 sera la nouvelle chaine, notre sortie                           #
    for i in range(0, len(Chaine)):                                      #
        if Chaine[i] == 'A':                                              #
            C2 = C2 + regle                                                 #
        elif Chaine[i] == "-":                                            #
            C2 = C2 + "-"                                                 #
        elif Chaine[i] == "+":                                            #
            C2 = C2 + "+"                                                 #
    return(C2)                                                          #


def Fractale(Chaine, regle, n):                                         #
    #Cette fonction sert a tracer des fractales a partir d'une chaine   #
    C = Chaine                                                            #
    for k in range(0, n):                                                #
        C = Substitution(C, regle)                                         #
    # modifier le second paramètre
    # #
    Dessin(C, 2, 60, -200, 0)
#########################################################################

goto(-300, 0)
Fractale('A', "A-A++A-A", 5)

os.system("pause")
