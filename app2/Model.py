import json
from PyQt6.QtWidgets import QScrollArea, QFileDialog, QWidget, QLabel, QPushButton, QVBoxLayout, QApplication

class Model:
    def __init__(self):
        self.data = {}
        self.vue = None
        self.controller = None
        self.right_layouts = QVBoxLayout()  # Layout pour le dock droit
        self.left_layouts = QVBoxLayout()   # Layout pour le dock gauche

    def set_vue(self, vue):
        self.vue = vue

    def set_controller(self, controller):
        self.controller = controller

    def load_data(self, filepath):
        try:
            with open(filepath, 'r') as file:
                self.data = json.load(file)
        except FileNotFoundError:
            print(f"Fichier {filepath} introuvable.")

    def display_data(self):
        if self.vue is None:
            return

        self.clear_left_dock()
        self.clear_right_dock()

        if not self.data:
            print("Aucune donnée chargée.")
            return

        # Configuration pour le dock gauche
        scroll_area_left = QScrollArea()
        scroll_widget_left = QWidget()
        scroll_widget_left.setLayout(self.left_layouts)
        scroll_area_left.setWidget(scroll_widget_left)
        scroll_area_left.setWidgetResizable(True)

        # Configuration pour le dock droit
        scroll_area_right = QScrollArea()
        scroll_widget_right = QWidget()
        scroll_widget_right.setLayout(self.right_layouts)
        scroll_area_right.setWidget(scroll_widget_right)
        scroll_area_right.setWidgetResizable(True)

        # Ajout des éléments du fichier JSON au dock gauche
        for category, items in self.data.items():  # Utilisez self.data.items() pour itérer sur les éléments du fichier JSON
            for item in items:  # Utilisez item pour référencer chaque élément dans les sous-listes
                button = QPushButton(f"{item}")
                button.setMinimumSize(130, 30)
                button.clicked.connect(lambda _, btn=button: self.toggle_button_location(btn))
                self.left_layouts.addWidget(button)
                QApplication.processEvents()  # Forcer la mise à jour de l'interface utilisateur

        self.vue.layoutGDock.addWidget(scroll_area_left)
        self.vue.layoutDDock.addWidget(scroll_area_right)
        
        # Recharger les données du panier
        self.load_panier()
        
    def load_panier(self):
        # Charger les données du fichier panier.json s'il existe
        try:
            with open('panier.json', 'r') as file:
                panier_data = json.load(file)
            self.clear_right_dock()
            for item_name in panier_data.get("panier", {}).keys():
                button = QPushButton(f"{item_name}")
                button.setMinimumSize(150, 30)
                button.clicked.connect(lambda _, btn=button: self.toggle_button_location(btn))
                self.right_layouts.addWidget(button)
                QApplication.processEvents()
        except FileNotFoundError:
            print("Fichier panier.json introuvable.")
        except json.JSONDecodeError:
            print("Erreur de décodage JSON dans le fichier panier.json.")

    def toggle_button_location(self, button):
        # Vérifie la position actuelle du bouton et le déplace en conséquence
        if button.parent() == self.left_layouts.parentWidget():
            self.move_button_to_dock(button)
        else:
            self.move_button_back_to_left(button)

    def move_button_to_dock(self, button):
        # Supprimer le bouton du layout actuel (dock gauche)
        button.setParent(None)

        # Ajouter le bouton au layout dans le dock droit
        self.right_layouts.addWidget(button)

    def move_button_back_to_left(self, button):
        # Supprimer le bouton du layout actuel (dock droit)
        button.setParent(None)

        # Ajouter le bouton au layout dans le dock gauche
        self.left_layouts.addWidget(button)

    def save_right_dock_to_json(self, filename='panier.json'):
        # Sauvegarder les données du dock droit dans un fichier JSON
        panier = {}
        for i in range(self.right_layouts.count()):
            widget = self.right_layouts.itemAt(i).widget()
            if isinstance(widget, QPushButton):
                item_name = widget.text()
                panier[item_name] = 1  # Vous pouvez ajuster la valeur selon vos besoins

        data_to_save = {"panier": panier}

        with open(filename, 'w', encoding='utf-8') as file:
            json.dump(data_to_save, file, ensure_ascii=False, indent=4)

    def clear_left_dock(self):
        # Supprime tous les widgets du layout du dock gauche
        while self.left_layouts.count():
            item = self.left_layouts.takeAt(0)
            widget = item.widget()
            if widget is not None:
                widget.setParent(None)

    def clear_right_dock(self):
        # Supprime tous les widgets du layout du dock droit
        while self.right_layouts.count():
            item = self.right_layouts.takeAt(0)
            widget = item.widget()
            if widget is not None:
                widget.setParent(None)
