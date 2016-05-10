# -*- coding: utf-8 -*-

import os

def poisson_theta_mle(d):
    """
    Computes the Maximum Likelihood Estimate for a given 1D training
    dataset from a Poisson distribution.
    
    """
    return sum(d) / len(d)
    
import math

def likelihood_poisson(x, lam):
    """
    Computes the class-conditional probability for an univariate
    Poisson distribution
    
    """
    if x // 1 != x:
        likelihood = 0
    else:
        likelihood = math.e**(-lam) * lam**(x) / math.factorial(x)
    return likelihood
    
# Drawing training data

import numpy as np

true_param = 1.0
poisson_data = np.random.poisson(lam=true_param, size=100)

mle_poiss = poisson_theta_mle(poisson_data)

print('MLE:', mle_poiss)

# Plot Probability Density Function
from matplotlib import pyplot as plt
    
x_range = np.arange(0, 5, 0.1)
y_true = [likelihood_poisson(x, true_param) for x in x_range]
y_mle = [likelihood_poisson(x, mle_poiss) for x in x_range]

plt.figure(figsize=(10,8))
plt.plot(x_range, y_true, lw=2, alpha=0.5, linestyle='--', label='true parameter ($\lambda={}$)'.format(true_param))
plt.plot(x_range, y_mle, lw=2, alpha=0.5, label='MLE ($\lambda={}$)'.format(mle_poiss))
plt.title('Poisson probability density function for the true and estimated parameters')
plt.ylabel('p(x|theta)')
plt.xlim([-1,5])
plt.xlabel('random variable x')
plt.legend()

plt.show()

os.system("pause")