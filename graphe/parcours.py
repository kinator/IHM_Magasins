import filepile

def parcours(dico_graphe: dict, depart: tuple, arrivee: tuple) -> list:
    '''La fonction explore le labyrinthe à partir de son graphe associé et renvoie une liste des
    chemins possibles entre depart et arrivee.'''
    
    chemin = []            # chemin actuel
    pile = filepile.Pile()        # pile pour la recherche en profondeur
    visite = []         # sommets visités

    pile.empiler(depart)
    
    while not pile.est_vide():
        sommet = pile.depiler()
        chemin.append(sommet)
        
        if sommet == arrivee:
            return chemin  # chemin trouvé
        
        for voisin in dico_graphe[sommet]:
            if voisin not in visite:
                visite.append(sommet)
                pile.empiler(voisin)
    
    # si on arrive ici, ca veut dire qu'il n'y a pas de chemin entre le depart et l'arrivee
    return "Pas de chemin trouvé"


def parcours_opti(graphe: dict, depart: tuple, arrivee: tuple) -> list:
    for i in range(len(graphe)):
        parcours(graphe, depart, arrivee)

# Exemple d'utilisation
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
