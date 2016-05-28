# -*- coding: utf-8 -*-

import os

""" 
Programme permettant de visualiser l'effet de l'intégration par méthode de 
Verlet (aussi appelée leap-frog dans une formulation légèrement différente 
mais équivalente) pour un amas constitué d'un nombre réduit de masses histoire 
de faire une visualisation en 3D du problème.

L'idée est principalement de vérifier que mon implémentation du schéma 
d'intégration proposé dans le sujet d'informatique commune Centrale 2015 tient 
à peu près la route.
"""

# Les paramètres principaux de la simulation
m = [1.0] * 5
p0 = [[0, 1, 2], [0, -1, -2], [1.0, 3, 0], [-2, -1, 0], [1, -1, 0]]
vcom = 0.15  # On va s'arranger pour avoir une quantité de mvt globale nulle
v0 = [[0, 0, vcom], [vcom, 0, -vcom],
      [-vcom, vcom, 0], [0, -vcom, vcom], [0, 0, -vcom]]
deltat = 1e-3       # Le pas de temps
tmax = 57           # Le temps total
n = int(tmax / deltat)  # Le nombre total de pas
tfantome = 1        # Le temps passé dans le trait fantôme
ifantome = int(tfantome / deltat)  # et le nombre de pas correspondant
# Coeff multiplicatif pour que les sorties se fassent à intervalle de temps
# (ici 0.01) indépendant du pas de temps choisi (sauf s'il est trop petit bien sûr)
mult = int(0.01 / deltat + 1)


# D'abord quelques fonctions pour faire "comme si" les listes étaient en fait
# des vecteurs.

def smul(nombre, liste):
    """ Multiplication d'un vecteur par un scalaire. """
    L = []                       # Initialisation à une liste vide
    for element in liste:        # On itère sur les éléments
        L.append(nombre * element)  # On rajoute la valeur idoine
    return L                     # On n'oublie pas de renvoyer le résultat


def vsom(L1, L2):
    """ Fais l'addition vectorielle L1+L2 de deux listes. """
    L = [0] * len(L1)        # Inialisation à une liste de 0
    for i in range(len(L1)):  # On regarde toutes les positions
        L[i] = L1[i] + L2[i]  # Addition
    return L


def vdif(L1, L2):
    """ Fait la différence vectorielle L1-L2 de deux listes. """
    L = []                      # Initialisation à une liste vide
    for i in range(len(L1)):    # On regarde toutes les positions
        L.append(L1[i] - L2[i])  # Rajout de la soustraction
    return L


def norme(v):
    """ Calcule la norme euclidienne d'un vecteur dont on donne ses
    composantes dans une base orthonormée. """
    norme2 = 0                   # Initialisation de la norme carrée
    for i in range(len(v)):      # On passe toutes les composantes
        norme2 = norme2 + v[i]**2  # Ajout du carré de la composante
    return norme2**0.5           # Le résultat est la racine carrée de la somme


# La partie physique à présent. On commence par le calcul des forces

def force2(m1, p1, m2, p2):
    """ Renvoie une liste représentative de la force exercée par la particule 
    2 sur la particule 1. """
    P1P2 = vdif(p2, p1)           # Le vecteur P1P2
    G = 6.67e-11                 # Constante universelle de gravitation
    G = 1
    # Constante multiplicative devant le vecteur
    a = G * m1 * m2 / norme(P1P2)**3
    return smul(a, P1P2)          # Renvoie du vecteur a*P1P2


def forceN(j, m, pos):
    """ Force gravitationnelle totale exercée par toutes les particules sur la 
    particule j. """
    force = smul(0, pos[j])  # Initialisation au vecteur nul de bonne taille
    for k in range(len(m)):  # On passe toutes les particules en revue
        if k != j:          # Si on n'est pas sur la particule concernée
            f_k_sur_j = force2(m[j], pos[j], m[k], pos[
                               k])  # Force individuelle
            force = vsom(force, f_k_sur_j)  # et ajout à la force totale
    return force            # Renvoi de la force total après sommation

# Puis l'utilisation de l'intégrateur pour calculer la position suivante de
# chaque particule.


def pos_suiv(m, pos, vit, h):
    """ Version où l'on parcourt manuellement les trois dimensions d'espace. 
    Attention, l'accélération vaut la force divisée par la masse (on aurait 
    mieux fait de calculer les accélérations directement pour économiser 
    quelques calculs...). """
    L = []                   # Initialisation des nouvelles positions
    for j in range(len(m)):  # On parcourt les particules une à une
        mj, pj, vj = m[j], pos[j], vit[j]  # Des raccourcis pour la lisibilité
        force = forceN(j, m, pos)          # Vecteur force totale sur j
        # Initialisation nouvelle position pour j
        next = smul(0, pj)
        for k in range(len(pj)):         # Boucle sur les dimensions d'espace
            next[k] = pj[k] + vj[k] * h + h**2 / 2 * force[k] / mj  # et Verlet
        L.append(next)       # Ajout du résultat à la liste
    return L                 # et renvoi final une fois complètement remplie

# dont on a besoin pour déterminer la vitesse et donc l'ensemble de l'état
# suivant du système


def etat_suiv(m, pos, vit, h):
    """ Calcul de l'état suivant (position et vitesse) pour toutes les 
    particules connaissant ces valeurs à la date t_i. """
    new_pos = pos_suiv(
        m, pos, vit, h)  # On calcule tout de suite les nouvelles positions
    new_vit = []                    # Liste vide pour les nouvelles vitesses
    for j in range(len(m)):         # Les particules, une à une
        mj, vj = m[j], vit[j]          # Raccourcis
        fi = smul(1 / mj, forceN(j, m, pos))     # Accélération à t_i
        fip1 = smul(1 / mj, forceN(j, m, new_pos))  # Accélération à t_{i+1}
        # Initialisation à la vitesse nulle pour la taille
        next_vj = smul(0, vj)
        for k in range(len(vj)):    # Boucle sur les dimensions d'espace
            next_vj[k] = vj[k] + h / 2 * \
                (fi[k] + fip1[k])  # Application de Verlet
        new_vit.append(next_vj)     # Ajout à la liste des vitesses
    # Renvoi des nouvelles positions et nouvelles vitesses
    return new_pos, new_vit


def simulation_verlet(deltat, n):
    """ Simulation globale avec un pas de temps deltat (il a fini par 
    sortir du bois :o) et un nombre n de pas de temps à effectuer."""
    pos = p0  # Pas besoin de conversion pour cet exemple
    vit = v0
    liste_positions = [pos]  # Initialisation de la liste à renvoyer
    for i in range(n):     # Autant de fois que demandé,
        if i % 1000 == 0:
            print(i)  # Un peu de feedback
        # on détermine l'état suivant
        pos, vit = etat_suiv(m, pos, vit, deltat)
        liste_positions.append(pos)  # Ajout (sans conversion inverse)
    return liste_positions

# Maintenant, on va quand même utiliser les facilités de Numpy pour
# effectuer le calcul

import numpy as np

positions = np.array(simulation_verlet(deltat, n))

# Et à présent, les animations proprement dites

import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d.axes3d as p3
from matplotlib import animation  # Pour l'animation progressive

fig = plt.figure(figsize=(10, 10))
ax = p3.Axes3D(fig)  # Attaching 3D axis to the figure

# Creating line objects.
# NOTE: Can't pass empty arrays into 3d version of plot()
data = [positions[:, i, :] for i in range(len(m))]
lignes = [ax.plot(dat[:, 0], dat[:, 1], dat[:, 2])[0] for dat in data]

cote = 3
ax.set_xlim3d([-cote, cote])
ax.set_xlabel('X')
ax.set_ylim3d([-cote, cote])
ax.set_ylabel('Y')
ax.set_zlim3d([-cote, cote])
ax.set_zlabel('Z')

ax.set_title("Petit amas stellaire, $t={}$".format(tmax))

plt.savefig('PNG/M_schema_de_verlet3D_total.png')

# plt.show()


def init():
    for l in lignes:
        l.set_xdata([])
        l.set_ydata([])
        l.set_y3d_properties([])


def animate(i):
    ax.set_title('Petit amas stellaire, $t={}$'.format(
        round(mult * i * deltat, 1)))
    for j in range(len(lignes)):
        l = lignes[j]
        if mult * i < ifantome:
            pos = positions[:mult * i, j, :]
        else:
            pos = positions[mult * i - ifantome:mult * i, j, :]
        l.set_xdata(pos[:, 0])
        l.set_ydata(pos[:, 1])
        l.set_3d_properties(pos[:, 2])
    # On modifie l'angle de vue au fur et à mesure
    ax.view_init(elev=10, azim=(i / 10) % 360)

# L'animation proprement dite
anim = animation.FuncAnimation(fig, animate, frames=int(n / mult), interval=20)

#anim.save('PNG/M_schema_de_verlet3D.mp4', fps=30)

plt.show()

os.system("pause")
