# -*- coding: utf-8 -*-

import os


def subdivision(msg):
    n = len(msg)
    Ls = []  # liste des symboles
    table = []  # liste des couples
    cumul = 0
    for s in msg:
        if not s in Ls:
            Ls.append(s)
            table.append((s, cumul / n))
            for s2 in msg:
                if s2 == s:
                    cumul += 1
    return table


def bornes(s, table):
    n = len(table)
    for k in range(n):
        sk, ck = table[k]
        if sk == s:
            if k == n - 1:
                return ck, 1.0  # le dernier intervalle
            else:
                return ck, table[k + 1][1]


def symbole(x, table):
    n = len(table)
    bi = 1.0
    for k in range(n - 1, -1, -1):
        bs = bi
        s, bi = table[k]
        if x >= bi:
            return s, bi, bs


def code(msg, table):
    Bi, Bs = 0., 1.
    for s in msg:
        bi, bs = bornes(s, table)
        d = Bs - Bi
        Bi, Bs = Bi + d * bi, Bi + d * bs
        print(Bi, Bs)  # pour voir l'intervalle
    return (Bi + Bs) / 2


def decode(x, table):
    msg = ''
    s = ''
    while s != '/':
        s, bi, bs = symbole(x, table)
        msg += s
        x = (x - bi) / (bs - bi)
    return msg

msg = 'CLEMENCEAU/'
# msg='AAABAAAC/'
# msg='ABCDEFGHIJKLMNO/'
table = subdivision(msg)
# print(table)
x = code(msg, table)
print(x)
print(len(msg))
print(decode(x, table))
print(msg)

os.system("pause")
