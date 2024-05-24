import filepile

def dijkstra(graphe: dict, depart: str, bk_liste: list = []) -> dict:
    file1 = filepile.File(len(graphe.keys()))
    file1.enfiler(depart)
    distance = {depart: [0, [depart]]}

    while not file1.est_vide():
        sommet = file1.defiler()
        dist_actuelle, chemin_actuel = distance[sommet]
        voisins = graphe[sommet]

        for voisin, poids in voisins.items():
            if voisin not in bk_liste:
                nouvelle_distance = dist_actuelle + poids
                if voisin not in distance or nouvelle_distance < distance[voisin][0]:
                    distance[voisin] = [nouvelle_distance, chemin_actuel + [voisin]]
                    file1.enfiler(voisin)
                    
    return distance

def parcours(graphe: dict, depart: str, arrivee: str) -> list:
    distances = dijkstra(graphe, depart)
    if arrivee not in distances:
        return "Pas de chemin trouvé"
    
    chemin = distances[arrivee][1]
    return chemin

def parcours_opti(graphe: dict, depart: str, arrivee: str, points_interet: list) -> list:
    chemin_complet = []
    point_courant = depart

    for point in points_interet:
        segment_chemin = parcours(graphe, point_courant, point)
        if segment_chemin == "Pas de chemin trouvé":
            return "Pas de chemin trouvé"
        chemin_complet.extend(segment_chemin[:-1]) # -1 permet de ne pas prendre le dernier élément de la liste sinon il serait ajouté en double
        point_courant = point
        print("test "+ str(point))

    segment_chemin = parcours(graphe, point_courant, arrivee)
    if segment_chemin == "Pas de chemin trouvé":
        return "Pas de chemin trouvé"
    chemin_complet.extend(segment_chemin)

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
    

    points_interet : list = [(0, 5), (3, 2)]
    depart = (0, 0)
    arrivee = (5, 5)
    chemin_plus_court = parcours_opti(graphe_exemple, depart, arrivee, points_interet)
    print(f"Chemin le plus court entre {depart} et {arrivee}: {chemin_plus_court}")
