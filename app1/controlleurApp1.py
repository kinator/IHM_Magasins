import sys
from cadrillage import Case, Fichier, Magasin
from vueApp1 import VueMain
from PyQt6.QtWidgets import QApplication

class Controleur:
    
    def __init__(self):
        
        self.__projet_path: str = ""
        self.__check_projet: bool = False
        
        self.vue: VueMain = VueMain()
        self.modele: Magasin = Magasin("", 10, 10)
        self.fichier: Fichier = Fichier()
                
        self.vue.nouveauClicked.connect(self.nouveauProjet)
        self.vue.openClicked.connect(self.ouvrirFichier)
        self.vue.deleteClicked.connect(self.deleteFichier)
        self.vue.caseCliquee.connect(self.setFocusPlan)
        self.vue.ajoutProduit.connect(self.ajouterProduit)
        self.vue.choixEntree.connect(self.setEntree)
        self.vue.choixSortie.connect(self.setSortie)
        self.vue.tailleChanger.connect(self.modifTaille)

    
    def nouveauProjet(self, dico) -> None:
        self.__check_projet = True
        self.modele = Magasin(dico["nom_magasin"], self.vue.getX(), self.vue.getY(), (0,0), (0,0) )
        
        self.__current_projet = dico["projet"]
        
        self.fichier.setAdresse(dico["adresse_magasin"])
        self.fichier.setAuteur(dico["auteur"])
        self.fichier.setDate(dico["date"])
        self.fichier.setImagePlan(dico["fichier_plan"])
        self.fichier.setNomMagasin(dico["nom_magasin"])
        self.fichier.setNomProjet(dico["projet"])
        self.fichier.setFichierGraphe(dico["projet"] + "_graphe")
        self.fichier.setFichierProduits(dico["projet"] + "_produits")
        
        self.updateVue()
                
    def ouvrirFichier(self, chemin: str) -> None:
        self.fichier.open(chemin)
        self.__projet_path = chemin
        self.modele.construireAvecGraphe(self.fichier.getMagasin())
        self.modele.setDict(self.fichier.getProduits())
        self.modele.setEntree(self.fichier.getEntree())
        self.modele.setSortie(self.fichier.getSortie())
        self.vue.setEntree(self.fichier.getEntree())
        self.vue.setSortie(self.fichier.getSortie())
        
        self.updateVue()
    
    def enregistrerFichier(self) -> None:
        if self.__check_projet:
            self.fichier.setCasesMagasin(self.modele.getCases())
            self.fichier.setEntree(self.modele.getEntree())
            self.fichier.setSortie(self.modele.getSortie())
            self.fichier.save(self.__projet_path)
            
    def deleteFichier(self) -> None:
        self.fichier.delete(self.__projet_path)
        self.__check_projet = False

    def updateVue(self) -> None:
        self.vue.updatePlan(self.fichier.getImagePlan())
        
    def setFocusPlan(self, case: tuple) -> None:
        self.vue.plan.setFocus(self.modele.getCase(case))
        self.vue.updateListProduits(self.modele.getCase(case).getContenu())
        
    def ajouterProduit(self, produit: str, case: tuple) -> None:
        self.modele.setContenu(case, produit)
        self.vue.updateListProduits(self.modele.getCase(case).getContenu())
        
    def setEntree(self, case : tuple) -> None:
        self.modele.setEntree(case)
        self.vue.setEntree(case)

    def setSortie(self, case : tuple) -> None:
        self.modele.setSortie(case)
        self.vue.setSortie(case)
        
    def modifTaille(self, height: int, width: int) -> None:
        self.modele.setHeight(height)
        self.modele.setWidth(width)
        self.modele.creationMagasin()


# --- main --------------------------------------------------------------------
if __name__ == "__main__":

    # création d'une QApplication
    app = QApplication(sys.argv)

    # # création de la fenêtre de l'application
    fenetre = Controleur()

    # lancement de l'application
    sys.exit(app.exec())    