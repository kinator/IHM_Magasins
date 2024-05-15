# -*- coding: utf-8 -*-
'''
:Titre : TP2
:Auteur : L. Conoir
:Date : 03/2023
'''

import numpy as np


def dico_voisins(sommets: np.array, matrice: np.array)-> dict:
    '''La fonction renvoie le dictionnaire des voisins du graphe associé à la matrice d'adjacence
et au tableau des sommets.

:param: sommets : tableau des sommets
        matrice : matrice d'adjacence du graphe
:examples:
>>> exemple_sommets = np.array(['A', 'B', 'C', 'D'])
>>> exemple_matrice = np.array([[0, 1, 4, 2], [1, 0, 3, 0], [4, 3, 0, 0], [2, 0, 0, 0]])
>>> dico_voisins(exemple_sommets, exemple_matrice)
{'A': {'B': 1, 'C': 4, 'D': 2},
 'B': {'A': 1, 'C': 3},
 'C': {'A': 4, 'B': 3},
 'D': {'A': 2}}

    '''
    assert isinstance(sommets, np.ndarray), "Le premier argument utilisé n'est pas conforme : type np.array([]) attendu."   # vérification de l'argument
    assert isinstance(matrice, np.ndarray), "Le deuxième argument utilisé n'est pas conforme : type np.array([]) attendu."   # vérification de l'argument

    resultat = {}                         # dictionnaire des voisins
    ordre = sommets.shape[0]              # nombre des sommets
    
    for indice1 in range(ordre):          # indice d'un sommet parmi le tableau de sommets

        sommet = sommets[indice1]             # nom de ce sommet
        voisins = matrice[indice1]            # tableau de ses voisins
        dico = {}                             # dictionnaire des distances des voisins
        
        for indice2 in range(ordre):          # indice du voisin

            voisin = sommets[indice2]             # nom du voisin
            distance = voisins[indice2]           # distance sommet-voisin
            
            if distance != 0:                     # si il existe une arête ou un arc
                dico[voisin] = distance               # on déclare le voisin avec sa distance

        resultat[sommet] = dico               # ajout du dictionnaire des distances des voisins au sommet

    return resultat



def ordre(dico: dict)-> int:
    '''La fonction renvoie l'ordre du graphe.
:examples:
>>> exemple_voisins = {'A': {'B': 1, 'C': 4, 'D': 2}, 'B': {'A': 1, 'C': 3}, 'C': {'A': 4, 'B': 3}, 'D': {'A': 2}}
>>> ordre(exemple_voisins)
4
    '''
    assert isinstance(dico, dict), "L'argument utilisé n'est pas conforme : type dict() attendu."   # vérifications des arguments

    return len(dico.keys())




def degre_sommet(dico: dict, sommet: str, oriente: bool = False)-> int:
    '''La fonction renvoie le degré du sommet dans le graphe.
:examples:
>>> exemple_voisins1 = {'A': {'B': 1, 'C': 4, 'D': 2}, 'B': {'A': 1, 'C': 3}, 'C': {'A': 4, 'B': 3}, 'D': {'A': 2}}
>>> exemple_voisins2 = {'A': {'B': 1, 'C': 4}, 'B': {'A': 1, 'C': 3}, 'C': {'B': 3}, 'D': {'A': 2}}
>>> degre_sommet(exemple_voisins1, 'B')
2
>>> degre_sommet(exemple_voisins2, 'A', True)
4
    '''
    assert isinstance(dico, dict), "Le premier argument utilisé n'est pas conforme."   # vérifications des arguments
    assert isinstance(sommet, str), "Le deuxième argument utilisé n'est pas conforme."
    assert sommet in dico.keys(), "Le sommet est inconnu."

    resultat = len(dico[sommet].keys())    # on compte les voisins du sommet : successeurs (degré sortant)
    
    if oriente :                           # si le graphe est orienté

        for voisins in dico.values() :          # pour chaque groupe de voisins déclarés

            if sommet in voisins :                   # on regarde si le sommet en fait partie
                resultat = resultat + 1                   # prédécesseurs (degré entrant)

    return resultat




def degre_graphe(dico: dict, oriente: bool = False)-> int:
    '''La fonction renvoie le degré du graphe.
:examples:
>>> exemple_voisins = {'A': {'B': 1, 'C': 4, 'D': 2}, 'B': {'A': 1, 'C': 3}, 'C': {'A': 4, 'B': 3}, 'D': {'A': 2}}
>>> degre_graphe(exemple_voisins)
3
    '''
    assert isinstance(dico, dict), "L'argument utilisé n'est pas conforme : type dict() attendu."   # vérification de l'argument
    
    maximum = 0

    for sommet in dico.keys():

        nb_voisins = degre_sommet(dico, sommet, oriente)    # il suffit de mettre à jour l'appel de fonction
        
        if nb_voisins > maximum:
            maximum = nb_voisins

    return maximum



def taille(dico: dict, oriente: bool = False)-> int:
    '''La fonction renvoie la taille du graphe.
:examples:
>>> exemple_voisins = {'A': {'B': 1, 'C': 4, 'D': 2}, 'B': {'A': 1, 'C': 3}, 'C': {'A': 4, 'B': 3}, 'D': {'A': 2}}
>>> taille(exemple_voisins)
4
    '''
    assert isinstance(dico, dict), "L'argument utilisé n'est pas conforme : type dict() attendu."   # vérification de l'argument

    compteur = 0                                          # déclaration du nombre de relations

    for sommet in dico.keys():                            # pour chaque sommet

        compteur = compteur + degre_sommet(dico, sommet)      # on ajoute au compteur le nombre de ses voisins

    if not oriente :                                      # si le graphe est non oriente
        compteur = compteur // 2                              # on divise par 2

    return compteur
