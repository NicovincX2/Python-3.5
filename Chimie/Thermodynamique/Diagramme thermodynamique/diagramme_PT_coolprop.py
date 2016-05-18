# -*- coding: utf-8 -*-

import os

"""
Fabrication simple d'un diagramme PT avec CoolProp. Malheureusement, on n'a
accès qu'à la partie "fluide" du diagramme donc l'équilibre liquide/vapeur,
mais c'est déjà pas mal.
"""

import matplotlib.pyplot as plt
from CoolProp.Plots import PropsPlot

fluid = 'Water'                  # Le fluide choisi (plus dans CoolProp.CoolProp.FluidsList())
pt_plot = PropsPlot(fluid, 'pt') # Le type de diagramme
plt.yscale('log')                # Échelle logarithmique en pression
pt_plot._draw_graph()            # Dessin du graphe obligatoire avant sauvegarde
plt.savefig('T2_diagramme_PT_coolprop_{}.png'.format(fluid))

os.system("pause")
