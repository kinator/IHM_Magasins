import sys
from PyQt6.QtWidgets import QApplication, QToolBar , QLabel, QMainWindow, QInputDialog
from PyQt6.QtCore import Qt, pyqtSignal
from PyQt6.QtGui import QAction ,QIcon
            
class VueOutil(QMainWindow):

    def __init__(self):
        
        super().__init__()
        
        self.affiche_tool("Outil")
        
        # barre de menu
        
        menu_bar = self.menuBar()

        menu_fichier = menu_bar.addMenu('&Fichier')
        menu_edition = menu_bar.addMenu('&Edition')
        menu_theme = menu_bar.addMenu('&Style')
        
        # new_outil = QAction(QIcon(sys.path[0] + '/../icones/plus.png'), 'Nouveau', self)
        # new_outil.triggered.connect(self.ajoutOutil)
        # menu_fichier.addAction(new_outil)
        
        # outil_suivant = QAction(QIcon(sys.path[0] + '/../icones/right.png'), 'Suivant', self)
        # outil_suivant.triggered.connect(self.outilSuivant)
        # menu_fichier.addAction(outil_suivant)
        
        # outil_precedent = QAction(QIcon(sys.path[0] + '/../icones/left.png'), 'Précédent', self)
        # outil_precedent.triggered.connect(self.outilPrecedent)
        # menu_fichier.addAction(outil_precedent)

        menu_theme.addAction('Theme sombre')
        menu_theme.addAction('Theme clair')
        
        #barre d'outils 
        
        # barre_outil = QToolBar('Principaux outils')
        # self.addToolBar(barre_outil)

        # barre_outil.addAction(new_outil)
        # barre_outil.addAction(outil_precedent)
        # barre_outil.addAction(outil_suivant)

        # show
        
        self.setWindowTitle('Boîte à outils')
        self.resize(600, 400)
        self.setWindowFlags(Qt.WindowType.WindowCloseButtonHint)
        self.move((QApplication.screens()[0].size().width() - self.width())// 2, (QApplication.screens()[0].size().height() - self.height()) // 2)
        self.show()

    # signaux vers extérieur
    
    precedentClicked : pyqtSignal = pyqtSignal()
    suivantClicked : pyqtSignal = pyqtSignal()
    ajoutClicked : pyqtSignal = pyqtSignal(str)
    
    def outilPrecedent(self) -> None :
        self.precedentClicked.emit()
    
    def outilSuivant(self) -> None :
        self.suivantClicked.emit()
    
    def ajoutOutil(self) -> None :
        reponses , validation = QInputDialog.getText(None  ,"Saisir le nom du nouvel outil.","Nom ...")
    
        if(validation and reponses != '') :
            self.ajoutClicked.emit(reponses)
        
    def updateVue(self, outil: str) -> None:
        self.affiche_tool(outil)
        
    def affiche_tool(self , outil : str):
        self.current = QLabel(outil)
        self.current.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.setCentralWidget(self.current)

if __name__ == "__main__":

    print(f' --- main --- ')
    app = QApplication(sys.argv)
    
    fenetre = VueOutil()
    
    sys.exit(app.exec())