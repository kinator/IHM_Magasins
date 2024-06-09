import map
import parcours

if __name__ == "__main__":
    supermarche = map.mapping("supermarche.json", "produits.json", "panier.json")

    points_interet = supermarche.coordonnees_par_article()
    depart = supermarche.get_depart()
    arrivee = supermarche.get_arrivee()

    print(points_interet)
    chemin_plus_court = parcours.parcours_opti(supermarche.get_parcours(), depart, arrivee, points_interet)
    print(f"Chemin le plus court entre {depart} et {arrivee}: {chemin_plus_court}")
