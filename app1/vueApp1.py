import sys
from PyQt6.QtWidgets import QApplication, QLabel
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt

class Image(QLabel):

    def __init__(self):
        '''Constructeur de la classe'''

        # appel au constructeur de la classe mère
        super().__init__() 
        
        self.image = QPixmap('./models/plan1.jpg')
        self.setPixmap(self.image)

        self.show()


# --- main --------------------------------------------------------------------
if __name__ == "__main__":

    # création d'une QApplication
    app = QApplication(sys.argv)

    # # création de la fenêtre de l'application
    fenetre = Image()

    # lancement de l'application
    sys.exit(app.exec())