import sys
from PyQt6.QtWidgets import QApplication
from Model import Model
from Vue import Vue
import map
import parcours

class Controller:
    def __init__(self):
        self.model = Model()
        self.view = Vue()
        self.model.set_vue(self.view)
        self.model.set_controller(self)
        self.view.set_controller(self)  
        self.load_data('data.json')  

    def load_data(self, filepath):
        self.model.load_data(filepath)
        self.model.display_data()

    def save_right_dock(self):
        self.model.save_right_dock_to_json('panier.json')
        self.update_optimal_path()

    def update_optimal_path(self):
        supermarche = map.mapping("supermarche.json", "produits.json", "panier.json")
        points_interet = supermarche.coordonnees_par_article()
        depart = supermarche.get_depart()
        arrivee = supermarche.get_arrivee()
        chemin_optimal = parcours.parcours_opti(supermarche.get_parcours(), depart, arrivee, points_interet)
        self.view.update_path(chemin_optimal)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    controller = Controller()
    controller.view.showMaximized()
    sys.exit(app.exec())
