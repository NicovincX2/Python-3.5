# -*- coding: utf-8 -*-

import os
import matplotlib.pyplot as plt
import seaborn
seaborn.set()
colors = seaborn.color_palette()
import utils

# We will first simulate a population. Using a "true" model of our choice; a straight line.
x = repeat(arange(200), 100)
x += randn(len(x)) * 5
a, b = 2, 100  # Parameters of the model
poly_order = 1  # A straight line
y = polyval([a, b], x) + randn(len(x)) * 70

# Show the simulated true population
plot(x, y, "o", markersize=3, alpha=.15)

# Show the true model on top of the population
true_m = polyval([a, b], x)
plot(x, true_m, linewidth=4);

# Now sample from the population
sample_size = 20
ind = permutation(arange(len(x)))[:sample_size]
x_sample = x[ind]
y_sample = y[ind]

# Show the sample
plot(x_sample, y_sample, "o")

# Fit the model to the sample with a straight line model
poly_order = 1
ab = polyfit(x_sample, y_sample, poly_order)

# Evalute the estimated model
y_fit = polyval(ab, x_sample)

# Show the model fit to the sample
plot(x_sample, y_fit, colors[4]);

# Define a function to compute R2 since we're doing it a few times
compute_r2 = lambda true, pred: 1 - sum(square(true - pred)) / sum(square(true - mean(true)))
r2 = compute_r2(y_sample, y_fit)
print ("R^2 = %.2f" % r2)

y_fit_truem = polyval([a, b], x_sample)
r2_true = compute_r2(y_sample, y_fit_truem)
print ("True R^2: %.2f" % r2_true)

# Use leave-one-out cross validation
from sklearn.cross_validation import LeaveOneOut
y_hat = zeros_like(y_fit)

# Iterate through the folds
for i, (train, test) in enumerate(LeaveOneOut(sample_size)):
    # Split the data
    x_train, x_test = x_sample[train], x_sample[test]
    y_train, y_test = y_sample[train], y_sample[test]
    
    # We fit the model to the training set
    ab_hat = polyfit(x_train, y_train, 1)
    
    # Make a prediction about the held-out sample and enter into the yhat vector
    y_hat[i] = polyval(ab_hat, x_test)

# Compute the cross-validated R^2
r2_cv = compute_r2(y_sample, y_hat)

print ("R^2 estimated on the sample: %.2f" % r2)
print ("R^2 estimated on the population: %.2f" % r2_true)
print ("Cross-validated R^2: %.2f" % r2_cv)

# Plot the original population
plot(x, y, "o", markersize=3, alpha=.15)
xlabel("X")
ylabel("Y")

# Show the true model on top of the population
plot(x, true_m, linewidth=3, alpha=.7)

# Show the sample
plot(x_sample, y_sample, "o", markersize=8, alpha=.8)

# Show the fit of the linear model from above
plot(x_sample, y_fit, linewidth=3, alpha=.7)

# Now let's fit a more complex model. A plolynomial of 4th order.
# This model is not similar to a the true model (a straight line), but will
# represent better the specific data in the sample better than a straight
# line, because it will be able to adapt better to the small variability in
# the data in the sample due to chance.
params = polyfit(x_sample, y_sample, deg=4)
y_fit_p4 = polyval(params, x_sample)
sorter = argsort(x_sample)
plot(x_sample[sorter], y_fit_p4[sorter], linewidth=3, alpha=.7);

# The polynomial of 4th order (gold) passes closer to each sample data
# point (red) than the straight line (purple) does. It shuld have a higher
# R2 than the straight-line model.
r2_line = compute_r2(y_sample, y_fit)
r2_cube = compute_r2(y_sample, y_fit_p4)
print ("Line model: %.2f" % r2_line)
print ("Cubic model: %.2f" % r2_cube)

yhat_line = zeros_like(y_sample)
yhat_cube = zeros_like(y_sample)

for i, (train, test) in enumerate(LeaveOneOut(sample_size)):
    
    x_train = x_sample[train]
    y_train = y_sample[train]
    
    x_test = x_sample[test]
    
    line_model = polyfit(x_train, y_train, 1)
    cube_model = polyfit(x_train, y_train, 4)
    
    yhat_line[i] = polyval(line_model, x_test)
    yhat_cube[i] = polyval(cube_model, x_test)

r2_line_cv = compute_r2(y_sample, yhat_line)
r2_cube_cv = compute_r2(y_sample, yhat_cube)

print ("Line model (full fit): %.2f" % r2_line)
print ("Line model (cross-validated): %.2f" % r2_line_cv)
print ("Cubic model (full fit): %.2f" % r2_cube)
print ("Cubic model (cross-validated): %.2f" % r2_cube_cv)

os.system("pause")

