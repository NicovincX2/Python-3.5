# -*- coding: utf-8 -*-

import os
import numpy as np

def moyenne_mobile_impaire(y,k):
    def mobile(y,k,n):
        if n + k//2 >= len(y):
            return []
        else:
            return [sum(y[n - k//2 : n + 1 + k//2]) / k] + mobile(y,k,n + 1)
    return list(np.repeat(None,k//2)) + mobile(y,k,k//2)


donnees = [7.2, 7.85, 7.25, 7.45, 7.52, 7.17, 6.93, 7.54, 7.48, 7.49, 7.04, 6.24, 6.55, 7.55, 6.5, 7.18, 6.13, 7.88, 6.74, 6.56, 6.24, 6.32, 6.75, 5.96, 6.15, 6.05, 5.57, 5.92, 4.3, 4.68, 5.63, 4.9, 4.34, 3.6]

from pygal import *

banquise = Line(x_label_rotation=45)

banquise.title = "Évolution de la surface de la banquise au  minimum de septembre de 1979 à 2012 (source : National Snow and Ice Data Center)"

banquise.x_labels = list(map(str, range(1979, 2013)))

banquise.add("surface de la banquise au  minimum de septembre",donnees)

banquise.add("Moyenne mobile d'ordre 7", moyenne_mobile_impaire(donnees,7))

banquise.render_to_file("banquise.svg")

os.system("pause")
