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

def parcours(graphe, depart, arrivee):
    distances = dijkstra(graphe, depart)
    if arrivee not in distances:
        return "Pas de chemin trouvé"
    
    chemin = distances[arrivee][1]
    return chemin

def parcours_opti(graphe, depart, arrivee, points_interet):
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
