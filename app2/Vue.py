import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QDockWidget, QPushButton, QLabel, QSizePolicy, QScrollBar, QScrollArea
from PyQt6.QtCore import Qt, pyqtSignal
from PyQt6.QtGui import QAction

class Vue(QMainWindow):
    
    
    def __init__(self):
        super().__init__()
        
        # Configuration de la fenêtre principale
        self.setWindowTitle("Gestion magasin")
        self.setFixedHeight(800)
        self.setFixedWidth(1200)

        # Création de la barre de menu
        self.bar = self.menuBar()
        self.bar.setFixedHeight(30)

        # Création des menus
        self.theme = self.bar.addMenu('&Thème')

        # Création des actions de menu
        self.white_theme = QAction('&Thème Clair', self)
        self.black_theme = QAction('&Thème Sombre', self)

        # Ajout des actions aux menus
        self.theme.addAction(self.white_theme)
        self.theme.addAction(self.black_theme)
        
        # Création des docks et des layouts
        self.WidgetDockGauche = QWidget()
        self.layoutGDock = QVBoxLayout()
        self.WidgetDockGauche.setLayout(self.layoutGDock)

        self.DockG = QDockWidget('Articles : ')
        self.addDockWidget(Qt.DockWidgetArea.LeftDockWidgetArea, self.DockG)
        self.DockG.setWidget(self.WidgetDockGauche)
        self.DockG.setFixedHeight(700)
        self.DockG.setFixedWidth(200)

        self.WidgetDockDroit = QWidget()
        self.layoutDDock = QVBoxLayout()
        self.WidgetDockDroit.setLayout(self.layoutDDock)
        
        self.VerifBtn = QPushButton("Mettre à jour")
        self.layoutDDock.addWidget(self.VerifBtn)

        self.DockD = QDockWidget('Panier : ')
        self.addDockWidget(Qt.DockWidgetArea.RightDockWidgetArea, self.DockD)
        self.DockD.setWidget(self.WidgetDockDroit)
        self.DockD.setFixedHeight(700)
        self.DockD.setFixedWidth(200)
        
        # Création du widget central
        self.centralWidget = QWidget()
        self.centralLayout = QVBoxLayout()
        self.centralWidget.setLayout(self.centralLayout)
        self.setCentralWidget(self.centralWidget)
        
        # Changement de style
        for file in listdir(self.__styles):
            if file.endswith(".qss"):
                self.variables = {}
                self.variables[f"action_style + file.removesuffix('.qss')"] = QAction(text=file.removesuffix(".qss"), parent=self)
                menu_style.addAction(self.variables[f"action_style + file.removesuffix('.qss')"])        
                self.variables[f"action_style + file.removesuffix('.qss')"].triggered.connect(self.changeStyle)
        
        self.show()
        
        # Connecter le bouton "Mettre à jour" à la méthode save_right_dock du contrôleur
        self.VerifBtn.clicked.connect(self.save_right_dock)
        
    def changeStyle(self):
        with open(self.__styles + self.sender().text() + ".qss", "r") as f:
            self.currentstyle = f.read()
            self.setStyleSheet(self.currentstyle)
        
    def set_controller(self, controller):
        self.controller = controller


    def save_right_dock(self):
        if hasattr(self, 'controller'):
            self.controller.save_right_dock()

    def update_docks(self):
        # Mettre à jour les contenus des docks sans recréer les docks eux-mêmes
        self.DockG.widget().update()
        self.DockD.widget().update()

   
    
    
    
