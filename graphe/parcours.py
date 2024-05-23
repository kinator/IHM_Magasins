import filepile

def parcours(dico_graphe: dict, depart: tuple, arrivee: tuple) -> list:
    chemin = []
    pile = filepile.Pile()
    visite = []

    pile.empiler(depart)
    
    while not pile.est_vide():
        sommet = pile.depiler()
        chemin.append(sommet)
        
        if sommet == arrivee:
            return chemin
        
        for voisin in dico_graphe[sommet]:
            if voisin not in visite:
                visite.append(voisin)
                pile.empiler(voisin)
    
    return "Pas de chemin trouvé"

def parcours_opti(graphe: dict, depart: tuple, arrivee: tuple, points_interet: list) -> list:
    '''La fonction cherche le chemin le plus rapide pour prendre un ou plusieurs articles dans le supermarché.'''
    
    chemin_complet = []
    point_courant = depart

    for point in points_interet:
        chemin = parcours(graphe, point_courant, point)
        if chemin == "Pas de chemin trouvé":
            return "Pas de chemin trouvé"
        chemin_complet.extend(chemin[:-1])
        point_courant = point
        print("test "+ str(point))

    chemin = parcours(graphe, point_courant, arrivee)
    if chemin == "Pas de chemin trouvé":
        return "Pas de chemin trouvé"
    chemin_complet.extend(chemin)
    
    return chemin_complet


if __name__ == "__main__":
    graphe_exemple = {
    (0, 0): {(0, 1): 1, (1, 0): 1},
    (0, 1): {(0, 0): 1, (0, 2): 1, (1, 1): 1},
    (0, 2): {(0, 1): 1, (0, 3): 1, (1, 2): 1},
    (0, 3): {(0, 2): 1, (0, 4): 1, (1, 3): 1},
    (0, 4): {(0, 3): 1, (0, 5): 1, (1, 4): 1},
    (0, 5): {(0, 4): 1, (1, 5): 1},
    (1, 0): {(0, 0): 1, (1, 1): 1, (2, 0): 1},
    (1, 1): {(0, 1): 1, (1, 0): 1, (1, 2): 1, (2, 1): 1},
    (1, 2): {(0, 2): 1, (1, 1): 1, (1, 3): 1, (2, 2): 1},
    (1, 3): {(0, 3): 1, (1, 2): 1, (1, 4): 1, (2, 3): 1},
    (1, 4): {(0, 4): 1, (1, 3): 1, (1, 5): 1, (2, 4): 1},
    (1, 5): {(0, 5): 1, (1, 4): 1, (2, 5): 1},
    (2, 0): {(1, 0): 1, (2, 1): 1, (3, 0): 1},
    (2, 1): {(1, 1): 1, (2, 0): 1, (2, 2): 1, (3, 1): 1},
    (2, 2): {(1, 2): 1, (2, 1): 1, (2, 3): 1, (3, 2): 1},
    (2, 3): {(1, 3): 1, (2, 2): 1, (2, 4): 1, (3, 3): 1},
    (2, 4): {(1, 4): 1, (2, 3): 1, (2, 5): 1, (3, 4): 1},
    (2, 5): {(1, 5): 1, (2, 4): 1, (3, 5): 1},
    (3, 0): {(2, 0): 1, (3, 1): 1, (4, 0): 1},
    (3, 1): {(2, 1): 1, (3, 0): 1, (3, 2): 1, (4, 1): 1},
    (3, 2): {(2, 2): 1, (3, 1): 1, (3, 3): 1, (4, 2): 1},
    (3, 3): {(2, 3): 1, (3, 2): 1, (3, 4): 1, (4, 3): 1},
    (3, 4): {(2, 4): 1, (3, 3): 1, (3, 5): 1, (4, 4): 1},
    (3, 5): {(2, 5): 1, (3, 4): 1, (4, 5): 1},
    (4, 0): {(3, 0): 1, (4, 1): 1, (5, 0): 1},
    (4, 1): {(3, 1): 1, (4, 0): 1, (4, 2): 1, (5, 1): 1},
    (4, 2): {(3, 2): 1, (4, 1): 1, (4, 3): 1, (5, 2): 1},
    (4, 3): {(3, 3): 1, (4, 2): 1, (4, 4): 1, (5, 3): 1},
    (4, 4): {(3, 4): 1, (4, 3): 1, (4, 5): 1, (5, 4): 1},
    (4, 5): {(3, 5): 1, (4, 4): 1, (5, 5): 1},
    (5, 0): {(4, 0): 1, (5, 1): 1},
    (5, 1): {(4, 1): 1, (5, 0): 1, (5, 2): 1},
    (5, 2): {(4, 2): 1, (5, 1): 1, (5, 3): 1},
    (5, 3): {(4, 3): 1, (5, 2): 1, (5, 4): 1},
    (5, 4): {(4, 4): 1, (5, 3): 1, (5, 5): 1},
    (5, 5): {(4, 5): 1, (5, 4): 1}
    }
    

    points_interet : list = [(0, 5)]
    depart = (0, 0)
    arrivee = (5, 5)
    chemin_plus_court = parcours_opti(graphe_exemple, depart, arrivee, points_interet)
    print(f"Chemin le plus court entre {depart} et {arrivee}: {chemin_plus_court}")
