import json
from PyQt6.QtWidgets import QScrollArea,QFileDialog, QWidget, QLabel, QPushButton, QVBoxLayout, QApplication

class Model:
    def __init__(self):
        self.data = {}
        self.vue = None
        self.controller = None
        self.right_layouts = {}  # Dictionnaire pour stocker les layouts des catégories dans le dock droit
        self.left_layouts = {}   # Dictionnaire pour stocker les layouts des catégories dans le dock gauche

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

        # Configuration pour le dock gauche
        scroll_area_left = QScrollArea()
        scroll_widget_left = QWidget()
        layout_left = QVBoxLayout(scroll_widget_left)
        scroll_area_left.setWidget(scroll_widget_left)
        scroll_area_left.setWidgetResizable(True)

        # Configuration pour le dock droit
        scroll_area_right = QScrollArea()
        scroll_widget_right = QWidget()
        layout_right = QVBoxLayout(scroll_widget_right)
        scroll_area_right.setWidget(scroll_widget_right)
        scroll_area_right.setWidgetResizable(True)

        # Ajout des éléments du fichier JSON au dock gauche
        for category, items in self.data.items():
            category_label_left = QLabel(category)
            layout_left.addWidget(category_label_left)

            # Ajout de la catégorie au dock droit
            category_label_right = QLabel(category)
            layout_right.addWidget(category_label_right)

            # Création d'un layout pour les items de cette catégorie dans le dock droit
            category_layout_right = QVBoxLayout()
            layout_right.addLayout(category_layout_right)
            self.right_layouts[category] = category_layout_right

            # Création d'un layout pour les items de cette catégorie dans le dock gauche
            category_layout_left = QVBoxLayout()
            layout_left.addLayout(category_layout_left)
            self.left_layouts[category] = category_layout_left

            for item in items:
                button = QPushButton(f"{item}")
                button.setMinimumSize(150, 30)
                button.clicked.connect(lambda _, cat=category, btn=button: self.toggle_button_location(btn, cat))
                category_layout_left.addWidget(button)
                QApplication.processEvents()  # Forcer la mise à jour de l'interface utilisateur

        self.vue.layoutGDock.addWidget(scroll_area_left)
        self.vue.layoutDDock.addWidget(scroll_area_right)

    def toggle_button_location(self, button, category):
        # Vérifie la position actuelle du bouton et le déplace en conséquence
        if button.parent() == self.left_layouts[category].parentWidget():
            self.move_button_to_dock(button, category)
        else:
            self.move_button_back_to_left(button, category)

    def move_button_to_dock(self, button, category):
        # Supprimer le bouton du layout actuel (dock gauche)
        button.setParent(None)

        # Ajouter le bouton au layout de la catégorie correspondante dans le dock droit
        self.right_layouts[category].addWidget(button)

    def move_button_back_to_left(self, button, category):
        # Supprimer le bouton du layout actuel (dock droit)
        button.setParent(None)

        # Ajouter le bouton au layout de la catégorie correspondante dans le dock gauche
        self.left_layouts[category].addWidget(button)

    def save_right_dock_to_json(self, filename=None):
        dialog = QFileDialog()
        dialog.setAcceptMode(QFileDialog.AcceptMode.AcceptSave)
        dialog.setFileMode(QFileDialog.FileMode.AnyFile)
        dialog.setNameFilter("JSON (*.json)")
        dialog.setViewMode(QFileDialog.ViewMode.Detail)
        if filename:
            dialog.selectFile(filename)
        
        if dialog.exec():
            filenames = dialog.selectedFiles()
            if filenames:
                filename = filenames[0]
            else:
                return  # L'utilisateur a annulé

        if not filename:
            return  # Si le nom de fichier est toujours vide, ne rien faire

        # Ajouter l'extension .json si elle n'est pas fournie
        if not filename.endswith(".json"):
            filename += ".json"

        panier = {}
        for category, layout in self.right_layouts.items():
            for i in range(layout.count()):
                widget = layout.itemAt(i).widget()
                if isinstance(widget, QPushButton):
                    item_name = widget.text()
                    panier[item_name] = 1  # Vous pouvez ajuster la valeur selon vos besoins

        data_to_save = {"panier": panier}

        with open(filename, 'w', encoding='utf-8') as file:
            json.dump(data_to_save, file, ensure_ascii=False, indent=4) 

        
       