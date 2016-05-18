# -*- coding: utf-8 -*-

from __future__ import division
import os
import matplotlib.pyplot as plt
import numpy as np
import utils
import seaborn
seaborn.set()
colors = seaborn.color_palette()

# For example if we have some data X
X1 = randn(100, 2)
plot(X1[:, 0], X1[:, 1], "o");

# And we multiple that data by a matrix A
A = array([[1, .5], [.5, 1]])
X2 = dot(X1, A)
plot(X2[:, 0], X2[:, 1], "o");

# Multiplying by the inverse of matrix A will undue the
# linear transformation of X that was obtained by multiplying by A
Ainv = inv(A)
X1b = dot(X2, Ainv)
plot(X1b[:, 0], X1b[:, 1], "o");

# We can check this assertion formally in Python with the caveat that there
# is some very small numerical rounding errors.
assert all(X1 - X1b < 1e-5), "Matrix 1 does not equal matrix 2"

# We can also get built-in assertion with consideration of floating point precision
from numpy.testing import assert_array_almost_equal
assert_array_almost_equal(X1, X1b)

# Another way to say this is that the matrix obtained by multiplying A with
# its inverse is a matrix that will not change the values of X. This matrix
# is known as the identity matrix and contains 1s on the diagonal and 0s in
# every other entry.
I = dot(A, inv(A))
assert all(I == eye(I.shape[0]))

# Fabricate a dataset with 4 variables
X = randn(100, 4)
# Fabricate a variable y that depends on these four variables and some noise
noise = randn(100) * 10
y = 1 * X[:, 0] + 7 * X[:, 1] + 3 * X[:, 2] + 5 * X[:, 3] + 7 + noise

# To capture the constant term, we will add a column of 1s to our regressor matrix
X = column_stack((X, ones(100)))

# Fit the model based on the ordinary last squares (OLS) formula
w_ols = dot(dot(inv(dot(X.T, X)), X.T), y) 

# Note how the lack of builtin matrix multiplication for arrays is a bit annoying
# We can also use matrix objects
X_mtx = asmatrix(X)
y_mtx = asmatrix(y).T
w_ols2 = inv(X_mtx.T * X_mtx) * X_mtx.T * y_mtx

# We see these are the same (once we account for the 2D nature of the matrix
assert_array_almost_equal(w_ols.reshape(w_ols2.shape), w_ols2)

# Use numpy's lstsq function to fit the model
# lstsq returns a 4-tuple
w_lstsq, residue, rnk, s = lstsq(X, y)

# You can also do
w_lstsq = lstsq(X, y)[0]

# If you are following the MATLAB tutorial, note that the argument order for lstsq is backward relative to regress

# These are also identical
assert_array_almost_equal(w_ols, w_lstsq)

# First we compute our models prediction
modelprediction = dot(X, w_ols)

# Visualize this prediction by plotting it against our data
# The imperfections arise from the noise we added to the data
plot(modelprediction, y, "o", color=colors[1])
xlabel("model prediction")
ylabel("original data");

# Then we subract the model prediction from the measured data, square that difference and take the mean
mse_ols = mean((y - modelprediction) ** 2)
print ("Our mean squared error is %.4f using ordinary least squares regression" % mse_ols)

# Various solvers live in the optimize package
from scipy import optimize

# Define an anonymous function that returns the mean squared error between our data
# and the result of multiplying the predictor matrix by a weight vector
costfunc = lambda w: mean(square(y - dot(X, w)))

# Start the search with all weights at 0
seed = zeros(5)

# Fit the model by searching over a space of cost function values and finding the lowest
# Set the limit on function evaluations to infinity
optsol = optimize.fmin(costfunc, seed, maxfun=inf)

axes(aspect="equal")
plot(w_ols, optsol, "D", color=colors[2], markersize=7)
xlabel("OLS solution")
ylabel("Optimize solution");

mse_optim = mean(square(y - dot(X, optsol)))
print ("OLS MSE: %.4f" % mse_ols)
print ("Optimized MSE: %.4f " % mse_optim)

os.system("pause")

