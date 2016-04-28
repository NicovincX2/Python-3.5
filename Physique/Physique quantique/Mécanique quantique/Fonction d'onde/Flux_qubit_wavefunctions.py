# -*- coding: utf-8 -*-

import os
from scipy import *
import sys
from wavefunction import *

#
# Define how many states should be calculated
# truncate infinite series to [-N,N]
N = 5; 
nstates = 2*N+1

## 
# Costants
#
h = 6.626e-34
h_ = h/(2*pi)
e = 1.602e-19
phi0 = h/(2*e)

Ej = 1.0   # unit
#Cj = 1
#Ec = e**2/(2*Cj)
alpha = 0.8

#Ej = 40 * Ec
Ec = Ej/40.0
Cj = e**2/(2*Ec)

Mp = 2*Cj*(phi0/(2*pi))**2
Mm = Mp * (1+2*alpha)

fi = 0.45
ff = 0.55
fs = 0.001

#
# Range of flux
#
F = arange(fi, ff, fs) # 0.49:0.0001:0.51;
idx = 0 

##
# Set up vectors and matrices
#
k = arange(-N,N+1) #-N:N;
l = arange(-N,N+1) #-N:N;
bp = h_**2 * k**2 / (2*Mp);
bm = h_**2 * l**2 / (2*Mm);
Bp = diag(bp);
Bm = diag(bm);
I = eye(nstates);

# Construct M
M0 = zeros((nstates**2,nstates**2), dtype=complex)
# B^{p}C term
M0 = M0 + recastMtoT(nstates, Bp, I);
# CB^{m} term
M0 = M0 + recastMtoT(nstates, I, Bm);
# E_{J}(2-alpha)C term
M0 = M0 + Ej*(2+alpha)*recastMtoT(nstates, I, I);
# Ej/2 * D^{(-1,0)}CD^{(0,-1)} term
M0 = M0 - Ej/2*recastMtoT(nstates, kd(nstates,-1,0), kd(nstates,0,-1));
# Ej/2 * D^{(-1,0)}CD^{(0,+1)} term
M0 = M0 - Ej/2*recastMtoT(nstates, kd(nstates,-1,0), kd(nstates,0,+1));
# Ej/2 * D^{(+1,0)}CD^{(0,-1)} term
M0 = M0 - Ej/2*recastMtoT(nstates, kd(nstates,+1,0), kd(nstates,0,-1));
# Ej/2 * D^{(+1,0)}CD^{(0,+1)} term
M0 = M0 - Ej/2*recastMtoT(nstates, kd(nstates,+1,0), kd(nstates,0,+1));

E = zeros((len(F), nstates**2)).astype(float)
t01 = zeros(len(F)).astype(float)
t02 = zeros(len(F)).astype(float)
t03 = zeros(len(F)).astype(float)
t12 = zeros(len(F)).astype(float)
t13 = zeros(len(F)).astype(float)
t23 = zeros(len(F)).astype(float)


kdp1 = kdp(nstates, 2)+kdp(nstates, -2)
kdp2 = kdp(nstates, 2)-kdp(nstates, -2)

M1 = recastMtoT(nstates, I, kd(nstates,0,-2))
M2 = recastMtoT(nstates, I, kd(nstates,0,+2))


for f in F:

    # alpha * Ej/2 * cos(2*pi*f)* C D^{(0,-2)} term
    M = M0 - (alpha*Ej/2*cos(2*pi*f) + sqrt(-1) * alpha*Ej/2*sin(2*pi*f))* M1;
    # alpha * Ej/2 * cos(2*pi*f)* C D^{(0,+2)} term
    M = M - (alpha*Ej/2*cos(2*pi*f) - sqrt(-1) * alpha*Ej/2*sin(2*pi*f))* M2;
    # alpha * Ej/2 * cos(2*pi*f)* C D^{(0,-2)} term
    ##M = M - sqrt(-1) * alpha*Ej/2*sin(2*pi*f) * recastMtoT(nstates, I, kd(nstates,0,-2));
    # alpha * Ej/2 * cos(2*pi*f)* C D^{(0,+2)} term
    ##M = M + sqrt(-1) * alpha*Ej/2*sin(2*pi*f) * recastMtoT(nstates, I, kd(nstates,0,+2));

    # Solve EVP: Mx=Ex
    eval, evec = eigenvectors_sorted(M)
    #eval, evec = solve_eigenproblem(M)
    
    #S(:,:,idx) = V;
    E[idx][:] = transpose(eval)

    # Calc transition elements for driving operator O
    phia0 = 0.15*phi0;
    O = -2*pi*alpha*Ej * phia0/phi0 * (sin(2*pi*f)/2 * kdp1 + cos(2*pi*f)/(2*1j) * kdp2);

    c0 = evec[0,:]
    c1 = evec[3,:]
    c2 = evec[4,:]
    c3 = evec[7,:]

    t01[idx] = abs(dot(conj(c0), dot(O, c1)))
    t02[idx] = abs(dot(conj(c0), dot(O, c2)))
    t03[idx] = abs(dot(conj(c0), dot(O, c3)))
    t12[idx] = abs(dot(conj(c1), dot(O, c2)))
    t13[idx] = abs(dot(conj(c1), dot(O, c3)))
    t23[idx] = abs(dot(conj(c2), dot(O, c3)))

    idx = idx + 1;

fig, ax = subplots(1, 1, figsize=(12,10))

for idx in [0, 3, 4, 7, 9, 10]:
    ax.plot(F, E[:,idx])

fig, ax = subplots(1, 1, figsize=(12,10))

for idx in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
    ax.plot(F, E[:,idx])

fig, ax = subplots(1, 1, figsize=(12,10))

ax.plot(F, t01, label='t01')
ax.plot(F, t02, label='t02')
ax.plot(F, t03, label='t03')
ax.plot(F, t12, label='t12')
ax.plot(F, t13, label='t13')
ax.plot(F, t23, label='t23')

ax.legend();

os.system("pause")

