# -*- coding: utf-8 -*-

import os
import numpy as np
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def mle_gauss_mu(samples):
    """
    Calculates the Maximum Likelihood Estimate for a mean vector
    from a multivariate Gaussian distribution.
    
    Keyword arguments:
        samples (numpy array): Training samples for the MLE.
            Every sample point represents a row; dimensions by column.
            
    Returns a row vector (numpy.array) as the MLE mean estimate.
    
    """
    dimensions = samples.shape[1]
    mu_est = np.zeros((dimensions,1))
    for dim in range(dimensions):
        mu_est = np.zeros((dimensions,1))
        col_mean = sum(samples[:,dim])/len(samples[:,dim])
        mu_est[dim] = col_mean
    return mu_est

def mle_gausscov(samples, mu_est):
    """
    Calculates the Maximum Likelihood Estimate for the covariance matrix.
    
    Keyword Arguments:
        x_samples: np.array of the samples for 1 class, n x d dimensional 
        mu_est: np.array of the mean MLE, d x 1 dimensional
        
    Returns the MLE for the covariance matrix as d x d numpy array.
    
    """
    dimensions = samples.shape[1]
    assert (dimensions == mu_est.shape[0]), "columns of sample set and rows of'\
                'mu vector (i.e., dimensions) must be equal."
    cov_est = np.zeros((dimensions,dimensions))
    for x_vec in samples:
        x_vec = x_vec.reshape(dimensions,1)
        cov_est += (x_vec - mu_est).dot((x_vec - mu_est).T)
    return cov_est / len(samples)

# true parameters and 100 3D training data points

mu_vec = np.array([[0],[0]])
cov_mat = np.eye(2)

multi_gauss = np.random.multivariate_normal(mu_vec.ravel(), cov_mat, 100)
print('Dimensions: {}x{}'.format(multi_gauss.shape[0], multi_gauss.shape[1]))

import prettytable

# mean estimate
mu_mle = mle_gauss_mu(multi_gauss)
mu_mle_comp = prettytable.PrettyTable(["mu", "true_param", "MLE_param"])
mu_mle_comp.add_row(["",mu_vec, mu_mle])
print(mu_mle_comp)

# covariance estimate
cov_mle = mle_gausscov(multi_gauss, mu_mle)
mle_gausscov_comp = prettytable.PrettyTable(["covariance", "true_param", "MLE_param"])
mle_gausscov_comp.add_row(["",cov_mat, cov_mle])
print(mle_gausscov_comp)

### Implementing the Multivariate Gaussian Density Function

def pdf_multivariate_gauss(x, mu, cov):
    """
    Caculate the multivariate normal density (pdf)

    Keyword arguments:
        x = numpy array of a "d x 1" sample vector
        mu = numpy array of a "d x 1" mean vector
        cov = "numpy array of a d x d" covariance matrix
        
    """
    assert(mu.shape[0] > mu.shape[1]), 'mu must be a row vector'
    assert(x.shape[0] > x.shape[1]), 'x must be a row vector'
    assert(cov.shape[0] == cov.shape[1]), 'covariance matrix must be square'
    assert(mu.shape[0] == cov.shape[0]), 'cov_mat and mu_vec must have the same dimensions'
    assert(mu.shape[0] == x.shape[0]), 'mu and x must have the same dimensions'
    part1 = 1 / ( ((2* np.pi)**(len(mu)/2)) * (np.linalg.det(cov)**(1/2)) )
    part2 = (-1/2) * ((x-mu).T.dot(np.linalg.inv(cov))).dot((x-mu))
    return float(part1 * np.exp(part2))

Z_true.shape

# Plot Probability Density Function
from matplotlib import pyplot as plt

fig = plt.figure(figsize=(9, 9))
ax = fig.gca(projection='3d')

X = np.linspace(-5, 5, 100)
Y = np.linspace(-5, 5, 100)
X,Y = np.meshgrid(X,Y)

Z_mle = []
for i,j in zip(X.ravel(),Y.ravel()):
    Z_mle.append(pdf_multivariate_gauss(np.array([[i],[j]]), mu_mle, cov_mle))
Z_mle = np.asarray(Z_mle).reshape(len(Z_mle)**0.5, len(Z_mle)**0.5)   
surf = ax.plot_wireframe(X, Y, Z_mle, color='red', rstride=2, cstride=2, alpha=0.3, label='MLE')

Z_true = []
for i,j in zip(X.ravel(),Y.ravel()):
    Z_true.append(pdf_multivariate_gauss(np.array([[i],[j]]), mu_vec, cov_mat))
Z_true = np.asarray(Z_true).reshape(len(Z_true)**0.5, len(Z_true)**0.5)
surf = ax.plot_wireframe(X, Y, Z_true, color='green', rstride=2, cstride=2, alpha=0.3, label='true param.')

ax.set_zlim(0, 0.2)
ax.zaxis.set_major_locator(plt.LinearLocator(10))
ax.zaxis.set_major_formatter(plt.FormatStrFormatter('%.02f'))
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('p(x)')
ax.legend()

plt.title('True vs. Predicted Gaussian densities')

plt.show()

os.system("pause")