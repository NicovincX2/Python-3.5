# -*- coding: utf-8 -*-

import os
import pymc as pm
import numpy as np
import matplotlib.pyplot as plt

n = 4
for i in range(10):
    ax = plt.subplot(2, 5, i + 1)
    if i >= 5:
        n = 15
    plt.imshow(pm.rwishart(n + 1, np.eye(n)), interpolation="none",
               cmap=plt.cm.hot)
    ax.axis("off")

plt.suptitle("Random matrices from a Wishart Distribution");

os.system("pause")

