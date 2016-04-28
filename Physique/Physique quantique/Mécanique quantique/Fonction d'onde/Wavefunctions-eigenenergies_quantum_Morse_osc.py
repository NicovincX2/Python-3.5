# -*- coding: utf-8 -*-

import os
from scipy import *
from scipy import optimize
from wavefunction import *
from wavefunction.wavefunction1d import *

h = 6.626e-34
h = 1
h_ = h/(2*pi)
e = 1.602e-19
cf = 1          # if cf = h_, use units where h_ = 1

mm = 1          # oscillator mass
omega = 2 * pi  # oscillator frequency in GHz
x0 = 0          # shift in oscillator potiential minimum

D = 5.0
b = 0.5

args = {'D': D, 'b': b}

k = -h_ ** 2 / (2 * mm)

x_min = -pi
x_max =  pi
N = 750 

def U_morse(x, args):
    """
    Morse oscillator potential
    """
    
    D = args['D']
    b = args['b']
    
    u = D * (1 - exp(-b*x)) ** 2

    return u

x = linspace(x_min, x_max, N)
U = U_morse(x, args);
x_opt_min = optimize.fmin(U_morse, [0.0], (args,))

print("Found potential minima at = %f" % x_opt_min)

fig, ax = subplots()

ax.plot(x, U)
ax.plot(x_opt_min, U_morse(x_opt_min, args), 'o')

#ax.set_ylim(-10, 80)
ax.set_xlabel(r'$x$', fontsize=18)
ax.set_ylabel(r'$U(x)$', fontsize=18);

u = assemble_u_potential(N, U_morse, x, args)

K = assemble_K(N, k, x_min, x_max)

V = assemble_V(N, u, x_min, x_max)

H = K + V

evals, evecs = solve_eigenproblem(H)
NN = 10

fig, axes = subplots(NN, 1, figsize=(10,NN*1), sharex=True, sharey=True)

for n in range(NN):
    Y = evecs[NN-n-1]
    axes[n].plot(x, Y.real)

axes[n].set_xlabel(r'$x$', fontsize=18);

fig, ax = subplots(figsize=(12,8))

ax.plot(x, U, 'k')
for n in range(10):
    Y = evals[n] + evecs[n]

    mask = where(Y > U)    
    ax.plot(x[mask], evals[n] * ones(shape(x))[mask], 'k--')

    mask = where(Y > U-2.0)
    ax.plot(x[mask], Y[mask].real)
    
ax.set_xlim(-2, 4)
ax.set_ylim(0, 4)
ax.set_xlabel(r'$x$', fontsize=18)
ax.set_ylabel(r'$U(x)$', fontsize=18);

nbound = 0
boundidx = []

for i in range(0,N):
    if nbound < 10: 
        if inner(evecs[i], evecs[i]) > 0.85:
            nbound = nbound + 1
        boundidx.append(i)
            
print "Found bound states: ", boundidx

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

print "inner_prod:\n"
print_matrix(inner_prod)

print "expect_pos ="
print2DMatrix(expect_pos)

print "expect_kin:\n"
print_matrix(expect_kin)

print "eigenenergies = " 
print evals[0:nbound].real

os.system("pause")

