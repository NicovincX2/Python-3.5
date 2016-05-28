# -*- coding: utf-8 -*-

import os


def allouer(n):
    return [0] * n


def taille(t):
    return len(t)


def afficherMot(tab, i, k):
    s = ''
    for j in range(k):
        s += chr(96 + tab[i + j])
    return s


def strToTab(s):
    return [ord(c) - 96 for c in s]


def enTeteDeSuffixe(mot, tab, k):
    m = taille(mot)
    if k + m > taille(tab):
        return False
    for j in range(m):
        if mot[j] != tab[k + j]:
            return False
    return True


def rechercherMot(mot, tab):
    for k in range(taille(tab) - taille(mot) + 1):
        if enTeteDeSuffixe(mot, tab, k):
            return True
    return False


def compterOccurrences(mot, tab):
    nb = 0
    for k in range(taille(tab) - taille(mot) + 1):
        if enTeteDeSuffixe(mot, tab, k):
            nb += 1
    return nb


def frequenceLettre(tab):
    n = taille(tab)
    f = allouer(26)
    for k in range(n):
        f[tab[k]] += 1
    return f


def afficherFrequenceBigramme(tab):
    n = taille(tab)
    mot = allouer(2)
    bigrs = []
    occs = []
    for i in range(n - 1):
        mot[0] = tab[i]
        mot[1] = tab[i + 1]
        bigr = afficherMot(mot, 0, 2)
        if bigr not in bigrs:
            bigrs.append(bigr)
            occs.append(compterOccurrences(mot, tab))
    for j in range(len(bigrs)):
        print(bigrs[j], occs[j])


def comparerSuffixes(tab, k1, k2):
    n = taille(tab)
    if k1 >= n and k2 >= n:
        return 0
    if k1 >= n:
        return -1
    if k2 >= n:
        return 1
    if tab[k1] < tab[k2]:
        return -1
    if tab[k1] > tab[k2]:
        return 1
    return comparerSuffixes(tab, k1 + 1, k2 + 1)


def comparerSuffixesIter(tab, k1, k2):
    n = taille(tab)
    while k1 < n and k2 < n:
        if tab[k1] < tab[k2]:
            return -1
        if tab[k1] > tab[k2]:
            return 1
        k1 += 1
        k2 += 1
    if k1 >= n and k2 >= n:
        return 0
    if k1 >= n:
        return -1
    return 1


def calculerSuffixes(tab):
    def quicksort(t):
        if len(t) < 2:
            return t
        pivot = t[0]
        t1 = []
        t2 = []
        for x in t[1:]:
            if comparerSuffixes(tab, x, pivot) < 0:
                t1.append(x)
            else:
                t2.append(x)
        return quicksort(t1) + [pivot] + quicksort(t2)
    return quicksort(list(range(len(tab))))


def comparerMotSuffixe(mot, tab, k):
    m = taille(mot)
    n = taille(tab)
    i = 0
    while i < m and k < n:
        if mot[i] < tab[k]:
            return -1
        if mot[i] > tab[k]:
            return 1
        i += 1
        k += 1
    if i >= m:
        return 0
    else:
        return 1


def rechercherMot2(mot, tab, tabS):
    g = 0
    d = taille(tab) - 1
    while g < d:
        m = (g + d) // 2
        c = comparerMotSuffixe(mot, tab, tabS[m])
        if c == 0:
            return True
        if c <= 0:
            d = m
        else:
            g = m + 1
    return comparerMotSuffixe(mot, tab, tabS[g]) == 0


def rechercherPremierSuffixe(mot, tab, tabS):
    g = 0
    d = taille(tab) - 1
    while g < d:
        m = (g + d) // 2
        c = comparerMotSuffixe(mot, tab, tabS[m])
        if c <= 0:
            d = m
        else:
            g = m + 1
    if comparerMotSuffixe(mot, tab, tabS[g]) == 0:
        return g
    else:
        return -1


def rechercherDernierSuffixe(mot, tab, tabS):
    g = 0
    d = taille(tab) - 1
    while g < d:
        m = 1 + (g + d) // 2
        c = comparerMotSuffixe(mot, tab, tabS[m])
        if c >= 0:
            g = m
        else:
            d = m - 1
    if comparerMotSuffixe(mot, tab, tabS[g]) == 0:
        return g
    else:
        return -1


def compterOccurrences2(mot, tab, tabS):
    prem = rechercherPremierSuffixe(mot, tab, tabS)
    if prem < 0:
        return 0
    else:
        return rechercherDernierSuffixe(mot, tab, tabS) - prem + 1


def afficherFrequenceKgramme(tab, tabS, k):
    n = taille(tab)
    mot = allouer(k)
    Kgrs = []
    occs = []
    for i in range(n - k - 1):
        for j in range(k):
            mot[j] = tab[i + j]
        Kgr = afficherMot(mot, 0, k)
        if Kgr not in Kgrs:
            Kgrs.append(Kgr)
            occs.append(compterOccurrences2(mot, tab, tabS))
    for j in range(len(Kgrs)):
        print(Kgrs[j], occs[j])


tab = strToTab('quelbonbonbon')
tabS = calculerSuffixes(tab)
mot = strToTab('bon')
afficherFrequenceKgramme(tab, tabS, 6)

os.system("pause")
