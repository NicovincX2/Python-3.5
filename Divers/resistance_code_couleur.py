# -*- coding:utf-8 -*-

# http://codes-sources.commentcamarche.net/source/50206-calcul-de-resistances

"""
Permet de trouver la valeur d'une résistance à partir du code couleur et vice versa:
-Le code couleur est entré par des listboxs et la valeur s'affiche dans le champ de saisie.
-La valeur est entrée dans un champ de saisie et les couleurs sont actualisées.
"""

# Calcul de résistances
# Ecrit et développé par Amaury

from tkinter import *
from math import log
import os

cent, dix, unit, multip, tolere = 0, 0, 0, 1, 0

# Dictionnaires de décodage: associent leurs valeurs aux couleurs.
chiffres = {"#d18220": 0, "black": 0, "brown": 1, "red": 2, "orange": 3,
            "yellow": 4, "green": 5, "blue": 6, "purple": 7, "grey": 8, "white": 9}
multiplicateur = {"#8f966f": 0.01, "gold": 0.1, "black": 1, "brown": 10, "red": 10**2, "orange": 10 **
                  3, "yellow": 10**4, "green": 10**5, "blue": 10**6, "purple": 10**7, "grey": 10**8, "white": 10**9}
tolerence = {"#8f966f": 0.1, "gold": 0.05, "brown": 0.01,
             "red": 0.02, "green": 0.005, "blue": 0.0025, "purple": 0.001}

# Dictionnaires de codage: associent leurs couleurs aux valeurs.
couleurs = {-2: "#8f966f", -1: "gold", 0: "black", 1: "brown", 2: "red", 3: "orange",
            4: "yellow", 5: "green", 6: "blue", 7: "purple", 8: "grey", 9: "white"}
couleurs2 = {-2: "#8f966f", -1: "gold", 0: "#d18220", 1: "brown", 2: "red",
             3: "orange", 4: "yellow", 5: "green", 6: "blue", 7: "purple", 8: "grey", 9: "white"}

# Listes des couleurs à insérer dans les Listbox.
coul = ["noir", "marron", "rouge", "orange", "jaune",
        "vert", "bleu", "violet", "gris", "blanc"]
mult = ["argent", "or", "noir", "marron", "rouge",
        "orange", "jaune", "vert", "bleu", "violet"]
tole = ["argent", "or", "marron", "rouge", "vert", "bleu", "violet"]

# Correspondances entre le texte affiché dans les Listbox et les couleurs
# affichées.
traduction = {"argent": "#8f966f", "or": "gold", "aucun": "#d18220", "noir": "black", "marron": "brown", "rouge": "red",
              "orange": "orange", "jaune": "yellow", "vert": "green", "bleu": "blue", "violet": "purple", "gris": "grey", "blanc": "white"}


def Select(liste):
    # Acquiert la valeur choisie par l'utilisateur dans une Listbox.

    choix = traduction[str(liste.get(liste.curselection()))]
    return choix

# Ces 5 fonctions appellent sur évènement la fonction Select() avec pour
# argument le nom de la liste où l'évènement à eut lieu.


def Select1(e):
    global res, cent
    coul = Select(val1)
    res.create_rectangle(120, 11, 140, 89, fill=coul, outline=coul)
    cent = chiffres[coul] * 100
    Decode()


def Select2(e):
    global res, dix
    coul = Select(val2)
    res.create_rectangle(150, 11, 170, 89, fill=coul, outline=coul)
    dix = chiffres[coul] * 10
    Decode()


def Select3(e):
    global res, unit
    coul = Select(val3)
    res.create_rectangle(180, 11, 200, 89, fill=coul, outline=coul)
    unit = chiffres[coul]
    Decode()


def Select4(e):
    global res, multip
    coul = Select(val4)
    res.create_rectangle(210, 11, 230, 89, fill=coul, outline=coul)
    multip = multiplicateur[coul]
    Decode()


def Select5(e):
    global res, tolere
    coul = Select(val5)
    res.create_rectangle(360, 11, 380, 89, fill=coul, outline=coul)
    tolere = tolerence[coul]
    Decode()


def Draw():
    # Dessine une résistance vierge dans le Canevas.

    global res, valeur

    res.create_line(20, 50, 100, 50, width=5)
    res.create_line(480, 50, 400, 50, width=5)
    res.create_rectangle(100, 10, 400, 90, fill="#d18220", outline="black")
    valeur.insert(
        0, "Entrer une valeur ou indiquer le code couleur de la résistance")


def Decode():
    # Décode la valeur d'une résistance à partir du code couleur. Cette
    # fonction n'effectue que le calcul et l'affichage.

    global valeur, cent, dix, unit, multip, tolere
    resistance = float((cent + dix + unit) * multip)

    valeur.delete(0, END)
    ecart = tolere * resistance

    if tolere == 0:
        valeur.insert(0, SI(resistance, "code") + " Ohms")

    else:
        valeur.insert(0, "(" + SI(resistance, "code") +
                      "  +/-  " + SI(ecart, "code") + ") " + "Ohms")
    valeur.bind("<Button-1>", Del)


def Code(e):
    # Cette fonction code une résistance à partir d'une valeur entrée par
    # l'utilisateur.

    global res, valeur, couleurs, couleurs2, typ, val1, val2, val3, val4

    chaine = valeur.get()  # Acqusition de la valeur.
    try:
        # Isolement de la valeur numérique et du multiple SI (k,M,G,m,µ,n).
        tab = chaine.split(" ")
    except:
        tab = [chaine]

    # Convertit le tableau contenant la valeur et le multiple en une valeur
    # numérique.
    nombre = int(SI(tab, "decode"))

    taille = 0

    # Choisit le type de décodage : Standard à 3 anneaux ou Précision à 4
    # anneaux.
    tip = typ.get()

    if (tip == 2):  # Récupère chaque composantes du nombre : unités, dizaine, centaines (si précision), ainsi que le multiplicateur.

        while (nombre > 999):
            nombre = nombre / 10
            taille = taille + 1

        cent = nombre / 100
        nombre = nombre - cent * 100
        dix = nombre / 10
        nombre = nombre - dix * 10
        # Envoie aux Listbox la couleur correspondant au chiffre obtenue
        val1.select_set(cent)
        # Fait lire au programme la valeur précédement envoyée aux Listbaox.
        Select1(e)
        # Cette pirouette est nécessaire pour pouvoir ensuite tolérencer la
        # résistance choisie.

    elif (tip == 1):

        while (nombre > 99):
            nombre = nombre / 10
            taille = taille + 1

        res.create_rectangle(
            120, 11, 140, 89, fill="#d18220", outline="#d18220")

        dix = int(nombre / 10)
        nombre = nombre - dix * 10

    val2.select_set(dix)
    Select2(e)
    val3.select_set(nombre)
    Select3(e)
    val4.select_set(taille + 2)
    Select4(e)


def SI(nombre, sens):
    # Code ou décode un nombre au format SI: VALEUR+[Espace]+MULTIPLES

    if sens == "code":  # Fonction de codage: récupère un nombre et retourne une chaine de caractères
        try:
            taille = log(nombre, 10)
        except:
            pass

        nombre = float(nombre)

        # Affecte un pultiple en fonction de la taille du nombre
        if (taille >= 8.999999):
            chaine = str(nombre / (10**9)) + " G"

        elif (taille >= 5.999999):
            chaine = str(nombre / (10**6)) + " M"

        elif (taille >= 2.999999):
            chaine = str(nombre / (10**3)) + " k"

        elif (taille <= -6.000001):
            chaine = str(nombre * (10**9)) + " n"

        elif (taille <= -3.000001):
            chaine = str(nombre * (10**6)) + " µ"

        elif (taille <= -0.000001):
            chaine = str(nombre * (10**3)) + " m"

        else:
            chaine = str(nombre) + " "

        return chaine

    # Fonction de décodage: récupère un tableau [VALEUR,multiple] et retourne
    # une valeur numérique
    elif sens == "decode":

        tab = nombre

        if len(tab) == 1:
            valeur = float(tab[0])

        elif tab[1] == "k":
            valeur = float(tab[0]) * (10**3)

        elif tab[1] == "M":
            valeur = float(tab[0]) * (10**6)

        elif tab[1] == "G":
            valeur = float(tab[0]) * (10**9)

        elif tab[1] == "m":
            valeur = float(tab[0]) * (10**-3)

        elif tab[1] == "u":
            valeur = float(tab[0]) * (10**-6)

        elif tab[1] == "n":
            valeur = float(tab[0]) * (10**-9)

        return float(valeur)


def Del(e):
    # Efface le contenu de la zone de saisie si l'utilisateur clique dedans

    global valeur

    valeur.delete(0, END)
    # Empèche la programme d'effacer la zone à chaque clic: permet de modifier
    # la valeur entrée sans la voire s'effacer...
    valeur.bind("<Button-1>", Passer)


def Passer(e):
    pass  # No comment  ;)

########################## Interface Graphique ##########################

root = Tk()

res = Canvas(root, width=500, height=100, bg="ivory")
res.grid(row=0, column=0, columnspan=5)

txt1 = Label(root, text="Centaines :")
txt2 = Label(root, text="Dixaines :")
txt3 = Label(root, text="Unités :")
txt4 = Label(root, text="Multiplicateur :")
txt5 = Label(root, text="Tolérence :")
txt6 = Label(root, text="Résistance :")

txt1.grid(row=1, column=0)
txt2.grid(row=1, column=1)
txt3.grid(row=1, column=2)
txt4.grid(row=1, column=3)
txt5.grid(row=1, column=4)
txt6.grid(row=3, column=0)

val1 = Listbox(root, height=10)
val2 = Listbox(root, height=10)
val3 = Listbox(root, height=10)
val4 = Listbox(root, height=10)
val5 = Listbox(root, height=10)

valeur = Entry(root, width=70)

valeur.grid(row=3, column=1, rowspan=2, columnspan=4)

valeur.bind("<Return>", Code)
valeur.bind("<Button-1>", Del)

for i in coul:
    val1.insert(END, i)
    val2.insert(END, i)
    val3.insert(END, i)

for i in mult:
    val4.insert(END, i)

for i in tole:
    val5.insert(END, i)

val1.bind('<Double-1>', Select1)
val2.bind('<Double-1>', Select2)
val3.bind('<Double-1>', Select3)
val4.bind('<Double-1>', Select4)
val5.bind('<Double-1>', Select5)

val1.grid(row=2, column=0)
val2.grid(row=2, column=1)
val3.grid(row=2, column=2)
val4.grid(row=2, column=3)
val5.grid(row=2, column=4)

typ = IntVar()

r1 = Radiobutton(root, text="Standard", variable=typ, value=1)
r2 = Radiobutton(root, text="Précision", variable=typ, value=2)

r1.grid(row=3, column=0)
r2.grid(row=4, column=0)

r1.select()
r2.deselect()

Draw()

Sign = Label(root, text="Ecrit et développé par Amaury")
Sign.grid(row=10, column=3, columnspan=2)

root.title("Code couleur des résistances")
root.resizable(False, False)
root.mainloop()

os.system('pause')
