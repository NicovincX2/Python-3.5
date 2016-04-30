# -*- coding: utf-8 -*-

import os
import matplotlib.pyplot as plt
import numpy as np
from __future__ import division
import utils
import seaborn
seaborn.set()
colors = seaborn.color_palette()

k = 10000
N = concatenate([chisquare(6, k / 2), randn(k / 2)])
mu = mean(N)
me = median(N)
sd = std(N)

hist(N, 100)
axvline(me, label="median", color=colors[1], linewidth=3)
axvline(mu, label="mean", color=colors[2], linewidth=3)
sd_y = ylim()[1] * .5
plot([mu - sd, mu + sd], [sd_y] * 2, "--", color=colors[2], linewidth=3, label="std dev")
title("Simulated true distribution (Chisquare, 6 DOF + Gaussian)")
legend();

n = 4
m = 8
sa = permutation(N)[:n]
sb = permutation(N)[:m]

d_empirical = mean(sa) - mean(sb)

sh0 = concatenate((sa, sb))

k = 10000
sa_rand = zeros((n, k))
sb_rand = zeros((m, k))
for i in xrange(k):
    iter_dist = permutation(sh0)
    sa_rand[:, i] = iter_dist[:n]
    sb_rand[:, i] = iter_dist[n:]
	
d = sa_rand.mean(axis=0) - sb_rand.mean(axis=0)
bar(*utils.pmf_hist(d, 100))
title("Distribution of the differences between the means of samples sa and sb")
ylabel("Probability of occurance")
xlabel("Difference (sa - sb)")

# Plot the actual difference we got
plot([d_empirical, d_empirical], ylim(), color=colors[4], linewidth=2.5)

# Get the probability of such a result by counting the number of larger (absolute) differences
p = sum(abs(d) > abs(d_empirical)) / k
text(xlim()[0], ylim()[1] * .95, "$H_0$ is true with %.2f probability" % p, size=12);

# First aggregate the samples
sh0 = concatenate((sa, sb))

# Resample 10,000 times with replacement
k = 10000
sa_rand = zeros((n, k))
sb_rand = zeros((m, k))
for i in xrange(k):
    sa_rand[:, i] = sh0[randint(0, n + m, n)]
    sb_rand[:, i] = sh0[randint(0, n + m, m)]
    
# Compute the difference and plot as before
d = median(sa_rand, axis=0) - median(sb_rand, axis=0)

bar(*utils.pmf_hist(d, 100), color=colors[3])
title('Distribution of the differences between the means of samples sa and sb')
ylabel('Probability of occurrence')
xlabel('Difference (sa - sb)')

plot([d_empirical] * 2, ylim(), color=colors[1], linewidth=2.5)

p = sum(abs(d) > abs(d_empirical)) / k
text(xlim()[0], ylim()[1] * .95, "$H_0$ is true with %.2f probability" % p);

os.system("pause")

