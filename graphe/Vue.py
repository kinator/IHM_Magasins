import sys
from os import listdir
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QDockWidget, QPushButton, QLabel, QSizePolicy, QScrollBar, QScrollArea
from PyQt6.QtCore import Qt, pyqtSignal
from PyQt6.QtGui import QAction
import widget
import map
import parcours

class Vue(QMainWindow):
    def __init__(self):
        super().__init__()
        
        # Configuration de la fenêtre principale
        self.setWindowTitle("Gestion magasin")

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
        self.DockG.setFixedHeight(890)
        self.DockG.setFixedWidth(230)

        self.WidgetDockDroit = QWidget()
        self.layoutDDock = QVBoxLayout()
        self.WidgetDockDroit.setLayout(self.layoutDDock)
        
        self.VerifBtn = QPushButton("Mettre à jour")
        self.layoutDDock.addWidget(self.VerifBtn)

        self.DockD = QDockWidget('Panier : ')
        self.addDockWidget(Qt.DockWidgetArea.RightDockWidgetArea, self.DockD)
        self.DockD.setWidget(self.WidgetDockDroit)
        self.DockD.setFixedHeight(890)
        self.DockD.setFixedWidth(230)
        
        # Load data for the widget
        self.supermarche = map.mapping("supermarche.json", "produits.json", "panier.json")
        points_interet = self.supermarche.coordonnees_par_article()
        depart = self.supermarche.get_depart()
        arrivee = self.supermarche.get_arrivee()
        self.chemin_optimal = parcours.parcours_opti(self.supermarche.get_parcours(), depart, arrivee, points_interet)
        
        # Création du widget central
        self.centralWidget = QWidget()
        self.centralLayout = QVBoxLayout(self.centralWidget)
        self.image_widget = widget.Image("./plan/plan4.png", self.height(), self.width(), self.supermarche, self.chemin_optimal)
        self.centralLayout.addWidget(self.image_widget)
        self.setCentralWidget(self.centralWidget)
        
        # Changement de style
        for file in listdir("./fichiers_qss/"):
            if file.endswith(".qss"):
                self.variables = {}
                self.variables[f"action_style + file.removesuffix('.qss')"] = QAction(text=file.removesuffix(".qss"), parent=self)
                self.theme.addAction(self.variables[f"action_style + file.removesuffix('.qss')"])        
                self.variables[f"action_style + file.removesuffix('.qss')"].triggered.connect(self.changeStyle)
        
        self.show()
        
        # Connecter le bouton "Mettre à jour" à la méthode save_right_dock du contrôleur
        self.VerifBtn.clicked.connect(self.save_right_dock)
        
    def changeStyle(self):
        with open("./fichiers_qss/" + self.sender().text() + ".qss", "r") as f:
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

    def update_path(self, chemin_optimal):
        self.chemin_optimal = chemin_optimal
        self.image_widget.chemin_optimal = chemin_optimal
        self.image_widget.update()  # Redraw the widget with the new path

def main():
    app = QApplication(sys.argv)
    vue = Vue()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()
