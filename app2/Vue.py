import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QDockWidget, QPushButton, QLabel
from PyQt6.QtCore import Qt, pyqtSignal
from PyQt6.QtGui import QAction

class Vue(QMainWindow):
    
    
    def __init__(self, controller):
        super().__init__()
        
        self.controller = controller

        # Configuration de la fenêtre principale
        self.setWindowTitle("Gestion magasin")
        self.setFixedHeight(800)
        self.setFixedWidth(1200)

        # Création de la barre de menu
        self.bar = self.menuBar()
        self.bar.setFixedHeight(30)

        # Création des menus
        self.folder = self.bar.addMenu('&Fichier')
        self.navigate = self.bar.addMenu('&Naviguer')
        self.theme = self.bar.addMenu('&Thème')

        # Création des actions de menu
        self.new = QAction('&Nouveau', self)
        self.new.setShortcut("ALT+CTRL+N")
        self.open = QAction('&Ouvrir', self)
        self.open.setShortcut("CTRL+O")
        self.save = QAction('&Enregistrer', self)
        self.save.setShortcut("CTRL+S")
        self.save_as = QAction('&Enregistrer-sous', self)
        self.save_as.setShortcut("CTRL+SHIFT+S")
        self.back = QAction('&Revenir en arrière', self)
        self.back.setShortcut("CTRL+Z")
        self.restore = QAction('&Rétablir', self)
        self.restore.setShortcut("CTRL+Y")
        self.white_theme = QAction('&Thème Clair', self)
        self.black_theme = QAction('&Thème Sombre', self)

        # Ajout des actions aux menus
        self.folder.addAction(self.new)
        self.folder.addAction(self.open)
        self.folder.addAction(self.save)
        self.folder.addAction(self.save_as)
        self.navigate.addAction(self.back)
        self.navigate.addAction(self.restore)
        self.theme.addAction(self.white_theme)
        self.theme.addAction(self.black_theme)

        # Création des docks et des layouts
        self.WidgetDockGauche = QWidget()
        self.layoutGDock = QVBoxLayout()
        self.WidgetDockGauche.setLayout(self.layoutGDock)

        self.DockG = QDockWidget('Articles : ')
        self.addDockWidget(Qt.DockWidgetArea.LeftDockWidgetArea, self.DockG)
        self.DockG.setWidget(self.WidgetDockGauche)
        self.DockG.setFixedHeight(600)
        self.DockG.setFixedWidth(200)

        self.WidgetDockCentre = QWidget()
        self.layoutDDock = QVBoxLayout()
        self.WidgetDockCentre.setLayout(self.layoutDDock)

        self.DockD = QDockWidget('Détails : ')
        self.addDockWidget(Qt.DockWidgetArea.RightDockWidgetArea, self.DockD)
        self.DockD.setWidget(self.WidgetDockCentre)
        self.DockD.setFixedHeight(600)
        self.DockD.setFixedWidth(200)

   
    # def display_data(self, data):
    #     for value in data.items():
    #         label = QPushButton(f"{value}")
    #         self.layoutGDock.addWidget(label)
    
    def display_data(self, data):
        for items in data.items():
            for item in items:
                button = QPushButton(f"{item}")
                self.layoutGDock.addWidget(button)
    