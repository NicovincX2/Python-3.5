# -*- coding: utf-8 -*-

import os
import numpy as np
from matplotlib import pyplot as plt


def comp_theta_mle(d):
    """
    Computes the Maximum Likelihood Estimate for a given 1D training
    dataset for a Rayleigh distribution.

    """
    theta = len(d) / sum([x**2 for x in d])
    return theta


def likelihood_ray(x, theta):
    """
    Computes the class-conditional probability for an univariate
    Rayleigh distribution

    """
    return 2 * theta * x * np.exp(-theta * (x**2))

training_data = [12, 17, 20, 24, 25, 30, 32, 50]

theta = comp_theta_mle(training_data)

print("Theta MLE:", theta)

# Plot Probability Density Function
from matplotlib import pyplot as plt

x_range = np.arange(0, 150, 0.1)
y_range = [likelihood_ray(x, theta) for x in x_range]

plt.figure(figsize=(10, 8))
plt.plot(x_range, y_range, lw=2)
plt.title('Probability density function for the Rayleigh distribution')
plt.ylabel('p(x|theta)')

ftext = 'theta = {:.5f}'.format(theta)
plt.figtext(.15, .8, ftext, fontsize=11, ha='left')


plt.ylim([0, 0.04])
plt.xlim([0, 120])
plt.xlabel('random variable x')

plt.show()

os.system("pause")
