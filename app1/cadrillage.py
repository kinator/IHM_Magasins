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
    modifStock() : change le stock d'un produit contenu dans la case
    removeContenu() : retire un produit au contenu de la case
    delContenu() : supprime le contenu de la case'''
    
    def __init__(self):
        self.__position: tuple = (0, 0)
        self.__est_stockable: bool = False
        self.__contenu: dict = {}
        self.__murs: list = ['N', 'S', 'E', 'W']
    
    def __init__(self, x: int, y: int, stock : bool):
        '''Méthode dédiée, constructeur de la classe'''
        self.__position: tuple = (x, y)
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


    def getContenu(self) -> dict:
        '''Méthode publique, renvoie le contenu de l'objet.'''
        return self.__contenu


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
        
    def modifStock(self, cakechose: Produit, stock: int) -> None:
        '''Méthode publique, affecte le contenu de l'objet.'''
        if cakechose in self.__contenu:
            self.__contenu = {cakechose.__str__ : stock} 
        
    def removeContenu(self, cakechose: Produit) -> None:
        '''Méthode publique, affecte le contenu de l'objet.'''
        self.__contenu.popitem(cakechose)
    
    def delContenu(self) -> None:
        '''Méthode publique, affecte le contenu de l'objet.'''
        self.__contenu = {}

class Magasin(object) :
    '''Classe définissant une grille à partir de ses dimensions
           largeur : nombre de cases en largeur
           hauteur : nombre de cases en longueur

Un objet, instance de cette classe, possède plusieurs méthodes :

    construireBordure() : construit les murs sur le contour du magasin
    detruireBordure() : détruit les murs sur le contour du magasin
    afficheMagasinVide() : affiche le magasin (sans contenu) avec tous les murs
    affichePlateau() : affiche le plateau (avec contenu et murs éventuels des cases)'''
    
    def __init__(self, largeur: int, hauteur: int):
        self.__largeur: int = largeur
        self.__hauteur: int = hauteur
        self.__cases: list = self.__creationMagasin()
        
        
    def __creationMagasin(self) -> list:
        '''Méthode privée, crée et renvoie la liste des cases'''
        liste_cases: list = []
        
        for y in range(self.__hauteur) :
            
            ligne_cases: list = []
        
            for x in range(self.__largeur) :
                nouvelle_case = Case(x, y)
                ligne_cases.append(nouvelle_case)
            
            liste_cases.append(ligne_cases)
        
        return liste_cases


    def getCases(self) -> list:
        '''Méthode publique, renvoie la liste des cases.'''
        return self.__cases


    def setContenu(self, position: tuple, cakechose: any) -> None:
        '''Méthode publique, affecte le contenu de la case à la position prévue.'''
        self.__cases[position[1]][position[0]].setContenu(cakechose)


    def getContenu(self, position: tuple) -> any:
        '''Méthode publique, renvoie le contenu de la case à la position prévue.'''
        return self.__cases[position[1]][position[0]].getContenu()


    def effaceContenu(self) -> None:
        '''Méthode publique, efface le contenu de toutes les cases.'''
        for y in range(self.__hauteur):
            for x in range(self.__largeur):
                self.__cases[y][x].setContenu(None)


    def construireAvecGraphe(self, graphe: dict) -> None:
        '''Méthode publique, définit les murs à partir d'un graphe.'''
        for case, voisines in graphe.items():
            x1, y1 = case

            for case_voisine in voisines:
                
                x2, y2 = case_voisine

                if y1 == y2 :
                    if x1 < x2 :
                        self.__cases[y1][x1].detruireMur('E')
                    else: 
                        self.__cases[y1][x1].detruireMur('W')
                else :
                    if y1 < y2 :
                        self.__cases[y1][x1].detruireMur('S')
                    else: 
                        self.__cases[y1][x1].detruireMur('N')


    def construireBordure(self) -> None:
        '''Méthode publique, définit une bordure extérieure de la grille.'''
        for colonne in range(self.__largeur) :
            self.__cases[0][colonne].construireMur('N')
            self.__cases[self.__hauteur - 1][colonne].construireMur('S')
        
        for ligne in range(self.__hauteur) :
            self.__cases[ligne][0].construireMur('W')
            self.__cases[ligne][self.__largeur - 1].construireMur('E')
    
    
    def detruireBordure(self) -> None:
        '''Méthode publique, enlève une bordure extérieure de la grille.'''
        for colonne in range(self.__largeur) :
            self.__cases[0][colonne].detruireMur('N')
            self.__cases[self.__hauteur - 1][colonne].detruireMur('S')
        
        for ligne in range(self.__hauteur) :
            self.__cases[ligne][0].detruireMur('W')
            self.__cases[ligne][self.__largeur - 1].detruireMur('E')
    
    
    def afficheMagasinVide(self) -> None:
        '''Méthode publique, affiche la grille vide avec tous les murs.'''                                
        for ligne in range(self.__hauteur) :
            print('+---' * self.__largeur + '+')
            print('|   ' * self.__largeur + '|')
            
        print('+---' * self.__largeur + '+\n')