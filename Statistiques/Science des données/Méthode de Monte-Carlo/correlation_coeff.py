# -*- coding: utf-8 -*-

import os
import matplotlib.pyplot as plt
import numpy as np
from __future__ import division
import utils
import seaborn
seaborn.set()
colors = seaborn.color_palette()

# Say our acutal measured correlation was 0.4
r_empirical = 0.4

# Simulate two IID normal variables
k = 10000  # number of sims
n = 30  # sample size
s1_sim = randn(k, n)
s2_sim = randn(k, n)

# Compute the correlation coefficient for each sample
r_dist = array(map(stats.pearsonr, s1_sim, s2_sim))[
    :, 0]  # Take first column (r values)

# Plot the distribution of coefficients obtained this way
bar(*utils.pmf_hist(r_dist, 100), color=colors[4])
title('Distribution of the Montecarlo-simulated correlation coefficients')
ylabel('Probability of occurrence')
xlabel('Corr(s1,s2)')

# Plot the observed correlation on this PMF
axvline(r_empirical, color=colors[0], linewidth=3)

# Obtain the probability of our observed value by counting how many
# r's from our randomization test were more extreme
p = sum(abs(r_empirical) > abs(r_dist)) / k
xpos = xlim()[0] * .95
ypos = ylim()[1] * .95
text(xpos, ypos, "$H_0$ is false with probability %.3f" % p, size=12)

os.system("pause")
