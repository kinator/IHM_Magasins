import sys
from os import listdir
from PyQt6.QtWidgets import QApplication, QLabel, QMainWindow, QToolBar, QStatusBar, QWidget, QPushButton, QFileDialog, QDockWidget, QHBoxLayout, QVBoxLayout, QLineEdit, QDateEdit
from PyQt6.QtGui import QPixmap, QIcon, QAction, QCursor
from PyQt6.QtCore import Qt, pyqtSignal, QDate

class Image(QLabel):

    def __init__(self, chemin: str, height: int, width: int):
        '''Constructeur de la classe'''

        # appel au constructeur de la classe mère
        super().__init__() 
        
        image = QPixmap(chemin)
        if image.height() > image.width():
            pixmap = image.
            pixmap = image.scaled(int(width*0.8), int(height*0.7),transformMode= Qt.TransformationMode.FastTransformation)
        self.setPixmap(pixmap)
        
        self.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        

##############################################################################
##############################################################################

class PopupFichier(QWidget):
    newProject : pyqtSignal = pyqtSignal(dict)

    def __init__(self, style: str):
        '''Constructeur de la classe'''

        # appel au constructeur de la classe mère
        super().__init__() 
        
        self.__path: str = sys.path[0]
        self.__images: str = self.__path + '\\images\\'
        self.setStyleSheet(style)
        
        self.setWindowTitle("Création d'un nouveau projet")
        self.setWindowIcon(QIcon(self.__images + 'Alteur_Table.JPG'))
        
        vLayout: QVBoxLayout = QVBoxLayout()
        layoutLabel1: QHBoxLayout = QHBoxLayout()
        layoutProjetAuteur: QHBoxLayout = QHBoxLayout()
        layoutLabel2: QHBoxLayout = QHBoxLayout()
        layoutDateNom: QHBoxLayout = QHBoxLayout()
        layoutFile: QHBoxLayout = QHBoxLayout()
        layoutButtons: QHBoxLayout = QHBoxLayout()
        self.setLayout(vLayout)


        labelProjet: QLabel = QLabel("Nom du projet :")
        labelAuteur: QLabel = QLabel("Nom de l'auteur :")
        layoutLabel1.addWidget(labelProjet)
        layoutLabel1.addWidget(labelAuteur)
        vLayout.addLayout(layoutLabel1)

        self.nomProjet: QLineEdit = QLineEdit()
        self.nomAuteur: QLineEdit = QLineEdit()
        layoutProjetAuteur.addWidget(self.nomProjet)
        layoutProjetAuteur.addWidget(self.nomAuteur)
        vLayout.addLayout(layoutProjetAuteur)


        labelDate: QLabel = QLabel("Date :")
        labelNom: QLabel = QLabel("Nom de l'établissement :")
        layoutLabel2.addWidget(labelDate)
        layoutLabel2.addWidget(labelNom)
        vLayout.addLayout(layoutLabel2)
        
        self.dateMagasin: QDateEdit = QDateEdit()
        self.nomMagasin: QLineEdit = QLineEdit()
        layoutDateNom.addWidget(self.dateMagasin)
        layoutDateNom.addWidget(self.nomMagasin)
        vLayout.addLayout(layoutDateNom)

        
        labelAdresse: QLabel = QLabel("Adresse de l'établissement :")
        vLayout.addWidget(labelAdresse)
        
        self.adresseMagasin: QLineEdit = QLineEdit()
        vLayout.addWidget(self.adresseMagasin)
        
        
        labelFile: QLabel = QLabel("adresse du fichier :")
        vLayout.addWidget(labelFile)
        
        self.adresseFile: QLineEdit = QLineEdit()
        self.fileDialog: QPushButton = QPushButton("...")
        layoutFile.addWidget(self.adresseFile)
        layoutFile.addWidget(self.fileDialog)
        vLayout.addLayout(layoutFile)
    
    
        self.confirm_button : QPushButton = QPushButton('Confirmer', self)        
        self.quit_button: QPushButton = QPushButton("Quitter", self)
        layoutButtons.addWidget(self.confirm_button)
        layoutButtons.addWidget(self.quit_button)
        vLayout.addLayout(layoutButtons)


        self.quit_button.clicked.connect(self.clickCancel)
        self.confirm_button.clicked.connect(self.ClickConfirm)
        self.fileDialog.clicked.connect(self.searchFile)
        
        self.show()

    def searchFile(self):
        self.dialog: QFileDialog = QFileDialog()
        self.adresseFile.setText(self.dialog.getOpenFileName(filter="*.jpg; *.png; *.jpeg; *.bitmap; *.gif")[0])

    def ClickConfirm(self):
        if self.nomProjet.text() != "" and self.nomAuteur.text() != "" and self.dateMagasin.date().getDate() != (2000,1,1) and self.nomMagasin.text() != "" and self.adresseMagasin.text() != "" and self.adresseFile.text() != "":
            dico: dict = {"Projet" : self.nomProjet.text(), "Auteur" : self.nomAuteur.text(), "Date" : self.dateMagasin.date().getDate(), "nom_magasin" : self.nomMagasin.text(), "adresse_magasin" : self.adresseMagasin.text(), "fichier_plan" : self.adresseFile.text()}
            self.newProject.emit(dico)
            print('True')
            self.close()
        
        
    def clickCancel(self):
        print('False')
        self.close()

##############################################################################
##############################################################################

class VueMain(QMainWindow):

    # Création des signaux
    nouveauClicked : pyqtSignal = pyqtSignal(dict)
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
        self.setMinimumWidth(900)
        self.setMinimumHeight(700)
        self.setWindowIcon(QIcon(self.__images + 'horse.png'))  


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
        self.Popup: PopupFichier = PopupFichier(self.currentstyle)
        self.Popup.newProject.connect(self.sendNouv)
    
    def sendNouv(self, dico):
        self.nouveauClicked.emit(dico)

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
        plan : Image = Image(path, self.height(), self.width())
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