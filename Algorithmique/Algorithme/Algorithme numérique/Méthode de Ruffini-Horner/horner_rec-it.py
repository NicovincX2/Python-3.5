# -*- coding: utf-8 -*-

import os


def horner_r(P, t):
    assert P != [], "Poly vide ?!"

    def parcours(Q, bi):
        if Q == []:
            return bi
        return parcours(Q[:-1], Q[-1] + t * bi)
    return parcours(P, 0)


def horner(P, t):
    n = len(P)
    assert n != 0, "Poly vide ?!"
    bi = 0
    for k in range(n - 1, -1, -1):
        bi = P[k] + t * bi
    return bi


def liste_horner_r(P, t):
    assert P != [], "Poly vide ?!"

    def parcours(Q, bi, acc_bi):
        if Q == []:
            return acc_bi
        bj = Q[-1] + t * bi
        return parcours(Q[:-1], bj, [bj] + acc_bi)
    return parcours(P, 0, [])


def liste_horner(P, t):
    n = len(P)
    assert n != 0, "Poly vide ?!"
    bi = 0
    poly_bi = []
    for k in range(n - 1, -1, -1):
        bi = P[k] + t * bi
        poly_bi = [bi] + poly_bi
    return poly_bi


def jeme_poly(P, j, t):
    n = j + 2
    c = len(P) + 1
    M = [[0 for k in range(c)] for k in range(n)]
    M[0] = [0] + P
    fac = 1
    for i in range(1, n):
        for j in range(c - 1 - i, -1, -1):
            M[i][j] = M[i - 1][j + 1] + t * M[i][j + 1]
        M[i][0] *= fac
        fac *= i
    return M[n - 1][0]


def reste(P, t):
    return horner(P, t)


def quotient(P, t):
    return liste_horner(P, t)[1:]


def jeme_poly_r(P, j, t):
    H = liste_horner(P, t)
    if j == 0:
        return H[0]
    return j * jeme_poly_r(H[1:], j - 1, t)

os.system("pause")
