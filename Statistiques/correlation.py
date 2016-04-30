# -*- coding: utf-8 -*-

import os
import matplotlib.pyplot as plt
import numpy as np
from __future__ import division
import utils
import seaborn
seaborn.set()
colors = seaborn.color_palette()

# First there's the longwinded arithmetic
# (Note this isn't all that longwinded since it's a vectorized calculationg)
r1 = mean(((s1 - s1.mean()) / s1.std()) * ((s2 - s2.mean()) / s2.std()))

# We can also use functions from the scipy.stats package
from scipy import stats
r2 = mean(stats.zscore(s1) * stats.zscore(s2))

# This package even offers a one-step function
# Note this returns a tuple (r, p)
r3, p3 = stats.pearsonr(s1, s2)

print ("%.3f, %.3f, %.3f" % (r1, r2, r3))

# Note that scatter(s1, s2) is equivalent to plot(s1, s2, "o")
plot(s1, s2, "o")
xlabel("Values in variable 1")
ylabel("Values in variable 2")

# We can display the simulated and computed correlations
annot = "Correlations:\nSimulated: %.3f\nEstimated: %.3f" % (w, r1)
text(xlim()[0] + .2, ylim()[1] - 1, annot, size=12);

# Number of samples
k = 1000
r_dist = zeros(k)

# Do the bootstrap
for i in xrange(k):
    idx = randint(0, n, n)
    r_dist[i] = stats.pearsonr(s1[idx], s2[idx])[0]

# Compute the two-tailed 95% confidence intervals
ci = utils.percentiles(r_dist, [2.5, 97.5])

# Plot the correlation with error bars
bar(0.5, r1, width=1)
plot([1, 1], ci, color=colors[2], linewidth=3)
xlim(0, 2)
ylim(0, 1)
xticks(())
title("Estimated correlation coefficient with error")
ylabel("Correlation between s1, s2");

k = 1000
r_dist = zeros(k)
for i in xrange(k):
    s1_rand = s1[randint(0, n, n)]
    s2_rand = s2[randint(0, n, n)]
    r_dist[i] = stats.pearsonr(s1_rand, s2_rand)[0]

bar(*utils.pmf_hist(r_dist, 20))
title('Distribution of correlations between s1 and s2')
ylabel('Likelihood of occurrence')
xlabel('Pearson correlation coefficient')

# Now plot the empirical correlation value
axvline(r1, color=colors[3], linewidth=3)
p = sum(abs(r1) < abs(r_dist)) / k
text(0.2, ylim()[1] * .95, "$H_0$ is true with %.2f probability" % p);

os.system("pause")

