import os


# -----------------------------------------------------------------------------
# --- class Outil
# -----------------------------------------------------------------------------
class Outil():

    # constructeur
    def __init__(self) -> None:
        
        # attributs
        self.__liste: list[str] = ['Style au bleu', "Crayon de bois d'arbre",
                                   'Go Meuh', 'Règle', 'PasCon', 'Feutres', 
                                   'Crayons colorés','Equerre avec angle droit',
                                   'Calcoul à triche']
        self.__indice: int = 0

    def getListe(self) -> list :
        return self.__liste
 
    def getOutil(self) -> str :
        return self.__liste[self.__indice]
    
    def setOutil(self, outil: str) -> None :
        self.__liste.append(outil)
        self.__indice = len(self.__liste) - 1

    def outilSuivant(self) -> str :
        self.__indice = (self.__indice + 1) % len(self.__liste)

    def outilPrecedent(self) -> str :
        self.__indice = (self.__indice - 1) % len(self.__liste)

    

# Programme principal : test du modèle ----------------------------------------
if __name__ == "__main__" :
    
    print('TEST: class Outil')

    caisse = Outil()
    print('Contenu de la caisse :\n', caisse.getListe())
    
    print('\nPremier outil disponible :', caisse.getOutil())
    
    caisse.outilSuivant()
    print('\nDeuxième outil disponible :', caisse.getOutil())
    