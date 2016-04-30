# -*- coding: utf-8 -*-

import os
import matplotlib.pyplot as plt
import moss
import seaborn
seaborn.set()
colors = seaborn.color_palette()

# Generate two random predictors
X = randn(100, 2)
# Create y as a weighted sum of the 2 predictors and noise
noise = randn(100)
y = 0.7 * X[:, 0] + 0.5 * X[:, 1] + noise
# Threshold y so that it is a binary classification.  Let's pretend this is
# medical data and 0 means the patient died and 1 means the patient lived.
# x1 and x2 are measures of symptoms
y = (y > 0).astype(int)

plot(X[y == 0, 0], X[y == 0, 1], "o", label="dead")
plot(X[y == 1, 0], X[y == 1, 1], "o", color=colors[2], label="alive")
legend();

from sklearn.linear_model import LogisticRegression
model = LogisticRegression().fit(X, y)

# We can call the predict() method of the model to get estimated values
y_hat = model.predict(X)

# To be closer to the matlab tutorial, you can also use the predict_proba() method
# to return probabilistc estimates in favor of each class
y_hat2 = argmax(model.predict_proba(X), axis=1)

assert all(y_hat == y_hat2)

a_c = logical_and(y == 1, y_hat == 1)
a_i = logical_and(y == 1, y_hat == 0)
d_c = logical_and(y == 0, y_hat == 0)
d_i = logical_and(y == 0, y_hat == 1)
plot(X[d_c, 0], X[d_c, 1], "o", color=colors[0], label="dead +")
plot(X[d_i, 0], X[d_i, 1], "o", color=colors[0], alpha=0.7, label="dead -")
plot(X[a_c, 0], X[a_c, 1], "o", color=colors[2], label="alive +")
plot(X[a_i, 0], X[a_i, 1], "o", color=colors[2], alpha=0.7, label="alive -")
legend();

# Define a function to generate fake data
def make_dataset():
    X = randn(100, 2)
    noise = randn(100)
    y = 0.7 * X[:, 0] + 0.5 * X[:, 1] + noise
    y = (y > 0).astype(int)
    return X, y

# Make two datasets as above
X1, y1 = make_dataset()
X2, y2 = make_dataset()

# Fit the linear model
line = LogisticRegression().fit(X1, y1)
# Add additional columns where the predictors are squared
X1_quad = hstack((X, X ** 2))
from sklearn.preprocessing import scale
X1_quad = scale(X1_quad)

# Predict with the line and quad models
line_model = LogisticRegression().fit(X1, y1)
yhat_line1 = line_model.predict(X1)
quad_model = LogisticRegression().fit(X1_quad, y1)
yhat_quad1 = quad_model.predict(X1_quad)

# Plot the models and estimates
figure(figsize=(12, 5))
# Plot the actual classes of Y1
subplot(121)
plot(X1[y1==0, 0], X1[y1==0, 1], "o", color=colors[0], markersize=15)
plot(X1[y1==1, 0], X1[y1==1, 1], "o", color=colors[2], markersize=15)

# Plot the predicted classs from the linear model
plot(X1[yhat_line1==0, 0], X1[yhat_line1==0, 1], "o", color=colors[0], markersize=7)
plot(X1[yhat_line1==1, 0], X1[yhat_line1==1, 1], "o", color=colors[2], markersize=7)

# Now do the same for the quadratic model
subplot(122)
plot(X1[y1==0, 0], X1[y1==0, 1], "o", color=colors[0], markersize=15)
plot(X1[y1==1, 0], X1[y1==1, 1], "o", color=colors[2], markersize=15)

# Plot the predicted classs from the linear model
plot(X1[yhat_quad1==0, 0], X1[yhat_quad1==0, 1], "o", color=colors[0], markersize=7)
plot(X1[yhat_quad1==1, 0], X1[yhat_quad1==1, 1], "o", color=colors[2], markersize=7)

# Compute the accuracy for each model
acc_line = line_model.score(X1, y1)
acc_quad = quad_model.score(X1_quad, y1)
print ("Linear: %.2f" % acc_line)
print ("Quadratic: %.2f" % acc_quad)

line_cv_acc = line_model.score(X2, y2)
X2_quad = scale(hstack((X2, X2 ** 2)))
quad_cv_acc = quad_model.score(X2_quad, y2)
print ("Linear model cross-validated accuracy: %.2f" % line_cv_acc)
print ("Quadratic model cross-validated accuracy: %.2f" % quad_cv_acc)

os.system("pause")

