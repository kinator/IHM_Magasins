import json
import map     
import parcours 

graphe1 = {
    '1': {'2': 1, '4': 1, '5': 1},
    '2': {'1': 1, '3': 1, '5': 1},
    '3': {'2': 1, '5': 1, '6': 1},
    '4': {'1': 1, '5': 1},
    '5': {'1': 1, '2': 1, '3': 1, '4': 1, '6': 1},
    '6': {'3': 1, '5': 1}
}

#supermarche = map.Supermarche(graphe1)
#map.ajout_article(supermarche, "supermarche.json")
#supermarche.afficher_supermarche()
#print(supermarche.dico_voisins())

supermarche = map.map("supermarche.json", "panier.json")

parcours.parcours_opti(supermarche.get_parcours(), supermarche.get_depart, supermarche.get_arrivee, ())

# BUG : corriger la relation entre parcours et mapping 
# Ajouter un fonctionnement de json qui fonctionne (car là il est un peu bugué...)
