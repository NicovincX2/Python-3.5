# -*- coding: utf-8 -*-

import os

# Generate a population with mean 0 and sd of 1
k = 10000
N = randn(k)

# Next we will simulate three samples of differnet sizes from the distribution N
n = [8, 65, 512]

# There are a variety of ways of getting random samples, we'll do it here
# by permuting and taking the first k values in the resulting array.
# Note that this method will sample *without* replacement, in contrast to
# indexing with the return from randint(), as we did before.
d_empirical = list()
for k in n:
    sa = permutation(N)[:k]
    sb = permutation(N)[:k]
    d_empirical.append(sa.mean() - sb.mean())

print (d_empirical)

n_samples = 100
for i, k in enumerate(n):
    sa = zeros(k)
    sb = zeros(k)
    
    sa, sb = [], []
    for j in xrange(n_samples):
        sa.append(permutation(N)[:k])
        sb.append(permutation(N)[:k])
    
    # Compute the difference vector and plot a histogram
    # Represent the histogram as a PMF
    
    d = mean(sa, axis=1) - mean(sb, axis=1)
    bar(*utils.pmf_hist(d, 20), color=colors[i], alpha=0.5, label="sample size = %d" % k)

# Add some description to the plot
title("Probability of getting a spurious\ndifference between two random samples\nas function of sample size.")
ylabel("Probability of occurrence")
xlabel("Difference between random samples")

# Additionally, plot the empirical diffences we obtained in the first step as vertical lines
colors = seaborn.color_palette("deep")
for i, d in enumerate(d_empirical):
    axvline(d, color=colors[i], linewidth=2)
    
legend(loc="best");

os.system("pause")

