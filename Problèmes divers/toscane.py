# -*- coding: utf-8 -*-

import os
from numpy.random import randint
from collections import Counter

s = [sum(randint(1, 7, size=3)) for k in range(100000)]
c = Counter(s)

from pygal import *

toscane = HorizontalBar()
for v in c:
    toscane.add(str(v), c[v])
toscane.render_to_file("toscane.svg")
toscane.title = "Effectifs des sorties du problème du duc de Toscane"

os.system("pause")
