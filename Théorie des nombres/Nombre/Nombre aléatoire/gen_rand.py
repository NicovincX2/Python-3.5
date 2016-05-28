# -*- coding: utf-8 -*-

import os
from numpy import rand
from matplotlib.pyplot import *
from random import random

rands = []
for i in range(100):
    rands.append(random())
plot(rands)

from random import gauss

grands = []
for i in range(100):
    grands.append(gauss(0, 1))
plot(grands)

plot(rand(100))

os.system("pause")
