import json, os
from produit import Produit

class Case(object) :
    '''Classe définissant une case à partir de sa position : x, y.

    Un objet, instance de cette classe, possède plusieurs méthodes :

    construireMur() : construit un mur de la case
    detruireMur() : détruit un mur de la case
    getContenu() : renvoie le contenu de la case
    setContenu() : affecte le contenu de la case
    getPosition() : renvoie la position de la case
    getStockable() : renvoie si la case est stockable ou non
    getMurs() : renvoie la liste des murs de la case
    estDansStock() : renvoie si le produit est stocker dans la case
    addContenu() : ajoute un produit au contenu de la case
    removeContenu() : retire un produit au contenu de la case
    delContenu() : supprime le contenu de la case'''
    
    def __init__(self, x=0, y=0, stock=False):
        self.__position = (x, y)
        self.__est_stockable = stock
        self.__contenu = {}
        self.__murs = ['N', 'S', 'E', 'W']

    def __init__(self, pos : tuple, stock : bool):
        '''Méthode dédiée, constructeur de la classe'''
        self.__position: tuple = pos
        self.__est_stockable: bool = stock
        self.__contenu: dict = {}
        self.__murs: list = ['N', 'S', 'E', 'W']


    def construireMur(self, mur: str) -> None:
        '''Méthode publique, construit un mur de l'objet.'''
        if mur not in self.__murs :
            self.__murs.append(mur)


    def detruireMur(self, mur: str) -> None:
        '''Méthode publique, détruit un mur de l'objet.'''
        if mur in self.__murs :
            self.__murs.remove(mur)


    def setContenu(self, cakechose: dict) -> None:
        '''Méthode publique, affecte le contenu de l'objet.'''
        self.__contenu = cakechose

    def setStockable(self, info : bool):
        '''Méthode publique, affecte le contenu de l'objet.'''
        self.__est_stockable = info

    def getContenu(self) -> dict:
        '''Méthode publique, renvoie le contenu de l'objet.'''
        return self.__contenu
    
    def est_vide(self) :
        if not self.__contenu:
            return False
        else:
            return True


    def getPosition(self) -> tuple:
        '''Méthode publique, renvoie la position de l'objet : tuple (x, y)'''
        return self.__position
    
    def getStockable(self) -> tuple:
        '''Méthode publique, renvoie si la case est stockable ou non.'''
        return self.__est_stockable

    def getMurs(self) -> list:
        '''Méthode publique, renvoie la liste des murs.'''
        return self.__murs
    
    def estDansStock(self, cakechose: Produit) -> bool:
        '''Méthode publique, renvoie le contenu de l'objet.'''
        return cakechose in self.__contenu
    
    def addContenu(self, cakechose: Produit, stock: int) -> None:
        '''Méthode publique, affecte le contenu de l'objet.'''
        if cakechose not in self.__contenu:
            self.__contenu = {cakechose.__str__ : stock}

    def removeContenu(self, cakechose: Produit) -> None:
        '''Méthode publique, affecte le contenu de l'objet.'''
        self.__contenu.popitem(cakechose)
    
    def delContenu(self) -> None:
        '''Méthode publique, affecte le contenu de l'objet.'''
        self.__contenu = {}

class Magasin(object) :
    '''Classe définissant un magasin à partir de ses dimensions
           largeur : nombre de cases en largeur
           hauteur : nombre de cases en longueur

    Un objet, instance de cette classe, possède plusieurs méthodes :

    construireBordure() : construit les murs sur le contour du magasin
    detruireBordure() : détruit les murs sur le contour du magasin
    afficheMagasinVide() : affiche le magasin (sans contenu) avec tous les murs
    affichePlateau() : affiche le plateau (avec contenu et murs éventuels des cases)'''

    def __init__(self):
        self.__largeur: int = 75
        self.__hauteur: int = 75
        self.__cases: list = self.__creationMagasin()
        self.__entree : tuple = (0, 0)
        self.__sortie : tuple = (0, 0)
        self.__nom : str = ''
    
    def __init__(self, nom_enseigne : str, largeur: int, hauteur: int, entree_x : int = 0, entree_y : int = 0, sortie_x : int = 0, sortie_y : int = 0):
        self.__largeur: int = largeur
        self.__hauteur: int = hauteur
        self.__cases: dict = self.__creationMagasin(largeur, hauteur)
        self.__entree : tuple = (entree_x, entree_y)
        self.__sortie : tuple = (sortie_x, sortie_y)
        self.__nom : str = nom_enseigne

    def __init__(self, nom_enseigne : str, largeur: int, hauteur: int, entree : tuple = (0, 0), sortie : tuple = (0, 0)):
        self.__largeur: int = largeur
        self.__hauteur: int = hauteur
        self.__cases: dict = self.__creationMagasin()
        self.__entree : tuple = (entree)
        self.__sortie : tuple = (sortie)
        self.__nom : str = nom_enseigne

    
    def __creationMagasin(self) -> dict:
        '''Méthode privée, crée et renvoie la liste des cases'''
        cases = {}
        for y in range(self.__hauteur):
            for x in range(self.__largeur):
                nouvelle_case = Case((x, y), False)
                cases[(x, y)] = nouvelle_case
        return cases

    def getCases(self):
        '''Méthode publique, renvoie la liste des cases.'''
        return self.__cases

    def getContenu(self, position: tuple) -> any:
        '''Méthode publique, renvoie le contenu de la case à la position prévue.'''
        
        return self.__cases[str(position)].getContenu()
    
    def getEntree(self):
        return self.__entree
    
    def getSortie(self):
        return self.__sortie
    
    def getNomEnseigne(self):
        return self.__nom
    
    def getMagasin(self):
        return self.__cases
    
    def case_est_vide(self, position : tuple):
        '''Méthode publique, renvoie False si le contenue du dictionnaire contenant la case est vide, True sinon.'''
        if not self.getContenu(position):
            return False
        else:
            return True

    def setContenu(self, position: tuple, cakechose: any) -> None:
        '''Méthode publique, affecte le contenu de la case à la position prévue.'''
        self.__cases[str((position[1], position[0]))].setContenu(cakechose)

    def setEntree(self, x : int, y : int):
        self.__entree = (x, y)

    def setEntree(self, pos : tuple):
        self.__entree = (pos)

    def setSortie(self, x, y):
        self.__sortie = (x, y)

    def setSortie(self, pos : tuple):
        self.__sortie = (pos)

    def setNomEnseigne(self, nom : str):
        self.__nom = nom

    def effaceContenu(self) -> None:
        '''Méthode publique, efface le contenu de toutes les cases.'''
        for y in range(self.__hauteur):
            for x in range(self.__largeur):
                self.__cases[str((y, x))].setContenu(None)


    def construireAvecGraphe(self, graphe: dict) -> None:
        '''Méthode publique, définit les murs à partir d'un graphe.'''
        for case, voisines in graphe.items():
            x1, y1 = case

            for case_voisine in voisines:
                
                x2, y2 = case_voisine

                if y1 == y2 :
                    if x1 < x2 :
                        self.__cases[(y1, x1)].detruireMur('E')
                    else: 
                        self.__cases[(y1, x1)].detruireMur('W')
                else :
                    if y1 < y2 :
                        self.__cases[(y1, x1)].detruireMur('S')
                    else: 
                        self.__cases[(y1, x1)].detruireMur('N')


    def construireBordure(self) -> None:
        '''Méthode publique, définit une bordure extérieure du magasin.'''
        for colonne in range(self.__largeur) :
            self.__cases[(0, colonne)].construireMur('N')
            self.__cases[(self.__hauteur - 1, colonne)].construireMur('S')
        
        for ligne in range(self.__hauteur) :
            self.__cases[(ligne, 0)].construireMur('W')
            self.__cases[(ligne, self.__largeur - 1)].construireMur('E')
    
    
    def detruireBordure(self) -> None:
        '''Méthode publique, enlève une bordure extérieure de lau magasin.'''
        for colonne in range(self.__largeur) :
            self.__cases[(0, colonne)].detruireMur('N')
            self.__cases[(self.__hauteur - 1, colonne)].detruireMur('S')
        
        for ligne in range(self.__hauteur) :
            self.__cases[(ligne, 0)].detruireMur('W')
            self.__cases[(ligne, self.__largeur - 1)].detruireMur('E')
    
    
    def afficheMagasinVide(self) -> None:
        '''Méthode publique, affiche le magasin vide avec tous les murs.'''
        for ligne in range(self.__hauteur) :
            print('+---' * self.__largeur + '+')
            print('|   ' * self.__largeur + '|')
            
        print('+---' * self.__largeur + '+\n')

    def __str__(self) :
        '''Méthode dédiée, affiche le magasin avec son contenu et les murs existants.'''
        affichage = ''
        for y in range(self.__hauteur):
            ligne1, ligne2 = '', ''
            for x in range(self.__largeur):
                case = self.__cases[(x, y)]
                murs = case.getMurs()
                contenu = ' ' if case.est_vide() else 'P'
                ligne1 += '+---' if 'N' in murs else '+   '
                ligne2 += '| ' + contenu + ' ' if 'W' in murs else '  ' + contenu + ' '
            affichage += ligne1 + '+\n' + ligne2 + '|\n'
        affichage += '+---' * self.__largeur + '+\n'
        return affichage
    
class Fichier:
    def __init__(self, jsonFile: str | None = None) -> None:
        self.data_magasin = {}
        self.data_cases = {}
        self.data_produits = {}

        if jsonFile:
            self.open(jsonFile)

    def open(self, jsonFile: str):

        if not os.path.exists(jsonFile):
            return "Error, file does not exist"
        
        with open(jsonFile, "r", encoding='utf-8') as file:
            print(f'loading file: {jsonFile}', end='... \n')
            self.data_magasin = json.load(file)
        
        chemin_fichier_graphe = self.data_magasin['fichier_graphe']
        chemin_fichier_produits = self.data_magasin['fichier_produits']
        
        with open(chemin_fichier_graphe, 'r', encoding='utf-8') as file:
            print(f'loading file: {chemin_fichier_graphe}', end='... \n')
            self.data_cases = json.load(file)
        
        
        with open(chemin_fichier_produits, 'r', encoding='utf-8') as file:
            print(f'loading file: {chemin_fichier_produits}', end='... \n')
            self.data_produits = json.load(file)

    def save(self, jsonFile: str) -> None:
        print(f'saving files: {jsonFile}, {self.getFichierGraphe()} and {self.getFichierProduits()}', end='... ')

        if not os.path.exists(jsonFile):
            f = open(jsonFile, "x") ; f.close()

        with open(jsonFile, "w", encoding='utf-8') as file:
            json.dump(self.data_magasin,file,ensure_ascii=False)

        with open(self.getFichierGraphe(), "w", encoding='utf-8') as file:
            json.dump(self.data_cases, file, ensure_ascii=False)

        with open(self.getFichierProduits(), "w", encoding='utf-8') as file:
            json.dump(self.data_produits, file, ensure_ascii=False)

        print(f'done!')

    def delete(self, jsonFile : str):
        print(f'delete files: {jsonFile}, {self.getFichierGraphe()} and {self.getFichierProduits()}', end='... ')

        if not os.path.exists(jsonFile):
            return "Error, file does not exist"
        
        os.remove(self.getFichierGraphe())
        os.remove(self.getFichierProduits())
        os.remove(jsonFile)


    
    def addProduit(self,emplacement : tuple, p: Produit) -> None:
        self.data_produits[emplacement] = Produit
    

    # les différents setter permmetant de mettre à jour les fichier
    def getMagasin(self):
        return self.data_cases['graphe']

    def getProduits(self):
        return self.data_produits

    def getEntree(self):
        return self.data_cases['entree']

    def getSortie(self):
        return self.data_cases['sortie']
    
    def getNomProjet(self):
        return self.data_magasin['nom_projet']
    
    def getAuteur(self):
        return self.data_magasin['auteur']
    
    def getDate(self):
        return self.data_magasin['date']
    
    def getNomMagasin(self):
        return self.data_magasin['nom_magasin']
    
    def getAdresse(self):
        return self.data_magasin['adresse_magasin']
    
    def getFichierGraphe(self):
        return self.data_magasin['fichier_graphe']

    def getFichierProduits(self):
        return self.data_magasin['fichier_produits']
    
    def getImagePlan(self):
        return self.data_magasin['image_plan']
    
    # les différents getter pour récupérer les différents info des json
    def setEntree(self, entree : tuple):
        self.data_cases['entree'] = entree

    def setSortie(self, sortie : tuple):
        self.data_cases['sortie'] = sortie
    
    def setCasesMagasin(self, cases : dict):
        self.data_cases['graphe'] = cases
    
    def setNomProjet(self, nom : str):
        self.data_magasin['nom_projet'] = nom

    def setAuteur(self, author : str):
        self.data_magasin['auteur'] = author

    def setDate(self, date : tuple):
        self.data_magasin['date'] = str(date)

    def setNomMagasin(self, name : str):
        self.data_magasin['nom_magasin'] = name

    def setAdresse(self, adresse : str):
        self.data_magasin['adresse_magasin'] = adresse

    def setFichierGraphe(self, file : str):
        self.data_magasin['fichier_graphe'] = file

    def setFichierProduits(self, file : str):
        self.data_magasin['fichier_produits'] = file

    def setImagePlan(self, file : str):
        self.data_magasin['image_plan'] = file

if __name__ == '__main__':
    laby = Magasin('test', 8, 8, (0, 0), (0, 0))
    print('Grille de dimensions 8 x 8 avec bordure (par défaut) :')
    print(laby)
    # input("Appuyer sur 'Entrée'")
    
    print('\nSans bordure :')
    laby.detruireBordure()
    print(laby)
    # input("Appuyer sur 'Entrée'")
    
    print("\nAvec bordure")
    laby.construireBordure()
    print(laby)
    # input("Appuyer sur 'Entrée'")

    graphe: dict = {(0, 0): {(0, 1): 1, (1, 0): 1}, (0, 1): {(0, 0): 1, (1, 1): 1}, (0, 2): {(1, 2): 1}, 
                    (0, 3): {(0, 4): 1, (1, 3): 1}, (0, 4): {(0, 3): 1, (0, 5): 1},
                    (0, 5): {(0, 4): 1, (0, 6): 1}, (0, 6): {(0, 5): 1, (0, 7): 1}, (0, 7): {(0, 6): 1}, 
                    (1, 0): {(0, 0): 1, (2, 0): 1}, (1, 1): {(0, 1): 1, (2, 1): 1},
                    (1, 2): {(0, 2): 1, (2, 2): 1}, (1, 3): {(0, 3): 1, (1, 4): 1}, (1, 4): {(1, 3): 1, (2, 4): 1}, 
                    (1, 5): {(1, 6): 1, (2, 5): 1}, (1, 6): {(1, 5): 1, (1, 7): 1}, (1, 7): {(1, 6): 1, (2, 7): 1}, 
                    (2, 0): {(1, 0): 1, (2, 1): 1, (3, 0): 1}, (2, 1): {(1, 1): 1, (2, 0): 1, (3, 1): 1}, 
                    (2, 2): {(1, 2): 1, (2, 3): 1}, (2, 3): {(2, 2): 1, (2, 4): 1}, 
                    (2, 4): {(1, 4): 1, (2, 3): 1, (2, 5): 1}, (2, 5): {(1, 5): 1, (2, 4): 1, (3, 5): 1}, 
                    (2, 6): {(2, 7): 1, (3, 6): 1}, (2, 7): {(1, 7): 1, (2, 6): 1, (3, 7): 1}, 
                    (3, 0): {(2, 0): 1, (4, 0): 1}, (3, 1): {(2, 1): 1, (3, 2): 1}, 
                    (3, 2): {(3, 1): 1, (3, 3): 1, (4, 2): 1}, (3, 3): {(3, 2): 1, (3, 4): 1}, 
                    (3, 4): {(3, 3): 1, (3, 5): 1}, (3, 5): {(2, 5): 1, (3, 4): 1}, (3, 6): {(2, 6): 1, (4, 6): 1}, 
                    (3, 7): {(2, 7): 1, (4, 7): 1},
                    (4, 0): {(3, 0): 1, (5, 0): 1}, (4, 1): {(5, 1): 1}, (4, 2): {(3, 2): 1, (5, 2): 1}, (4, 3): {(4, 4): 1}, 
                    (4, 4): {(4, 3): 1, (4, 5): 1, (5, 4): 1}, (4, 5): {(4, 4): 1, (4, 6): 1, (5, 5): 1}, 
                    (4, 6): {(3, 6): 1, (4, 5): 1}, (4, 7): {(3, 7): 1, (5, 7): 1}, 
                    (5, 0): {(4, 0): 1, (6, 0): 1}, (5, 1): {(4, 1): 1, (6, 1): 1}, (5, 2): {(4, 2): 1, (5, 3): 1, (6, 2): 1},
                    (5, 3): {(5, 2): 1, (5, 4): 1, (6, 3): 1}, (5, 4): {(4, 4): 1, (5, 3): 1, (6, 4): 1}, 
                    (5, 5): {(4, 5): 1, (5, 6): 1}, (5, 6): {(5, 5): 1, (5, 7): 1},
                    (5, 7): {(4, 7): 1, (5, 6): 1, (6, 7): 1}, 
                    (6, 0): {(5, 0): 1, (6, 1): 1}, (6, 1): {(5, 1): 1, (6, 0): 1, (7, 1): 1}, (6, 2): {(5, 2): 1, (7, 2): 1}, 
                    (6, 3): {(5, 3): 1, (7, 3): 1}, (6, 4): {(5, 4): 1, (6, 5): 1, (7, 4): 1}, 
                    (6, 5): {(6, 4): 1, (6, 6): 1}, (6, 6): {(6, 5): 1}, (6, 7): {(5, 7): 1, (7, 7): 1}, 
                    (7, 0): {(7, 1): 1}, (7, 1): {(6, 1): 1, (7, 0): 1, (7, 2): 1}, (7, 2): {(6, 2): 1, (7, 1): 1}, 
                    (7, 3): {(6, 3): 1}, (7, 4): {(6, 4): 1, (7, 5): 1}, (7, 5): {(7, 4): 1, (7, 6): 1},
                    (7, 6): {(7, 5): 1, (7, 7): 1}, (7, 7): {(6, 7): 1, (7, 6): 1}}
    
    print("\nConstruction avec un graphe :")
    laby.construireAvecGraphe(graphe)
    print(laby)
    # input('Appuyez sur entrée')

    print("Le magasin sans rien dans les cases")
    laby.afficheMagasinVide()

    print(laby.getSortie())
    print(laby.getEntree())

    print('Test : class Fichier')
    fichier : Fichier = Fichier()

    print("\ttesting from json:", end= ' ')
    annuaireJS : Fichier = Fichier("exempleProjet.json")

    print(annuaireJS.getProduits())
    # input('Appuyez sur entrée')
    print(annuaireJS.getMagasin())
    # input('Appuyez sur entrée')
    print(annuaireJS.getAdresse())
    # input('Appuyez sur entrée')
    print(annuaireJS.getAuteur())
    # input('Appuyez sur entrée')
    print(annuaireJS.getDate())
    # input('Appuyez sur entrée')
    print(annuaireJS.getEntree())
    # input('Appuyez sur entrée')
    print(annuaireJS.getNomMagasin())
    # input('Appuyez sur entrée')
    print(annuaireJS.getNomProjet())
    # input('Appuyez sur entrée')
    print(annuaireJS.getSortie())

    annuaireJS.setFichierGraphe('aaa.json')
    annuaireJS.setFichierProduits('bbb.json')

    annuaireJS.save("test.json")

    annuaireJS.delete('test.json')