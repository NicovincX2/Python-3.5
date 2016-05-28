# -*- coding: utf-8 -*-

import os
import matplotlib.pyplot as plt
import numpy as np
from __future__ import division
import utils
import seaborn
seaborn.set()
colors = seaborn.color_palette()

# First create a vector of x values spanning the support of the histogram
x = linspace(d.min(), d.max(), 1000)

# Let's define a function to calculate the gaussian function for a given
# x, mean, and std
gauss = lambda x, m, s: (1 / (s * sqrt(2 * pi)) *
                         exp(-0.5 * ((x - m) / s) ** 2))

# We could iterate through the x values and calculate a y value for each
# using this equation
y0 = zeros_like(x)
for i, x_i in enumerate(x):
    y0[i] = gauss(x_i, m, s)

# You can also do it in one step with a vectorized computation.
# In general, avoid for loops, as vectorized expressions are much faster.
y = gauss(x, m, s)

# Use a normed histogram to match the range of the probaiblity density function
hist(d, 15, normed=True)
plot(x, y)

# Calculate the height of the gaussian for the outlier distribution and plot
x1 = linspace(d1.min(), d1.max(), 10000)
y1 = gauss(x1, m1, s1)
hist(d1, 15, normed=True)
plot(x1, y1)

from scipy import stats
x = linspace(-4, 4, 10001)
hist(stats.norm(0, 1).rvs(1000), 30, normed=True, alpha=.6)
plot(x, stats.norm(0, 1).pdf(x), linewidth=6)
plot(x, gauss(x, 0, 1), linewidth=3)

os.system("pause")
