#-*- coding: utf-8 -*-

# http://codes-sources.commentcamarche.net/source/39144-implementation-de-la-tortue-logo-application-aux-fractales

from tkinter import *
from math import radians, cos, sin, sqrt
from random import randrange, uniform
import os


class tortue:
    """Tortue(canvas,x=0,y=0,angle=0,crayon=1,couleur='black',epaisseur=1)"""

    def __init__(self, canvas, x=0, y=0, angle=0, crayon=1, couleur='black', epaisseur=1):
        self.canvas = canvas
        self.crayon = crayon
        self.x = x
        self.y = y
        self.angle = angle
        self.couleur = couleur
        self.epaisseur = epaisseur

    def __repr__(self):
        return "canvas : %s\ncrayon :%d\nx      : %d\ny      : %d\nangle  : %d" % (self.canvas, self.crayon, self.x, self.y, self.angle)

    def avance(self, l):
        """avance(l)\n\nl:distance dont on souhaite avancer"""
        X, Y = self.x + l * cos(radians(self.angle)
                                ), self.y - l * sin(radians(self.angle))
        if self.crayon:
            self.canvas.create_line(
                self.x, self.y, X, Y, fill=self.couleur, width=self.epaisseur)
        self.x, self.y = X, Y

    def tourne_gauche(self, theta):
        """tourne_gauche(theta)\n\nTourne à gauche d'un angle theta"""
        self.angle += theta

    def tourne_droite(self, theta):
        """tourne_droite(theta)\n\nTourne à droite d'un angle theta"""
        self.tourne_gauche(-theta)

    def pose_crayon(self):
        """pose_crayon()\n\nPose le crayon"""
        self.crayon = 1

    def leve_crayon(self):
        """leve_crayon()\n\nLève le crayon"""
        self.crayon = 0


def koch(T, l, n):
    # Fractacle de Koch
    if n <= 0:
        T.avance(l)
    else:
        koch(T, l / 3, n - 1)
        T.tourne_gauche(60)
        koch(T, l / 3, n - 1)
        T.tourne_droite(120)
        koch(T, l / 3, n - 1)
        T.tourne_gauche(60)
        koch(T, l / 3, n - 1)


def flocon(T, l, n):
    # Flocon de Koch
    koch(T, l, n)
    T.tourne_droite(120)
    koch(T, l, n)
    T.tourne_droite(120)
    koch(T, l, n)


def arbre(T, l, n):
    # arbre fractal
    if n <= 0:
        T.avance(l)
        T.avance(-l)
    else:
        T.avance(0.7 * l)
        T.tourne_gauche(30)
        arbre(T, 2 * l / 3, n - 1)
        T.tourne_droite(60)
        arbre(T, 2 * l / 3, n - 1)
        T.tourne_gauche(30)
        T.avance(-0.7 * l)


def arbre_random(T, l, n):
    # arbre fractal randomisé
    if n <= 0:
        T.avance(l)
        T.avance(-l)
    else:
        longueur = uniform(0.5 * l, 0.8 * l)
        tampon = T.epaisseur
        T.epaisseur = int(longueur / 6)
        T.avance(longueur)
        angle_g = randrange(10, 45)
        T.tourne_gauche(angle_g)
        arbre_random(T, 4 * l / 5, n - 1)
        angle_d = randrange(10, 45)
        T.tourne_droite(angle_g + angle_d)
        arbre_random(T, 4 * l / 5, n - 1)
        T.tourne_gauche(angle_d)
        T.avance(-longueur)
        T.epaisseur = tampon


def dragon(T, l, n):
    # fractale du dragon
    # (récursivité croisée)
    k = sqrt(2) / 2

    def dragon_endroit(T1, l1, n1):
        if n1 <= 0:
            T1.avance(l1)
        else:
            T1.tourne_gauche(45)
            dragon_endroit(T1, l1 * k, n1 - 1)
            T1.tourne_droite(90)
            dragon_envers(T1, l1 * k, n1 - 1)
            T1.tourne_gauche(45)

    def dragon_envers(T2, l2, n2):
        if n2 <= 0:
            T2.avance(l2)
        else:
            T2.tourne_droite(45)
            dragon_endroit(T2, l2 * k, n2 - 1)
            T2.tourne_gauche(90)
            dragon_envers(T2, l2 * k, n2 - 1)
            T2.tourne_droite(45)
    dragon_endroit(T, l, n)


if __name__ == '__main__':
    root = Tk()
    can = Canvas(root, height=400, width=1000, bg='white')
    can.pack()
    T = tortue(can)
    T.y = 150
    flocon(T, 300, 5)
    T.x = 475
    T.y = 350
    T.angle = 90
    arbre_random(T, 100, 10)
    T.x = 750
    T.y = 250
    T.angle = 0
    dragon(T, 200, 15)
    root.mainloop()

os.system("pause")
