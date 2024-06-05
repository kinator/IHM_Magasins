import sys
from cadrillage import Case, Fichier, Magasin
from vueApp1 import VueMain
from PyQt6.QtWidgets import QApplication

class Controleur:
    
    def __init__(self):
            
        self.__path: str = sys.path[0]
        self.__images: str = self.__path + '\\images\\'
        self.__plans: str = self.__path[:-5] + '\\models\\'
        self.__projets: str = self.__path[:-5] + '\\projects\\'
        
        self.vue: VueMain = VueMain()
        self.modele: Magasin = Magasin()
        self.fichier: Fichier = Fichier()
        self.vue.updatePlan(self.__plans + "plan1.jpg")
        
        self.vue.nouveauClicked.connect(self.nouveauProjet)
        
    
    def nouveauProjet(self, dico):
        print(dico)
        self.modele = Magasin(self.vue.getX(), self.vue.getY(), 0, 0, 0, 0, dico["nom_magasin"])
        
        self.fichier.setAdresse(dico["adresse_magasin"])
        self.fichier.setAuteur(dico["Auteur"])
        self.fichier.setDate(dico["Date"])
        self.fichier.setFichierPlan(dico["fichier_plan"])
        self.fichier.setNomMagasin(dico["nom_magasin"])
        self.fichier.setNomProjet(dico["Projet"])
        
        self.vue.updatePlan(dico["fichier_plan"])
        
    def ouvrirFichier(self):
        pass
        
    #Exemple fichier Json
    #{"cases" :
    #   [
    #       {"x" : 1, "y": 2, "produits" : [{"id" : 1, "nom": "carotte", "stock" : 10}, {"id" : 1, "nom": "pomme_de_terre", "stock" : 5}]}, 
    #       {"x" : 4, "y": 3, "produits" : [{"id" : 3, "nom": "fraise", "stock" : 99}]}
    #   ],
    #   "projet" : {"Projet" : "projet magasin", "Auteur" : "tom", "Date" : "(2001, 2 ,5)", "nom_magasin" : "nom_mag", "adresse_magasin" : "adresse", "fichier_plan" : "chemin\\fichier.text"}
    #}


# --- main --------------------------------------------------------------------
if __name__ == "__main__":

    # création d'une QApplication
    app = QApplication(sys.argv)

    # # création de la fenêtre de l'application
    fenetre = Controleur()

    # lancement de l'application
    sys.exit(app.exec())    