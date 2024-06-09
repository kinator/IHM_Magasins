import sys, random, json
from os import listdir
from PyQt6.QtWidgets import QApplication, QLabel, QMainWindow, QToolBar, QStatusBar, QWidget, QPushButton, QFileDialog, QDockWidget, QHBoxLayout, QVBoxLayout, QLineEdit, QDateEdit, QSpinBox, QScrollArea, QTextEdit
from PyQt6.QtGui import QPixmap, QIcon, QAction, QCursor, QColor, QPen, QPainter, QPolygon
from PyQt6.QtCore import Qt, pyqtSignal, QDate, QPoint, QRect, QEvent

import map
import parcours

class Image(QLabel):
    
    caseClicked: pyqtSignal = pyqtSignal(tuple)

    def __init__(self, chemin: str, height: int, width: int, supermarche, chemin_optimal):
        '''Constructeur de la classe'''

        # appel au constructeur de la classe mère
        super().__init__()

        self.supermarche = supermarche
        self.chemin_optimal = chemin_optimal
        
        self.limHeight, self.limWidth = supermarche.get_height(), supermarche.get_width()
        self.toggleGrillage = False
        
        self.__chemin = chemin
        self.cubeList = {}
        self.focusCase = ()

        # Initialisation de l'image
        self.image = QPixmap(self.__chemin)
        self.image = self.image.scaled(int(width*0.8), int(height*0.7), transformMode= Qt.TransformationMode.FastTransformation)

        layout = QVBoxLayout()
        self.setLayout(layout)

        p = self.palette()
        self.setPalette(p)

        self.heightCadre = self.image.height()
        self.widthCadre = self.image.width()

        self.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.mousePressEvent = self.clickCase

        self.show()
    
    def getToggle(self) -> bool:
        return self.toggleGrillage
    
    def updateImage(self, chemin) -> None:
        self.__chemin = chemin
        self.image = QPixmap(chemin)
        self.image = self.image.scaled(int(self.width()*0.8), int(self.height()*0.7), transformMode= Qt.TransformationMode.FastTransformation)
        
    def updateCadrillage(self) -> None:
        self.cubeList = {}
        cell_width = self.rectangle.width() // self.limWidth
        cell_height = self.rectangle.height() // self.limHeight

        for i in range(self.limHeight):
            for j in range(self.limWidth):
                self.cubeList[f"({i},{j})"] = {}
                self.cubeList[f"({i},{j})"]["rect"] = QRect(j * cell_width, i * cell_height, cell_width, cell_height)
                self.cubeList[f"({i},{j})"]["poly"] = QPolygon(self.cubeList[f"({i},{j})"]["rect"])
        
    def paintEvent(self, event) -> None:
        self.qp = QPainter(self)
        self.qp.setPen(QColor("black"))
        self.rectangle = QRect(0, 0, self.width(), self.height())
        self.qp.drawPixmap(self.rectangle, self.image)

        self.updateCadrillage()
        self.afficherGrille()
        self.afficherArticlesEtChemin()

        self.qp.end()

    def afficherGrille(self) -> None:
        if self.toggleGrillage == True:
            for i in range(self.limHeight):
                for j in range(self.limWidth):
                    self.qp.drawRect(self.cubeList[f"({i},{j})"]["rect"])

    def afficherArticlesEtChemin(self) -> None:
        # Dessiner les articles
        for (x, y), case in self.supermarche.cellules.items():
            if case.articles:
                self.qp.setBrush(QColor(255, 0, 0))  # Rouge pour les articles
                self.qp.drawRect(self.cubeList[f"({y},{x})"]["rect"])

        # Dessiner le chemin optimal
        if self.chemin_optimal:
            self.qp.setBrush(QColor(0, 255, 0))  # Vert pour le chemin
            for (x, y) in self.chemin_optimal:
                self.qp.drawRect(self.cubeList[f"({y},{x})"]["rect"])

        # Dessiner le point de départ et d'arrivée
        depart = self.supermarche.get_depart()
        arrivee = self.supermarche.get_arrivee()

        self.qp.setBrush(QColor(255, 165, 0))  # Orange pour le départ
        self.qp.drawRect(self.cubeList[f"({depart[1]},{depart[0]})"]["rect"])

        self.qp.setBrush(QColor(0, 0, 255))  # Bleu pour l'arrivée
        self.qp.drawRect(self.cubeList[f"({arrivee[1]},{arrivee[0]})"]["rect"])

    def supprimerGrille(self) -> None:
        self.cubeList = []
    
    def setCouleurCase(self) -> None:
        pass
    
    def setCaseWidth(self, num: int = 75) -> None:
        self.limWidth = num
        self.update()

    def setCaseHeight(self, num: int = 75) -> None:
        self.limHeight = num
        self.update()

    def setToggle(self, b: bool) -> None:
        self.toggleGrillage = b
        self.update()
    
    def updateAll(self, path):
        self.updateImage(path)
        self.update()
    
    def clickCase(self, event):
        if self.toggleGrillage:
            pos = event.pos()
            i = 0
            j = 0

            while i + j < self.limWidth + (self.limHeight-1) and not self.cubeList[f"({j},{i})"]["poly"].containsPoint(pos, Qt.FillRule.OddEvenFill):
                i += 1
                if i % self.limWidth == 0:
                    i = 0
                    j += 1
                
            self.caseClicked.emit((j,i))
        else: self.focusCase = None
      
    def setFocus(self, case) -> None:
        self.focusCase = case.getPosition()
    
    def getFocus(self) -> tuple:
        return self.focusCase
    
    def isFocused(self) -> bool:
        return self.focusCase != None


class MainWindow(QMainWindow):
    def __init__(self, supermarche, chemin_optimal):
        super().__init__()

        self.supermarche = supermarche
        self.chemin_optimal = chemin_optimal

        self.initUI()

    def initUI(self):
        self.setWindowTitle('Supermarché')

        self.image_widget = Image("./plan/plan4.png", self.height(), self.width(), self.supermarche, self.chemin_optimal)
        self.setCentralWidget(self.image_widget)

        self.showMaximized()


def main():
    app = QApplication(sys.argv)

    supermarche = map.mapping("supermarche.json", "produits.json", "panier.json")

    points_interet = supermarche.coordonnees_par_article()
    depart = supermarche.get_depart()
    arrivee = supermarche.get_arrivee()
    chemin_optimal = parcours.parcours_opti(supermarche.get_parcours(), depart, arrivee, points_interet)

    main_window = MainWindow(supermarche, chemin_optimal)

    sys.exit(app.exec())

if __name__ == '__main__':
    main()
