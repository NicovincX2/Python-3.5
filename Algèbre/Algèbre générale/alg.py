# -*- coding: utf-8 -*-

import os

def big(loi , neutre )  :
    """
    - loi est une lci de type (a,a) -> a
    - neutre est le neutre de loi
    - retourne une fonction qui prend une liste [x1, x2, ...]
    et renvoie ((neutre 'loi' x1) 'loi' x2) 'loi' ...
 
    >>> big(lambda x, y : x + y, 0)([2, 3, 4])
    9
    """
    def fonc_reductrice(xs) :
        """
        C'est la fonction qui sera retournée par big(loi, neutre)
        xs est une liste d'éléments de type a
 
        >>> fonc_reductrice([2, 3, 4]) # dans le cas où loi est + et neutre est 0
        9
        """
        return 0
    return fonc_reductrice
 
def reduit(loi, collection, neutre) :
    """
    on fabrique reduce à partir de big
    """
    return 0#avec big
 
def filtre(predicat, xs) :
    """
    Renvoie la liste des éléments de xs qui vérifient le prédicat
 
    >>> filtre(lambda x : x >= 3, [1, 2, 3, 4])
    [3, 4]
    """
    return 0#reduit(???, xs, ???)
 
 
def applique(fonc, xs) :
    """
    Renvoie la liste des images des éléments de xs par fonc
 
    >>> applique(ord , ['a', 'b', 'c'])
    [97, 98, 99]
    """
    return 0#reduit(???, xs, ???)

os.system("pause")

