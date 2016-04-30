# -*- coding: utf-8 -*-

import os
import seaborn

seaborn.set()
colors = seaborn.color_palette()

import utils

# For 3D plotting we need to import some extra stuff
from mpl_toolkits.mplot3d import Axes3D

# First create two random vectors in 3 dimensional space
v1 = rand(3, 1)
v2 = rand(3, 1)

# And scale them to unit length
v1 = v1 / norm(v1)
v2 = v2 / norm(v2) 

# Plot the vectors
o = zeros(3) # origin

# We'll use the object oriented plotting interface
f = figure(figsize=(8, 8))
ax = f.add_subplot(111, projection="3d", axisbg="white")
ax.plot(*[[o[i], v1[i]] for i in range(3)], linewidth=3, label="vector1")
ax.plot(*[[o[i], v2[i]] for i in range(3)], linewidth=3, label="vector2")
for axisl in ["x", "y", "z"]:
    getattr(ax, "set_%slabel" % axisl)(axisl)  # Here's a fun trick
legend();

f = figure(figsize=(8, 8))
ax = f.add_subplot(111, projection="3d", axisbg="white")
ax.plot(*[[o[i], v1[i]] for i in range(3)], linewidth=3, label="vector1")
ax.plot(*[[o[i], v2[i]] for i in range(3)], linewidth=3, label="vector2")
for axisl in ["x", "y", "z"]:
    getattr(ax, "set_%slabel" % axisl)(axisl)  # Here's a fun trick
legend()

for i in range(100):
    # generate a point that is a weighted sum of the 2 vectors
    w1 = randn(1)
    w2 = randn(1)
    point = w1 * v1 + w2 * v2
    ax.plot(*point, marker=".", color="k")

# We can find a vector that is orthogonal to the plane defined by v1 and v2
# by taking the vector cross product.  See the wikipedia page for a
# definition of cross product
v3 = cross(v1.reshape(1, 3), v2.reshape(1, 3)).squeeze()  # Must be right shape for cross()
ax.plot(*[[o[i], v3[i]] for i in range(3)], linewidth=3, label="orthogonal vector")
legend();

print (v3[0] * v1[0] + v3[1] * v1[1] + v3[2] * v1[2])
print (dot(v3, v1))

theta = arccos(dot(v2.T, v1)).squeeze()
# and radians can be converted to degrees
theta_deg = theta * (180 / pi)
print (theta, theta_deg)

os.system("pause")

