import sys, time, json
from os import listdir
from PyQt6.QtWidgets import QApplication, QLabel, QMainWindow, QToolBar, QStatusBar, QWidget, QGridLayout, QPushButton, QFileDialog, QDockWidget, QHBoxLayout, QVBoxLayout
from PyQt6.QtGui import QPixmap, QIcon, QAction, QCursor
from PyQt6.QtCore import Qt, pyqtSignal

class Image(QLabel):

    def __init__(self, chemin: str):
        '''Constructeur de la classe'''

        # appel au constructeur de la classe mère
        super().__init__() 
        
        self.image = QPixmap(chemin)
        self.setPixmap(self.image)
        
        self.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

##############################################################################
##############################################################################

class PopupFichier(QWidget):
    chosenFile : pyqtSignal = pyqtSignal(bool)

    def __init__(self, style: str):
        '''Constructeur de la classe'''

        # appel au constructeur de la classe mère
        super().__init__() 
        
        self.__path: str = sys.path[0]
        self.__images: str = self.__path + '\\images\\'
        self.setStyleSheet(style)
        
        self.setWindowTitle("Création d'un nouveau projet")
        self.setWindowIcon(QIcon(self.__images + 'Alteur_Table.JPG'))
        self.setFixedHeight(400)
        self.setFixedWidth(500)
        
        layout = QGridLayout()
        self.setLayout(layout)

        self.confirm_button : QPushButton = QPushButton('Confirmer', self)        
        self.quit_button: QPushButton = QPushButton("Quitter", self)
        
        layout.addWidget(self.confirm_button)
        layout.addWidget(self.quit_button)

        self.quit_button.clicked.connect(self.clickCancel)
        self.confirm_button.clicked.connect(self.ClickConfirm)
        
        self.show()


    def clickCancel(self):
        self.chosenFile.emit(False)
        print('False')
        self.close()

    def ClickConfirm(self):
        self.chosenFile.emit(True)
        print('True')
        self.close()

##############################################################################
##############################################################################

class VueMain(QMainWindow):

    # Création des signaux
    nouveauClicked : pyqtSignal = pyqtSignal()
    saveClicked : pyqtSignal = pyqtSignal()
    saveUnderClicked : pyqtSignal = pyqtSignal(str)
    openClicked : pyqtSignal = pyqtSignal(str)
    deleteClicked : pyqtSignal = pyqtSignal()
    annulerClicked : pyqtSignal = pyqtSignal()
    retablirClicked : pyqtSignal = pyqtSignal()

    def __init__(self):
        '''Constructeur de la classe'''

        # appel au constructeur de la classe mère
        super().__init__()
        
        self.__path: str = sys.path[0]
        self.__styles: str = self.__path + '\\fichiers_qss\\'
        self.__images: str = self.__path + '\\images\\'
        self.currentstyle: str = ""
        
        self.setWindowTitle("Exemple_Main")
        self.setWindowIcon(QIcon(self.__images + 'horse.png'))  
        self.setFixedWidth(900)
        self.setFixedHeight(700)


        # barre d'état
        self.barre_etat = QStatusBar()
        self.setStatusBar(self.barre_etat)
        self.barre_etat.showMessage("L'application est démarrée...", 2000)
        
        
        # Création des actions des menus de la barre de menus
        # Actions menu 'Fichier'
        action_nouveau_projet: QAction = QAction(QIcon(self.__images + 'ajouter.png'), '&Nouveau', self)
        action_nouveau_projet.setShortcuts(["SHIFT+CTRL+N"])

        action_ouvrir_projet : QAction = QAction(QIcon(self.__images + 'cmd_open.png'), '&Ouvrir', self)
        action_ouvrir_projet.setShortcuts(["SHIFT+CTRL+O"])
        
        action_save_projet : QAction = QAction(QIcon(self.__images + 'cmd_save.png'), '&Enregistrer', self)
        action_save_projet.setShortcuts(["CTRL+S"])

        action_save_under_projet : QAction = QAction(QIcon(self.__images + 'cmd_saveAs.png'), '&Enregistrer sous', self)
        action_save_under_projet.setShortcuts(["SHIFT+CTRL+S"])
        
        action_supprimer_projet : QAction = QAction(QIcon(self.__images + 'cmd_delete.png'), '&Supprimer', self)

        # Actions menu 'Navigation'
        action_annuler : QAction = QAction(QIcon(self.__images + 'left.png'), '&Annuler', self)
        action_annuler.setShortcuts(["CTRL+Z"])
        
        action_retablir : QAction = QAction(QIcon(self.__images + 'right.png'), '&Rétablir', self)
        action_retablir.setShortcuts(["CTRL+Y"])
        
        action_quadrillage : QAction = QAction('&Quadrillage', self)
        action_quadrillage.setShortcuts(["CTRL+Q"])
        
        action_produit : QAction = QAction('&Produits', self)
        action_produit.setShortcuts(["CTRL+P"])

        

        # Widget dock Quadrillage
        self.quadWidget: QWidget = QWidget(self)
        quadLayout: QVBoxLayout = QVBoxLayout()
        self.quadWidget.setLayout(quadLayout)
        self.quadWidget.setObjectName("dockingquad")
        self.quadWidget.setStyleSheet("QWidget#dockingquad {border: 1px solid black; background-color:white}")
        self.quadWidget.setVisible(False)

        quadSizeLabel: QLabel = QLabel("Taille du quadrillage :")
        quadSizeLabel2: QLabel = QLabel("Taille du quadrillage :")
        
        quadLayout.addWidget(quadSizeLabel)
        quadLayout.addWidget(quadSizeLabel2)
        
        # Widget dock produit
        self.prodWidget: QWidget = QWidget(self)
        prodLayout: QVBoxLayout = QVBoxLayout()
        self.prodWidget.setLayout(prodLayout)
        self.prodWidget.setObjectName("dockingproduit")
        self.prodWidget.setStyleSheet("QWidget#dockingproduit {border: 1px solid black; background-color:white}")
        self.prodWidget.setVisible(False)

        prodLabel: QLabel = QLabel("Nom du produit :")
        prodLabel2: QLabel = QLabel("Ajouter produit :")
        prodLabel3: QLabel = QLabel("Supprimer produit :")
        prodLabel4: QLabel = QLabel("Liste produit :")
        
        prodLayout.addWidget(prodLabel)
        prodLayout.addWidget(prodLabel2)
        prodLayout.addWidget(prodLabel3)
        prodLayout.addWidget(prodLabel4)
        

        # Création de la barre de menus
        menu_bar = self.menuBar()
        
        menu_fichier = menu_bar.addMenu('&Fichier')
        menu_fichier.addActions([action_nouveau_projet, action_ouvrir_projet, action_save_projet, action_save_under_projet, action_supprimer_projet])
        
        menu_navigation = menu_bar.addMenu('&Navigation')
        menu_navigation.addActions([action_annuler, action_retablir, action_quadrillage, action_produit])

        menu_style = menu_bar.addMenu('&Style')
        
        
        # Changement de style
        for file in listdir(self.__styles):
            if file.endswith(".qss"):
                self.variables = {}
                self.variables[f"action_style + file.removesuffix('.qss')"] = QAction(text=file.removesuffix(".qss"), parent=self)
                menu_style.addAction(self.variables[f"action_style + file.removesuffix('.qss')"])        
                self.variables[f"action_style + file.removesuffix('.qss')"].triggered.connect(self.changeStyle)
                
        
        # Création de la barre d'outils
        barre_outils = QToolBar("Outils", self)
        self.addToolBar(barre_outils)
        barre_outils.addActions([action_save_projet, action_save_under_projet, action_annuler, action_retablir])
        

        # Image du plan
        self.updatePlan(self.__images + "Alteur_Table.JPG")
        
        
        # slots
        action_nouveau_projet.triggered.connect(self.nouv)
        action_ouvrir_projet.triggered.connect(self.open)
        action_supprimer_projet.triggered.connect(self.delete)
        action_save_projet.triggered.connect(self.save)
        action_save_under_projet.triggered.connect(self.save_under)
        action_annuler.triggered.connect(self.annuler)
        action_retablir.triggered.connect(self.retablir)
        action_quadrillage.triggered.connect(self.changeDockGauche)
        action_produit.triggered.connect(self.changeDockGauche)
        
        self.show()


    # Fonctions
    def nouv(self) -> None:
        self.barre_etat.showMessage("Créer un nouveau projet....")
        self.nouveauClicked.emit()
        self.Popup: PopupFichier = PopupFichier(self.currentstyle)

    def open(self):
        self.barre_etat.showMessage("Ouverture d'un fichier....")
        self.boite = QFileDialog()
        chemin, validation = self.boite.getOpenFileName(directory = sys.path[0], filter = '*.json')
        if validation == '*.json':
            self.openClicked.emit(chemin)

    def save(self):
        self.barre_etat.showMessage("Enregistrement effectué....")
        self.saveClicked.emit()

    def save_under(self):
        self.barre_etat.showMessage("Enregitrer Sous....")
        self.boite = QFileDialog()
        chemin, validation = self.boite.getSaveFileName(directory = sys.path[0], filter = '*.json')
        if validation == '*.json':
            self.saveUnderClicked.emit(chemin)

    def delete(self):
        self.barre_etat.showMessage("Suppression d'un projet....")
        self.boite = QFileDialog()
        chemin, validation = self.boite.getOpenFileName(directory = sys.path[0], filter = '*.json')
        if validation == '*.json':
            self.deleteClicked.emit(chemin)

    def annuler(self):
        self.barre_etat.showMessage("Annuler....")
        self.annulerClicked.emit()

    def retablir(self):
        self.barre_etat.showMessage("Retour....")
        self.retablirClicked.emit()

    def changeStyle(self):
        with open(self.__styles + self.sender().text() + ".qss", "r") as f:
            self.currentstyle = f.read()
            self.setStyleSheet(self.currentstyle)
            
    def changeDockGauche(self):
        if self.sender().text() == "&Quadrillage" and self.quadWidget.isVisible() == False:
            self.dock: QDockWidget = QDockWidget("Options de quadrillage :")
            self.addDockWidget(Qt.DockWidgetArea.LeftDockWidgetArea, self.dock)
            self.dock.setMaximumWidth(400)
        
            self.dock.setWidget(self.quadWidget)
            self.quadWidget.setVisible(True)
            
        if self.sender().text() == "&Produits" and self.prodWidget.isVisible() == False:
            self.dock: QDockWidget = QDockWidget("Options de produits :")
            self.addDockWidget(Qt.DockWidgetArea.LeftDockWidgetArea, self.dock)
            self.dock.setMaximumWidth(400)
            
            self.dock.setWidget(self.prodWidget)
            self.prodWidget.setVisible(True)
            
    def updatePlan(self, path: str):
        plan : Image = Image(path)
        plan.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.setCentralWidget(plan)


# --- main --------------------------------------------------------------------
if __name__ == "__main__":

    # création d'une QApplication
    app = QApplication(sys.argv)

    # # création de la fenêtre de l'application
    fenetre = VueMain()

    # lancement de l'application
    sys.exit(app.exec())