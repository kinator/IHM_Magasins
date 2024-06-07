import sys, random, json
from os import listdir
from PyQt6.QtWidgets import QApplication, QLabel, QMainWindow, QToolBar, QStatusBar, QWidget, QPushButton, QFileDialog, QDockWidget, QHBoxLayout, QVBoxLayout, QLineEdit, QDateEdit, QSpinBox, QScrollArea, QTextEdit
from PyQt6.QtGui import QPixmap, QIcon, QAction, QCursor, QColor, QPen, QPainter, QPolygon
from PyQt6.QtCore import Qt, pyqtSignal, QDate, QPoint, QRect, QEvent

class Image(QLabel):
    
    caseClicked: pyqtSignal = pyqtSignal(tuple)

    def __init__(self, chemin: str, height: int, width: int):
        '''Constructeur de la classe'''

        # appel au constructeur de la classe mère
        super().__init__()
        
        self.limHeight, self.limWidth = 75, 75
        self.toggleGrillage = False
        
        self.__chemin = chemin
        self.cubeList = {}
        self.focusCase = ()

        #Initialisation de l'image
        self.image = QPixmap(self.__chemin)
        self.image = self.image.scaled(int(width*0.8), int(height*0.7),transformMode= Qt.TransformationMode.FastTransformation)

        layout = QVBoxLayout()
        self.setLayout(layout)

        p = self.palette()
        self.setPalette(p)

        self.heightCadre = self.image.height()
        self.widthCadre = self.image.width()

        self.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.mousePressEvent = self.clickCase

        self.show()
    
    #renvoie si la grille est afficher ou pas
    def getToggle(self) -> bool:
        return self.toggleGrillage
    
    #prend le chemin d'une image et l'affiche
    def updateImage(self, chemin) -> None:
        self.__chemin = chemin
        self.image = QPixmap(chemin)
        self.image = self.image.scaled(int(self.width()*0.8), int(self.height()*0.7),transformMode= Qt.TransformationMode.FastTransformation)
        
    #recrée le grillage *pas fini*
    def updateCadrillage(self) -> None:
        if self.toggleGrillage  == True:
            i, j = 1, 1
            self.cubeList = {}
            
            for i in range(self.limHeight):
                for j in range(self.limWidth):
                    self.cubeList[f"({i},{j})"] = {}
                    self.cubeList[f"({i},{j})"]["rect"] = QRect(int(self.rectangle.width() / self.limWidth * j), int(self.rectangle.height() / self.limHeight * i), int(self.rectangle.width() / self.limWidth), int(self.rectangle.height() / self.limHeight))
                    self.cubeList[f"({i},{j})"]["poly"] = QPolygon(QRect(int(self.rectangle.width() / self.limWidth * j), int(self.rectangle.height() / self.limHeight * i), int(self.rectangle.width() / self.limWidth), int(self.rectangle.height() / self.limHeight)))
        
    #Fonction qui permet d'afficher le grillage et l'image à chaque changement de la vue
    def paintEvent(self, event) -> None:
        self.qp = QPainter(self)
        self.qp.setPen(QColor("black"))
        self.rectangle = QRect(0, 0, self.width(), self.height())
        self.qp.drawPixmap(self.rectangle, self.image)
        self.updateCadrillage()
        self.afficherGrille()

        self.qp.end()

    #Fonction qui dessine le grillage
    def afficherGrille(self) -> None:
        if self.toggleGrillage == True:
            for i in range(self.limHeight):
                for j in range(self.limWidth):
                    self.qp.drawRect(self.cubeList[f"({i},{j})"]["rect"])

    #Fonction qui supprime le grillage
    def supprimerGrille(self) -> None:
        self.cubeList = []
    
    #Change la couleur du grillage *pas fini*
    def setCouleurCase(self) -> None:
        pass
    
    #Change la longueur du grillage
    def setCaseWidth(self, num: int = 75) -> None:
        self.limWidth = num
        self.update()

    #change la hauteur du grillage
    def setCaseHeight(self, num: int = 75) -> None:
        self.limHeight = num
        self.update()

    #Défini si la grille doit être afficher ou pas
    def setToggle(self, b: bool) -> None:
        self.toggleGrillage = b
        self.update()
    
    #update l'image et le grillage
    def updateAll(self, path):
        self.updateImage(path)
        self.update()
    
    #Activer lors du clique sur une case, renvoie la position de la case
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
      
    #Défini la case qui a été sélectionnée
    def setFocus(self, case) -> None:
        self.focusCase = case.getPosition()
    
    #Renvoie la position de la case sélectionnée
    def getFocus(self) -> tuple:
        return self.focusCase
    
    #Renvoie si une case est sélectionnée
    def isFocused(self) -> bool:
        return self.focusCase != None