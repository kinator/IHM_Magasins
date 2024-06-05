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
        self.DockG.setFixedHeight(700)
        self.DockG.setFixedWidth(200)

        
        self.WidgetDockDroit = QWidget()
        self.layoutDDock = QVBoxLayout()
        self.WidgetDockDroit.setLayout(self.layoutDDock)
        

        self.DockD = QDockWidget('Nouvelle liste : ')
        self.addDockWidget(Qt.DockWidgetArea.RightDockWidgetArea, self.DockD)
        self.DockD.setWidget(self.WidgetDockDroit)
        self.DockD.setFixedHeight(700)
        self.DockD.setFixedWidth(200)
        
        self.show()
        
        # Connecter l'action "Enregistrer-sous" à une fonction pour sauvegarder le dock droit
        self.save_as.triggered.connect(self.save_right_dock)
        
    def set_controller(self, controller):
        self.controller = controller

    def reload_json(self):
        if hasattr(self, 'controller'):
            self.controller.reload_json()

    def save_right_dock(self):
        if hasattr(self, 'controller'):
            self.controller.save_right_dock()

    def update_docks(self):
        # Mettre à jour les contenus des docks sans recréer les docks eux-mêmes
        self.DockG.widget().update()
        self.DockD.widget().update()

   
    
    
    
