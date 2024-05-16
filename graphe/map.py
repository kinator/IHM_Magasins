import json
import filepile
import outils

class Case:
    def __init__(self):
        self.articles = {}

    def ajouter_article(self, article, quantite=1):
        if article in self.articles:
            self.articles[article] += quantite
        else:
            self.articles[article] = quantite

    def __str__(self):
        return str(self.articles)


class Supermarche:
    def __init__(self, graphe):
        self.graphe = graphe
        self.cellules = {sommet: Case() for sommet in graphe}

    def ajouter_article(self, sommet, article, quantite=1):
        if sommet in self.cellules:
            self.cellules[sommet].ajouter_article(article, quantite)

    def afficher_supermarche(self):
        for sommet, cellule in self.cellules.items():
            print(f"Cellule {sommet}: {cellule}")

    def dico_voisins(self):
        return self.graphe


def ajout_article(supermarche, fichier_json):
    with open(fichier_json, 'r', encoding='utf-8') as f:
        data = json.load(f)
        for sommet, articles in data.items():
            for article, quantite in articles.items():
                supermarche.ajouter_article(sommet, article, quantite)



