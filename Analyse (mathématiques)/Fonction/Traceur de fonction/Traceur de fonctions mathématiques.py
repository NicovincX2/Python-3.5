# -*- coding:utf-8 -*-

# http://codes-sources.commentcamarche.net/source/view/29942/967682#browser

# Ce script est un traceur de fonctions mathématique, développé avec
# python et la bibliothèque graphique Tkinter ###

#################################################### Les imports #########
from tkinter import *       # Importation de la bibliothèque graphique Tkinter
# Importation des fonctions mathématique sin(), cos(), sqrt(), ...
from math import *
# Importation du module affichant diverses messageBoxes
from tkinter import messagebox
import sys
import os                # Module utilisé pour les éxeptions
##########################################################################


########################################################### Les Classes ##
class Repere(Canvas):
    """Cette class permet de gérer l'affichage d'un repère orthonormal, et d'effectuer le traçage de courbes mathématiques"""

    def __init__(self, width=600, height=400, color="#FFFFFF"):
        # Construction du widget parent
        Canvas.__init__(self)
        # Width et height -> impaire car pixel du "milieu" est un pixel impaire
        # (ex: 401 -> pixel milieu = 201) :
        if (width % 2 == 0):
            width += 1
        if (height % 2 == 0):
            height += 1
        # Configuration du widget selon les options
        self.configure(width=width, height=height, bg=color)
        # Enregistrement des valeurs width et height
        self.width, self.height = width, height
        # Variable contenant les infos propres à chaque courbe (équation,
        # couleur, option , ...)
        self.courbe = []

    def trace_axe(self, xmax=10, xmin=-10, ymax=10, ymin=-10, grad=2):
        """ Méthode permettant de tracer les axes selon des valeurs maximales et minimales en x et y..
        L'option grad est une option d'affichage de graduations sur les axes :
            grad == -1 -> Rien
            grad == 0 -> simplement deux axes sans rien d'autre
            grad == 1 -> deux axes + flèches en début et fin de chaque axe
            grad == 2 -> petites graduations seulement sur les axes, selon valeurs minimum et maximum de ces axes
            grad == 3 -> graduations traversant tout le canvas, selon valeurs minimum et maximum des axes """

        # On efface les anciens axes (+ graduations) si anciens axes il y a
        self.delete("axe", "grad")

        # Gestion des erreurs d'attributs :
        if xmax <= 0:
            xmax = 10
            messagebox.showwarning(
                "Attention !!!", "Valeur de \"xmax\" rectifiée à 10 car inférieur ou égal à 0")
        if xmin >= 0:
            xmin = -10
            messagebox.showwarning(
                "Attention !!!", "Valeur de \"xmin\" rectifiée à -10 car supérieur ou égal à 0")
        if ymax <= 0:
            ymax = 10
            messagebox.showwarning(
                "Attention !!!", "Valeur de \"ymax\" rectifiée à 10 car inférieur ou égal à 0")
        if ymin >= 0:
            ymin = -10
            messagebox.showwarning(
                "Attention !!!", "Valeur de \"ymin\" rectifiée à -10 car supérieur ou égal à 0")
        if grad < -1 or grad > 3:
            grad = 2
            messagebox.showwarning(
                "Attention !!!", "Mode de graduation fixé à 2, car la valeur soumise est incorrect")

        # Calcul nbr pixel de la partie gauche des abscisses
        npix_x = int(float(self.width) / (-xmin + xmax) * (-xmin))
        # Calcul nbr pixel de la partie haute des ordonnées
        npix_y = int(float(self.height) / (-ymin + ymax) * ymax)
        # Enregistrement des valeurs min et max en x et en y
        self.val_xy = [[xmax, xmin], [ymax, ymin]]

        # Création des graduations selon l'option choisie :
        if grad == 0:
            arrow = NONE
        if grad == 1:
            arrow = BOTH
        if grad == 2:  # Graduation partielle
            arrow = NONE
            # Graduations sur l'axe x -> partie négative puis positive :
            for x in range(npix_x + 1, 0, int(npix_x / xmin)):
                self.create_line(x, npix_y - 2, x, npix_y + 5, tag="grad")
            for x in range(npix_x + 1, self.width + 1, int(npix_x / (-xmin))):
                self.create_line(x, npix_y - 2, x, npix_y + 5, tag="grad")
            # Graduations sur l'axe x -> partie positive puis négative :
            for y in range(npix_y + 1, 0, int(-npix_y / ymax)):
                self.create_line(npix_x - 2, y, npix_x + 5, y, tag="grad")
            for y in range(npix_y + 1, self.height + 1, int(npix_y / ymax)):
                self.create_line(npix_x - 2, y, npix_x + 5, y, tag="grad")
        if grad == 3:  # Graduation complète
            arrow = NONE
            # Graduations sur l'axe x -> partie négative puis positive :
            for x in range(npix_x + 1, 0, int(-npix_x / (-xmin))):
                self.create_line(x, 1, x, self.height,
                                 fill="#dbd8d8", tag="grad")
            for x in range(npix_x + 1, self.width + 1, int(npix_x / (-xmin))):
                self.create_line(x, 1, x, self.height,
                                 fill="#dbd8d8", tag="grad")
            # Graduations sur l'axe x -> partie positive puis négative :
            for y in range(npix_y + 1, 0, int(-npix_y / ymax)):
                self.create_line(1, y, self.width, y,
                                 fill="#dbd8d8", tag="grad")
            for y in range(npix_y + 1, self.height + 1, int(npix_y / ymax)):
                self.create_line(1, y, self.width, y,
                                 fill="#dbd8d8", tag="grad")

        if grad != -1:
            # Création de l'axe x (des abscisses)
            self.create_line(0, npix_y + 1, self.width,
                             npix_y + 1, arrow=arrow, tag="axe")
            # Création de l'axe y (des ordonnées)
            self.create_line(npix_x + 1, 0, npix_x + 1,
                             self.height, arrow=arrow, tag="axe")

    def trace_courbe(self, equa, color="#000000", mod="normal", step=10):
        """ Méthode permettant de tracer une courbe d'équation définie par l'attribut "equa".
        De plus, celle-ci accepte un attribut, mod, qui permet d'afficher la courbe de différentes manières :
        mod == "normal" -> affiche la courbe de façon linéaire
        mod == "point" -> affiche certains points seulement de la courbe
        mod == "both" -> affiche des deux manières précédentes
        step est utilisé uniquement quand mod == "point" ou "both". Cela affiche les points tout les step pixel """

        for i in range(len(self.courbe)):      # Cas s'il y a des doublons :
            if equa == self.courbe[i][0]:        # Si l'équation existe déjà :
                if messagebox.askquestion("Fonction déjà existante", "Cette fonction existe déjà.\nVoulez-vous écraser la précédente ?") == "no":
                    return None
                else:
                    # On efface la courbe (+ les points s'ils existent)
                    self.delete("courbe_" + equa, "point_" + equa)
                    # On enlève la courbe de self.courbe
                    del self.courbe[i]
                    break

        # On enregistre les infos de la courbe
        self.courbe.append([equa, color, mod, step])
        res = []        # Liste contenant les coordonnées de chaque pixel affichable
        for i in range(1, self.width + 1):
            x = self.convert_pix_to_unit("x", i)
            try:
                y_pix = self.convert_unit_to_pix("y",  eval(equa))
            except (NameError, TypeError, SyntaxError, ValueError):
                # On affiche un message d'erreur
                messagebox.showerror(
                    str(sys.exc_info()[0]), "L'équation \"" + equa + "\" semble erronée")
                # On supprime la dernière entrée de la liste self.courbe, car
                # elle est érronée
                self.courbe.pop()
                break       # On sort de la boucle for
            if (-(self.height**2) < y_pix < (self.height**2)):
                # On n'enregistre que les résultats servant à l'affichage
                res.append((i, y_pix))

        try:
            if (mod == "normal") or (mod == "both"):
                self.create_line(res, fill=color, tag="courbe_" + equa)
            if (mod == "point") or (mod == "both"):
                for i in range(0, len(res) - 1):
                    if not res[i][0] % step:
                        self.create_oval(res[i + 1][0] - 2, res[i + 1][1] - 2, res[i + 1][
                                         0] + 2, res[i + 1][1] + 2, fill=color, tag="point_" + equa)
            # Retourne 1 si tout c'est bien passé sinon on retourne rien (None)
            return 1
        except:
            return None

    def convert_pix_to_unit(self, axe, val):
        """ Convertie les pixels (par raport à un des axes) en unités """
        if axe == "x":
            pix = (self.val_xy[0][0] - self.val_xy[0][1]) / float(self.width)
            return self.val_xy[0][1] + pix * val
        elif axe == "y":
            pix = (self.val_xy[1][0] - self.val_xy[1][1]) / float(self.height)
            return self.val_xy[1][0] - pix * val
        else:
            return None

    def convert_unit_to_pix(self, axe, val):
        """ Convertie une unitée en pixel (par rapport à un des axes) """
        if axe == "x":
            unit = float(self.width) / (self.val_xy[0][0] - self.val_xy[0][1])
            return unit * (-self.val_xy[0][1]) + unit * val + 1
        elif axe == "y":
            unit = float(self.height) / (self.val_xy[1][0] - self.val_xy[1][1])
            return unit * self.val_xy[1][0] - unit * val + 1
        else:
            return None
##########################################################################


################################################# Début du programme #####
if __name__ == '__main__':
    # On importe le module Tix pour des widgets Tkinter préfabriqués et le
    # module de choix de couleur (ds une boite de dialogue) :
    from tkinter import tix, colorchooser, font

########################## Variables globales ########################
    color = "#999999"       # Couleur de la courbe en cours        ##
######################################################################

#------------------------------ Partie traçage d'une nouvelle courbes ---------------------------#
    # Fonction lançant le traçage de la courbe :
    def tracer():
        try:
            # Si le pas est trop gros, on demande à l'utilisateur si il veut qd
            # même tracer la courbe
            if (int(pas_en.get()) > 50) and (mod.get() != "normal"):
                if messagebox.askquestion("Conseil :", "Vous avez rentré une valeur de pas très élevé. Il se peut que la courbe ne s'affiche pas.\n Voulez-vous continuez ?") == "no":
                    return None
            if not rep.trace_courbe(equa=equa_en.get(), color=color, mod=mod.get(), step=int(pas_en.get())):
                equa_en.configure(bg="#c85e48")
            else:      # On réinitialise tous si la courbe a bien été tracé
                inisialis_trace_part()

        except ValueError:
            messagebox.showerror(
                "Attention !!!", "La valeur du pas \"" + pas_en.get() + "\" semble erronée.")

    def inisialis_trace_part():       # Pour initialiser ts les éléments de lbfr_tracer
        global color
        color = "#999999"
        equa_en.configure(bg=color)
        equa_en.delete(0, END)
        pas_en.delete(0, END)
        pas_en.insert(0, "10")
        color_bt.configure(bg=color)
        normal_rbt_mod.select()

    # Fonction permettant le choix de la couleur de la fonction :
    def choix_color():
        global color
        color = str(colorchooser.askcolor(
            title="Choisir la couleur de la fonction", color="#999999")[1])
        color_bt.configure(bg=color)
#------------------------------------------------------------------------------------------------#


#-------------------------------- Partie configuration du fenetrage -----------------------------#
    # Fonction lançant le traçage de la courbe :
    def config_window():
        try:
            xmax, xmin = float(lben_xmax.entry.get()), float(
                lben_xmin.entry.get()),
            ymax, ymin = float(lben_ymax.entry.get()), float(
                lben_ymin.entry.get())

            rep.delete(ALL)         # On supprime ts les éléments du canvas
            lb_coords.configure(text="x= -- et y= --")
            tmp_courbe = rep.courbe[0:]
            rep.courbe = []         # On supprime ttes les entrées de rep.courbe

            # Gestion des erreurs d'attributs :
            # Ce même bout de code apparaît déjà ds la class Repere, mais c'est normal
            # puisqu'elle est conçue pour être indépendante (pour être
            # réutilisable) du reste du code (donc gestion des erreurs
            # indépendantes)
            if xmax <= 0:
                xmax = 10
                lben_xmax.entry.delete(0, END)
                lben_xmax.entry.insert(0, "10")
                messagebox.showwarning(
                    "Attention !!!", "Valeur de \"xmax\" rectifiée à 10 car inférieur ou égal à 0")
            if xmin >= 0:
                xmin = -10
                lben_xmin.entry.delete(0, END)
                lben_xmin.entry.insert(0, "-10")
                messagebox.showwarning(
                    "Attention !!!", "Valeur de \"xmin\" rectifiée à -10 car supérieur ou égal à 0")
            if ymax <= 0:
                ymax = 10
                lben_ymax.entry.delete(0, END)
                lben_ymax.entry.insert(0, "10")
                messagebox.showwarning(
                    "Attention !!!", "Valeur de \"ymax\" rectifiée à 10 car inférieur ou égal à 0")
            if ymin >= 0:
                ymin = -10
                lben_ymin.entry.delete(0, END)
                lben_ymin.entry.insert(0, "-10")
                messagebox.showwarning(
                    "Attention !!!", "Valeur de \"ymin\" rectifiée à -10 car supérieur ou égal à 0")

            rep.trace_axe(xmax=xmax, xmin=xmin, ymax=ymax, ymin=ymin,
                          grad=grad.get())  # On trace les nvo axes
            for crb in tmp_courbe:     # Et on retrace les courbes
                rep.trace_courbe(equa=crb[0], color=crb[
                                 1], mod=crb[2], step=crb[3])

        except:
            messagebox.showerror(
                "Erreur !!!", "Une ou plusieurs données pour le fenètrage, ne sont pas des données numériques.\nVeuillez rectifier.")

    def reinitialisation():
        lben_xmax.entry.delete(0, END)
        lben_xmin.entry.delete(0, END)
        lben_ymax.entry.delete(0, END)
        lben_ymin.entry.delete(0, END)

        lben_xmax.entry.insert(0, "10")
        lben_xmin.entry.insert(0, "-10")
        lben_ymax.entry.insert(0, "10")
        lben_ymin.entry.insert(0, "-10")

        rep.courbe = []
        normal_rbt_grad.select()
        config_window()
#------------------------------------------------------------------------------------------------#

############################### Fonctions Mathématiques ##################

    def H(x):
        return (atan(x) + atan(1 / x) + (pi / 2)) / pi

    def SH(x):
        return (exp(x) - exp(-x)) / 2

    def CH(x):
        return (exp(x) + exp(-x)) / 2

    def TH(x):
        return SH(x) / CH(x)

    def aSH(x):
        return log((x + sqrt(1 + x**2)), exp(1))

    def aCH(x):
        return log((x + sqrt(-1 + x**2)), exp(1))

    def aTH(x):
        return (-1 + x**2) / (1 + x**2)

    def h(x):
        return (atan(x) + atan(1 / x) + (pi / 2)) / pi

    def sh(x):
        return (exp(x) - exp(-x)) / 2

    def ch(x):
        return (exp(x) + exp(-x)) / 2

    def th(x):
        return SH(x) / CH(x)

    def ash(x):
        return log((x + sqrt(1 + x**2)), exp(1))

    def ach(x):
        return log((x + sqrt(-1 + x**2)), exp(1))

    def ath(x):
        return (-1 + x**2) / (1 + x**2)

    def ln(x):
        return log(x, exp(1))

##########################################################################
#---------------------------------------- Autres fonctions --------------------------------------#
    def apropos():
        messagebox.showinfo("À propos ...", """Ce programme a été réalisé par Gulius (email: gulius44@hotmail.com), modifié par CodeNameX2.\n
Il a été écrit en Python 3.5, et utilise (donc nécéssite) les modules sys, tkinter, math, tkmessagebox, tix, tkcolorchooser, et Tkfont.\n\n
\n\nRalala, j'ai tjs révé de faire un About de ce style.\nMerci\n\n
        ----------------------------------------
                    Python powered
                  Longue vie à Python
                   Et à l'Open-Source
        ----------------------------------------\n""")

    def coords_write(event):
        lb_coords.configure(text="x= %4.2f et y= %4.2f" % (
            rep.convert_pix_to_unit("x", event.x), rep.convert_pix_to_unit("y", event.y)))
        rep.delete("croix")
        rep.create_text(event.x, event.y, text="+", font=font_big, tag="croix")

    def del_croix(event):
        # Enlève le chtite croix si le bouton drt de la sourie est préssé
        rep.delete("croix")
        lb_coords.configure(text="x= -- et y= --")
#------------------------------------------------------------------------------------------------#

    # Création du widget maître :
    root = tix.Tk()
    root.title("Traceur de fonctions mathématiques  - by Gulius")

    # Création des widgets esclaves #
    # Label ac les coordonnées :
    font_big = font.Font(size=15, weight="bold")
    lb_coords = Label(root, text="x= -- et y= --", font=font_big)
    lb_coords.grid(columnspan=3, padx=5, pady=5)
    # Repère -> 600*400, avec grad==2, sur fond blanc :
    rep = Repere()
    rep.trace_axe()
    rep.configure(borderwidth=0)
    # Si on presse le bouton gch de la souris sur le canvas, ça nous donne les
    # coords au pts cliqué
    rep.bind("<Button-1>", coords_write)
    rep.bind("<Button-3>", del_croix)       # Enlève la chtite croix
    rep.grid(row=1, columnspan=3, padx=10, pady=10, sticky=N)
    # LabelFrame_Tracer -> frame contenant les éléments pour tracer une courbe
    # :
    lbfr_tracer = tix.LabelFrame(root, label="Tracer une courbe")
    lbfr_tracer.frame.configure(width=rep.width / 2, height=100)
    lbfr_tracer.grid(row=2, sticky=NW)
    # Eléments de lbfr_tracer :
    Label(lbfr_tracer, text="Equation :").place(y=23, x=10)
    equa_en = Entry(lbfr_tracer, width=20, bg="#999999", justify="right")
    equa_en.place(y=20, x=70)
    Label(lbfr_tracer, text="Pas :").place(y=90, x=10)
    pas_en = Entry(lbfr_tracer, width=5, bg="#999999", justify="right")
    pas_en.insert(0, "10")
    pas_en.place(y=88, x=40)
    color_bt = Button(lbfr_tracer, text="Couleur équation",
                      relief=SOLID, border=1, command=choix_color)
    color_bt.place(x=130, y=88)
    Button(lbfr_tracer, text="Tracer", command=tracer).place(x=248, y=88)
    # Les RadioButton & co
    mod = StringVar()   # Variable Tkinter contenant la valeur de la case cochée
    mod.set("normal")
    Label(lbfr_tracer, text="Mod -->").place(x=10, y=53)
    normal_rbt_mod = Radiobutton(
        lbfr_tracer, text="Normal", value="normal", variable=mod)
    normal_rbt_mod.place(x=50, y=50)
    Radiobutton(lbfr_tracer, text="Point", value="point",
                variable=mod).place(x=115, y=50)
    Radiobutton(lbfr_tracer, text="Both", value="both",
                variable=mod).place(x=172, y=50)
    # LabelFrame_Repere_Option -> frame contenant les éléments pour configurer
    # le repère
    lbfr_rep = tix.LabelFrame(root, label="Configuration du repère")
    lbfr_rep.frame.configure(width=rep.width, height=100)
    lbfr_rep.grid(row=2, column=1, columnspan=2, sticky=NW)
    # Eléments de lbfr_rep :
    Label(lbfr_rep, text="Fenètrage :").place(x=10, y=20)
    lben_xmin = tix.LabelEntry(lbfr_rep, label="xmin ->  ")
    lben_xmin.entry.insert(0, "-10")
    lben_xmin.entry.configure(width=5, justify="right")
    lben_xmin.place(x=30, y=35)
    lben_xmax = tix.LabelEntry(lbfr_rep, label="xmax -> ")
    lben_xmax.entry.insert(0, "10")
    lben_xmax.entry.configure(width=5, justify="right")
    lben_xmax.place(x=30, y=55)
    lben_ymin = tix.LabelEntry(lbfr_rep, label="ymin ->  ")
    lben_ymin.entry.insert(0, "-10")
    lben_ymin.entry.configure(width=5, justify="right")
    lben_ymin.place(x=31, y=75)
    lben_ymax = tix.LabelEntry(lbfr_rep, label="ymax -> ")
    lben_ymax.entry.insert(0, "10")
    lben_ymax.entry.configure(width=5, justify="right")
    lben_ymax.place(x=31, y=95)
    Button(lbfr_rep, text="Mettre à jour",
           command=config_window).place(x=430, y=88)
    Button(lbfr_rep, text="Réinitialiser",
           command=reinitialisation).place(x=525, y=88)
    # Les RadioButtons & co
    grad = IntVar()
    grad.set(2)
    Label(lbfr_rep, text="Type de graduation -> ").place(x=190, y=20)
    Radiobutton(lbfr_rep, text="Sans axes        ",
                value=-1, variable=grad).place(x=300, y=20)
    Radiobutton(lbfr_rep, text="Axes simples    ",
                value=0, variable=grad).place(x=300, y=45)
    Radiobutton(lbfr_rep, text="Axes + flèches ",
                value=1, variable=grad).place(x=300, y=70)
    normal_rbt_grad = Radiobutton(
        lbfr_rep, text="Axes + graduations simples    ", value=2, variable=grad)
    normal_rbt_grad.place(x=400, y=20)
    Radiobutton(lbfr_rep, text="Axes + graduations complètes",
                value=3, variable=grad).place(x=400, y=45)
    # Différents Buttons en bas à droite pour quitter+aide+apropos
    fr_but_br = Frame(root)
    fr_but_br.grid(row=3, column=2, sticky=NE)
    Button(fr_but_br, text="À propos", command=apropos).pack(
        side=LEFT, padx=5, pady=5)
    Button(fr_but_br, text="Quitter", command=root.destroy).pack(
        side=LEFT, padx=5, pady=5)

    root.mainloop()         # On démarre l'application Tkinter

    os.system("pause")
##########################################################################
