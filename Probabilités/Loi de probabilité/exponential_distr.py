# -*- coding: utf-8 -*-

import os
from __future__ import division
import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt

k = 0.4
x = arange(0, 15, 0.1)
y = k * exp(-k * x)
plt.plot(x, y, '-')
plt.title('Exponential: $k$ =%.2f' % k, fontsize=15)
plt.xlabel('x', fontsize=15)
plt.ylabel('Probability density', fontsize=15)
plt.show()

os.system("pause")
