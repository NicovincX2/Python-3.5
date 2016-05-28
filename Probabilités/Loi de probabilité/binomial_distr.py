# -*- coding: utf-8 -*-

import os
from __future__ import division
import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt

N = 6
p = 0.5
n = arange(0, 20)
y = stats.binom.pmf(n, N, p)
plt.plot(n, y, 'o-')
plt.title('Binomial: N=%i , p=%.2f' % (N, p), fontsize=15)
plt.xlabel('n', fontsize=15)
plt.ylabel('Probability of n', fontsize=15)
plt.show()

os.system("pause")
