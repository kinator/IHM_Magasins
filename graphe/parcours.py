import filepile

def parcours(dico_graphe: dict, depart: tuple, arrivee: tuple) -> list:
    '''La fonction explore le labyrinthe à partir de son graphe associé et renvoie une liste des
    chemins possibles entre depart et arrivee.'''
    
    chemin = []            # chemin actuel
    pile = filepile.Pile()        # pile pour la recherche en profondeur
    visite = []        

    pile.empiler(depart)
    
    while not pile.est_vide():
        sommet = pile.depiler()
        chemin.append(sommet)
        
        if sommet == arrivee:
            return chemin  
        for voisin in dico_graphe[sommet]:
            if voisin not in visite:
                visite.append(sommet)
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

    chemin = parcours(graphe, point_courant, arrivee)
    if chemin == "Pas de chemin trouvé":
        return "Pas de chemin trouvé"
    chemin_complet.extend(chemin)
    
    return chemin_complet

if __name__ == "__main__":
    graphe_exemple = {
        (0, 0): {(0, 1): 1, (1, 0): 1},
        (0, 1): {(0, 0): 1, (1, 1): 1},
        (1, 0): {(0, 0): 1, (1, 1): 1},
        (1, 1): {(0, 1): 1, (1, 0): 1}
    }

    depart = (0, 0)
    arrivee = (1, 1)
    chemin_plus_court = parcours_opti(graphe_exemple, depart, arrivee)
    print(f"Chemin le plus court entre {depart} et {arrivee}: {chemin_plus_court}")
