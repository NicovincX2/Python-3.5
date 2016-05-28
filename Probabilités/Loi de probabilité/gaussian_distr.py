# -*- coding: utf-8 -*-

import os
from __future__ import division
import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt

u = 5  # mean
s = 1  # standard deviation
x = arange(0, 15, 0.1)
y = (1 / (np.sqrt(2 * np.pi * s * s))) * exp(-(((x - u)**2) / (2 * s * s)))
plt.plot(x, y, '-')
plt.title('Gaussian: $\mu$=%.1f, $\sigma$=%.1f' % (u, s), fontsize=15)
plt.xlabel('x', fontsize=15)
plt.ylabel('Probability density', fontsize=15)
plt.show()

os.system("pause")
