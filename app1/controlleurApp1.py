import sys
from cadrillage import Case
from vueApp1 import VueMain
from PyQt6.QtWidgets import QApplication

class Controleur:
    
    def __init__(self):
            
        self.__path: str = sys.path[0]
        self.__images: str = self.__path + '\\images\\'
        self.__plans: str = self.__path[:-5] + '\\models\\'
        self.__projets: str = self.__path[:-5] + '\\projects\\'
        
        self.vue: VueMain = VueMain()
        self.vue.updatePlan(self.__plans + "plan1.jpg")
        
        self.vue.nouveauClicked.connect(self.nouveauProjet)
        
    
    def nouveauProjet(self, dico):
        print(dico)


# --- main --------------------------------------------------------------------
if __name__ == "__main__":

    # création d'une QApplication
    app = QApplication(sys.argv)

    # # création de la fenêtre de l'application
    fenetre = Controleur()

    # lancement de l'application
    sys.exit(app.exec())    