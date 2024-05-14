import sys
from PyQt6.QtWidgets import QApplication, QLabel, QMainWindow, QToolBar, QStatusBar, QWidget
from PyQt6.QtGui import QPixmap, QIcon, QAction
from PyQt6.QtCore import Qt, pyqtSignal

class VueMain(QMainWindow):

    # Création des signaux
    nouveauClicked : pyqtSignal = pyqtSignal()
    saveClicked : pyqtSignal = pyqtSignal()
    saveUnderClicked : pyqtSignal = pyqtSignal()
    openClicked : pyqtSignal = pyqtSignal()
    deleteClicked : pyqtSignal = pyqtSignal()
    annulerClicked : pyqtSignal = pyqtSignal()
    retablitClicked : pyqtSignal = pyqtSignal()

    def __init__(self):
        '''Constructeur de la classe'''

        # appel au constructeur de la classe mère
        super().__init__()
        
        self.__path: str = sys.path[0]
        
        self.setWindowTitle("Exemple_Main")
        self.setWindowIcon(QIcon(self.__path + 'icon.JPG'))  
        self.setFixedWidth(800)
        self.setFixedHeight(600)

        # barre d'état
        self.barre_etat = QStatusBar()
        self.setStatusBar(self.barre_etat)
        self.barre_etat.showMessage("L'application est démarrée...", 2000)
        
        # Création des actions des menus de la barre de menus
        # Actions menu 'Fichier'
        action_nouveau_projet: QAction = QAction(QIcon(self.__path + '\\images\\ajouter.png'), '&Nouveau', self)
        action_nouveau_projet.setShortcuts(["SHIFT+CTRL+N"])

        action_ouvrir_projet : QAction = QAction('&Ouvrir', self)
        action_ouvrir_projet.setShortcuts(["SHIFT+CTRL+O"])
        
        action_save_projet : QAction = QAction('&Enregistrer', self)
        action_save_projet.setShortcuts(["CTRL+S"])

        action_save_under_projet : QAction = QAction('&Enregistrer sous', self)
        action_save_under_projet.setShortcuts(["SHIFT+CTRL+S"])
        
        action_supprimer_projet : QAction = QAction('&Supprimer', self)

        # Actions menu 'Navigation'
        action_annuler : QAction = QAction(QIcon(self.__path + '\\images\\left.png'),'&Annuler', self)
        action_annuler.setShortcuts(["CTRL+Z"])
        
        action_retablier : QAction = QAction(QIcon(self.__path + '\\images\\right.png'),'&Rétablir', self)
        action_retablier.setShortcuts(["CTRL+Y"])
        
        # Actions menu 'Style
        action_theme_blanc : QAction = QAction('&Thème Blanc', self)

        action_theme_sombre : QAction = QAction('&Thème Sombre', self)


        # Création de la barre de menus
        menu_bar = self.menuBar()
        
        menu_fichier = menu_bar.addMenu('&Fichier')
        menu_fichier.addActions([action_nouveau_projet, action_ouvrir_projet, action_save_projet, action_save_under_projet, action_supprimer_projet])
        
        menu_navigation = menu_bar.addMenu('&Navigation')
        menu_navigation.addActions([action_annuler, action_retablier])

        menu_style = menu_bar.addMenu('&Style')
        menu_style.addActions([action_theme_blanc, action_theme_sombre])
        
        
        # signaux and slots (signaux à l'intérieur)
        action_nouveau_projet.triggered.connect(self.nouv)
        action_ouvrir_projet.triggered.connect(self.open)
        action_supprimer_projet.triggered.connect(self.delete)
        action_save_projet.triggered.connect(self.save)
        action_save_under_projet.triggered.connect(self.save_under)
        action_annuler.triggered.connect(self.annuler)
        action_retablier.triggered.connect(self.retablir)
        
        self.show()


    # Fonctions
    def nouv(self) -> None:
        self.barre_etat.showMessage("Créer un nouveau projet....")
        self.nouveauClicked.emit()
        check = True
        Popup: QWidget = QWidget()
        Popup.show()
        #while check:
        #    pass

    def open(self):
        self.barre_etat.showMessage("Ouverture d'un fichier....")
        self.openClicked.emit()

    def save(self):
        self.barre_etat.showMessage("Enregistrement effectué....")
        self.saveClicked.emit()

    def save_under(self):
        self.barre_etat.showMessage("Enregitrer Sous....")
        self.saveUnderClicked.emit()

    def delete(self):
        self.barre_etat.showMessage("Suppression d'un projet....")
        self.deleteClicked.emit()

    def annuler(self):
        self.barre_etat.showMessage("Annuler....")
        self.annulerClicked.emit()

    def retablir(self):
        self.barre_etat.showMessage("Rétablissement de la dernière action....")
        self.retablitClicked.emit()



# --- main --------------------------------------------------------------------
if __name__ == "__main__":

    # création d'une QApplication
    app = QApplication(sys.argv)

    # # création de la fenêtre de l'application
    fenetre = VueMain()

    # lancement de l'application
    sys.exit(app.exec())