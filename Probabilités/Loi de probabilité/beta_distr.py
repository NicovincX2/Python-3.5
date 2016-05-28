# -*- coding: utf-8 -*-

import os
from __future__ import division
import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt

a = 0.5
b = 0.5
x = arange(0.01, 1, 0.01)
y = stats.beta.pdf(x, a, b)
plt.plot(x, y, '-')
plt.title('Beta: a=%.1f, b=%.1f' % (a, b), fontsize=15)
plt.xlabel('x', fontsize=15)
plt.ylabel('Probability density', fontsize=15)
plt.show()

os.system("pause")
