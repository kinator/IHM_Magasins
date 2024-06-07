import sys, random, json
from os import listdir
from PyQt6.QtWidgets import QApplication, QLabel, QMainWindow, QToolBar, QStatusBar, QWidget, QPushButton, QFileDialog, QDockWidget, QHBoxLayout, QVBoxLayout, QLineEdit, QDateEdit, QSpinBox, QScrollArea
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
    
    def getToggle(self) -> bool:
        return self.toggleGrillage
    
    def updateImage(self, chemin) -> None:
        self.__chemin = chemin
        self.image = QPixmap(chemin)
        self.image = self.image.scaled(int(self.width()*0.8), int(self.height()*0.7),transformMode= Qt.TransformationMode.FastTransformation)
        
    def updateCadrillage(self) -> None:
        if self.toggleGrillage  == True:
            i, j = 1, 1
            self.cubeList = {}
            
            for i in range(self.limHeight):
                for j in range(self.limWidth):
                    self.cubeList[f"({i},{j})"] = {}
                    self.cubeList[f"({i},{j})"]["rect"] = QRect(int(self.rectangle.width() / self.limWidth * j), int(self.rectangle.height() / self.limHeight * i), int(self.rectangle.width() / self.limWidth), int(self.rectangle.height() / self.limHeight))
                    self.cubeList[f"({i},{j})"]["poly"] = QPolygon(QRect(int(self.rectangle.width() / self.limWidth * j), int(self.rectangle.height() / self.limHeight * i), int(self.rectangle.width() / self.limWidth), int(self.rectangle.height() / self.limHeight)))
        
    def paintEvent(self, event) -> None:
        self.qp = QPainter(self)
        self.qp.setPen(QColor("black"))
        self.rectangle = QRect(0, 0, self.width(), self.height())
        self.qp.drawPixmap(self.rectangle, self.image)
        self.updateCadrillage()
        self.afficherGrille()

        self.qp.end()

    def afficherGrille(self) -> None:
        if self.toggleGrillage == True:
            for i in range(self.limHeight):
                for j in range(self.limWidth):
                    self.qp.drawRect(self.cubeList[f"({i},{j})"]["rect"])

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
        self.focusCase = case
        
        
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
    ajoutProduit : pyqtSignal = pyqtSignal(QPushButton)
    caseCliquee : pyqtSignal = pyqtSignal(tuple)

    def __init__(self):
        '''Constructeur de la classe'''

        # appel au constructeur de la classe mère
        super().__init__()
        
        self.__path: str = sys.path[0]
        self.__styles: str = self.__path + '\\fichiers_qss\\'
        self.__images: str = self.__path + '\\images\\'
        self.currentstyle: str = ""
        self.currentImage: str = ""
        
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

        action_afficher_grillage : QAction = QAction('&Afficher cadrillage', self)
        action_afficher_grillage.setShortcuts(["CTRL+C"])

        

        # Widget dock Quadrillage
        self.quadWidget: QWidget = QWidget(self)
        quadLayout: QVBoxLayout = QVBoxLayout()
        self.quadWidget.setLayout(quadLayout)
        self.quadWidget.setObjectName("dockingquad")
        self.quadWidget.setStyleSheet("QWidget#dockingquad {border: 1px solid black; background-color:white}")
        self.quadWidget.setVisible(False)

        quadSizeLabel: QLabel = QLabel("Hauteur du quadrillage :")
        self.lineY = QSpinBox()
        self.lineY.setRange(1, 100)
        self.lineY.setValue(75)
        self.lineY.setSingleStep(1)
        quadLayout.addWidget(quadSizeLabel)
        quadLayout.addWidget(self.lineY)
        quadLayout.addSpacing(12)
        
        quadSizeLabel: QLabel = QLabel("Largeur du quadrillage :")
        self.lineX = QSpinBox()
        self.lineX.setRange(1, 100)
        self.lineX.setValue(75)
        self.lineX.setSingleStep(1)
        quadLayout.addWidget(quadSizeLabel)
        quadLayout.addWidget(self.lineX)
        quadLayout.addSpacing(12)

        quadSizeLabel2: QLabel = QLabel("Taille du quadrillage :")
        quadLayout.addWidget(quadSizeLabel2)
        
        quadLayout.insertStretch(-1, 1)

        
        # Widget dock produit
        self.prodWidget: QWidget = QWidget(self)
        prodLayout: QVBoxLayout = QVBoxLayout()
        self.prodWidget.setLayout(prodLayout)
        self.prodWidget.setObjectName("dockingproduit")
        self.prodWidget.setStyleSheet("QWidget#dockingproduit {border: 1px solid black; background-color:white}")
        self.prodWidget.setVisible(False)
        
        scroll_area_left = QScrollArea()
        
        tempWidget: QWidget = QWidget()
        tempLayout: QVBoxLayout = QVBoxLayout()
        scroll_area_left.setWidget(tempWidget)
        tempWidget.setLayout(tempLayout)
        scroll_area_left.setWidgetResizable(True)

        filepath = self.__path + "\\data.json"
        data = {}
        try:
            with open(filepath, 'r', encoding="utf-8") as file:
                data = json.load(file)
        except FileNotFoundError:
            print(f"Fichier {filepath} introuvable.")
            
            # Ajout des éléments du fichier data.JSON au dock gauche
        for category, items in data.items():  # Utilisez self.data.items() pour itérer sur les éléments du fichier JSON
            tempLayout.addWidget(QLabel(f"{category} :"))
            for item in items:  # Utilisez item pour référencer chaque élément dans les sous-listes
                print(item)
                button = QPushButton(f"{item}")
                button.setMinimumSize(130, 30)
                button.clicked.connect(lambda _, btn=button: self.ajouterProduit(btn))
                tempLayout.addWidget(button)
            tempLayout.addSpacing(15)

        prodLayout.addWidget(scroll_area_left)
        

        # Création de la barre de menus
        menu_bar = self.menuBar()
        
        menu_fichier = menu_bar.addMenu('&Fichier')
        menu_fichier.addActions([action_nouveau_projet, action_ouvrir_projet, action_save_projet, action_save_under_projet, action_supprimer_projet])
        
        menu_navigation = menu_bar.addMenu('&Navigation')
        menu_navigation.addActions([action_annuler, action_retablir, action_quadrillage, action_produit, action_afficher_grillage])

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
        barre_outils.addActions([action_save_projet, action_save_under_projet, action_annuler, action_retablir, action_afficher_grillage])
        

        # Image du plan
        self.plan : Image = Image(self.__images + "squaretransp.png", self.height(), self.width())
        self.setCentralWidget(self.plan)
        
        
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
        action_afficher_grillage.triggered.connect(self.toggleGrillage)
        self.lineX.valueChanged.connect(self.changerTailleGrille)
        self.lineY.valueChanged.connect(self.changerTailleGrille)
        self.plan.caseClicked.connect(self.caseClick)

        self.show()


    # Fonctions
    def nouv(self) -> None:
        self.barre_etat.showMessage("Créer un nouveau projet....")
        self.Popup: PopupFichier = PopupFichier(self.currentstyle)
        self.Popup.newProject.connect(self.sendNouv)
    
    def sendNouv(self, dico) -> None:
        self.currentImage = dico["fichier_plan"]
        self.nouveauClicked.emit(dico)

    def open(self) -> None:
        self.barre_etat.showMessage("Ouverture d'un fichier....")
        self.boite = QFileDialog()
        chemin, validation = self.boite.getOpenFileName(directory = sys.path[0], filter = '*.json')
        if validation == '*.json':
            print(chemin)
            self.openClicked.emit(chemin)

    def save(self) -> None:
        self.barre_etat.showMessage("Enregistrement effectué....")
        self.saveClicked.emit()

    def save_under(self) -> None:
        self.barre_etat.showMessage("Enregitrer Sous....")
        self.boite = QFileDialog()
        chemin, validation = self.boite.getSaveFileName(directory = sys.path[0], filter = '*.json')
        if validation == '*.json':
            self.saveUnderClicked.emit(chemin)

    def delete(self) -> None:
        self.barre_etat.showMessage("Suppression d'un projet....")
        self.boite = QFileDialog()
        chemin, validation = self.boite.getOpenFileName(directory = sys.path[0], filter = '*.json')
        if validation == '*.json':
            self.deleteClicked.emit(chemin)

    def annuler(self) -> None:
        self.barre_etat.showMessage("Annuler....")
        self.annulerClicked.emit()

    def retablir(self) -> None:
        self.barre_etat.showMessage("Retour....")
        self.retablirClicked.emit()
        
    def ajouterProduit(self, button) -> None:
        self.ajoutProduit.emit(button)

    def changeStyle(self) -> None:
        with open(self.__styles + self.sender().text() + ".qss", "r") as f:
            self.currentstyle = f.read()
            self.setStyleSheet(self.currentstyle)
            
    def changeDockGauche(self) -> None:
        if self.sender().text() == "&Quadrillage" and self.quadWidget.isVisible() == False:
            self.dock: QDockWidget = QDockWidget("Options de quadrillage :")
            self.addDockWidget(Qt.DockWidgetArea.LeftDockWidgetArea, self.dock)
            self.dock.setMaximumWidth(400)
            self.dock.setMinimumWidth(180)
        
            self.dock.setWidget(self.quadWidget)
            self.quadWidget.setVisible(True)
            
        if self.sender().text() == "&Produits" and self.prodWidget.isVisible() == False:
            self.dock: QDockWidget = QDockWidget("Options de produits :")
            self.addDockWidget(Qt.DockWidgetArea.LeftDockWidgetArea, self.dock)
            self.dock.setMaximumWidth(400)
            self.dock.setMinimumWidth(180)

            self.dock.setWidget(self.prodWidget)
            self.prodWidget.setVisible(True)
            
    def toggleGrillage(self) -> None:
        if self.plan.getToggle() == False:
            self.plan.setToggle(True)
            print("It's true")
        elif self.plan.getToggle() == True:
                self.plan.setToggle(False)
                print("It's false")
                
    def getX(self) -> int:
        return self.lineX.value()
    
    def getY(self) -> int:
        return self.lineY.value()
    
    def caseClick(self, t: tuple) -> None:
        self.caseCliquee.emit(t)

    def changerTailleGrille(self) -> None:
        self.plan.setCaseHeight(self.lineY.value())
        self.plan.setCaseWidth(self.lineX.value())
            
    def updatePlan(self, path: str) -> None:
        self.plan.updateAll(path)
        

# --- main --------------------------------------------------------------------
if __name__ == "__main__":

    # création d'une QApplication
    app = QApplication(sys.argv)

    # # création de la fenêtre de l'application
    fenetre = VueMain()

    # lancement de l'application
    sys.exit(app.exec())