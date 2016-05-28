# -*- coding: utf-8 -*-

import os
import matplotlib.pyplot as plt

plt.jet()  # set the color map. When your colors are lost, re-run this.

import sklearn.datasets as datasets

X, Y = datasets.make_blobs(centers=4, cluster_std=0.5, random_state=0)

plt.scatter(X[:, 0], X[:, 1])
plt.scatter(X[:, 0], X[:, 1], c=Y)

from sklearn.cluster import KMeans

kmeans = KMeans(4, random_state=8)
Y_hat = kmeans.fit(X).labels_

plt.scatter(X[:, 0], X[:, 1], c=Y_hat)
plt.scatter(X[:, 0], X[:, 1], c=Y_hat, alpha=0.4)
mu = kmeans.cluster_centers_
plt.scatter(mu[:, 0], mu[:, 1], s=100, c=np.unique(Y_hat))
print(mu)

from sklearn.datasets import fetch_mldata
from sklearn.cluster import KMeans
from sklearn.utils import shuffle
X_digits, _, _, Y_digits = fetch_mldata(
    "MNIST Original").values()  # fetch dataset from internet
# shuffle dataset (which is ordered!)
X_digits, Y_digits = shuffle(X_digits, Y_digits)
# take only the last instances, to shorten runtime of KMeans
X_digits = X_digits[-5000:]

plt.rc("image", cmap="binary")  # use black/white palette for plotting
for i in xrange(10):
    plt.subplot(2, 5, i + 1)
    plt.imshow(X_digits[i].reshape(28, 28))
    plt.xticks(())
    plt.yticks(())
plt.tight_layout()

kmeans = KMeans(20)
mu_digits = kmeans.fit(X_digits).cluster_centers_

plt.figure(figsize=(16, 6))
for i in xrange(2 * (mu_digits.shape[0] / 2)):  # loop over all means
    plt.subplot(2, mu_digits.shape[0] / 2, i + 1)
    plt.imshow(mu_digits[i].reshape(28, 28))
    plt.xticks(())
    plt.yticks(())
plt.tight_layout()

os.system("pause")
