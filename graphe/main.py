import map
import parcours

if __name__ == "__main__":
    # Charger le supermarché en utilisant les fichiers JSON
    supermarche = map.mapping("supermarche.json", "produits.json", "panier.json")

    # Obtenir les données nécessaires pour le parcours
    panier = supermarche.get_panier()
    depart = supermarche.get_depart()
    arrivee = supermarche.get_arrivee()

    # Effectuer le parcours optimal
    chemin_plus_court = parcours.parcours_opti(supermarche.get_parcours(), depart, arrivee, panier)
    
    # Afficher le chemin le plus court
    print(f"Chemin le plus court entre {depart} et {arrivee}: {chemin_plus_court}")
