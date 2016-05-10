# -*- coding: utf-8 -*-

import os
import numpy 
import math
from matplotlib import pyplot

# constants
g = 9.81
l = 1.0

def simulate_pendulum(phi_init, omega_init, numSteps, deltaT):
    t = numpy.zeros(numSteps)

    phi = numpy.zeros(numSteps)
    phi[0] = phi_init

    omega = numpy.zeros(numSteps)
    omega[0] = omega_init

    for n in range(1,numSteps):
        t[n] = deltaT * n # store the time for plotting.

        alpha_t = -(g/l) * math.sin(phi[n-1])
        omega_t = omega[n-1] + (delta_t * alpha_t)
        phi_t = phi[n-1] + (delta_t * omega_t)
        omega[n] = omega_t
        phi[n] = phi_t

    return (t, phi, omega)

# initial conditions
phi_0 = math.pi / 6.  # initial angle
omega_0  = 0.         # pendulum initially at rest

N = 1000              # time steps to run the simulation for
delta_t = 0.01        # simulation step size

(t, phi, omega) = simulate_pendulum(phi_0, omega_0, N, delta_t)

pyplot.figure(figsize=(10,4))
pyplot.xlabel('t', fontsize=14)
pyplot.ylabel(r'$\phi$', fontsize=14)
pyplot.hold(True)
pyplot.plot(t, phi)

os.system("pause")