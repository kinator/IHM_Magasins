import sys, modeleOutil, vueOutil
from PyQt6.QtWidgets import QApplication

# -----------------------------------------------------------------------------
# --- class Controleur
# -----------------------------------------------------------------------------
class Controleur() :

    # constructeur
    def __init__(self) -> None:

        # attributs
        self.modele = modeleOutil.Outil()
        self.vue = vueOutil.VueOutil()
        self.maj_vue() 
        
        # signaux venant de la vue ---> redirigés vers slots du controleur
        self.vue.precedentClicked.connect(self.precedent)
        self.vue.suivantClicked.connect(self.suivant)
        self.vue.ajoutClicked.connect(self.ajout)


    def precedent(self) -> None :
        self.modele.outilPrecedent()
        self.maj_vue()
    
    def suivant(self) -> None :
        self.modele.outilSuivant()
        self.maj_vue()

    def ajout(self, outil: str) -> None :
        if outil != '':
            self.modele.setOutil(outil)
            self.maj_vue()

    def maj_vue(self) -> None :
        outil_actuel = self.modele.getOutil()
        self.vue.updateVue(outil_actuel)
    
    
    
# Programme principal : test du controleur ------------------------------------
if __name__ == "__main__" :

    print('TEST: class Controleur')
    
    app = QApplication(sys.argv)
    
    control_outil = Controleur()
    
    sys.exit(app.exec())