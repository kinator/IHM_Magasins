import sys
from PyQt6.QtWidgets import QApplication
from Model import Model
from Vue import Vue

class Controller:
    def __init__(self):
        self.model = Model()
        self.view = Vue()
        self.load_data('data.json')  # Charger les données lors de l'initialisation

    def load_data(self, filepath):
        self.model.load_data(filepath)
        self.view.display_data(self.model.get_data())

if __name__ == "__main__":
    app = QApplication(sys.argv)
    controller = Controller()
    sys.exit(app.exec())
