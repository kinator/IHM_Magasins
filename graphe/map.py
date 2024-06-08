import json

class Case:
    def __init__(self):
        self.articles = []

    def ajouter_article(self, article):
        if article not in self.articles:
            self.articles.append(article)

    def __str__(self):
        return str(self.articles)


class Supermarche:
    def __init__(self, graphe, depart, arrivee, panier):
        self.graphe = graphe
        self.depart = depart
        self.arrivee = arrivee
        self.cellules = {sommet: Case() for sommet in graphe}
        self.panier = panier_en_liste(panier)
        self.height = max(sommet[1] for sommet in graphe) + 1
        self.width = max(sommet[0] for sommet in graphe) + 1

    def ajouter_article(self, sommet, article):
        if sommet in self.cellules:
            self.cellules[sommet].ajouter_article(article)

    def afficher_supermarche(self):
        for sommet, cellule in self.cellules.items():
            print(f"Cellule {sommet}: {cellule}")

    def coordonnees_par_article(self):
        panier_articles = set(self.panier)
        coordonnees = []
        for sommet, case in self.cellules.items():
            if any(article in panier_articles for article in case.articles):
                coordonnees.append(sommet)
        return coordonnees

    def dico_voisins(self):
        return self.graphe

    def get_parcours(self):
        return self.graphe

    def get_depart(self):
        return self.depart

    def get_arrivee(self):
        return self.arrivee
    
    def get_panier(self):
        return self.panier
    
    def get_height(self):
        return self.height

    def get_width(self):
        return self.width


def ajout_article(supermarche, fichier_json):
    with open(fichier_json, 'r', encoding='utf-8') as f:
        data = json.load(f)
        for sommet, articles in data.items():
            if sommet.startswith("(") and sommet.endswith(")"):
                coordonnees = tuple(map(int, sommet.strip("()").split(',')))
                for article in articles:
                    supermarche.ajouter_article(coordonnees, article)


def panier_en_liste(fpanier):
    with open(fpanier, 'r', encoding='utf-8') as f:
        panier_json = json.load(f)
        panier_dict = panier_json.get("panier", {})
        return list(panier_dict.keys()) 



def mapping(fgraphe, farticle, fpanier):
    with open(fgraphe, 'r', encoding='utf-8') as f:
        data = json.load(f)
        
        graphe = {tuple(map(int, key.strip("()").split(','))): 
                  {tuple(map(int, k.strip("()").split(','))): v for k, v in value.items()}
                  for key, value in data["graphe"].items()}
        
        entree = tuple(map(int, data["entree"].strip("()").split(','))) # tuple() permet de définir un tuple, map() permet de remplacer la boucle en appliquant int() à chaque élément, strip() enlève les parenthèses, split() divise la chaine par les virgules
        sortie = tuple(map(int, data["sortie"].strip("()").split(',')))
    
    supermarche = Supermarche(graphe, entree, sortie, fpanier)
    ajout_article(supermarche, farticle)

    return supermarche
