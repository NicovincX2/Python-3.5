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
cf = 1

ceta = 0.05
J = 0.9725
Ic = 13.3e-6
Ib = J * Ic
Cj = 4.3e-12

mm = Cj * (1 + ceta) * (Phi0/(2*pi))**2 * cf
Ej = Phi0/(2*pi) * Ic / cf

args = {'Ej': Ej, 'Ic': Ic, 'Ib': Ib}

k = -h_ ** 2 / (2 * mm)

x_min = -pi
x_max =  pi
N = 750 

def U_current_biased(x, args):
    """
    Potential for a current-biased phase qubit potential
    (the washboard potential)
    """
    Ej = args['Ej']
    Ic = args['Ic']
    Ib = args['Ib']

    u = - Ej * (cos(x) + Ib / Ic * x)

    return u

x = linspace(x_min, x_max, N)

U = U_current_biased(x, args)

# analytical formula for minima points of potential
x_opt_min = arcsin(Ib/Ic)
print("x_opt_min = %f " % x_opt_min)

x_opt_max = -math.asin(Ib/Ic) + pi
print("x_opt_max = %f" % x_opt_max)

U_min = U_current_biased(x_opt_min, args)
U_max = U_current_biased(x_opt_max, args)
dU = U_max - U_min
dx = x_opt_max - x_opt_min

print("dU = %f" % dU)

fig, ax = subplots()

ax.plot(x, U/Ej)
ax.plot(x_opt_min, U_current_biased(x_opt_min, args) / Ej, 'o')

ax.set_ylim(-1.55, -1.5)
ax.set_xlim(0.8,2.2)
ax.set_xlabel(r'$x$', fontsize=18)
ax.set_ylabel(r'$U(x)/E_J$', fontsize=18);

u = assemble_u_potential(N, U_current_biased, x, args)

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
ax.plot(x_opt_min, U_current_biased(x_opt_min, args) / Ej, '.')

for n, m in enumerate(boundidx):
    Y0 = evals[m]/Ej * ones(shape(x))
    Y = 0.001 * evecs[m] + Y0

    ax.plot(x, Y0.real, 'k--')
    ax.plot(x, Y.real)
    
ax.set_ylim(-1.535, -1.52)
ax.set_xlim(0.8,2.2)
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

print("Bound energy-levels:")
(evals[boundidx] - evals[boundidx[0]]).real / Ej

print("Harmonicity:")
((evals[boundidx] - evals[boundidx[0]]) / (evals[boundidx[1]]-evals[boundidx[0]])).real

print ("inner_prod:\n")
print_matrix(inner_prod)

print ("expect_pos:\n")
print_matrix(expect_pos)

print ("expect_kin:\n")
print_matrix(expect_kin)

os.system("pause")

