# -*- coding: utf-8 -*-

import os

## Petits alias pour clarifier (optionnel)
nb_d_elements    = len  # le nb d'éléments d'une collection
ens_des_elements = set  # l'ensemble des éléments d'une collection
 
## Méthode 1 : parcours "naturel" à l'aide d'une boucle
def multi1( elmt_cherche, multiensemble ) :
    """
    - Compte l'ordre de multiplicité de elmt dans un multiensemble
    - On crée un compteur, nul au départ
    - On parcourt le multiensemble et on incrémente le compteur si l'élément
    lu est égal à l'élément à compter
    - On retourne le compteur une fois sorti de la boucle
    >>> M = [ 1, 1, 1, 1, 2, 2, 5 ] * 1000
    >>> multi( 1, M )      
    4000
    """
    cpt = 0
    for elmt_lu in multiensemble :
        if elmt_lu == elmt_cherche :
            cpt += 1
    return cpt
 
    
## Méthode 2 : uniligne avec liste par compréhension
def multi2( elmt_cherche, multiensemble ) :
    return nb_d_elements( [ elmt_lu for elmt_lu in multiensemble if elmt_lu == elmt_cherche ] )
    
 
## Méthode 3 : on utilise le fait que True == 1 et False == 0
def multi3( elmt_cherche, multiensemble ) :
    cpt = 0
    for elmt_lu in multiensemble :
        cpt += ( elmt_lu == elmt_cherche ) # plus lent car on rajoute systématiquement des 0 ce qui est inutile
    return cpt

os.system("pause")

