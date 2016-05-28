# -*- coding:utf-8 -*-

from tkinter import *
from time import *
import sys
import os


class Application:

    def __init__(self):
        self.Terminated = False
        self.root = Tk()
        self.root.title('Barre qui avance avec un thread...')
        self.root.geometry('600x160')
        self.root.protocol("WM_DELETE_WINDOW", self.finirapplication)

        self.valeur = 1

        self.c1 = Canvas(self.root, bg="white")
        self.c1.pack(side=LEFT, expand=YES, fill=BOTH)

        self.barre = self.c1.create_rectangle(10, 50, 11, 100, fill="yellow")

        # Boutons du 4éme canvas :
        bouton_animate = Button(
            self.root, text="Démarrer", command=self.ianimate)
        bouton_stop = Button(self.root, text="Arrêt", command=self.stop)
        bouton_reprendre = Button(
            self.root, text="Reprendre", command=self.reprendre)
        bouton_reset = Button(
            self.root, text="Remise à zéro", command=self.reset)
        bouton_animate.pack(side=TOP, expand=YES)
        bouton_stop.pack(side=TOP, expand=YES)
        bouton_reprendre.pack(side=TOP, expand=YES)
        bouton_reset.pack(side=TOP, expand=YES)

        self.root.mainloop()

    def stop(self):
        # Thread Stop :
        self.Terminated = True

    def redessiner(self, x):
        # Mise a jour de la barre :
        self.valeur = x

        self.c1.coords(self.barre, 10, 50, 10 + x, 100)

    def redessinertout(self, event=None):
        # Mise a jour de la barre avec la valeur donnée par self.valeur :
        self.redessiner(self.valeur)

    def reset(self, event=None):
        if self.Terminated == False:
            self.Terminated = True
            self.redessiner(1)

    def reprendre(self):
        # Reprise de l'animation :
        self.animate()

    def ianimate(self):
        # Lancement animation 0-500 :
        self.valeur = 0
        self.animate()

    def animate(self):
        # Lancement de l'animation
        if self.Terminated == True:
            self.Terminated = False

        while not self.Terminated:
            for i in range(500):
                if self.Terminated == True:
                    return
                if i >= self.valeur:
                    self.valeur = i
                    sleep(0.01)
                    self.redessiner(i)
                    self.root.update()
                    # update du controle
                    self.valeur = 0

    def finirapplication(self):
        self.Terminated = True
        self.stop()
        sys.exit()

# Lancement programme principal :
if __name__ == "__main__":
    app = Application()

os.system("pause")
