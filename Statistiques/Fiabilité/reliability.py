# -*- coding: utf-8 -*-

import os
import matplotlib.pyplot as plt
import seaborn
seaborn.set()
colors = seaborn.color_palette()
import moss

n_obs = 100
X = column_stack((randn(n_obs, 4), ones(n_obs)))

w = rand(5)
noise = randn(100) * 5
y = dot(X, w) + noise

ols_fit = lambda X, y: dot(dot(inv(dot(X.T, X)), X.T), y)
w_ols = ols_fit(X, y)

bar(arange(5) + .1, w, .4, label="actual weights")
bar(arange(5) + .5, w_ols, .4, color=colors[1], label="estimated weights")

iterations = 1000
w_boot = zeros((iterations, len(w_ols)))
for i in xrange(iterations):

    # Get an index vector to sample with replacement
    samp = randint(0, n_obs, n_obs)

    # Resample data and model
    samp_X = X[samp, :]
    samp_y = y[samp]

    # Fit the model on this iteration
    w_boot[i, :] = ols_fit(samp_X, samp_y)

# Get the 95% confidence interval for each weight (across each column in
# the design matrix)
w_ols_ci = moss.percentiles(w_boot, [2.5, 97.5], axis=0)

# The bar() function expects errorbar coordinates to be relative to bar height
# We have a convenience function in our plotting library to convert these
ebar_coords = seaborn.ci_to_errsize(w_ols_ci, w_ols)

# Plot the confidence intervals as error bars on our barplot from above
bar(arange(5) + .1, w, .4, label="actual weights")
bar(arange(5) + .5, w_ols, .4, yerr=ebar_coords,
    color=colors[1], ecolor="gray", label="estimated weights")

X = column_stack((randn(1000, 4), ones(1000)))
w = rand(5)

# Large sample high noise; N = 1000, noise std = 5
y_large_n = dot(X, w) + randn(1000) * 5

# Small sample low noise; high signal to noise ratio
y_lownoise = dot(X[:100], w) + randn(100)

# Small sample, high noise
y_noisy = dot(X[:100], w) + randn(100) * 5

# Bootstrap all three models
n_boot = 1000
w_boot1 = moss.bootstrap(X, y_large_n, n_boot=n_boot, func=ols_fit)
w_boot2 = moss.bootstrap(X[:100], y_lownoise, n_boot=n_boot, func=ols_fit)
w_boot3 = moss.bootstrap(X[:100], y_noisy, n_boot=n_boot, func=ols_fit)

# The median of these bootstrapped estimates are the weights for each model.
# You could also use the mean if you prefer.
w_model1 = median(w_boot1, axis=0)
w_model2 = median(w_boot2, axis=0)
w_model3 = median(w_boot3, axis=0)

# Compute the 95% confidence intervals on parameter estimates
pcts = [2.5, 97.5]
ci1 = moss.percentiles(w_boot1, pcts, axis=0)
ci2 = moss.percentiles(w_boot2, pcts, axis=0)
ci3 = moss.percentiles(w_boot3, pcts, axis=0)

barx = linspace(0, 1, 6)[:-1]
models = [w, w_model1, w_model2, w_model3]
cis = [None] + map(seaborn.ci_to_errsize, [ci1, ci2, ci3], models[1:])
for i, model in enumerate(models):
    bar(barx + i, model, 0.2, yerr=cis[i], color=colors[i], ecolor="gray")
xticks([.5, 1.5, 2.5, 3.5], ["model", "large N", "low noise", "noisy"])

# We will use the R^2 function from the Scikit-learn function
from sklearn.metrics import r2_score
r2_model1 = r2_score(y_large_n, dot(X, w_model1))
r2_model2 = r2_score(y_lownoise, dot(X[:100], w_model2))
r2_model3 = r2_score(y_noisy, dot(X[:100], w_model3))

print('Model 1 is reliable but not accurate. R^2 = %.2f' % r2_model1)
print('Model 2 is reliable and accurate. R^2 = %.2f' % r2_model2)
print('Model 3 is neither reliable nor accurate. R^2 = %.2f' % r2_model3)

# Here are the weights
w = rand(3)

# Simulate data from 3 uncorrelated regressors
X_orth = randn(100, 3)

# Signal with no noise
y_orth = dot(X_orth, w)

# Add noise that with a std proportional to the signal std
y_orth = y_orth + std(y_orth) * randn(100)

# Simulate data from 3 correlated regressors.  To do this first we define
# a covariance matrix, S.
cor = 0.8  # This is the correlation to induce between the variables
S = eye(3)
S[S == 0] = cor

# Then simulate data that comes from a 3-D gaussian (mean 0) with this
# covariance matrix
X_corr = random.multivariate_normal(zeros(3), S, 100)
y_corr = dot(X_corr, w)
y_corr = y_corr + std(y_corr) * randn(100)

# Bootstrap the model fits for the correlated and uncorrelated data
n_boot = 1000
boot_orth = moss.bootstrap(X_orth, y_orth, n_boot=n_boot, func=ols_fit)
boot_corr = moss.bootstrap(X_corr, y_corr, n_boot=n_boot, func=ols_fit)

# Calculate the 95% confidence intervals on the 2 sets of weights
pcts = [2.5, 97.5]
ci1 = moss.percentiles(boot_orth, pcts, axis=0)
ci2 = moss.percentiles(boot_corr, pcts, axis=0)

barx = linspace(0, 1, 4)[:-1]
models = [w, median(boot_orth, axis=0), median(boot_corr, axis=0)]
cis = [None] + map(seaborn.ci_to_errsize, [ci1, ci2], models[1:])
for i, model in enumerate(models):
    bar(barx + i, model, 1. / 3, yerr=cis[i], color=colors[i], ecolor="gray")
xticks([.5, 1.5, 2.5], ["model", "orthogonal", "correlated"])

# Assume that this is the population of data
x_pop = randn(1000) + 4
noise = randn(1000) * 5
y_pop = 1.5 * x_pop ** 2 + noise

# And this is a random sample we collect in an experiment
n = 10
samp = permutation(arange(len(y_pop)))[:n]
x_samp = x_pop[samp]
y_samp = y_pop[samp]

plot(x_pop, y_pop, "o", label="population")
plot(x_samp, y_samp, "o", color=colors[2], label="sample")

from scipy.optimize import curve_fit
modelfunc = lambda x, a, b, c: a * x ** b + c
# Bootstrap the linear and nonlinear fitting procedures
w_ols_boot, w_nonlin_boot = [], []
for i in xrange(100):

    # Get the bootstrap index
    boot_samp = random.randint(0, n, n)
    boot_x = x_samp[boot_samp]
    boot_y = y_samp[boot_samp]

    # Fit a linear model
    w_ols_boot.append(lstsq(moss.add_constant(boot_x), boot_y)[0])
    w_nonlin_boot.append(
        curve_fit(modelfunc, boot_x, boot_y, maxfev=100000)[0])
w_ols_boot = array(w_ols_boot)
w_nonlin_boot = array(w_nonlin_boot)

# Visualize the reliability of the parameter estimates of the linear model
ols_model = median(w_ols_boot, axis=0)
pcts = [16, 84]
ols_ci = percentile(w_ols_boot, pcts, axis=0)
nonlin_model = median(w_nonlin_boot, axis=0)
nonlin_ci = percentile(w_nonlin_boot, pcts, axis=0)
ols_ebars = seaborn.ci_to_errsize(ols_ci, ols_model)
bar(range(2), ols_model, 1, yerr=ols_ebars, ecolor="gray", label="OLS")
nonlin_ebars = seaborn.ci_to_errsize(nonlin_ci, nonlin_model)
bar(range(2, 5), nonlin_model, 1, yerr=nonlin_ebars,
    ecolor="gray", color=colors[1], label="nonlinear")
xticks(arange(5) + .5, ["slope", "constant", "slope", "exponent", "constant"])
legend()

os.system("pause")
