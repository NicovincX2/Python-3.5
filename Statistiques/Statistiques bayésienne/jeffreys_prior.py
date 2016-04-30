# -*- coding: utf-8 -*-

import os
import numpy as np
import matplotlib.pyplot as plt

figsize(12.5, 5)

x = np.linspace(0.000, 1, 150)
y = np.linspace(1.0, 1.0, 150)
lines = plt.plot(x, y, color="#A60628", lw=3)
plt.fill_between(x, 0, y, alpha=0.2, color=lines[0].get_color())
plt.autoscale(tight=True)
plt.ylim(0, 2);

figsize(12.5, 5)

psi = np.linspace(-10, 10, 150)
y = np.exp(psi) / (1 + np.exp(psi)) ** 2
lines = plt.plot(psi, y, color="#A60628", lw=3)
plt.fill_between(psi, 0, y, alpha=0.2, color=lines[0].get_color())
plt.autoscale(tight=True)
plt.ylim(0, 1);

os.system("pause")

