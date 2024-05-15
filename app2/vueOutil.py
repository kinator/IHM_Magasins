import sys
from PyQt6.QtWidgets import QApplication, QToolBar , QLabel, QMainWindow, QInputDialog, QLineEdit, QPushButton, QVBoxLayout, QWidget, QTextEdit, QDockWidget
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
        
        new_outil = QAction(QIcon(sys.path[0] + '/../icones/ajouter.png'), 'Nouveau', self)
        new_outil.triggered.connect(self.ajoutOutil)
        menu_fichier.addAction(new_outil)
        
        # outil_suivant = QAction(QIcon(sys.path[0] + '/../icones/right.png'), 'Suivant', self)
        # outil_suivant.triggered.connect(self.outilSuivant)
        # menu_fichier.addAction(outil_suivant)
        
        # outil_precedent = QAction(QIcon(sys.path[0] + '/../icones/left.png'), 'Précédent', self)
        # outil_precedent.triggered.connect(self.outilPrecedent)
        # menu_fichier.addAction(outil_precedent)

        menu_theme.addAction('Theme sombre')
        menu_theme.addAction('Theme clair')
        
        # Onglet gauche 
        
        # self.layoutPrincipal = QVBoxLayout() ; self.setLayout(self.layoutPrincipal)
        
        # self.article = QLabel("Articles : ")
        # self.nomArticle = QLineEdit("Maquereau") # A remplacer par le nom exacte du produit selectionner
        # # self.boutonAddArticle = QPushButton((QIcon(sys.path[0] + '/../icones/ajouter.png'), 'Ajouter', self))
        
        self.txtarticle = QLabel("Articles : ")
        self.txtproduits = QLineEdit("Maquereau") # A changer avec les noms en temps réel
        self.btnAddArticle = QPushButton("Ajouter")
        
        
        
        self.dock = QDockWidget("Articles : ")
        self.addDockWidget(Qt.DockWidgetArea.LeftDockWidgetArea, self.dock)
        self.dock.setWidget(self.txtarticle)
        
        self.dock.setWidget(self.txtproduits)
        self.dock.setWidget(self.btnAddArticle)
        self.dock.setMinimumWidth(200)
        
        
       
        
        
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