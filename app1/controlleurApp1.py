import sys
from cadrillage import Case, Fichier, Magasin
from vueApp1 import VueMain
from PyQt6.QtWidgets import QApplication

class Controleur:
    
    def __init__(self):
            
        self.__path: str = sys.path[0]
        self.__images: str = self.__path + '\\images\\'
        self.__plans: str = self.__path[:-5] + '\\models\\'
        
        self.__projet_path: str = ""
        self.__check_projet: bool = False
        
        self.vue: VueMain = VueMain()
        self.modele: Magasin = Magasin("", 10, 10)
        self.fichier: Fichier = Fichier()
                
        self.vue.nouveauClicked.connect(self.nouveauProjet)
        self.vue.openClicked.connect(self.ouvrirFichier)
        self.vue.caseCliquee.connect(self.setFocusPlan)
        self.vue.ajoutProduit.connect(self.ajouterProduit)

    
    def nouveauProjet(self, dico) -> None:
        self.__check_projet = True
        print(dico)
        self.modele = Magasin(dico["nom_magasin"], self.vue.getX(), self.vue.getY(), (0,0), (0,0) )
        
        self.__current_projet = dico["Projet"]
        
        self.fichier.setAdresse(dico["adresse_magasin"])
        self.fichier.setAuteur(dico["Auteur"])
        self.fichier.setDate(dico["Date"])
        self.fichier.setImagePlan(dico["fichier_plan"])
        self.fichier.setNomMagasin(dico["nom_magasin"])
        self.fichier.setNomProjet(dico["Projet"])
        self.fichier.setFichierGraphe(dico["Projet"] + "_graphe")
        self.fichier.setFichierProduits(dico["Projet"] + "_produits")
        
        self.updateVue()
                
    def ouvrirFichier(self, chemin: str) -> None:
        self.fichier.open(chemin)
        self.__projet_path = chemin
        self.modele.construireAvecGraphe(self.fichier.getMagasin())
        self.modele.setEntree(self.fichier.getEntree())
        self.modele.setSortie(self.fichier.getSortie())
        
        self.updateVue()
    
    def enregistrerFichier(self) -> None:
        if self.__check_projet:
            self.fichier.setCasesMagasin(self.modele.getCases())
            self.fichier.save(self.__projet_path)
            
    def delete(self) -> None:
        self.fichier.delete(self.__projet_path)
        self.__check_projet = False

    def updateVue(self) -> None:
        self.vue.updatePlan(self.fichier.getImagePlan())
        
    def setFocusPlan(self, t: tuple) -> None:
        self.vue.plan.setFocus(self.modele.getCase(t))
        
    def ajouterProduit(self, produit: str, case: tuple) -> None:
        self.modele.setContenu(case, produit)
        self.vue.updateListProduits(self.modele.getCase(case).getContenu())
        
# --- main --------------------------------------------------------------------
if __name__ == "__main__":

    # création d'une QApplication
    app = QApplication(sys.argv)

    # # création de la fenêtre de l'application
    fenetre = Controleur()

    # lancement de l'application
    sys.exit(app.exec())    