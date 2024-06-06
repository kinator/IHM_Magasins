import map
import parcours

if __name__ == "__main__":
    supermarche = map.mapping("supermarche.json", "articles.json")

    points_interet = [(3, 2), (4,1), (1,2), (0, 5)]
    depart = supermarche.get_depart()
    arrivee = supermarche.get_arrivee()

    chemin_plus_court = parcours.parcours_opti(supermarche.get_parcours(), depart, arrivee, points_interet)
    print(f"Chemin le plus court entre {depart} et {arrivee}: {chemin_plus_court}")
