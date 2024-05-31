import json

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
            if sommet.startswith("(") and sommet.endswith(")"):
                coordonnees = tuple(map(int, sommet.strip("()").split(',')))
                for article, quantite in articles.items():
                    supermarche.ajouter_article(coordonnees, article, quantite)

def mapping(fgraphe, farticle):
    with open(fgraphe, 'r', encoding='utf-8') as f:
        data = json.load(f)
        
        graphe = {tuple(map(int, key.strip("()").split(','))): 
                  {tuple(map(int, k.strip("()").split(','))): v for k, v in value.items()}
                  for key, value in data["graphe"].items()}
        
        entree = tuple(map(int, data["entree"].strip("()").split(',')))
        sortie = tuple(map(int, data["sortie"].strip("()").split(',')))
    
    supermarche = Supermarche(graphe, entree, sortie)
    ajout_article(supermarche, farticle)

    return supermarche
