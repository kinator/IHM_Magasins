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

def permuter(points):
    if len(points) == 0:
        return [[]]
    permutations = []
    for i in range(len(points)):
        rest = points[:i] + points[i+1:]
        for p in permuter(rest):
            permutations.append([points[i]] + p)
    return permutations

def parcours_opti(graphe: dict, depart: tuple, arrivee: tuple, points_interet: list) -> list:
    def calculer_chemin_total(ordre_points: list) -> list:
        chemin_complet = []
        point_courant = depart
        for point in ordre_points:
            segment_chemin = parcours(graphe, point_courant, point)
            if segment_chemin == "Pas de chemin trouvé":
                return "Pas de chemin trouvé"
            chemin_complet.extend(segment_chemin[:-1])
            point_courant = point
        segment_chemin = parcours(graphe, point_courant, arrivee)
        if segment_chemin == "Pas de chemin trouvé":
            return "Pas de chemin trouvé"
        chemin_complet.extend(segment_chemin)
        return chemin_complet

    permutations_points = permuter(points_interet)

    meilleur_chemin = None
    meilleure_distance = float('inf')

    for perm in permutations_points:
        chemin = calculer_chemin_total(perm)
        if chemin != "Pas de chemin trouvé":
            distance_chemin = sum(graphe[chemin[i]][chemin[i + 1]] for i in range(len(chemin) - 1))
            if distance_chemin < meilleure_distance:
                meilleure_distance = distance_chemin
                meilleur_chemin = chemin

    return meilleur_chemin if meilleur_chemin is not None else "Pas de chemin trouvé"
