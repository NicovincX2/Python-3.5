# -*- coding: utf-8 -*-

import os
from __future__ import division
import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt

u=3
n=arange(0,15)
y=stats.poisson.pmf(n,u)
plt.plot(n,y,'o-')
plt.title('Poisson: $\mu$ =%i' % u,fontsize=15)
plt.xlabel('n',fontsize=15)
plt.ylabel('Probability of n',fontsize=15)
plt.show()

os.system("pause")