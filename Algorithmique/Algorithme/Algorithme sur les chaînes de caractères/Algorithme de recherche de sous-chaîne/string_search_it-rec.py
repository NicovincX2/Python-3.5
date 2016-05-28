# -*- coding: utf-8 -*-

import os


def Recherche_iterative(motif, source):
    i = 0
    j = 0
    while i < len(motif) and j < len(source):
        if motif[i] == source[j]:
            i = i + 1
            j = j + 1
        else:
            j = j - i + 1
            i = 0
    return i == len(motif)


def Est_prefixe(motif, source):
    if motif == '':
        return True
    elif source == '':
        return False
    else:
        return motif[0] == source[0] and Est_prefixe(motif[1:], source[1:])


def Recherche_recursive(motif, source):
    if source == '':
        return motif == ''
    else:
        return Est_prefixe(motif, source) or Recherche_recursive(motif, source[1:])

# print(Est_prefixe('Py','Python'))
# print(Recherche_iterative('to','Python'))
print(Recherche_recursive('ton', 'Python'))
print(Recherche_recursive('thon', 'Python'))

os.system("pause")
