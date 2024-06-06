import sys
from pathlib import Path
from cadrillage import Case, Fichier, Magasin
from vueApp1 import VueMain
from PyQt6.QtWidgets import QApplication

class Controleur:
    
    def __init__(self):
            
        self.__path: str = sys.path[0]
        self.__images: str = self.__path + '\\images\\'
        self.__plans: str = self.__path[:-5] + '\\models\\'
        
        self.__current_projet: str = ""
        self.__projet_path: str = ""
        self.__check_projet: bool = False
        
        self.vue: VueMain = VueMain()
        self.modele: Magasin = Magasin("", 10, 10)
        self.fichier: Fichier = Fichier()
        self.vue.updatePlan(self.__plans + "plan1.jpg")
        
        self.vue.nouveauClicked.connect(self.nouveauProjet)
    
    
    def nouveauProjet(self, dico):
        self.__check_projet = True
        print(dico)
        self.modele = Magasin(self.vue.getX(), self.vue.getY(), 0, 0, 0, 0, dico["nom_magasin"])
        
        self.__current_projet = dico["Projet"]
        
        self.fichier.setAdresse(dico["adresse_magasin"])
        self.fichier.setAuteur(dico["Auteur"])
        self.fichier.setDate(dico["Date"])
        self.fichier.setImagePlan(dico["fichier_plan"])
        self.fichier.setNomMagasin(dico["nom_magasin"])
        self.fichier.setNomProjet(dico["Projet"])
        self.fichier.setFichierGraphe(dico["Projet"] + "_graphe")
        self.fichier.setFichierProduits(dico["Projet"] + "_produits")
        
        self.vue.updatePlan(dico["fichier_plan"])
        
    def ouvrirFichier(self, chemin: str):
        self.fichier.open(chemin)
        self.__current_projet = Path(chemin).parts[-1]
        self.__projet_path = chemin
    
    def enregistrerFichier(self):
        if self.__check_projet:
            self.fichier.setCasesMagasin(self.modele.getCases())
            self.fichier.save(self.__projet_path)
            
    def delete(self):
        self.fichier.delete(self.__current_projet)
        self.__check_projet = False


# --- main --------------------------------------------------------------------
if __name__ == "__main__":

    # création d'une QApplication
    app = QApplication(sys.argv)

    # # création de la fenêtre de l'application
    fenetre = Controleur()

    # lancement de l'application
    sys.exit(app.exec())    