#-*- coding: utf-8 -*-

"""
Ce petit script a pour but de générer des motifs de deux sortes : des motifs dits "simples" et des motifs dits de "Escher" (en référence à certaines oeuvres de Escher).

En mettant les motifs simples en mosaïque, l'espace libre entre eux sera de la même forme que chaque motif.

En mettant les motifs de Escher en mosaïque, on va obtenir des lignes de motifs où chaque motif est répété avec alternance des couleurs. De plus, les lignes pairs vont dans le sens inverse des lignes impaires. Le tableau "Regular Division of The Plane IV, 1957" de Escher est un bel exemple.

Le principe de génération de ces deux types de motifs est assez similaire en réalité.

N'hésitez pas à jouer avec les paramètres dans le main pour générer des images différentes. Le sens de ces paramètres est expliqué dans la documentation des méthodes de la classe Motif.

PS : il faut la bibliothèque PIL pour pouvoir générer l'image de sortie.
"""

# http://codes-sources.commentcamarche.net/source/54982-generation-aleatoire-de-motifs

import abc
import random
import os
from PIL import Image, ImageDraw
#Image, ImageDraw

__author__ = "Maxime BRIDE"
__version__ = "1.3"


class AbstractMotif(object):
    __metaclass__ = abc.ABCMeta

    def __init__(self, w, h):
        """
        Initialise le motif de base.

        Args:
           w (int): la largeur de la matrice.
           h (int): la hauteur de la matrice.
        """

        if w <= 1:
            w = 2
        elif w % 2 == 1:
            w += 1

        if h <= 1:
            h = 2
        elif h % 2 == 1:
            h += 1

        self._motif = []
        self._w = w
        self._h = h

    @abc.abstractmethod
    def generate(self):
        pass

    def draw(self, rx=1, ry=1, sf=1, c1=(255, 255, 255), c2=(0, 0, 0)):
        """
        Dessine le motif sur une image.

        Args:
           rx (int): le nombre de répétitions horizontales du motif.
           ry (int): le nombre de répétitions verticales du motif.
           sf (int): le facteur de redimensionnement du motif.
           c1 (tuple): la couleur de fond du motif.
           c2 (tuple): la couleur des pixels du motif.

        Returns:
                Image. L'image issue du dessin.
        """

        if rx <= 0:
            rx = 1
        if ry <= 0:
            ry = 1

        if sf <= 0:
            sf = 1

        w = rx * self._w * sf
        h = ry * self._h * sf

        ranrx = range(rx)
        ranry = range(ry)

        # Création de l'image et de l'objet de dessin.
        img = Image.new('RGB', (w, h), c1)
        draw = ImageDraw.Draw(img)

        # Dessin des rectangles sur l'image.
        for (i, j) in self._motif:
            for k in ranrx:
                for l in ranry:
                    x = (i + self._w * k) * sf
                    y = (j + self._h * l) * sf
                    draw.rectangle((x, y, x + sf - 1, y + sf - 1), fill=c2)

        return img


class SimpleMotif(AbstractMotif):
    """
    Un motif tel que défini ici est caractérisié par :
     - une taille de N * N avec N pair et strictement positif.
     - autant de pixels "blancs" que de pixels "noirs".
     - le fait qu'un pixel à la position (x, y) a une couleur inverse de celle
       du pixel à la position ((x + N / 2) % N, (y + N / 2) % N).
    """

    def __init__(self, n=8):
        """
        Initialise le motif de base.

        Args:
           n (int): la taille de la matrice.
        """

        super(SimpleMotif, self).__init__(n, n)

    def generate(self):
        self._motif = []

        pixels = [(x, y) for x in range(self._w) for y in range(self._h)]
        w2 = self._w / 2
        h2 = self._h / 2

        while len(pixels) > 0:
            p1 = random.choice(pixels)
            pixels.remove(p1)

            p2 = ((p1[0] + w2) % self._w, (p1[1] + h2) % self._h)
            pixels.remove(p2)

            self._motif.append(p1)


class EscherMotif(AbstractMotif):
    """
    Un motif tel que défini ici est caractérisié par :
     - une taille de W * H avec W et H pairs et strictement positifs.
     - autant de pixels "blancs" que de pixels "noirs".
     - un décalage horizontal TX (Cf. "Moins formellement").
     - le fait que pour chaque chaque pixel P1 en (x1, x2) de couleur c1, il y
       a 3 pixels associés :
       - P2 en (x2 = (x1 + (W / 2)) % W, y2 = y1) de couleur c2 != c1.
       - P3 en (x3 = ((W / 2) - x1 - TX) % W, y3 = (y1 + (H / 2)) % H) de
         couleur c3 = c2.
       - P4 en (x4 = (x3 + (W / 2)) % W, y4 = y3) de couleur c4 = c1.
    Moins formellement, une fois mis en mosaïque, on va obtenir des lignes de
    motifs où chaque motif est répété avec alternance des couleurs. De plus,
    les lignes paires vont dans le sens inverse des lignes impaires et en sont
    décalées de TX pixels.
    Le tableau "Regular Division of The Plane IV, 1957" de Escher est un bel
    exemple.
    """

    def __init__(self, w=8, h=8, mw=0, mh=0, tx=0):
        """
        Initialise le motif de base.

        Args:
           w (int): la largeur de la matrice.
           h (int): la hauteur de la matrice.
           tx (int): le décalage des lignes impaires par rapport aux lignes
           paires.
        """

        super(EscherMotif, self).__init__(w, h)

        self._tx = tx

    def generate(self):
        self._motif = []

        pixels = [(x, y) for x in range(self._w) for y in range(self._h)]
        w2 = self._w / 2
        h2 = self._h / 2

        while len(pixels) > 0:
            p1 = random.choice(pixels)
            pixels.remove(p1)

            p2 = ((p1[0] + w2) % self._w, p1[1])
            pixels.remove(p2)

            p3 = ((w2 - p1[0] - self._tx) % self._w, (p1[1] + h2) % self._h)
            pixels.remove(p3)

            p4 = ((p3[0] + w2) % self._w, p3[1])
            pixels.remove(p4)

            self._motif.append(p1)
            self._motif.append(p4)


if __name__ == "__main__":
    SIMPLE = True
    W = 8
    H = 8
    TX = 0
    RX = 8
    RY = 8
    SF = 5
    C1 = (224, 225, 131)
    C2 = (113, 113, 0)
    OUTPUT = "motif.png"
    TYPE = "PNG"

    if SIMPLE:
        m = SimpleMotif(W)
    else:
        m = EscherMotif(W, H, TX)
    m.generate()
    img = m.draw(RX, RY, SF, C1, C2)
    img.save(OUTPUT, TYPE)

os.system("pause")
