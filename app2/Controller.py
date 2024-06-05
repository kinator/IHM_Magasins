import sys
from PyQt6.QtWidgets import QApplication
from Model import Model
from Vue import Vue

class Controller:
    def __init__(self):
        self.model = Model()
        self.view = Vue()
        self.model.set_vue(self.view)
        self.model.set_controller(self)
        self.view.set_controller(self)  # Passer une référence du contrôleur à la vue
        self.load_data('data.json')  # Charger les données lors de l'initialisation

    def load_data(self, filepath):
        self.model.load_data(filepath)
        self.model.display_data()

    def save_right_dock(self):
        self.model.save_right_dock_to_json('panier.json')
        
    def reload_json(self):
        self.model.reload_json()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    controller = Controller()
    controller.view.show()
    sys.exit(app.exec())
