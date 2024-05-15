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