# -*- coding: utf-8 -*-

import os
from scipy import *
from scipy import optimize
from wavefunction import *
from wavefunction.wavefunction1d import *

h = 6.626e-34
h_ = h/(2*pi)
e = 1.602e-19
Phi0 = h / (2 * e)
cf = h_

Ic = 1.7e-6
Cj = 700e-15
L = 0.72e-9

mm = Cj * (Phi0/(2*pi))**2 * cf
beta = 2*pi*L*Ic / Phi0
Ej = Phi0/(2*pi) * Ic / cf

phi = 5.0;
gamma = phi / beta;

args = {'Ej': Ej, 'beta': beta, 'gamma': gamma}

k = -h_ ** 2 / (2 * mm)

x_min = -0.7*pi
x_max =  4*pi
N = 750 

def U_flux_biased(x, args):
    """
    Flux-biased phase qubit potential
    """
    Ej = args['Ej']
    beta = args['beta']
    gamma = args['gamma']
    
    u = -Ej * (cos(x) - 1 / (2 * beta) * x ** 2 + gamma * x)
    
    return u

x = linspace(x_min, x_max, N)

U = U_flux_biased(x, args)

x_opt_min = optimize.fmin(U_flux_biased, 0.5, (args,))
print("\nFound dmin = %f " % x_opt_min)

x_opt_max = optimize.fmin(lambda x, args: -U_flux_biased(x, args), [2.5], (args,))
print("\nFound dmax = %f" % x_opt_max)

U_min = U_flux_biased(x_opt_min, args)
U_max = U_flux_biased(x_opt_max, args)

dU = U_max - U_min
dx = x_opt_max - x_opt_min

print("Barrier: dU = %f" % (dU / Ej))

fig, ax = subplots()

ax.plot(x, U/Ej)
ax.plot(x_opt_min, U_flux_biased(x_opt_min, args) / Ej, 'o')

#ax.set_ylim(-1.55, -1.5)
#ax.set_xlim(0.8,2.2)
ax.set_xlabel(r'$x$', fontsize=18)
ax.set_ylabel(r'$U(x)/E_J$', fontsize=18);

fig, ax = subplots()

ax.plot(x, U/Ej)
ax.plot(x_opt_min, U_flux_biased(x_opt_min, args) / Ej, 'o')

ax.set_ylim(-2, -1.6)
ax.set_xlim(0.5, 3.0)
ax.set_xlabel(r'$x$', fontsize=18)
ax.set_ylabel(r'$U(x)/E_J$', fontsize=18);

u = assemble_u_potential(N, U_flux_biased, x, args)

K = assemble_K(N, k, x_min, x_max)

V = assemble_V(N, u, x_min, x_max)

H = K + V

evals, evecs = solve_eigenproblem(H)

nbound = 0
boundidx = []

for i in range(0,N):
    if evals[i] > U_min - 0.5 * dU and evals[i] < U_max + 0.5 * dU:
        if inner(evecs[i] * (x_opt_min-dx < x) * (x < x_opt_max), evecs[i]) > 0.95:
            nbound = nbound + 1
            boundidx.append(i)

print ("Found bound states: ", boundidx)

NN = len(boundidx)

fig, axes = subplots(NN, 1, figsize=(10, NN * 1), sharex=True, sharey=True)

for n, m in enumerate(boundidx):
    axes[n].plot(x, real(evecs[m]))

axes[n].set_xlim(0.5, 2.5)
axes[n].set_xlabel(r'$x$', fontsize=18)

fig.tight_layout();

fig, ax = subplots(figsize=(12,8))

ax.plot(x, U/Ej, 'k')
ax.plot(x_opt_min, U_flux_biased(x_opt_min, args) / Ej, '.')

for n, m in enumerate(boundidx):
    Y0 = evals[m]/Ej * ones(shape(x))
    Y = 0.01 * evecs[m] + Y0

    ax.plot(x, Y0.real, 'k--')
    ax.plot(x, Y.real)
    
ax.set_ylim(-1.8, -1.7)
ax.set_xlim(0.5,3.0)
ax.set_xlabel(r'$x$', fontsize=18)
ax.set_ylabel(r'$U(x)$', fontsize=18);

inner_prod = zeros((len(boundidx), len(boundidx))).astype(np.complex)
expect_pos = zeros((len(boundidx), len(boundidx))).astype(np.complex)
expect_kin = zeros((len(boundidx), len(boundidx))).astype(np.complex)

for i, l in enumerate(boundidx):
    for j, k in enumerate(boundidx):
    
        psi_l = wavefunction_normalize(x, evecs[l])
        psi_k = wavefunction_normalize(x, evecs[k])
    
        inner_prod[i,j] = inner_product(x, psi_l, psi_k)                 # <psi_l|psi_k>
        expect_pos[i,j] = inner_product(x, psi_l, x * psi_k)             # <psi_l|x|psi_k>
        expect_kin[i,j] = inner_product(x, psi_l, derivative(x, psi_k))  # <psi_l|p|psi_k>

print ("Bound energy-levels:")
real((evals[boundidx] - evals[boundidx[0]]) / (evals[boundidx[1]]-evals[boundidx[0]]))

print ("inner_prod:\n")
print_matrix(inner_prod)

print ("expect_pos:\n")
print_matrix(expect_pos)

print ("expect_kin:\n")
print_matrix(expect_kin)

os.system("pause")

