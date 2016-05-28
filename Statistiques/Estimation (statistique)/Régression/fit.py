# -*- coding: utf-8 -*-

import os
import matplotlib.pyplot as plt
import seaborn
seaborn.set()
colors = seaborn.color_palette()
import moss
from scipy.optimize import curve_fit

scatter(x_pop, y_pop, facecolor='none')
l, r = xlim()
xx = linspace(l, r, 200)
# Loop over each bootstrap iteration and compute that models prediction
# for all of the x values
y_model = []
for i, w in enumerate(w_ols_boot):
    y_i = dot(xx, w_ols_boot[i][0]) + w_ols_boot[i][1]
    y_model.append(y_i)

# Plot the linear prediction and transparent error bars
pcts = [16, 84]
plot(xx, median(y_model, axis=0))
lin_ci = moss.percentiles(y_model, pcts, axis=0)
fill_between(xx, *lin_ci, color=colors[0], alpha=.2)

# Now derive the nonlinear predictions and plot
y_model_nlin = []
for i, w in enumerate(w_nonlin_boot):
    y_i = modelfunc(xx, *w)
    y_model_nlin.append(y_i)
plot(xx, median(y_model_nlin, axis=0))
nlin_ci = moss.percentiles(y_model_nlin, pcts, axis=0)
fill_between(xx, *nlin_ci, color=colors[1], alpha=.2)

scatter(x_pop, y_pop, facecolor='none')
plot(xx, mean(y_model_nlin, 0), label="mean", color=colors[3])
plot(xx, median(y_model_nlin, 0), label="median", color=colors[4])
legend(loc="best")

figure(figsize=(9, 9))
plot_type = ["slope", "exponent", "constant"]
for pi in range(3):
    subplot(3, 1, pi + 1)
    hist(w_nonlin_boot[:, pi], 25, color=colors[pi])
    title(plot_type[pi])

figure(figsize=(9, 6))
plot_type = ["slope", "constant"]
for pi in range(2):
    subplot(2, 1, pi + 1)
    hist(w_ols_boot[:, pi], 25, color=colors[pi])
    title(plot_type[pi])

os.system("pause")
