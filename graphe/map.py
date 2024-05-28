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
    def __init__(self, graphe, entree, sortie):
        self.graphe = graphe
        self.cellules = {sommet: Case() for sommet in graphe if sommet not in ['entree', 'sortie']}
        self.entree = entree
        self.sortie = sortie

    def ajouter_article(self, sommet, article, quantite=1):
        if sommet in self.cellules:
            self.cellules[sommet].ajouter_article(article, quantite)

    def afficher_supermarche(self):
        for sommet, cellule in self.cellules.items():
            print(f"Cellule {sommet}: {cellule}")
        print(f"Entrée: {self.entree}")
        print(f"Sortie: {self.sortie}")

    def dico_voisins(self):
        return self.graphe
    
import filepile
import outils

class Supermarche:
    def __init__(self, graphe, depart, arrivee):
        self.graphe = graphe
        self.depart = depart
        self.arrivee = arrivee
        self.cellules = {sommet: Case() for sommet in graphe}

    def ajouter_article(self, sommet, article, quantite=1):
        if sommet in self.cellules:
            self.cellules[sommet].ajouter_article(article, quantite)

    def afficher_supermarche(self):
        for sommet, cellule in self.cellules.items():
            print(f"Cellule {sommet}: {cellule}")

    def dico_voisins(self):
        return self.graphe

    def get_parcours(self):
        return self.graphe

    def get_depart(self):
        return self.depart

    def get_arrivee(self):
        return self.arrivee



def ajout_article(supermarche, fichier_json):
    with open(fichier_json, 'r', encoding='utf-8') as f:
        data = json.load(f)
        for sommet, articles in data.items():
            for article, quantite in articles.items():
                supermarche.ajouter_article(sommet, article, quantite)

def map(fgraphe, farticle):

    with open(fgraphe, 'r', encoding='utf-8') as f:
        graphe = json.load(f)

    supermarche = Supermarche(graphe, (0, 0), (5, 5))
    ajout_article(supermarche, farticle)

    return supermarche



