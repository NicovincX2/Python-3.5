#-*- coding: utf-8 -*-

# http://codes-sources.commentcamarche.net/source/51135-illustration-de-sinus-et-de-cosinus

"""
Un programme simple qui permet d'illustrer dynamiquement les fonctions sinus et cosinus. Ecrit pour Python 2.6, l'interface graphique fait appel à Tkinter. Pas de difficulté majeure si ce n'est la structuration du code en classe. Une particularité : c'est l'utilisation d'une variable de classe self.u, qui contient une valeur entière en pixels, sur laquelle se basent toutes les dimensions proportionnelles de l'application. En d'autres termes, tapez 12 dans cette valeur pour avoir une petite taille de la fenêtre (et les canvas qu'elle contient), tapez 24, et l'interface doublera de taille...
"""

# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
# Illustration du SINUS et du COSINUS
# -----------------------------------------------------------------------------
# Auteur : Calogero GIGANTE
# Version python : 2.6.4. avec Tkinter
# Objectif : illustrer dynamiquement le sin et le cos d'un angle en degrés.
# Date : 17 janvier 2010
# Site web : www.gigante.be
# Site python : www.gigante.be/python
# License : GPL
# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------

from PIL import Image, ImageTk
from tkinter import *
from tkinter import messagebox
from math import *
import os

class Application:
    def __init__(self):
        self.root=Tk()
        self.root.title('Sinus et cosinus - par C. Gigante')

        self.u = 24 # unite en px servant à dimensionner TOUS les composants graphiques
        self.trait = 2 # épaisseur en px des barres cos et sin

        # création des 4 canvas :
        self.c1 = Canvas(self.root, bg="white", width=12*self.u, height=12*self.u)
        self.c1.grid(row=0, column=0, padx=0, pady=0)
        self.c2 = Canvas(self.root, bg="white", width=17*self.u, height=12*self.u)
        self.c2.grid(row=0, column=1, padx=0, pady=0)
        self.c3 = Canvas(self.root, bg="white", width=12*self.u, height=17*self.u)
        self.c3.grid(row=1, column=0, padx=0, pady=0)
        self.c4 = Canvas(self.root,             width=17*self.u, height=17*self.u)
        self.c4.grid(row=1, column=1, padx=0, pady=0)

        self.nbre_de_pixels_sur_axe_x = self.u * 12
        # sur ce nombre de pixels, s'étendent 360 degrés.
        self.nbre_pixels_pour_1_deg = float(self.nbre_de_pixels_sur_axe_x)/360

        coordspoursin = []
        for t in range(0,self.nbre_de_pixels_sur_axe_x,1):
            x = t
            y = sin ( radians( x / self.nbre_pixels_pour_1_deg ))
            xx = 2 * self.u + x
            yy = 6 * self.u - (4 * self.u) * y
            coordspoursin.append((xx, yy))

        coordspourcos = []
        # attention, ici, on a tenu compte de l'orientation vers le bas du tracé
        # de la fonction cosinus
        for t in range(0,self.nbre_de_pixels_sur_axe_x,1):
            y = t
            x = cos ( radians( y / self.nbre_pixels_pour_1_deg ))
            yy = 2 * self.u + y
            xx = 6 * self.u + (4 * self.u) * x
            coordspourcos.append((xx, yy))

        # dessins des éléments fixes du 1er canvas :
        self.c1.create_line(  6 * self.u, 11 * self.u,  6 * self.u,  1 * self.u, arrow=LAST, tag="c1_axex")
        self.c1.create_line(  1 * self.u,  6 * self.u, 11 * self.u,  6 * self.u, arrow=LAST, tag="c1_axey")
        self.c1.create_oval(  2 * self.u,  2 * self.u, 10 * self.u, 10 * self.u)
        self.c1.create_text(  7 * self.u,  1 * self.u, text="1")
        self.c1.create_text( 11 * self.u,  5 * self.u, text="1")
        self.c1.create_text(  1 * self.u,  5 * self.u, text="-1")
        self.c1.create_text(  5 * self.u, 11 * self.u, text="-1")
        self.c1_x0 = 6 * self.u
        self.c1_y0 = 6 * self.u
        # dessins des éléments mobiles du 1er canvas :
        self.arc1 = self.c1.create_arc(  5 * self.u,  5 * self.u, 7 * self.u, 7 * self.u, start = 0, extent = 0, fill="", style=ARC, outline="#EFEFEF", width = 1, tag="arc1")
        self.barrecosc1 = self.c1.create_line(  self.c1_x0,  self.c1_y0 - (self.trait/2), 10 * self.u,  6 * self.u - (self.trait/2), fill="green", width=self.trait, tag="barrecosc1")
        #              le (- self.trait/2) de self.barrecosc1 sert à décaler légèrement la vue de la barre cosinus de l'axe horizontal
        self.barresinc1 = self.c1.create_line(  10 * self.u,  6 * self.u, 10 * self.u,  6 * self.u, fill="red", width=self.trait, tag="barresinc1")
        self.rayon =  self.c1.create_line(  self.c1_x0,  self.c1_y0, 10 * self.u,  6 * self.u, tag="rayon")
        self.boule1 = self.c1.create_oval(  9.8 * self.u,  5.8 * self.u, 10.2 * self.u, 6.2 * self.u, fill="orange", width=0, tag="boule1")

        # dessins des éléments fixes du 2ème canvas :
        self.c2.create_line( 1 * self.u,  6 * self.u, 16 * self.u,  6 * self.u, arrow=LAST, tag="c2_axex")
        self.c2.create_line( 2 * self.u, 11 * self.u,  2 * self.u,  1 * self.u, arrow=LAST, tag="c2_axey")
        self.c2.create_line(  5 * self.u,  5.5 * self.u,  5 * self.u,  6.5 * self.u) # trait x
        self.c2.create_line(  8 * self.u,  5.5 * self.u,  8 * self.u,  6.5 * self.u) # trait x
        self.c2.create_line( 11 * self.u,  5.5 * self.u, 11 * self.u,  6.5 * self.u) # trait x
        self.c2.create_line( 14 * self.u,  5.5 * self.u, 14 * self.u,  6.5 * self.u) # trait x
        self.c2.create_line( 1.5 * self.u,  2 * self.u, 2.5 * self.u,  2 * self.u) # trait y
        self.c2.create_line( 1.5 * self.u, 10 * self.u, 2.5 * self.u, 10 * self.u) # trait y
        self.c2.create_text(  1 * self.u,  2 * self.u, text="1")
        self.c2.create_text(  1 * self.u, 10 * self.u, text="-1")
        self.c2.create_text(  3 * self.u, 1 * self.u, text="Sin(x)")
        self.c2.create_text( 15 * self.u, 5 * self.u, text="x (degré)")
        self.c2.create_line( coordspoursin, fill="blue", smooth=1 )
        self.c2_x0 = 2 * self.u
        self.c2_y0 = 6 * self.u
        # dessins des éléments mobiles du 2ème canvas :
        self.barresinc2 = self.c2.create_line(  2 * self.u,  6 * self.u, 2 * self.u,  6 * self.u, fill="red", width=self.trait, tag="barresinc2")
        self.boule2 = self.c2.create_oval(  1.8 * self.u,  5.8 * self.u, 2.2 * self.u, 6.2 * self.u, fill="orange", width=0, tag="boule2")

        # dessins des éléments fixes du 3ème canvas :
        self.c3.create_line( 6 * self.u,  1 * self.u,  6 * self.u, 16 * self.u, arrow=LAST, tag="c3_axex")
        self.c3.create_line( 1 * self.u,  2 * self.u, 11 * self.u,  2 * self.u, arrow=LAST, tag="c3_axey")
        self.c3.create_line(  2 * self.u,  1.5 * self.u,  2 * self.u,  2.5 * self.u) # trait y
        self.c3.create_line( 10 * self.u,  1.5 * self.u, 10 * self.u,  2.5 * self.u) # trait y
        self.c3.create_line( 5.5 * self.u,  5 * self.u, 6.5 * self.u,  5 * self.u) # trait x
        self.c3.create_line( 5.5 * self.u,  8 * self.u, 6.5 * self.u,  8 * self.u) # trait x
        self.c3.create_line( 5.5 * self.u, 11 * self.u, 6.5 * self.u, 11 * self.u) # trait x
        self.c3.create_line( 5.5 * self.u, 14 * self.u, 6.5 * self.u, 14 * self.u) # trait x
        self.c3.create_text(  2 * self.u,  1 * self.u, text="-1")
        self.c3.create_text( 10 * self.u,  1 * self.u, text="1")
        self.c3.create_text(  7 * self.u,  1 * self.u, text="Cos(x)")
        self.c3.create_text(  8 * self.u, 16 * self.u, text="x (degré)")
        self.c3.create_line( coordspourcos, fill="blue", smooth=1 )
        self.c3_x0 = 6 * self.u
        self.c3_y0 = 2 * self.u
        # dessins des éléments mobiles du 3ème canvas :
        self.barrecosc3 = self.c3.create_line(  self.c3_x0,  self.c3_y0, self.c3_x0 + 4 * self.u,  self.c3_y0, fill="green", width=self.trait, tag="barrecosc3")
        self.boule3 = self.c3.create_oval( 9.8 * self.u,  1.8 * self.u, 10.2 * self.u, 2.2 * self.u, fill="orange", width=0, tag="boule3")

        # éléments du 4ème canvas :
        imgsin = ImageTk.PhotoImage(file = "D:\Python Programmes\Programmes\Illustration de sinus et cosinus\img_sinus.gif")
        imgcos = ImageTk.PhotoImage(file = "D:\Python Programmes\Programmes\Illustration de sinus et cosinus\img_cosinus.gif")
        img1 = Label(self.c4, image=imgsin)
        img1.pack(side=TOP)
        self.controle = Scale(self.c4, from_ = 0, to = 360, label="Degrés", resolution = 1, tickinterval=45, orient=HORIZONTAL, length = 15*self.u, command = self.redessinertout)
        self.controle.pack(side=TOP)
        img2 = Label(self.c4, image=imgcos)
        img2.pack(side=TOP)
        bouton_apropos = Button(self.c4, text="A propos de ce programme...", command=self.afficherapropos)
        bouton_apropos.pack(side=RIGHT)

        self.root.mainloop()

    def redessinertout(self, event=None):
        angle = int(self.controle.get())
        nouv_sin = sin(radians(angle))
        nouv_cos = cos(radians(angle))

        # update de l'arc symbolisant l'angle dans le canvas 1
        arc_angle = angle
        if arc_angle == 360:
            arc_angle = 359 # ceci est fait pour éviter la disparition de l'arc quand l'angle atteint 360 deg.
        self.c1.itemconfigure("arc1",extent=arc_angle)

        # update de la boule 1 (et du rayon) :
        x = self.c1_x0 + nouv_cos * 4 * self.u
        y = self.c1_y0 - nouv_sin * 4 * self.u
        self.c1.coords("rayon", self.c1_x0, self.c1_y0, x, y) # update du rayon
        self.c1.coords("boule1", x - 0.2 * self.u, y - 0.2 * self.u, x + 0.2 * self.u, y + 0.2 * self.u)

        # update de la barre du sin dans le canvas 1
        dx = self.c1_x0 + nouv_cos * 4 * self.u
        dy = self.c1_y0 - nouv_sin * 4 * self.u
        self.c1.coords("barresinc1",  dx,  6 * self.u, dx,  dy)

        # update de la barre du cos dans le canvas 1
        self.c1.coords("barrecosc1", self.c1_x0 ,  self.c1_y0 - (self.trait/2) , self.c1_x0 + nouv_cos * 4 * self.u, self.c1_y0 - (self.trait/2) )

        # update de la barre du sin dans le canvas 2
        dx2 = self.c2_x0 + angle * self.nbre_pixels_pour_1_deg
        dy2 = self.c2_y0 - nouv_sin * 4 * self.u
        self.c2.coords("barresinc2",  dx2,  6 * self.u, dx2,  dy2)
        # update de la boule 2 dans le canvas 2
        self.c2.coords("boule2",  dx2 - 0.2 * self.u,  dy2 - 0.2 * self.u, dx2 + 0.2 * self.u,  dy2 + 0.2 * self.u)

        # update de la barre du cos dans le canvas 3
        dx3 = self.c3_x0 + nouv_cos * 4 * self.u
        dy3 = self.c3_y0 + angle * self.nbre_pixels_pour_1_deg
        self.c3.coords("barrecosc3", self.c3_x0, dy3, dx3,  dy3)
        # update de la boule 3 dans le canvas 3
        self.c3.coords("boule3",  dx3 - 0.2 * self.u,  dy3 - 0.2 * self.u, dx3 + 0.2 * self.u,  dy3 + 0.2 * self.u)

    def afficherapropos(self):
        tkMessageBox.showinfo(
            "A propos de...",
            "Sinus et Cosinus\n\n"+
            "Un petit programme écrit en Python 2.6 qui\n"+
            "utilise Tkinter et qui permet simplement\n"+
            "de visualiser dynamiquement le sinus\n"+
            "et le cosinus d'un angle en degrés.\n\n"+
            "Auteur : Calogero GIGANTE - www.gigante.be - 2010")

# départ du programme principal :

f = Application()
os.system("pause")
