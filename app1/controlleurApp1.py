import sys
from cadrillage import Case
from vueApp1 import VueMain
from PyQt6.QtWidgets import QApplication

class Controleur:
    
    def __init__(self):
            
        self.__path: str = sys.path[0]
        self.__styles: str = self.__path + '\\fichiers_qss\\'
        self.__images: str = self.__path + '\\images\\'
        
        self.vue: VueMain = VueMain()
        self.vue.updatePlan(self.__images + "icon.png")


# --- main --------------------------------------------------------------------
if __name__ == "__main__":

    # création d'une QApplication
    app = QApplication(sys.argv)

    # # création de la fenêtre de l'application
    fenetre = Controleur()

    # lancement de l'application
    sys.exit(app.exec())    