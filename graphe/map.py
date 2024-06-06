import json

class Case:
    def __init__(self):
        self.articles = []

    def ajouter_article(self, article, quantite=1):
        self.articles.append((article, quantite))

    def __repr__(self):
        return f"Articles: {self.articles}"

class Supermarche:
    def __init__(self, graphe, depart, arrivee, fpanier, fproduits):
        self.graphe = graphe
        self.depart = depart
        self.arrivee = arrivee
        self.cellules = {sommet: Case() for sommet in graphe}
        self.points_interet = []

        # Charger les articles du panier
        with open(fpanier, 'r', encoding='utf-8') as f:
            panier_data = json.load(f)
            for article in panier_data.values():
                self.points_interet.extend(article)

        # Charger les produits sur chaque case
        self.charger_produits(fproduits)

    def ajouter_article(self, sommet, article, quantite=1):
        if sommet in self.cellules:
            self.cellules[sommet].ajouter_article(article, quantite)

    def charger_produits(self, fproduits):
        with open(fproduits, 'r', encoding='utf-8') as f:
            produits_data = json.load(f)
            for sommet_str, articles in produits_data.items():
                sommet = tuple(map(int, sommet_str.strip("()").split(",")))
                for article in articles:
                    self.ajouter_article(sommet, article)

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

    def get_panier(self):
        return self.points_interet

def mapping(fgraphe, fproduits, fpanier):
    with open(fgraphe, 'r', encoding='utf-8') as f:
        graphe_data = json.load(f)
        graphe = graphe_data["graphe"]
        depart = tuple(map(int, graphe_data["entree"].strip("()").split(",")))
        arrivee = tuple(map(int, graphe_data["sortie"].strip("()").split(",")))

    supermarche = Supermarche(graphe, depart, arrivee, fpanier, fproduits)

    return supermarche
