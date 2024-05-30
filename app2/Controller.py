import sys
from PyQt6.QtWidgets import QApplication
from Model import Model
from Vue import Vue

class Controller:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def load_data(self, filepath):
        self.model.load_data(filepath)
        self.view.display_data(self.model.get_data())

if __name__ == "__main__":
    app = QApplication(sys.argv)
    model = Model()
    vue = Vue(None)
    controller = Controller(model, vue)
    vue.controller = controller
    controller.load_data('data.json')
    vue.show()
    sys.exit(app.exec())
